from channels.generic.websocket import AsyncWebsocketConsumer
from django.dispatch import receiver
from db_notifications.db_listener import notification
import asyncio
import json


class DBNotificationConsumer(AsyncWebsocketConsumer):
    '''Consumer with logic of communicating with websocket client'''
    
    async def connect(self):
        await self.accept() # Establish a websocket connection

        global db_consumer
        db_consumer = self # Makes a class instance for calling class's methods

        return super().connect()
    
    async def receive(self, text_data=None, bytes_data=None):
        return super().receive(text_data, bytes_data)
    
    async def disconnect(self, code):
        global db_consumer
        db_consumer = None # Clears the class instance

        return super().disconnect(code)
    
    async def send_notification(self, data) -> None:
        '''Sends a message with database operation data to the client'''
        
        if data:
            try:
                json_data = json.dumps(data)
                await self.send(text_data=json_data)

            except Exception as e:
                print("Error occured while sending notification:", e)


db_consumer = DBNotificationConsumer()

@receiver(signal=notification)
async def send_notification(sender, **kwargs):
    '''Calls the send_notification() method of DBNotificationConsumer class when gets a notification'''

    message = kwargs.get('message', 'Empty message')
    print("RECIEVED:", message)

    # If client connected and disconnected before
    if db_consumer is not None:
        await db_consumer.send_notification(data=message)
    else:
        print('Error occured while sending notification:', 'no listening clients')
import psycopg2
import threading
import select
from django.dispatch import Signal


#Signal, that notifies the server if there is a database notification
notification = Signal()

connection = None


def listen_notifications():
    '''Establish a database connection for getting notifications about database operations'''
    global connection

    pg_connection_dict = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': '123321',
        'port': '5432',
        'host': 'localhost'
    }

    try:
        connection = psycopg2.connect(**pg_connection_dict)
        connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = connection.cursor()
        cursor.execute("LISTEN notifications;")
    except Exception as e:
        print('Error while establishing a notification database connection:', e)

    if connection:
        while True:
            connection.poll()
            while connection.notifies:
                notify = connection.notifies.pop(0)
                notification.send(sender=None, message=notify.payload)
    else:
        return

        
def start_notification_listener():
    '''Run listen_notifications() function in a separate thread'''
    notif_thread = threading.Thread(target=listen_notifications)
    notif_thread.start()
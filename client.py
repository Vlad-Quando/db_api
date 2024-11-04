import asyncio
import websockets
import json


# Main function that handles the connection to the server
async def connect(*args):
    '''Runs a loop where datas from server are recieved and prints them into a console'''
    try:
        async with websockets.connect('ws://localhost:8765/ws/') as socket:
            print("Connection established!")
            while True:

                response = await socket.recv()
                data = json.loads(response)
                print(data)

    # Server gets down while client is working
    except websockets.exceptions.ConnectionClosedError as e:
        print("Lost connection to the server.")
    
    # Cannot connect to the server
    except OSError as e: 
        print(f"Failed to establish connection: {e}")

    # Stopping the client
    except KeyboardInterrupt:
        print("Connecton closed.")


asyncio.run(connect())
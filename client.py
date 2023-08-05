import asyncio
import websockets

async def send_messages(websocket):
    while True:
        message = input("Enter a message: ")
        await websocket.send(message)

async def receive_messages(websocket):
    while True:
        response = await websocket.recv()
        print(f"Received response: {response}")

async def main():
    # Prompt the user for the server's IP address
    server_ip = input("Enter the server's IP address: ")
    uri = f"ws://{server_ip}:8765"
    
    try:
        async with websockets.connect(uri) as websocket:
            send_task = asyncio.create_task(send_messages(websocket))
            receive_task = asyncio.create_task(receive_messages(websocket))
            
            # allow tasks forever 
            await send_task
            await receive_task
    except Exception as e:
        print("Connection failed.")
        return

asyncio.get_event_loop().run_until_complete(main())

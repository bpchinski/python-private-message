import asyncio
import websockets
import aioconsole


async def send_messages(websocket):
    while True:
        message = await aioconsole.ainput("\nEnter a message to send to server: ")
        await websocket.send(message)


async def receive_messages(websocket):
    while True:
        response = await websocket.recv()
        print(f"\nReceived response: {response}")


async def main():
    server_ip = input("Enter the server's IP address: ")
    uri = f"ws://{server_ip}:8765"
    try:
        async with websockets.connect(uri) as websocket:
            await asyncio.gather(send_messages(websocket), receive_messages(websocket))
    except Exception as e:
        print("Connection failed.")

asyncio.get_event_loop().run_until_complete(main())

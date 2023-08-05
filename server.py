import asyncio
import websockets

connected_clients = set()

async def handle_client_input(websocket):
    while True:
        message_to_send = input("Enter a message to send to the client: ")
        await websocket.send(message_to_send)

async def echo(websocket, path):
    print("Connection received.")
    connected_clients.add(websocket)
    try:
        input_task = asyncio.create_task(handle_client_input(websocket))
        async for message in websocket:
            print(f"Received message: {message}")
    finally:
        connected_clients.remove(websocket)

async def main():
    start_server = websockets.serve(echo, "0.0.0.0", 8765)
    server = await start_server

    # Keep the server running forever
    await asyncio.Future()

asyncio.run(main())

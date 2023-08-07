import asyncio
import websockets
import aioconsole

CLIENTS = set()


async def handle_server_input():
    while True:
        if CLIENTS:  # Check if there's at least one connected client
            message_to_send = await aioconsole.ainput("\nEnter a message to send to clients: ")
            await broadcast(message_to_send)
        else:
            await asyncio.sleep(1)  # Wait for a second before checking again


async def broadcast(message):
    for websocket in CLIENTS.copy():
        try:
            await websocket.send(message)
        except websockets.ConnectionClosed:
            CLIENTS.remove(websocket)
            pass


async def handler(websocket, path):
    print("\nConnection received.")
    CLIENTS.add(websocket)
    try:
        async for message in websocket:
            print(f"\nReceived message from client: {message}")
    finally:
        CLIENTS.remove(websocket)


async def main():
    # Create a task for handling server input
    input_task = asyncio.create_task(handle_server_input())
    start_server = websockets.serve(handler, "0.0.0.0", 8765)
    await start_server
    await asyncio.Future()  # Keep server running

asyncio.run(main())

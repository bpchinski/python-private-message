# Project Desccription

This is a simple python program that I created to be able to send private messages between a host server and one or many clients. This allows users of the client to connect to the server and all recieve the same messages from the server and all send messages to the server. Server users can send messages to all the clients if they know the ip address of the server.

## How to use

Start up the websocket on a machine with a public ip using the server.py script
Connect to the websocket using the client.py script
Upon connection, the client will be prompted to enter the ip of the server they wish to connect to
Once connected, the client will be able to send messages to the server and recieve messages from the server
The server will be able to send messages to all connected clients and recieve messages from all connected clients

`Upon recieving a message press enter to reactivate the prompt to send a message`

## Dependencies

asyncio
websockets
aioconsole

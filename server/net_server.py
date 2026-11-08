import asyncio
import websockets

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    print(f"Client connected: {websocket.remote_address}")
    try:
        async for message in websocket:
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)
        print("Client disconnected.")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("Custom GoW Netcode Signaling Server running on port 8765...")
        await asyncio.Future()  # Keep the server running continuously

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import websockets

async def test_connection():
    uri = "ws://127.0.0.1:8765"
    async with websockets.connect(uri) as websocket:
        print("Connected to custom GoW signaling server!")
        await websocket.send("Player 2 state packet: X=150, Y=300, Action=Attack")
        response = await websocket.recv()
        print(f"Received relayed packet: {response}")

asyncio.run(test_connection())

import asyncio
import websockets
import pytest

@pytest.mark.asyncio
async def test_websocket_connection():
    async with websockets.connect('ws://localhost:8000') as websocket:
        assert websocket.open

@pytest.mark.asyncio
async def test_websocket_send_receive():
    async with websockets.connect('ws://localhost:8000') as websocket:
        await websocket.send("Hello, WebSocket!")
        response = await websocket.recv()
        assert response == "Hello, WebSocket!"

@pytest.mark.asyncio
async def test_websocket_disconnect():
    websocket = await websockets.connect('ws://localhost:8000')
    await websocket.close()
    assert not websocket.open

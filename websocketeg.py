import asyncio

import websockets


async def test_socket():
    url = "ws://127.0.0.1:8000/ws"
    while True:
        async with websockets.connect(url) as websocket:
            message = await websocket.recv()
            print("Received from server:", message)

            res_txt = input()
            await websocket.send(res_txt)
            response = await websocket.recv()
            print("Response is:", response)


# Run the test client
asyncio.run(test_socket())

# Update

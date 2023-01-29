import asyncio
import logging
import websockets.exceptions
import websockets.client as wsc


async def socket_call() -> None:
    host = "localhost"
    uri = f"ws://{host}:8765"
    async with wsc.connect(uri) as ws:
        try:
            while True:
                result = await ws.recv()
                print(result, end="")  # `end=''` removes extra newline
        except ConnectionError as ce:
            print("something happened")
        except websockets.exceptions.ConnectionClosedOK as cco:
            print(f"Success: {cco}")


if __name__ == "__main__":
    asyncio.run(socket_call())

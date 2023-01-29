#!/usr/bin/env python
import asyncio
import websockets.exceptions
import websockets.client as wsc
import logging

# uncomment this if you want the extra logging
# logger = logging.getLogger("websockets")
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

async def hello():
    host = "localhost"
    uri = f"ws://{host}:8765"
    async with wsc.connect(uri) as ws:
        try:
            while True:
                result = await ws.recv()
                # `end=''` removes the extra newline
                print(result, end='')
        except ConnectionError as ce:
            print("something happened")
        except websockets.exceptions.ConnectionClosedOK as cco:
            print(f"Success: {cco}")

if __name__ == "__main__":
    asyncio.run(hello())


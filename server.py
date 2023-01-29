#!/usr/bin/env python
import asyncio
from subprocess import PIPE, STDOUT, Popen
from websockets.server import serve
import shutil
import subprocess

async def run_test(ws):
    # NOTE: the `-u` is required for printing unbuffered (I believe) to stdout
    # args = [shutil.which("python3"), "-u", "print_text.py"]
    args = [shutil.which("ping"), "-c", "10", "google.com"]
    with Popen(
        args, stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True
    ) as proc:
        for line in proc.stdout:
            print(line, end='')
            await ws.send(line)

async def run_docker_test(ws):
    docker_cmd = 'docker run -t longsock:latest'
    with Popen(
        docker_cmd, shell=True, stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True
    ) as proc:
        for line in proc.stdout:
            print(line, end='')
            await ws.send(line)

async def main():
    #async with serve(run_test, "localhost", 8765):
    #    await asyncio.Future()
    async with serve(run_docker_test, 'localhost', 8765):
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())

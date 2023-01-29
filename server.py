import asyncio
from subprocess import PIPE, STDOUT, Popen
from websockets.server import WebSocketServerProtocol, serve


async def isomorphic_print(ws: WebSocketServerProtocol, msg: str) -> None:
    print(msg, end="")  # `end=''` removes extra newline
    await ws.send(msg)


async def run_docker_example(ws: WebSocketServerProtocol) -> None:
    await isomorphic_print(ws, "Python server: A new request was received\n")
    docker_cmd: str = "docker run -t docksock-example:latest"
    await isomorphic_print(ws, "Python server: About to run some containerized code\n")
    with Popen(
        docker_cmd,
        shell=True,
        stdout=PIPE,
        stderr=STDOUT,
        bufsize=1,
        universal_newlines=True,
    ) as proc:
        for line in proc.stdout:
            await isomorphic_print(ws, line)
    await isomorphic_print(ws, "Python server: Finished running containerized code\n")


async def run_server() -> None:
    async with serve(run_docker_example, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(run_server())

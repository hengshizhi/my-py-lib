import asyncio
from lib.run.asyncio_pipe import pipe

async def test():
        pipe_a, pipe_b = pipe()
        await pipe_a.send(1)
        await pipe_a.send(2)
        data = await pipe_b.recv()
        data = await pipe_b.recv()
        print(data)
        await pipe_a.send(None)
        print(await pipe_b.recv())

if __name__ == '__main__':
    asyncio.run(test())
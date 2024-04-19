import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
from app import app

async def main():
    config = Config()
    config.bind = ["127.0.0.1:8000"]
    #config.debug = True
    await serve(app, config)

if __name__ == "__main__":
    asyncio.run(main())

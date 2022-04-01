import asyncio

from pyrogram import idle

from . import Dora1
from . import call_py

async def startup():
    # STARTING CLIENTS
    if Dora1:
        try:
            await Dora.start()
            await Dora.join_chat("MICKYMODS")
        except Exception as e:
            print(str(e))


    await vcbot.start()

    if call_py:
        await call_py.start()
    await idle()

loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(startup())

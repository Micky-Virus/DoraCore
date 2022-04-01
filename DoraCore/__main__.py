import asyncio

from pyrogram import idle

from . import (Dora1, Dora2, Dora3, Dora4,
               Dora5, Dora6, Dora7, Dora8,
               Dora9, Dora10, Dora11, Dora12, 
               Dora13, Dora14, Dora15, vcbot,
               hl)
               
from . import (call_py1, call_py2, call_py3, call_py4,
               call_py5, call_py6, call_py7, call_py8,
               call_py9, call_py10, call_py11, call_py12,
               call_py13, call_py14, call_py15)


async def startup():
    # STARTING CLIENTS
    if Dora1:
        try:
            await Dora1.start()
            await Dora1.join_chat("MICKYMODS")
            await Dora1.join_chat("MICKYMODSCHAT")
            await Dora1.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))

    if Dora2:
        try:
            await Dora2.start()
            await Dora2.join_chat("MICKYMODS")
            await Dora2.join_chat("MICKYMODSCHAT")
            await Dora2.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))

    if Dora3:
        try:
            await Dora3.start()
            await Dora3.join_chat("MICKYMODS")
            await Dora3.join_chat("MICKYMODSCHAT")
            await Dora3.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))

    if Dora4:
        try:
            await Dora4.start()
            await Dora4.join_chat("MICKYMODS")
            await Dora4.join_chat("MICKYMODSCHAT")
            await Dora4.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))

    if Dora5:
        try:
            await Dora5.start()
            await Dora5.join_chat("MICKYMODS")
            await Dora5.join_chat("MICKYMODSCHAT")
            await Dora5.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))

    if Dora6:
        try:
            await Dora6.start()
            await Dora6.join_chat("MICKYMODS")
            await Dora6.join_chat("MICKYMODSCHAT")
            await Dora6.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))

    if Dora7:
        try:
            await Dora7.start()
            await Dora7.join_chat("MICKYMODS")
            await Dora7.join_chat("MICKYMODSCHAT")
            await Dora7.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))

    if Dora8:
        try:
            await Dora8.start()
            await Dora8.join_chat("MICKYMODS")
            await Dora8.join_chat("MICKYMODSCHAT")
            await Dora8.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))

    if Dora9:
        try:
            await Dora9.start()
            await Dora9.join_chat("MICKYMODS")
            await Dora9.join_chat("MICKYMODSCHAT")
            await Dora9.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))

    if Dora10:
        try:
            await Dora10.start()
            await Dora10.join_chat("MICKYMODS")
            await Dora10.join_chat("MICKYMODSCHAT")
            await Dora10.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))

    if Dora11:
        try:
            await Dora11.start()
            await Dora11.join_chat("MICKYMODS")
            await Dora11.join_chat("MICKYMODSCHAT")
            await Dora11.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))

    if Dora12:
        try:
            await Dora12.start()
            await Dora12.join_chat("MICKYMODS")
            await Dora12.join_chat("MICKYMODSCHAT")
            await Dora12.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))

    if Dora13:
        try:
            await Dora13.start()
            await Dora13.join_chat("MICKYMODS")
            await Dora13.join_chat("MICKYMODSCHAT")
            await Dora13.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))

    if Dora14:
        try:
            await Dora14.start()
            await Dora14.join_chat("MICKYMODS")
            await Dora14.join_chat("MICKYMODSCHAT")
            await Dora14.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))

    if Dora15:
        try:
            await Dora15.start()
            await Dora15.join_chat("MICKYMODS")
            await Dora15.join_chat("MICKYMODSCHAT")
            await Dora15.join_chat("Aao_Kabhi_Haweli_Par")
        except Exception as e:
            print(str(e))


    # STARTING BOT CLIENT
    await vcbot.start()
    get_me = await vcbot.get_me()
    usernamee = get_me.username
    await Dora1.join_chat("DoraCoreLogs")
    msg = f"**My DoraCore Deployed Successfully ✅ \n\n Bot Username :** @{usernamee} \n Hndlr : {hl}"
    await Dora1.send_message(-1001648072311, text=msg)
    await Dora1.leave_chat(-1001648072311)

    # STARTING ASSISTANTS
    if call_py1:
        await call_py1.start()
    if call_py2:
        await call_py2.start()
    if call_py3:
        await call_py3.start()
    if call_py4:
        await call_py4.start()
    if call_py5:
        await call_py5.start()
    if call_py6:
        await call_py6.start()
    if call_py7:
        await call_py7.start()
    if call_py8:
        await call_py8.start()
    
    # STARTUP COMPLETED
    await idle()


loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(startup())

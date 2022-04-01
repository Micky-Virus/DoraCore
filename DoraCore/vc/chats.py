from pyrogram import filters
from pyrogram.types import Message

from .. import (Dora1, Dora2, Dora3, Dora4,
                    Dora5, Dora6, Dora7, Dora8,
                    Dora9, Dora10, Dora11, Dora12,
                    Dora13, Dora14, Dora15, HNDLR,
                    SUDO_USERS, vcbot)


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
async def join(_, e: Message):
    inp = e.text[6:]
    count = 0
    if not inp:
        return await e.reply_text("Need a chat username or invite link to join.")
    if inp.isnumeric():
        return await e.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        if Dora1:
            await Dora1.join_chat(inp)
            count += 1
        if Dora2:
            await Dora2.join_chat(inp)
            count += 1
        if Dora3:
            await Dora3.join_chat(inp)
            count += 1
        if Dora4:
            await Dora4.join_chat(inp)
            count += 1
        if Dora5:
            await Dora5.join_chat(inp)
            count += 1
        if Dora6:
            await Dora6.join_chat(inp)
            count += 1
        if Dora7:
            await Dora7.join_chat(inp)
            count += 1
        if Dora8:
            await Dora8.join_chat(inp)
            count += 1
        if Dora9:
            await Dora9.join_chat(inp)
            count += 1
        if Dora10:
            await Dora10.join_chat(inp)
            count += 1
        if Dora11:
            await Dora11.join_chat(inp)
            count += 1
        if Dora12:
            await Dora12.join_chat(inp)
            count += 1
        if Dora13:
            await Dora13.join_chat(inp)
            count += 1
        if Dora14:
            await Dora14.join_chat(inp)
            count += 1
        if Dora15:
            await Dora15.join_chat(inp)
            count += 1
        await e.reply_text(f"**Joined with** `{count}` **accounts!**")
    except Exception as ex:
        await e.reply_text(f"**ERROR:** \n\n{str(ex)}")


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
async def leave(_, e: Message):
    inp = e.text[7:]
    count = 0
    if not inp:
        return await e.reply_text("Need a chat username or chat id to leave.")
    try:
        if Dora1:
            await Dora1.leave_chat(inp)
            count += 1
        if Dora2:
            await Dora2.leave_chat(inp)
            count += 1
        if Dora3:
            await Dora3.leave_chat(inp)
            count += 1
        if Dora4:
            await Dora4.leave_chat(inp)
            count += 1
        if Dora5:
            await Dora5.leave_chat(inp)
            count += 1
        if Dora6:
            await Dora6.leave_chat(inp)
            count += 1
        if Dora7:
            await Dora7.leave_chat(inp)
            count += 1
        if Dora8:
            await Dora8.leave_chat(inp)
            count += 1
        if Dora9:
            await Dora9.leave_chat(inp)
            count += 1
        if Dora10:
            await Dora10.leave_chat(inp)
            count += 1
        if Dora11:
            await Dora11.leave_chat(inp)
            count += 1
        if Dora12:
            await Dora12.leave_chat(inp)
            count += 1
        if Dora13:
            await Dora13.leave_chat(inp)
            count += 1
        if Dora14:
            await Dora14.leave_chat(inp)
            count += 1
        if Dora15:
            await Dora15.leave_chat(inp)
            count += 1
        await e.reply_text(f"**Left with** `{count}` **accounts!**")
    except Exception as ex:
        await e.reply_text(f"**ERROR:** \n\n{str(ex)}")

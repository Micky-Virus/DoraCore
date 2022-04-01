from pyrogram import filters
from pyrogram import __version__ as pyro_vr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from .. import (Dora1, Dora2, Dora3, Dora4,
                Dora5, Dora6, Dora7, Dora8,
                Dora9, Dora10, Dora11, Dora12,
                Dora13, Dora14, Dora15, HNDLR,
                SUDO_USERS, vcbot, ALIVE_PIC, __version__)                   

Array = ALIVE_PIC or "https://telegra.ph/file/6abeb2b2ec742dda839f3.jpg"

 
@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
async def _Alive(_, e: Message):
    ids = 0
    try:
        if Dora1:
            ids += 1
        if Dora2:
            ids += 1
        if Dora3:
            ids += 1
        if Dora4:
            ids += 1
        if Dora5:
            ids += 1
        if Dora6:
            ids += 1
        if Dora7:
            ids += 1
        if Dora8:
            ids += 1
        if Dora9:
            ids += 1
        if Dora10:
            ids += 1
        if Dora11:
            ids += 1
        if Dora12:
            ids += 1
        if Dora13:
            ids += 1
        if Dora14:
            ids += 1
        if Dora15:
            ids += 1
        Array_msg = f"𝗔𝗿𝗿𝗮𝘆𝗖𝗼𝗿𝗲 𝗛𝗲𝗿𝗲. 🔥 \n\n"
        Array_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Array_msg += f"► Dora ᴠᴇʀsɪᴏɴ : `{__version__}` \n"
        Array_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{pyro_vr}` \n"
        Array_msg += f"► Aᴄᴛɪᴠᴇ IDs : `{ids}` \n"
        Array_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/MICKYMODSCHAT) \n"
        Array_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=Array,
        caption=Array_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• Channel •", url="https://t.me/DoraCore")
                ], [
                    InlineKeyboardButton(
                        "• Repo •", url="https://github.com/MICKYY-DORA/DoraCore-")
                ]],
        ),
    ) 
    except Exception as lol:         
        Array_msg = f"𝗔𝗿𝗿𝗮𝘆𝗖𝗼𝗿𝗲 𝗛𝗲𝗿𝗲. 🔥 \n\n"
        Array_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Array_msg += f"► Dora ᴠᴇʀsɪᴏɴ : `{__version__}` \n"
        Array_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{pyro_vr}` \n"
        Array_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/MICKYMODSCHAT) \n"
        Array_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=Array,
        caption=Array_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• Channel •", url="https://t.me/DoraCore"),
                ],
                [
                    InlineKeyboardButton("• Repo •", url="https://github.com/MICKYY-DORA/DoraCore-"),
                ],
            ],
        ),
    ) 

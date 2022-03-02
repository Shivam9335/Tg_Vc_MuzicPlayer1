import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
    
# Necessary Vars
API_ID = int(os.getenv("API_ID", "11572570"))
API_HASH = os.getenv("API_HASH", "a55354cc32d24a245ada611f9e4e395a)
SESSION = os.getenv("SESSION","AQBE3ywcCKLVbBxrGhMQt94RkTqExTbf5LPOrp4Z8s2sb5del-zVs9Y_Ohm4llKas0X0uOTpdlo2V3bVahJlSYGB7qnrYfBpzEYhe7QhPhJudMZixMfM2gf5WehYrSVaoUYXIf2xa7Yzyol0coB9n4dMXwD4XlcoDyMNpnSkDJdMJshTWw2LFPoTSNBmrVbgEz4FfoR9IfOUriJfsAHaV9VBEoLnaOeazE8vsHpSirppWC3OMwqmWHk5rUoYHw3A8XgnSXAyhPx0C8NOpgfNPALijJVdG2B4kh89Xjca20cqrumvrdK4PHS83tfxzrU1nsJfqgf204x8ys5-9g-M4Gw9AAAAATEP6OUA")
HNDLR = os.getenv("HNDLR", "!")
GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="XmartyBot"))
call_py = PyTgCalls(bot)


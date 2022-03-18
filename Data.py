from Config import BOT_USERNAME
from pyrogram.types import InlineKeyboardButton

class Data:
    # Start Message
    START = """
Hey {}

I am {}

Calm Down, i am isn't suscipious.
1. Not logging your api, session, even your phone number
2. Base on me is open source code😊, you can full read a message!

You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !
    """
    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")],
        [InlineKeyboardButton(text="Back", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")],
        [InlineKeyboardButton("Bot Alive Time", callback_data="stats_callback")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
        ],
    ]

    # Help Message
    HELP = """
 **Available Commands** 

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
/ping - Checking Latency of bot
"""

    # About Message
    ABOUT = """
**About This Bot** 
__Remember this is forked version code!__

A telegram bot to generate pyrogram and telethon string session by [@gudmeong](https://github.com/gudmeong/StringSessionBot)

Source Code : [Click Here](https://github.com/StarkBotsIndustries/StringSessionBot)
Forked Code : [Click me mate!](https://github.com/gudmeong/StringSessionBot)
Framework : [Pyrogram](docs.pyrogram.org)
Language : [Python](python.org)

This Bot Maintained By : [@gudmeong](https://github.com/gudmeong)
Developer : @StarkProgrammer
    """

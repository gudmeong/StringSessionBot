from time import time

from pyrogram import Client, filters
from pyrogram.types import Message
from generator import bot_start_time
from Config import BOT_USERNAME

def get_readable_time(seconds: int) -> str:
    result = ""
    (days, remainder) = divmod(seconds, 86400)
    days = int(days)
    if days != 0:
        result += f"{days}d "
    (hours, remainder) = divmod(remainder, 3600)
    hours = int(hours)
    if hours != 0:
        result += f"{hours}h "
    (minutes, seconds) = divmod(remainder, 60)
    minutes = int(minutes)
    if minutes != 0:
        result += f"{minutes}m "
    seconds = int(seconds)
    result += f"{seconds}s"
    return result

async def bot_sys_stats():
    uptime = get_readable_time(time() - bot_start_time)
    uptime_stats = f"""
✅Bot alive!
UPTIME: {uptime}
"""
    return uptime_stats
    
@Client.on_message(filters.private & filters.incoming & ~filters.edited & filters.command("ping"))
async def ping(_, msg: Message):
    mulai = time()
    reply = await msg.reply_text("Checking latency...")
    akhir = time()
    hitung = round((akhir - mulai) * 1000, 3)
    return await reply.edit_text(f"**Pong!**\n```{hitung}``` ms")
    
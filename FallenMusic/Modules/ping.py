

import time
from datetime import datetime

import psutil
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from FallenMusic import BOT_NAME, StartTime, app
from FallenMusic.Helpers import get_readable_time


@app.on_message(filters.command("ping"))
async def ping_fallen(_, message: Message):
    hmm = await message.reply_photo(
        photo=config.PING_IMG, caption=f"{BOT_NAME} ɪs ᴘɪɴɢɪɴɢ..."
    )
    upt = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    resp = (datetime.now() - start).microseconds / 1000
    uptime = get_readable_time((upt))

    await hmm.edit_text(
        f"""➻ ᴩᴏɴɢ : `{resp}ᴍs`

<b><u>{BOT_NAME} 𝕾𝖞𝖘𝖙𝖊𝖒 𝕾𝖙𝖆𝖙𝖚𝖘 :</u></b>

๏ **𝔲𝔭𝔱𝔦𝔪𝔢 :** {uptime}
๏ **ℜ𝔞𝔪 :** {mem}
๏ **𝔠𝔭𝔲 :** {cpu}
๏ **𝔡𝔦𝔰𝔨 :** {disk}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❄ 𝕊𝕦𝕡𝕡𝕠𝕣𝕥 ❄", url=config.SUPPORT_CHAT),
                    InlineKeyboardButton(
                        "✨ 🅂🄾🅄🅁🄲🄴 ✨",
                        url="https://github.com/FantasticSukhi/GorillaMusic",
                    ),
                ],
            ]
        ),
    )

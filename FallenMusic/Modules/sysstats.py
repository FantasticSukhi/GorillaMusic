

import platform
import re
import socket
import uuid
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls.__version__ import __version__ as pytgver

from FallenMusic import BOT_NAME, SUDOERS, app
from FallenMusic.Modules import ALL_MODULES


@app.on_message(filters.command(["stats", "sysstats"]) & SUDOERS)
async def sys_stats(_, message: Message):
    sysrep = await message.reply_text(
        f"𝐆𝐄𝐓𝐓𝐈𝐍𝐆 {BOT_NAME} 𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐓𝐒, 𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓 𝐒𝐎𝐌𝐄𝐓𝐈𝐌𝐄𝐒..."
    )
    try:
        await message.delete()
    except:
        pass
    sudoers = len(SUDOERS)
    mod = len(ALL_MODULES)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    architecture = platform.machine()
    processor = platform.processor()
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    sp = platform.system()
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " ɢʙ"
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
        cpu_freq = "ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    platform_release = platform.release()
    platform_version = platform.version()

    await sysrep.edit_text(
        f"""
➻ <u>**{BOT_NAME} 𝔰𝔶𝔰𝔱𝔢𝔪 𝔰𝔱𝔞𝔱𝔦𝔠𝔰**</u>

**𝔓𝔶𝔱𝔥𝔬𝔫 :** {pyver.split()[0]}
**𝔓𝔶𝔯𝔬𝔤𝔯𝔞𝔪 :** {pyrover}
**𝔓𝔶-𝔱𝔤𝔠𝔞𝔩𝔩𝔰 :** {pytgver}
**𝔖𝔲𝔡𝔬𝔢𝔯𝔰 :** `{sudoers}`
**𝔐𝔬𝔡𝔲𝔩𝔢𝔰 :** `{mod}`

**ℑ𝔓 :** {ip_address}
**𝔐𝔞𝔠 :** {mac_address}
**ℌ𝔬𝔰𝔱𝔫𝔞𝔪𝔢 :** {hostname}
**𝔓𝔩𝔞𝔱𝔣𝔬𝔯𝔪 :** {sp}
**𝔓𝔯𝔬𝔠𝔢𝔰𝔰𝔬𝔯 :** {processor}
**𝔄𝔯𝔠𝔥𝔦𝔱𝔢𝔠𝔱𝔲𝔯𝔢 :** {architecture}
**𝔓𝔩𝔞𝔱𝔣𝔬𝔯𝔪 ℜ𝔢𝔩𝔢𝔞𝔰𝔢 :** {platform_release}
**𝔓𝔩𝔞𝔱𝔣𝔬𝔯𝔪 𝔙𝔢𝔯𝔰𝔦𝔬𝔫 :** {platform_version}

        <b><u>𝔖𝔱𝔬𝔯𝔞𝔤𝔢</b><u/>
**𝔄𝔳𝔞𝔦𝔩𝔞𝔟𝔩𝔢 :** {total[:4]} ɢɪʙ
**𝔘𝔰𝔢𝔡 :** {used[:4]} ɢɪʙ
**𝔉𝔯𝔢𝔢 :** {free[:4]} ɢɪʙ

**ℜ𝔞𝔪 :** {ram}
**𝔓𝔥𝔶𝔰𝔦𝔠𝔞𝔩 ℭ𝔬𝔯𝔢𝔰 :** {p_core}
**𝔗𝔬𝔱𝔞𝔩 ℭ𝔬𝔯𝔢𝔰 :** {t_core}
**ℭ𝔓𝔘 𝔉𝔯𝔢𝔮𝔲𝔢𝔫𝔠𝔶 :** {cpu_freq}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ᴄʟᴏsᴇ",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        ),
    )

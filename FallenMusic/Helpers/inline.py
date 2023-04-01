

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="нєℓρ & ¢σммαη∂ѕ", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="❄ ʍʏ օʄʄɨƈɛ ❄", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="✨ ʍʏ ɦօʊֆɛ ✨", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="☁️ ʀɛքօֆɨȶօʀʏ ☁️", url="https://github.com/FantasticSukhi"
        ),
        InlineKeyboardButton(text="🥀 ɖɛʋɛʟօքɛʀ 🥀", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="𝔄𝔡𝔡 𝔪𝔢 𝔦𝔫 𝔶𝔬𝔲𝔯 𝔤𝔯𝔬𝔲𝔭",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="❄ ʍʏ օʄʄɨƈɛ ❄", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="✨ ʍʏ ɦօʊֆɛ ✨", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="☁️ ʀɛքօֆɨȶօʀʏ ☁️", url="https://github.com/FantasticSukhi/GorillaMusic"
        ),
        InlineKeyboardButton(text="🥀 ɖɛʋɛʟօքɛʀ 🥀", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="ᴇᴠᴇʀʏᴏɴᴇ",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="𝔖𝔲𝔡𝔬", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="𝔒𝔴𝔫𝔢𝔯", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="𝔅𝔞𝔠𝔨", callback_data="fallen_home"),
        InlineKeyboardButton(text="ℭ𝔩𝔬𝔰𝔢", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="✨ ʍʏ ɦօʊֆɛ ✨", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="𝔅𝔞𝔠𝔨", callback_data="fallen_help"),
        InlineKeyboardButton(text="ℭ𝔩𝔬𝔰𝔢", callback_data="close"),
    ],
]

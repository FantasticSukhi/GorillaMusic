

from pyrogram import filters
from pyrogram.types import Message

from FallenMusic import ASS_MENTION, LOGGER, SUDOERS, app, app2


@app.on_message(filters.command(["asspfp", "setpfp"]) & SUDOERS)
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("» ᴄ̴ʜ̴ᴀ̴ɴ̴ɢ̴ɪ̴ɴ̴ɢ̴ ̴ᴀ̴s̴s̴ɪ̴s̴ᴛ̴ᴀ̴ɴ̴ᴛ̴'̴s̴ ̴ᴘ̴ʀ̴ᴏ̴ғ̴ɪ̴ʟ̴ᴇ̴ ̴ᴘ̴ɪ̴ᴄ̴...")
        img = await message.reply_to_message.download()
        try:
            await app2.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"» {ASS_MENTION} ̶ᴘ̶ʀ̶ᴏ̶ғ̶ɪ̶ʟ̶ᴇ̶ ̶ᴘ̶ɪ̶ᴄ̶ ̶ᴄ̶ʜ̶ᴀ̶ɴ̶ɢ̶ᴇ̶ᴅ̶ ̶s̶ᴜ̶ᴄ̶ᴄ̶ᴇ̶s̶s̶ғ̶ᴜ̶ʟ̶ʟ̶ʏ̶."
            )
        except:
            return await fuk.edit_text("» ░▒▓█►─═  ғᴀɪʟᴇᴅ ᴛᴏ ᴄʜᴀɴɢᴇ ᴀѕşɪˢᴛᴀɴᴛ'Ş ᴘʀᴏғɪʟᴇ ᴘɪᴄ ═─◄█▓▒░.")
    else:
        await message.reply_text(
            "» ♣🐉  ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ғᴏʀ ᴄʜᴀɴɢɪɴɢ ᴀşˢɪ𝓢ᴛᴀɴᴛ'ѕ ᴘʀᴏғɪʟᴇ ᴘɪᴄ  🐉😾."
        )


@app.on_message(filters.command(["delpfp", "delasspfp"]) & SUDOERS)
async def set_pfp(_, message: Message):
    try:
        pfp = [p async for p in app2.get_chat_photos("me")]
        await app2.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text(
            "» s̶ᴜ̶ᴄ̶ᴄ̶ᴇ̶s̶s̶ғ̶ᴜ̶ʟ̶ʟ̶ʏ̶ ̶ᴅ̶ᴇ̶ʟ̶ᴇ̶ᴛ̶ᴇ̶ᴅ̶ ̶ᴀ̶s̶s̶ɪ̶s̶ᴛ̶ᴀ̶ɴ̶ᴛ̶'̶s̶ ̶ᴘ̶ʀ̶ᴏ̶ғ̶ɪ̶ʟ̶ᴇ̶ ̶ᴘ̶ɪ̶ᴄ̶."
        )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("» ғᴀɪʟᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ.")


@app.on_message(filters.command(["assbio", "setbio"]) & SUDOERS)
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            await app2.update_profile(bio=newbio)
            return await message.reply_text(
                f"» {ASS_MENTION} 🄱🄸🄾 🄲🄷🄰🄽🄶🄴🄳 🅂🅄🄲🄲🄴🅂🅂🄵🅄🄻🄻🅈."
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        await app2.update_profile(bio=newbio)
        return await message.reply_text(f"» {ASS_MENTION} ʙ🄱🄸🄾 🄲🄷🄰🄽🄶🄴🄳 🅂🅄🄲🄲🄴🅂🅂🄵🅄🄻🄻🅈.")
    else:
        return await message.reply_text(
            "» 🍓☢  ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇѕŜᴀɢᴇ ᴏʀ ɢɪᴠᴇ 丂ᴏᴍᴇ ᴛᴇ𝕏ᴛ ᴛᴏ şᴇᴛ ɪᴛ ᴀˢ ᴀsŞɪ丂ᴛᴀɴᴛ'𝕤 ʙɪᴏ  😳⛵."
        )


@app.on_message(filters.command(["assname", "setname"]) & SUDOERS)
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            await app2.update_profile(first_name=name)
            return await message.reply_text(
                f"» {ASS_MENTION} ⓃⒶⓂⒺ ⒸⒽⒶⓃⒼⒺⒹ ⓈⓊⒸⒸⒺⓈⓈⒻⓊⓁⓁⓎ."
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        await app2.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"» {ASS_MENTION} ⓃⒶⓂⒺ ⒸⒽⒶⓃⒼⒺⒹ ⓈⓊⒸⒸⒺⓈⓈⒻⓊⓁⓁⓎ.")
    else:
        return await message.reply_text(
            "» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇ丂丂ᴀɢᴇ ᴏʀ ɢɪᴠᴇ 丂ᴏᴍᴇ ᴛᴇ乂ᴛ ᴛᴏ 丂ᴇᴛ ɪᴛ ᴀ丂 ᴀ丂丂ɪ丂ᴛᴀɴᴛ'丂 ɴᴇᴡ ɴᴀᴍᴇ."
        )

import asyncio

import speedtest
from pyrogram import filters

from FallenMusic import SUDOERS, app


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆ 𝔖𝔭𝔢𝔢𝔡 𝔱𝔢𝔰𝔱 𝔬𝔣 𝔇𝔬𝔴𝔫𝔩𝔬𝔞𝔡𝔦𝔫𝔤......**")
        test.download()
        m = m.edit("**⇆ 𝔖𝔭𝔢𝔢𝔡 𝔱𝔢𝔰𝔱 𝔬𝔣 𝔇𝔬𝔴𝔫𝔩𝔬𝔞𝔡𝔦𝔫𝔤...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ 𝕾𝖕𝖊𝖊𝖉 𝕽𝖊𝖘𝖚𝖑𝖙𝖘...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(["speedtest", "spt"]) & SUDOERS)
async def speedtest_function(_, message):
    m = await message.reply_text("**» ℜ𝔲𝔫𝔫𝔦𝔫𝔤 𝔖𝔭𝔢𝔢𝔡𝔱𝔢𝔰𝔱...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **𝕽𝖊𝖘𝖚𝖑𝖙𝖘 𝖔𝖋 𝕾𝖕𝖊𝖊𝖉 𝕿𝖊𝖘𝖙** ✯
    
<u>**𝐂𝐥𝐢𝐞𝐧𝐭 :**</u>
**» __🄸🅂🄿 :__** {result['client']['isp']}
**» __🄲🄾🅄🄽🅃🅁🅈 :__** {result['client']['country']}
  
<u>**𝐒𝐄𝐑𝐕𝐄𝐑 :**</u>
**» __🄽🄰🄼🄴 :__** {result['server']['name']}
**» __🄲🄾🅄🄽🅃🅁🅈 :__** {result['server']['country']}, {result['server']['cc']}
**» __🅂🄿🄾🄽🅂🄾🅁 :__** {result['server']['sponsor']}
**» __🄻🄰🅃🄴🄽🄲🅈 :__** {result['server']['latency']}  
**» __🄿🄸🄽🄶 :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()

#!/usr/bin/python3.5

import asyncio
import fbchat
from Bot import Bot

# channel = 644067409021641
channel = 1106727539435744

client = fbchat.Client("testbotCNK@gmail.com", "Refraction")

bot = Bot(client)
print('Initialization Complete')

async def main():

    flag = False
    flagCheck = []

    while True:
        messages = await onMessage()
        last = messages[0].split(' ')
        print(last)

        if flagCheck != messages[7:]:
            flag = False

        if last[0] == 'Tess!':
            if flag is False:
                await bot.sentence(channel)
                flag = True
                flagCheck = messages[7:]

        if last[0] == '!eroSearch':
            if flag is False:
                flagCheck = messages[7:]
                try:
                    await bot.eroSearch(channel, last[1])
                    flag = True
                except:
                    pass


async def onMessage():
    msgs = []
    messages = await bot.lastMessages(channel)
    for msg in messages:
        msgs.append(msg.body)

    return msgs


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

#!/usr/bin/python3.5

import asyncio
import fbchat
from imagePull import getPic
import markovify

with open('fbMsg.txt') as f:
    texta = f.read()

with open('msgData.txt') as f:
    textb = f.read()

modelA = markovify.NewlineText(texta)
modelB = markovify.NewlineText(textb)

modelCombo = markovify.combine([modelA, modelB], [1.5, 1])

gID = 644067409021641
client = fbchat.Client("testbotCNK@gmail.com", "Refraction")

async def main():

    # group = client.getThreadInfo(gID, 0, thread_type='group')
    # sent = client.send(gID, 'test', message_type='group')

    # await sendPics()
    sentence = modelCombo.make_sentence()
    client.send(gID, sentence, message_type='group')

async def sendPics():
    images = await getPic(3, 'paizuri')

    for img in images:
        print(img)
        img = 'http://' + img[2:]
        client.sendRemoteImage(gID, message_type='group',
                               image=img)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

#!/usr/bin/python3.5

from imagePull import getPic
import markovify
import json


class Bot:

    def __init__(self, client):
        self.client = client

        # Markov Chain
        with open('fbChain.txt', encoding='utf-8') as f:
            jModelA = json.load(f)

        with open('discordChain.txt', encoding='utf-8') as f:
            jModelB = json.load(f)

        modelA = markovify.NewlineText.from_json(jModelA)
        modelB = markovify.NewlineText.from_json(jModelB)

        model = markovify.combine([modelA, modelB], [1.5, 1])
        self.model = model

    async def sendMessage(self, channel, message, cType='group'):
        client = self.client
        sent = client.send(channel, message, message_type=cType)
        return sent

    async def sendPicRemote(self, channel, url, cType='group'):
        client = self.client
        sent = client.sendRemoteImage(channel, message_type=cType,
                                      image=url)
        return sent

    async def lastMessages(self, channel, cType='group'):
        last = self.client.getThreadInfo(channel, 0, 15, thread_type='cType')

        return last

    async def sentence(self, channel):
        text = self.model.make_sentence()
        failed = 'Failed ;A;'
        send = self.sendMessage

        try:
            await send(channel, text)
            print(text)
        except Exception:
            await send(channel, failed)
            print(failed)

    async def eroSearch(self, channel, tags='paizuri'):
        print(tags)
        images = await getPic(3, tags)
        send = self.sendPicRemote

        for img in images:
            url = 'http://' + img[2:]
            await send(channel, url)
            try:
                await send(channel, url)
            except Exception:
                pass

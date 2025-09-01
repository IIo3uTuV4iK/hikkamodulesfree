import random
from asyncio import sleep
import os
from .. import loader, utils


@loader.owner
def register(cb):
    cb(PargeteraKrasMod())


class BladeMod(loader.Module):
    strings = {"name": "[🇰🇷|🇬🇷] Pargetera(☠️//🩸)Kras(⚜️)"}

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

    async def PargeteraKrascmd(self, message):
        '''Паргетера Крас[🦋|❤️\🩸/❤️|🦋]Утсановлен канал @Prgtm_ua'''
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>[<emoji document_id=5274193038892081385>❤️</emoji>]Крововышушение детей шалав Окончено[<emoji document_id=5350310102874203422>🦋</emoji>]</b>")
            return
        await utils.answer(
            message,
            "<b>[<emoji document_id=5274193038892081385>❤️</emoji>]Востановляю Крововышушение Детей шалав[<emoji document_id=5350310102874203422>🦋</emoji>]\n\n",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shabl = [" [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] ɜᴀᴋᴩᴏй ᴇбᴀᴧᴏ унижᴇнᴋᴀ ᴇбᴀнᴀя я ᴛʙᴏю ʍᴀʍᴀɯу ᴇбᴀᴧ [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] " ,

" [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] ᴛы ɜдᴇᴄь ᴛᴇᴩᴨиᴧᴀ ᴇбучᴀя ни нᴀ чᴛᴏ нᴇ ᴄᴨᴏᴄᴏбнᴀя [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] " ,

" [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] ᴦᴏʙнᴏᴩᴏжᴀя ᴛᴇᴧᴏчᴋᴀ ᴋᴏᴛᴏᴩᴀя ничᴇᴦᴏ иɜ ᴄᴇбя нᴇ ᴨᴩᴇдᴄᴛᴀʙᴧяᴇᴛ [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] " ,

" [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] ᴄынуᴧя ɯᴧюхи ᴇбᴀᴧᴏ ᴄʙᴏᴇ ɜᴀᴋᴩᴏй я ᴛᴇбᴇ ʍᴀʍɯᴀу ᴇбᴀᴧ [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] " ,

" [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] ᴏᴛᴄᴏᴄищᴇ ᴇбᴀннᴏᴇ ᴨᴏᴄʍᴇй ᴛуᴛ ᴛᴏᴧьᴋᴏ чᴀᴄ ʙъᴇбᴀᴛь я ᴛᴇбᴇ ʙыᴩʙу ᴋиɯᴋи и ᴄᴋᴏᴩʍᴧю их [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] " ,

" [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] ᴛʙᴏᴇй ʍᴀʍᴀɯᴇ ɯᴧюхᴇ ᴄʙинᴏᴨᴏдᴏбнᴏй  ɯᴧюхи ᴋᴏᴛᴏᴩᴀя ᴛуᴛ чᴧᴇн будᴇᴛ нᴀʙᴏᴩᴀчиʙᴀᴛь ᴨᴏᴛᴏʍ нᴀ ᴇбᴧᴇ ᴄынᴏᴋ ɯᴀᴧᴀʙы ᴄᴩᴀнᴏй [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] " ,

" [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] я ᴛᴇбᴇ ᴩᴇᴀᴧьнᴏ ɜдᴇᴄь чиᴄᴛᴏ ʍᴀʍᴀɯу ᴛʙᴏю ᴨᴩидᴀʙᴧю ᴄʙᴏиʍ хуᴇʍ нᴀчну хуяᴩиᴛь ᴇᴇ ᴛᴩуᴨᴇц ᴋуʙᴀᴧдᴏй дᴏ ᴛᴀᴋᴏй ᴄᴛᴇᴨᴇни чᴛᴏ ᴇᴇ ᴏᴄᴛᴀнᴋи ᴩᴀɜᴧᴇᴛяᴛᴄя нᴀ ᴄᴛᴩᴀᴛᴏᴄɸᴇᴩу [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] " ,

" [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] бᴏᴧʙᴀн ᴇбучий ʙбᴇй ᴄᴇбᴇ ʙ ᴦᴏᴧᴏʙу чᴛᴏ ᴛы ни ɜᴀ чᴛᴏ нᴇ ᴄʍᴏжᴇɯь ᴏᴄиᴧиᴛь ʍᴇня ʙ ϶ᴛᴏʍ ᴦᴏʙнᴏᴋᴏʍьюниᴛи ᴛᴩᴏᴧᴧинᴦᴀ [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] " ,

" [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] ᴄᴧыɯиɯь ʍᴇня ᴨᴇᴦᴀᴄ быᴄᴛᴩᴇᴇ ᴛᴀʍ ᴨᴇчᴀᴛᴀй у ᴛᴇбя ʍᴀʍᴀɯᴀ ɯᴧюхᴀ ᴦᴏʙнᴏᴇбᴧᴀя [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] " ,

" [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] ᴏдин хуй ɜдᴇᴄь нᴇ ᴏᴄиᴧиɯь ʍᴇня ɜᴀбиᴩᴀй ᴄʙᴏи ᴨᴏᴧᴏʍᴀнныᴇ ᴋᴏᴧᴇни и ɯуᴩуй ᴏᴛᴄюдᴀ нᴀ ᴩуᴋᴀх ᴄʙᴏих ʙᴇдь ᴏᴛ ᴛᴇбя нихуя цᴇᴧᴏᴦᴏ нᴇ ᴏᴄᴛᴀᴧᴏᴄь [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] " , 

" [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] ᴀ ну ɜᴀᴋᴩᴏй ᴇбᴀᴧᴏ ᴄучᴇныɯ ᴇбᴀнный я ᴛᴇбя ɜдᴇᴄь унижу ᴋᴀᴋ ɯᴧюху [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] " ,

" [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] ᴛы будᴇɯь ᴛᴀʍ иᴄᴋᴀᴛь ᴏᴨᴩᴀʙдᴀния ᴋᴀᴋ бы быᴄᴛᴩᴇᴇ ᴄʍыᴛьᴄя ᴏᴛ ʍᴏᴇй ᴏᴦᴩᴏʍнᴏй ɜᴀᴧуᴨы и ʍᴏих удᴀᴩᴏʙ [<emoji document_id=5350310102874203422>🦋</emoji>|<emoji document_id=5274193038892081385>❤️</emoji>\<emoji document_id=6037464823959129840>🩸</emoji>/<emoji document_id=5274193038892081385>❤️</emoji>|<emoji document_id=5350310102874203422>🦋</emoji>] " ,]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(shabl)))
            await sleep(time)
# meta author: rudagg
#meta developer: rudagg
import random
from asyncio import sleep
import os
from .. import loader, utils
from telethon.tl.functions.users import GetFullUserRequest
import time 
from telethon.tl.types import Message

@loader.tds
class WounderfullHelp(loader.Module):
    '''Модуль rudagg'''
    strings = {
    "name":  "[🖤] — RυⲇⲁⳒⳒ — [🖤]",
    "loading": "<b>[🖤] — Ⳑⲟⲁⲇⲓⲛⳋ RυⲇⲁⳒⳒ Ⲏⲉⳑⲣ... — [🖤]</b>",
    "not_chat": "<b>[🖤] — Ⲩⲟυ ⲱⲟʀⲋⲏⲓⲣ RυⲇⲁⳒⳒ — [🖤]</b>",} # name loader () \n


    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client
       
    async def rudagghelpcmd(self, message):
        """Запустить анимацию"""
        args = utils.get_args_raw(message)
        await message.edit("[🖤] — R — [🖤]")
        time.sleep(0.1)
        await message.edit("[🖤] — Rυ — [🖤]")
        time.sleep(0.1)
        await message.edit("[🖤] — Rυⲇ — [🖤]")
        time.sleep(0.1)
        await message.edit("[🖤] — Rυⲇⲁ — [🖤]")
        time.sleep(0.1)
        await message.edit("[🖤] — RυⲇⲁⳒ — [🖤]")
        time.sleep(0.1)
        await message.edit("[🖤] — RυⲇⲁⳒⳒ — [🖤]")
        time.sleep(0.1)
        await message.edit("🖤")
        time.sleep(0.1)
        await message.edit("🖤🖤")
        time.sleep(0.1)
        await message.edit("🖤🖤🖤")
        time.sleep(0.1)
        await message.edit("🖤🖤🖤🖤")
        time.sleep(0.1)
        await message.edit("🖤🖤🖤")
        time.sleep(0.1)
        await message.edit("🖤🖤")
        time.sleep(0.1)
        await message.edit("🖤")
        time.sleep(0.1)
        await message.edit("ᏒᏌᎠᎪ")
        time.sleep(0.1)
        await message.edit("ᏒᏌᎠᎪ ᎻᎬᏞᏢ")
        time.sleep(0.1)
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        
        message = await utils.answer(message, self.strings("loading"))

        try:
            user_id = (
                (
                    (
                        await self._client.get_entity(
                        args if not args.isdigit() else int(args)
                        )
                    ).id
                )
                if args
                else reply.sender_id
            )
        except Exception:
            user_id = self._tg_id

            user = await self._client(GetFullUserRequest(user_id))

            user_ent = user.users[0]

            photo = await self._client.download_profile_photo(user_ent.id, bytes)

            user_info = (
            "<b><emoji document_id=5807533543609340621>💀</emoji><emoji document_id=5373290243787070962>💀</emoji><emoji document_id=6037464506131549087>💀</emoji><I>ᏒᏌᎠᎪ ᎻᎬᏞᏢ</I><emoji document_id=5807533543609340621>💀</emoji><emoji document_id=5373290243787070962>💀</emoji><emoji document_id=6037464506131549087>💀</emoji>:</b>\n\n"
            "<b><emoji document_id=5222468670436943157>🤚</emoji>.r4epen - [<emoji document_id=5807533543609340621>💀</emoji>] Задержка + шапка: Запускает модуль Ruda 4epen [<emoji document_id=5807533543609340621>💀</emoji>]</b>\n\n"
            "<b><emoji document_id=5222468670436943157>🤚</emoji>.rger - [<emoji document_id=5810144570192694729>💀</emoji>] Задержка + шапка: Запускает модуль Ruda Germany [<emoji document_id=5810144570192694729>💀</emoji>]</b>\n\n"
            "<b><emoji document_id=5222468670436943157>🤚</emoji>.rskelet - [<emoji document_id=6037464506131549087>💀</emoji>] Задержка + шапка: Запускает модуль по Ruda Skelet [<emoji document_id=6037464506131549087>💀</emoji>]</b>\n\n"
            "<b><emoji document_id=5222468670436943157>🤚</emoji>.rblack - [<emoji document_id=5373290243787070962>💀</emoji>] Задержка + шапка: Запускает модуль Ruda Black [<emoji document_id=5373290243787070962>💀</emoji>]</b>\n\n"
            "<b><emoji document_id=5222468670436943157>🤚</emoji>.rblood - [<emoji document_id=5784988418459046074>💀</emoji>] Задержка + шапка: Запускает модуль Ruda Blood [<emoji document_id=5784988418459046074>💀</emoji>]"
            f"<b>Username:</b> @{user_ent.username or '☠️'}\n"
            f"<b>First name:</b> {user_ent.first_name or '🚫'}\n"
            f"<b>ID:</b> <code>{user_ent.id}</code>\n"
        )

        if photo:
            await self._client.send_file(
                message.peer_id,
                photo,
                caption=user_info,
                link_preview=False,
                reply_to=reply.id if reply else None,
            )
            if message.out:
                await message.delete()
        else:
            await utils.answer(
                message,
                user_info,
                reply_to=reply.id if reply else None,
                link_preview=False,
            )


    async def r4epencmd(self, message):
        '''[ ! ] Запускает модуль: Ruda 4epen [ ! ] \n'''
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Модуль #Ruda4epen остановил пронзание кишок сынков бляди. <emoji document_id=5807533543609340621>💀</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>Модуль #Ruda4epen начал пронзание кишок сынков бляди. <emoji document_id=5807533543609340621>💀</emoji>\n\n"
            "<emoji document_id=5222468670436943157>🤚</emoji> Чтобы остановить, пиши <code>.r4epen</code></b>"
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shabl = [ 
        "<emoji document_id=5807533543609340621>💀</emoji> ዘ𐌳 𐌲ᱛᱞꤕ ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ᱬ𐌳ተᱩ ꤕऊሃ ተꤕ ᱴᱛ ᱬሃንᱟઝ𐌳ᱤᱩዘᱛᱬሃ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ꤍᱤᱟᱦᱢᱦᱩ, 𐌓 ተꤕऊꤕ ꤕऊ𐌳ᱤᱩዘᱢઝ 𐌗ሃёᱬ ᱞ𐌳ንऊᱢଓ𐌳ᱵ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ተᱟ 𐌍ሃઝ𐌍𐌳 ꤕऊ𐌳ዘ𐌳𐌓 <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍᱢ ᱬዘꤕ ᱚꤕተઝ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍᱢ ᱬዘꤕ ꤍሃ𐌍ઝ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛઝ𐌳 ተᱟ ᱬዘꤕ ᱤᱢ𐌟ꤕᱦᱩ 𐌓ᱢԱ𐌳, 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ᱢꤍተᱞꤕऊᱤ𐌓ᱵ ଓᱛ ꤍᱤ𐌳ଓሃ #𐌳ᱚ𐌳ᱬଓ𐌳ꤕ𐌖 #ተ𐍂𐌳𐌗ተᱛ𐌖 <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተꤕऊꤕ ᱬ𐌳ተᱩ ଓᱟꤕऊ𐌳ᱤ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተꤕऊꤕ ᱬ𐌳ተᱩ ሃऊᱢᱤ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተꤕऊꤕ ᱬ𐌳ተᱩ ᱢꤍተᱞꤕऊᱢᱤ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተꤕऊꤕ ᱬ𐌳ተᱩ 𐌗ሃёᱬ ꤍᱤᱛᱬ𐌳ᱤ<emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊሃ 𐌍ꤕᱞꤕን ᱷꤕઝᱛᱤᱚሃ ଓ ᱚଓꤕᱞᱢ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ᱦᱴᱞꤕ𐌗𐌳ᱵ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተꤕऊꤕ ᱬ𐌳ተᱩ ꤕऊꤕዘᱵ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ 𐌗ሃёᱬ ᱚሃᱦሃ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተꤕऊꤕ ᱬ𐌳ተᱩ ꤕऊꤕዘᱢᱤ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ 𐌗ሃёᱬ ንሃऊᱟ ଓᱟऊᱢଓ𐌳ᱤ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ꤍᱤᱟᱦᱢᱦᱩ ᱬꤕዘ𐌓 ሃተઝ𐌳ዘᱛꤍ ꤕऊ𐌳ዘᱟᱢ 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ᱷ𐌳ꤍ ꤕऊꤕዘᱵ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ተᱟ ᱴ𐌳ꤍઝሃᱚ𐌳 ꤕऊ𐌳ዘ𐌳𐌓 ઝሃᱚ𐌳 ተᱟ ᱴᱛተሃ𐌗ᱤ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ተꤕᱤᱛ𐌍ઝ𐌳 ዘꤕ ᱴᱛተሃ𐌗𐌳ᱢ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ተꤕᱤᱛ𐌍ઝ𐌳, 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ᱞꤕ𐌲𐌳ᱤ ଓ ᱴᱛᱞዘ𐌗𐌳ऊꤕ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ተꤕᱤᱛ𐌍ઝ𐌳, 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ዘ𐌳 ꤍઝ𐌳ᱤꤕ ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ꤍଓᱢዘᱛᱬ𐌳ተઝ𐌳 ተᱟ ꤕऊ𐌳ዘ𐌳𐌓 <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተꤕऊꤕ ተሃተ𐌳 ᱬ𐌳ተᱩ 𐌗ሃ𐌓𐌍ሃ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ଓ 𐌗ሃᱢ ᱬዘꤕ ᱴᱛᱤንᱢ ተꤕᱤᱛ𐌍ઝ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱢᱦᱩ ઝ𐌳ઝ ଓ 45 𐌲ᱛᱚሃ ተଓᱛᱵ ᱬ𐌳ተᱩ ᱢꤍተᱞꤕऊᱤ𐌓ᱤ ዘ𐌳 ଓᱛᱢዘꤕ ଓᱛ ꤍᱤ𐌳ଓሃ 3-ሃ ᱞꤕᱢ𐌗ሃ? <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊꤕዘᱢᱤ ᱴᱛ ઝᱞ𐌳𐌓ᱬ 𐌲ᱛᱞઝᱢ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦ ተᱟ ᱬዘꤕ ᱴᱞᱛଓ𐌳ᱤᱩዘᱛ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦ ተᱟ ᱬዘꤕ 𐌗ᱛᱞᱛᱦᱛ 𐌟ꤕ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦ ተᱟ ᱬዘꤕ ઝ𐌳ઝ ዘ𐌳ᱚᱛऊዘᱛ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊሃ ꤍᱤᱟᱦ ተᱟ 𐌍ሃᱚ𐌳ઝ ꤕऊ𐌳ዘᱟᱢ 𐌳ᱞሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃᱢԱ𐌳 ᱬᱛꤕ𐌲ᱛ ꤍᱛꤍዘᱢ ᱤሃ𐌍ᱦꤕ ऊᱤ𐌓ᱚᱢዘ𐌳 ઝᱛዘ𐌍ꤕዘ𐌳𐌓 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ᱛᱴ𐌳ᱞᱟᱦ ተᱟ ꤕऊ𐌳ዘᱟᱢ ꤍሃઝ𐌳 𐌳ᱞሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍᱛꤍዘᱢ ᱬᱛꤕ𐌲ᱛ 𐌗ሃᱢԱ𐌳 ऊᱤ𐌓ᱚᱛꤕऊ ꤍሃઝ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ଓዘ𐌳ተሃᱞꤕ ተଓᱛᱵ ᱬ𐌳ተᱩ ዘ𐌳 ꤍଓᱛꤕᱬ 𐌗ሃꤕ ᱴᱛ𐌗ᱛᱞᱛዘᱵ ઝ𐌳ઝ ᱢ ଓꤕꤍᱩ ተଓᱛᱢ ᱴᱞᱛଓ𐌳ᱤᱩዘᱟᱢ ተᱞᱛᱤᱤᱢዘ𐌲 ᱬᱚꤕ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ଓ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤍଓᱛᱢ 𐌗ሃᱢ ተᱟઝ𐌳ᱵ ተ𐌳ઝ ተᱛ ऊᱤ𐌓ተᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተꤕ ን𐌳ᱤሃᱴᱛᱢ ዘ𐌳𐌗ሃᱢ ᱴᱞᱛઝᱞሃ𐌍ሃ ᱴᱞᱛተᱢଓ 𐌍𐌳ꤍᱛଓᱛᱢ ꤍተᱞꤕᱤઝᱢ ተᱟ ऊᱤ𐌓ተᱩ ᱛऊᱛꤍꤍ𐌳ዘ𐌳𐌓 𐌳ᱞሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ተᱟ ᱬᱛᱢ 𐌗ሃᱢ ꤍଓᱛᱢᱬᱢ 𐌲ሃऊ𐌳ᱬᱢ ऊᱛᱞᱛንᱚᱢᱤ ᱬᱛᱞ𐌓ઝ ꤕऊ𐌳ዘᱟᱢ ꤍሃઝ𐌳 𐌳𐌗𐌳𐌗 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተꤕ ᱴᱛ ऊᱛᱞᱛᱚꤕ ᱴᱞᱛଓᱛᱚᱢᱤ ଓዘ𐌳ተሃᱞꤕ 𐌳𐌗𐌳𐌗 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍᱛꤍꤕᱦ ተᱟ ᱬዘꤕ ᱴᱛ ऊᱤ𐌳ዘተሃ ऊᱤ𐌓ᱚᱢዘ𐌳 ꤍꤍ𐌳ዘ𐌳𐌓 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ዘ𐌳 ꤍଓᱛᱢ 𐌗ሃᱢ ዘ𐌳ꤍ𐌳ᱚᱢᱤ ઝ𐌳ઝ ꤕऊ𐌳ዘሃᱵ ꤍዘ𐌳ꤍተᱩ ዘ𐌳 ሃᱚᱛ𐌍ઝሃ ઝ𐌗ꤕ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ተᱟ ꤍ𐌳ꤍꤕᱦ ઝ𐌳ઝ ተᱛ ዘꤕ ᱴᱞ𐌳ଓᱢᱤᱩዘᱛ <emoji document_id=5807533543609340621>💀</emoji>",
                 " <emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ᱛऊᱛꤍꤍ𐌳ᱤ 𐌟ꤕ ଓዘ𐌳ተሃᱞꤕ",
                 " <emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃ𐌓 ተᱟ ᱬᱛꤕ𐌲ᱛ ꤍᱛꤍ𐌳ᱤ ᱴᱞᱢऊᱤꤕ𐌟ꤕዘዘᱛ <emoji document_id=5807533543609340621>💀</emoji>",
                 " <emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ଓዘ𐌳ተሃᱞꤕ 𐌗ሃꤕᱬ ዘ𐌳 𐌳ᱞऊᱢተሃ ᱴ𐌓ተᱩᱚꤕꤍ𐌓ተ ᱚଓ𐌳 ᱛተᱴᱞ𐌳ଓᱢᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 " <emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃᱢ ተᱟ ᱬᱛᱢ ꤍᱛꤍ𐌳ᱤ ᱢ ተᱛ𐌍ઝ𐌳 ዘ𐌳 𑁌ተᱛᱬ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ଓዘ𐌳ተሃᱞꤕ ዘ𐌳 ꤍଓᱛᱢ 𐌗ሃᱢ ᱴᱛ ꤍ𐌳𐌟ሃ, ऊሃᱚꤕተ ઝ𐌳ઝ ꤕऊ𐌳ዘᱟᱢ 𐌍𐌳ꤍᱛଓᱛᱢ ꤍሃઝ𐌳 ଓ ऊᱢዘᱛઝᱤᱩ ንᱟᱞᱢተᱩ ᱢꤍઝ𐌳ተᱩ ᱬᱛᱵ ን𐌳ᱤሃᱴሃ ઝ𐌗ꤕ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ᱞ𐌳ᱦሃ <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተꤕऊ𐌓 ꤕऊ𐌳ᱞᱢᱞሃᱵ ᱛተᱞሃऊꤕዘᱩ ꤕऊ𐌳ዘᱟᱢ <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> ꤍተꤕᱞଓ𐌓ተዘᱢઝ ꤕऊ𐌳ዘᱟᱢ ተꤕऊꤕ ઝᱤᱵଓ ꤍᱤᱛᱬ𐌳ᱤ 𐌗ሃꤕᱬ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴ𐌳ᱚ𐌳ᱞᱛ𐌍ዘ𐌳 ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> ᱬ𐌳ᱬ𐌳ዘ ተଓᱛᱵ ꤕऊ𐌳ᱦᱢᱞᱛଓ𐌳ᱤ ଓ ᱴ𐌳ઝᱢꤍተ𐌳ዘꤕ <emoji document_id=5807533543609340621>💀</emoji>","<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦ ઝ𐌳ઝ ዘᱞ𐌳ଓꤍተଓꤕዘዘᱟᱢ <emoji document_id=5807533543609340621>💀</emoji>","<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦᱩ ዘ𐌳 ꤍꤕઝሃዘᱚᱟ <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> ᱞᱛଓዘᱛ ᱴᱛ ተᱞ𐌳ꤕઝተᱛᱞᱢᱢ  ꤍ𐌳ꤍꤕᱦ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤕऊ𐌳ᱞᱢᱞᱛଓ𐌳ᱤ ተଓᱛᱵ ꤍꤕᱬꤕᱢઝሃ ꤍଓᱛᱢᱬ ᱢꤍተᱞꤕऊᱢተꤕᱤᱩꤍઝᱢᱬ 𐌗ሃꤕᱬ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦᱩ ዘᱛଓᱛ𐌲ᱛᱚዘ𐌓𐌓 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍԱሃ ተꤕ ଓ ઝᱢᱦᱛઝ <emoji document_id=5807533543609340621>💀</emoji>",
                 " <emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 𐌲ᱤ𐌳𐌲ᱛᱤꤕᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌳ऊᱢᱚዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 " <emoji document_id=5807533543609340621>💀</emoji> ᱴሃऊᱤᱢ𐌍ዘ𐌳 ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ଓᱟઝሃᱞꤕᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 " <emoji document_id=5807533543609340621>💀</emoji> ዘᱢንઝ𐌳 ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 " <emoji document_id=5807533543609340621>💀</emoji> ꤕऊሃ ተ𐌓 ᱴ𐌳ᱤᱢଓዘ𐌳 ሃ𐌟ᱢ <emoji document_id=5807533543609340621>💀</emoji>",
                 " <emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ᱚ𐌳ଓꤕᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 " <emoji document_id=5807533543609340621>💀</emoji> ᱴꤕꤍᱚሃ ተꤕ 𐌗ሃꤕᱬ ᱴ𐌳ᱬꤕተꤕᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 " <emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦᱩ ꤍᱴᱛઝᱛᱢዘ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤕऊሃ ተ𐌓 ଓ ᱚꤕᱞꤕଓሃᱷઝꤕ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴꤕꤍተሃ ተꤕ 𐌗ሃꤕᱬ ተሃᱦᱢᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌘ᱞ𐌳ዘተ𐌳ᱤᱩዘ𐌳 ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 " <emoji document_id=5807533543609340621>💀</emoji> ઝ𐌳ઝ ଓ ꤍተ𐌳ᱞᱢዘሃ ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 𐌳ተԱꤕᱴᱢᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 " <emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦᱩ ᱴᱞꤕᱚሃᱞઝᱛଓ𐌳ተ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 " <emoji document_id=5807533543609340621>💀</emoji>ଓꤕᱤᱢઝ𐌳 ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌟ᱛᱴᱛऊᱤ𐌓ᱚꤍઝᱢᱢ ꤕऊᱤᱢ𐌲𐌳ᱚ ተᱟ ꤍሃઝ𐌳 <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> 𐌲ዘᱢᱚᱛᱬሃᱚᱟᱢ 𐌲ᱤሃ𐌗ᱛᱚᱞᱟᱷ ꤍᱛꤍዘᱢ <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> ꤍઝᱛተᱛ𐌟ᱢᱞዘᱟᱢ ઝᱞᱢଓᱛઝᱞᱟᱤ 𐌗ሃᱢ ꤍᱤᱛଓᱢ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍᱞ𐌳ઝᱛꤍሃ𐌍ᱢᱢ 𐌲ዘᱢᱚᱛተᱞ𐌓ꤍ 𐌗ሃꤕᱬ ተ𐌓 ሃऊᱩᱵ <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> ꤕऊሃ ተଓᱛᱵ ᱬ𐌳ተᱩ ᱛዘ𐌳 ᱬዘꤕ 𐌗ሃᱢ ꤍᱛꤍꤕተ ऊᱤ𐌓 ᱚሃᱞ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌳 ተᱟ ᱬᱛᱢ 𐌗ሃᱢ ଓን𐌳ᱬꤕꤍተᱛ ꤍᱛꤍઝᱢ ꤍᱛꤍ𐌳ᱤ 𐌟ꤕ <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ 𐌓 ઝ𐌳ઝ ተଓᱛᱵ ᱬ𐌳ተᱩ 𐌓ᱢԱ𐌳ᱬᱢ ᱴᱞᱢᱚ𐌳ଓᱢᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ଓ ᱦઝᱛᱤᱩዘᱛᱬ ተሃ𐌳ᱤꤕተꤕ  <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ઝሃᱞᱢᱤઝᱢ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ꤕऊ𐌳ᱤ ተଓᱛᱵ ᱬ𐌳ተᱩ ሃ ᱴᱢଓዘሃᱦઝᱢ <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ን𐌳 ᱬ𐌳𐌲𐌳ንᱛᱬ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ተᱞሃऊዘᱛ𐌲ᱛ ን𐌳ଓᱛᱚ𐌳 <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ᱤꤕꤍተዘᱢԱᱟ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ᱚꤕᱞꤕଓ𐌳 <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ᱛઝዘ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ᱴᱛꤍተᱛ𐌓ዘዘᱛ ଓ ᱞᱛተ <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ሃዘᱢተ𐌳ን𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ᱴᱤᱢተᱟ <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ᱞ𐌳ઝᱛଓᱢዘᱟ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ଓ𐌳ዘዘᱟ <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ઝᱛᱬᱛᱚ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ተሃᱬऊᱛ𐌍ઝᱢ <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ઝ𐌳ᱴᱛተ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ଓꤕᱢᱴ-ᱦᱛᱴ𐌳 <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ꤍꤕઝꤍ-ᱦᱛᱴ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ઝᱛꤍᱬᱢተᱢ𐌍ꤕꤍઝᱛ𐌲ᱛ ᱬ𐌳𐌲𐌳ንᱢዘ𐌳 <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ᱴꤕᱞꤕᱚ ተ𐌳ऊ𐌳𐌍ઝᱛᱢ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ዘᱛ𐌲ᱢ ተꤕ 𐌳ऊ𐌳ꤍԱ𐌳ᱤ ꤍᱤꤕ𐌗ઝ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴ𐌳ऊꤕᱚዘ𐌳 ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ઝ𐌳ዘተሃንꤕᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦᱩ ꤍ ᱴᱞꤕꤍተᱢ𐌟𐌳ᱬ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ଓ ተ𐌓 ꤍԱሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ዘ𐌳ᱢꤍ𐌳ଓ𐌳 ꤍ𐌳ꤍꤕᱦᱩ 𐌍ᱛተ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦᱩ ꤍ ऊᱛઝሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ꤕ𐌗 ᱴꤕꤍተሃ ተଓᱛᱵ 𐌗ሃꤕᱬ ን𐌳ᱚꤕᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦᱩ 𐌍ᱛተዘ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱞᱛꤍଓꤕተᱤᱢᱤ ተ𐌓 𐌗ሃꤕᱬ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ଓꤕᱤᱢઝ𐌳ᱤꤕᱴዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ᱴꤕᱞꤕꤍተ𐌳ଓꤕᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ऊꤕን 𐌍ꤕꤍተᱢ ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ን𐌳ઝ𐌳ᱤᱛᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦᱩ ᱢᱬሃዘᱢተꤕተዘ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ተᱞᱛ𐌲𐌳ᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ऊꤕንᱞ𐌳ऊᱛተዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ଓ ଓ𐌳ᱤᱩꤕᱞꤕ ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ᱴᱞ𐌳𐌳𐌲ᱞᱢᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍԱሃ ተꤕ ଓ ሃ𐌗𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱬ𐌳ᱬ𐌳ዘ ተଓᱛ𐌓 ऊᱤ𐌓ᱚᱢዘ𐌳 ᱬዘꤕ ꤍᱛꤍ𐌳ᱤ𐌳 ᱴᱞᱢઝ𐌳ᱤᱢꤍᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴ𐌳ଓ𐌳ᱚዘ𐌳 ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ሃꤍᱢᱤꤕᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ଓᱟᱴᱞ𐌓ᱬᱢᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ଓᱟଓꤕን <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴ𐌳ᱬᱢዘሃተዘ𐌳 ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱞᱛꤍተᱢተሃተᱦዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ଓᱟᱴᱤ𐌳ተዘ𐌳 ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦᱩ ᱚꤕᱴ𐌳ንᱢተዘ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴꤕᱞꤕଓꤕን ተ𐌓 𐌗ሃꤕᱬ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ଓ ᱴꤕ𐌍ꤕዘઝሃ ተꤕ ꤍԱሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 𐌳𐌲ᱞᱵ ꤍ𐌍𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ሃऊᱢᱤ ተ𐌓 𐌗ሃꤕᱬ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦᱩ ᱴ𐌳ᱚ ተᱞ𐌳ᱴ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ଓᱟᱴᱞ𐌳ଓ𐌳ᱚᱢᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍተᱛᱴሃᱚᱛଓ𐌳 ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ᱴᱞ𐌳ᱴᱢᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ን𐌳 ᱴ𐌳𐌍ઝሃ ተ𐌓 ᱢᱴሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ઝ𐌳ꤍተᱞᱢᱞ𐌳ଓ𐌳ᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ተᱛዘઝ𐌳 ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤕऊሃ ተ𐌓 ᱴ𐌳ᱚ ዘ𐌳ᱴᱞ𐌓𐌟ꤕዘᱢꤕᱬ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ଓ ઝᱛꤍᱬ𐌳ꤍ ᱛተᱴᱞ𐌳ଓꤕᱤ <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ን𐌳ᱚᱞᱛተઝሃ <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ዘ𐌳 ꤍଓ𐌳ᱤઝꤕ <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ଓ ᱴꤕንᱚሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ 𐌟ᱢᱞዘሃᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ꤍଓᱢዘᱩᱵ <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ऊᱤ𐌓ᱚሃ𐌗ሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ꤕᱷꤕ ᱬᱛᱤᱛᱚሃᱵ <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ᱦꤕꤍተꤕᱞઝሃ ꤕऊ𐌳ᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ተଓᱛᱵ ᱬ𐌳ተᱩ ᱦᱤᱵ𐌗ሃ ꤕऊ𐌳ᱤ ଓ ᱞᱛተ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ዘꤕଓᱢᱚᱢᱬሃᱵ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ଓ 𐌲ᱞᱛऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተꤕऊꤕ ଓ ᱞᱛተ ꤍᱞ𐌳ᱤ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተꤕऊꤕ ዘ𐌳 ઝᱤᱟઝ ઝᱢዘሃᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተᱟ ꤍᱛꤍ𐌳ᱤ ᱬዘꤕ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ተꤕऊ𐌓 ᱦᱤᱵ𐌗ሃ ଓ ተሃ𐌳ᱤꤕተꤕ ઝᱤሃऊ𐌳 ꤕऊ𐌳ᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ଓ ᱞᱛተ ଓ ሃᱤᱢ𐌍ዘᱛᱬ ተሃ𐌳ᱤꤕተꤕ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ଓ ᱚሃᱬꤕ ተꤕऊ𐌓 ꤕऊ𐌳ᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱬ𑁌ᱞᱢᱢ <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ऊꤕᱤᱛ𐌲ᱛ ᱚᱛᱬ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ 𐌳ᱬ𐌘ᱢተꤕ𐌳ተᱞ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱬሃንꤕ𐌓 <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji>  ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ተᱵᱞᱩᱬᱟ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱴ𐌳ᱞઝᱛଓઝᱢ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ 𐌟ᱚ ଓᱛઝንን𐌳ᱤ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ዘ𐌳 ᱞꤕᱤᱩꤍ𐌳𐌗 <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ተଓᱛꤕᱢ ᱬ𐌳ᱬᱟ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ዘ𐌳 ᱚᱢଓ𐌳ዘꤕ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱴᱛᱚъꤕንᱚ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ꤍ𐌳ᱬᱛᱤꤕተ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱚሃᱦꤕଓᱛᱢ ઝ𐌳ऊᱢዘઝᱢ <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ተ𐌳ᱴᱛ𐌍ઝ𐌳ᱬᱢ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱤꤕꤍዘᱛᱢ ᱛᱴሃᱦઝᱢ <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ઝᱤ𐌳ꤍꤍ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ 𐌳ሃᱚᱢተᱛᱞᱢᱢ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ሃ𐌍ᱢተꤕᱤᱩꤍઝᱛᱢ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱚꤕઝᱛዘ𐌳ተ𐌳 <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ꤍ𐌳ᱚᱢઝ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱴ𐌳ᱞઝᱛଓઝᱢ ዘ𐌳 ଓተᱛᱞᱛᱬ 𑁌ተ𐌳𐌟ꤕ <emoji document_id=5807533543609340621>💀</emoji>", "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱤᱢ𐌘ተ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ऊ𐌳ᱞ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ꤍተᱛᱢᱤ𐌳 ዘ𐌳 ᱚᱢઝᱛᱬ ን𐌳ᱴ𐌳ᱚꤕ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ଓᱢተᱞᱢዘᱟ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ऊ𐌳ዘઝᱛᱬ𐌳ተ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱴᱛᱤᱢԱꤕᱢꤍઝᱛ𐌲ᱛ ሃ𐌍𐌳ꤍተઝ𐌳 <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ଓᱛꤕዘዘᱛᱢ 𐌍𐌳ꤍተᱢ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ଓᱛꤕዘઝᱛᱬ𐌳ተ𐌳 <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ᱬꤕ𐌟 ᱞꤕऊꤕᱞ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ዘ𐌳 ꤍᱢᱤꤕ ଓᱛᱤᱢ <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 𐌍ꤕᱞꤕን ᱚሃᱦሃ <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ଓ ᱚሃᱦꤕ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ઝ𐌳ዘ𐌳ଓᱟ <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ऊꤕንᱴᱞᱢᱞᱟଓዘᱛ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌳 ተᱟ ꤍଓᱛᱢᱬ 𐌓ንᱟઝᱛᱬ ᱬዘꤕ ଓ ઝᱛᱤᱛઝᱛᱤ𐌳 ऊᱢᱤ ઝ𐌳ઝ ଓ Աꤕᱞઝଓᱢ  <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ Աꤕᱞઝଓᱢ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ᱴᱛꤍᱛᱤᱩꤍተଓ𐌳 <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ᱛꤍଓꤕ𐌟𐌳ᱤ 𐌗ሃꤕᱬ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ᱞଓ𐌳ᱤ 𐌗ሃꤕᱬ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ᱴᱛ ꤍሃተᱢ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ ᱬᱛᱞ𐌳ᱤᱩዘᱛ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ 𐌍ተᱛ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ᱚᱢઝ𐌳  <emoji document_id=5807533543609340621>💀</emoji>",

"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛᱬዘᱵ 𐌍ተᱛ ተଓᱛ𐌓 ᱬ𐌳ተᱩ ᱦᱤᱵ𐌗𐌳 ꤕऊ𐌳ዘ𐌳𐌓 ᱬዘꤕ ꤍᱛꤍ𐌳ᱤ𐌳 ઝ𐌳𐌟ᱚᱟᱢ ᱚꤕዘᱩ ଓ ᱦઝᱛᱤꤕ  <emoji document_id=5807533543609340621>💀</emoji>",
		"<emoji document_id=5807533543609340621>💀</emoji> ን𐌳ઝᱞሃተꤕᱤ ተ𐌓 ଓ 𐌗ሃꤕ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ዘᱢዘ𐌳ᱞᱬ𐌳ተᱢଓዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ଓᱟꤍተ𐌳ଓꤕᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦᱩ ᱴ𐌳 ꤍተꤕᱴꤕዘᱚᱢᱢ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤕऊሃ ተ𐌓 ን𐌳 ᱚꤕᱴᱤᱛᱬ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ଓꤍᱴᱛᱬዘꤕᱤ ተ𐌓 𐌗ሃꤕᱬ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ዘ𐌳 ꤍᱢᱤꤕଓᱛᱤꤕ ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ዘ𐌳 ተ𐌓 ᱞሃ𐌗ዘሃᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ን𐌳ꤕऊ𐌳ተ𐌳 ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ሃᱚᱛऊᱞᱢᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱚ𐌳ᱞᱛ𐌟ዘ𐌳 ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴ𐌳 ᱴᱞꤕ𐌟ዘꤕᱬሃ ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤕऊሃ ተ𐌓 ᱴ𐌳ᱚ ଓ𐌳ᱚᱛᱢ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ሃऊꤕᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴᱛ 𐌗ሃᱵ ተ𐌓 ଓᱛᱚꤕᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ઝ𐌳𐌍𐌳ᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍᱴꤕԱᱢ𐌘ᱢ𐌍ዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ઝ𐌳ᱢ𐌘ᱛଓ𐌳 ተ𐌓 ᱴ𐌳 ꤕऊ𐌳ᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍᱢᱤᱩዘ𐌳 ተᱞ𐌳𐌗𐌳ᱵ ተ𐌓 <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦᱩ ᱴ𐌳ᱚ ᱤꤍᱚ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ଓᱟᱴᱞ𐌳ଓ𐌳ᱚᱢᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱴ𐌳 ዘ𐌳ଓ𐌳𐌲ᱛᱚዘꤕᱬሃ ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍઝᱛᱤᱩንઝ𐌳 ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ଓ ዘᱛንᱚᱞꤕ ተꤕ ꤍԱሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱬ𐌳ꤍꤍᱛଓ𐌳 ተ𐌓 𐌗ሃꤕᱬ ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ઝ𐌳ઝ 𐌍ꤕᱬᱴᱢᱛዘ ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱬᱢᱞዘ𐌳 ተ𐌓 𐌳ऊ𐌳ꤍԱ𐌳ᱤ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ᱤꤕ𐌲𐌳ᱤᱩዘ𐌳 ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦᱩ ઝ𐌳ઝ ᱚᱢ𐌲𐌲ꤕᱞ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> ઝ𐌳ઝ ઝᱛዘꤍᱛᱬᱛᱤᱩꤍઝ𐌳𐌓 ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji>  ꤕऊሃ ተ𐌓 ઝ𐌳ઝ ଓᱞꤕᱬꤕዘዘሃᱵ <emoji document_id=5807533543609340621>💀</emoji>",
                 "<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ଓ ተꤕ ᱴሃተᱢᱦꤕተꤍଓᱛଓ𐌳ᱤ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱛተᱤᱢ𐌍ዘ𐌳 ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ଓꤕᱞዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተꤕऊꤕ ଓ ᱞᱛተ ዘ𐌳ꤍᱞሃ 𐌗ሃꤕꤍᱛꤍᱢᱷꤕ ꤍᱤ𐌳ऊᱛዘꤕଓᱞᱛንዘᱛꤕ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ଓዘ𐌳ተሃᱞꤕ 𐌗ሃꤕᱚᱤᱢዘᱢተꤕᱤᱩዘ𐌳𐌓 ऊᱤ𐌓ᱚሃᱦᱢዘઝ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተ𐌓 ᱛተᱴꤕንᱚꤕᱤ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱴᱢንᱚ𐌳ᱴёᱞઝ𐌳 ꤕऊ𐌳ዘ𐌳𐌓 𐌓 𐌟ꤕ ተଓᱛᱵ ᱬ𐌳ᱬ𐌳ᱦሃ ଓ ᱞᱛተ ꤕऊ𐌳ᱤ ᱴᱛઝ𐌳 ተᱟ ᱬᱛᱢ 𐌓ᱢԱ𐌳 𐌗𐌳ଓ𐌳ᱤ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃᱢ ᱤᱛଓᱢ ꤍᱟዘᱛઝ ᱦᱤᱵ𐌗ᱢ ꤍተᱞ𐌳ዘዘᱛ𐌲ᱛ ꤍꤕᱬꤕᱢꤍተଓ𐌳 ᱛᱤᱢ𐌲ᱛ𐌘ᱞꤕዘᱛଓ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ꤍ𐌳ꤍꤕᱦᱩ ઝ𐌳ઝ ꤍተ𐌳ᱞᱴꤕᱞ <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ଓ ᱞᱛተ ተꤕऊ𐌓 ꤕऊ𐌳ᱤ ᱬᱞ𐌳ንᱛተ𐌳 ꤍꤍ𐌳ዘ𐌳𐌓 ተᱟ ᱛተꤍᱛꤍᱢ ተ𐌳ᱬ ᱦᱤᱵᱦꤕዘᱩઝ𐌳𐌓 ꤕऊሃዘ𐌓𐌍𐌳𐌓 <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ᱬ𐌳ᱬ𐌳ዘ 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ᱴᱢንᱚ𐌳𐌲ᱛᱤᱛଓ𐌳𐌓 ተଓ𐌳ᱞᱩ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ऊᱤ𐌓 ऊሃᱚሃ ተ𐌓 ꤕऊሃ <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ተᱟ ऊᱤ𐌓ተᱩ ᱦᱤᱵ𐌗𐌳 ꤕऊ𐌳ዘ𐌳𐌓 <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ઝᱤᱵઝଓᱛꤍᱞ𐌳ዘᱢᱷꤕ ꤍଓᱛꤕ ን𐌳ઝᱞᱛᱢ ᱬᱞ𐌳ንᱢዘᱢዘ𐌳 ꤕऊ𐌳ዘ𐌳𐌓 <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ꤕऊሃ ተ𐌓 ዘ𐌳ꤍᱢᱤᱩዘ𐌳 <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተꤕऊ𐌓 𐌳ዘዘᱢ𐌲ᱢᱤᱢᱞᱛଓ𐌳ᱤ ᱦᱤᱵ𐌗𐌳 ተꤕᱞᱴᱢᱤᱢଓ𐌳𐌓 ᱛተꤍᱛꤍᱢ 𐌲ᱞᱵ <emoji document_id=5807533543609340621>💀</emoji>",
"<emoji document_id=5807533543609340621>💀</emoji> ऊሃઝଓ𐌳ᱤᱩዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> 𐌗ሃꤕᱬ ተꤕऊ𐌓 ተᱛᱞᱬᱛᱦᱢᱤ ᱦᱤᱵ𐌗𐌳 ꤕऊሃ𐌍𐌳𐌓 <emoji document_id=5807533543609340621>💀</emoji>", 
"<emoji document_id=5807533543609340621>💀</emoji> ꤍᱛꤍዘᱢ ንᱚꤕꤍᱩ 𐌗ሃꤕᱴᱤꤕተᱢᱷꤕ ꤍꤍ𐌳ዘᱛꤕ ꤕऊ𐌳ዘᱛꤕ 𐌗𐌳𐌗𐌳 <emoji document_id=5807533543609340621>💀</emoji>"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(shabl)))
            await sleep(time)
            
    async def rgercmd(self, message):
        '''[ ! ] Запускает модуль: Ruda Germany (Media) [ ! ]'''
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Модуль #RudaGermany закончил православие. <emoji document_id=5810144570192694729>💀</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>Модуль #RudaGermany начал православие. <emoji document_id=5810144570192694729>💀</emoji>\n\n"
            "<emoji document_id=5222468670436943157>🤚</emoji> Чтобы остановить православие, пиши <code>.rger</code></b>",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        media = reply.media
        shablon = [ 
        "<emoji document_id=5810144570192694729>💀</emoji> ૯ઠƴ ੮ɞ૦ю ⲙɑ੮ь η૦ ઠƿυ੮ɑⲏςκυ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲙⲟύ ⲡⲁⲩⲕ ⲡⲩⲥⲕⲁⲉⲧ яⲇ ⲃ ⲧⲃⲟю ⲙⲁⲧь?",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥёⲧ ⲙⲟⲉⲙⲩ ⲡⲁⲩⲕⲩ, ⳡⲧⲟⳝы ⲟⲏ ⲉё ⲏⲉ ⲩⳝυⲃⲁⲗ ⲥⲃⲟυⲙ яⲇⲟⲙ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲃⲉⲣⲧυⲕⲁⲗьⲏⲟ ⲥⲟⲥⲉⲱь ⲙⲏⲉ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲕⲟⲣⲟⲗⲉⲃⲁ ⲡⲁⲩⲕⲟⲃ ⲡⲣυⳅⲃⲁⲗⲁ ⲇⲉⲧⲉύ ⲡⲁⲩⲕⲟⲃ υ ⲟⲏυ υⲇⲩⲧ ⲧⲉⳝя ⲉⳝⲁⲧь",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧⲃⲟя ⲙⲁⲧь ⲃⲕⲟⲗⲟⲗⲁ ⲥⲉⳝⲉ ⲏυⲕⲟⲧυⲏ, υ ⳃⲁⲥ ⲭⲟⲇυⲧ ⲥⲟⲥёⲧ ⲃⲥⲉⲙ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⳡⲧⲟⳝы ⲥⲟⲅⲣⲉⲧьⲥя ⳅυⲙⲟύ, я ⳅⲁⲥⲩⲏⲩⲗ ⲥⲃⲟύ ⳡⲗⲉⲏ ⲃ ⲧⲃⲟю ⲙⲁⲧь",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲡⲟⳝⲗяⲇь ⲧы ⲉⳝⲁⲏⲁя",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲕⲩⲇⲁ ⲧы ⲡⲟⲧⲩⲭⲁⲉⲱь ⲇⲉⲃⲟⳡⲕⲁ?",
		"<emoji document_id=5810144570192694729>💀</emoji> Я ⲏⲉ ⲣⲁⳅⲣⲉⲱⲁⲗ ⲧⲉⳝⲉ ⲃⲥⲧⲁⲃⲁⲧь ⲥ ⲕⲟⲗⲉⲏ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲇⲁⲃⲁύ ⲏⲉ ⲡυⳅⲇυ ⲙⲏⲉ ⲧⲩⲧ ⲁ ⲥⲟⲥυ ⲣⲉⳃⲉ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲱⲗюⲭⲟⳅⲁ я ⲧⲃⲟю ⲙⲁⲧь ⲧⲁⲡⲕⲟⲙ ⲃыⲉⳝⲁⲗ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲗⲉⲧⲁⲉⲧ ⲕⲣыⲱⲁ, ⲕⲟⲅⲇⲁ ⲃυⲇυⲧ ⲟⲅⲣⲟⲙⲏыύ ⳝυⲅ ⲇυⲕ ⲙⲟⲉⲅⲟ ⲡⲁⲩⳡⲕⲁ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲏⲁяⲣυⲃⲁύ ⲙⲏⲉ ⳅⲁⲗⲩⲡⲩ ⲱⲗюⲭⲁ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲡⲟⲕⲁ я ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь, ⲧы ⲥⲧⲟυⲱь ⲏⲁ ⲕⲟⲗⲉⲏяⲭ υ ⲗυⲯⲉⲱь яύцⲁ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲇⲁⲃⲁύ ⲡⲣыⲅⲁύ, ⲗⲟⲃⲗю ⲧⲉⳝя ⲭⲩⲉⲙ ⲅⲏυⲇⲁ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧυⲱⲉ ⲇⲩⲣⲁ, я ⲧⲉⳝя ⲃⲥⲉⲅⲟ ⲗυⲱь ⲉⳝⲁⲱⲩ ⲟⲥⲧⲣыⲙ ⲭⲩёⲙ ⲡⲁⲩⲕⲁ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲡⲟⲥⲁⲇυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲕⲟⲗ υ ⲡⲁⲩⲕυ ⲉё ⲡⲣυⲏяⲗυ ⲕⲁⲕ ⳅⲁ ⲇⲟⳝыⳡⲩ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲏⲉ ⲡⲟⲧⲩⲭⲁύ ⲧⲉⲗⲟⳡⲕⲁ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲣⲉⲯⲩ ⲧⲃⲟю ⲙⲁⲧь ⲥⲃυⲏⲟⲣⲩⲥⲥⲕⲩю",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲏⲁⲧяⲅυⲃⲁю ⲧⲃⲟύ ⲣⲟⲧυⲕ ⲕⲁⲕ ⳅυⲙⲏюю ⲣⲉⳅυⲏⲩ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲥⲟⲥⲉⲧ?",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧы ⲡⲟⲏяⲗ ⲡⲣυⲕⲟⲗ ⲥ ⲏⲁⲉⳝⲟⲙ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ, ⲕⲟⲅⲇⲁ ⲟⲏ ⲙⲏⲉ ⲥⲟⲥⲁⲗ, ⲁ ⲡⲟⲗⲩⳡυⲗ ⲧⲟⲗьⲕⲟ ⲭⲩⲉⲙ ⲡⲟ ⲉⳝⲁⲗⲩ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲁⲭⲩⲉⲏⲏⲟ ⲯⲉ ⲉⳝⲁⲧь ⲧⲉⳝя ⲃ ⲁⲏⲩⲥ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⳙⲇυ ⲡⲟⲙⲟύ ⲥⲃⲟύ ⲣⲟⲧⲁⲏ ⲡⲟⲥⲗⲉ ⲃⲡⲣыⲥⲕⲁ яⲇⲁ, я ⲉⳃё ⲏⲉ ⳅⲁⲕⲟⲏⳡυⲗ ⲧⲉⳝя ⲉⳝⲁⲧь",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲟⲣⲇⲁ ⲡⲁⲩⲕⲟⲃ υ ⲥⲁⲙⲁ ⲕⲟⲣⲟⲗⲉⲃⲁ υⲇёⲧ ⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃяⳅⲁⲗ ⲧⲃⲟю ⲙⲁⲧь цⲉⲡяⲙυ υ ⲉⳝⲩ ⲉё",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲡⲣⲟⲇⲁⲗ ⲧⲃⲟю ⲥⲉⲙью ⳝⲟⲙⲯⲁⲙ ⳅⲁ ⳝⲉⲥⲡⲗⲁⲧⲏⲟ, ⳡⲧⲟⳝы ⲟⲏυ ⲃыⲉⳝⲁⲗυ υ ⲕⲟⲏⳡυⲗυ ⲃ ⲧⲉⳝя",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲡⲁⲩⲕυ ⲇⲉⲗⲁюⲧ ⲣυⲧⲩⲁⲗ 9-υ ⲕⲟⲗⲉц ⲁⲇⲁ ⳡⲧⲟⳝы ⲧⲃⲟя ⲙⲁⲧь ⲥⲇⲟⲭⲗⲁ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲣⲉⲯⲩ ⲧⲃⲟю ⲙⲁⲧь ⲙⲉⳡⲟⲙ ⲡⲁⲩⲕⲁ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲥⲟⲥυ ⲙⲏⲉ ⲇⲩⲣⲟⳡⲕⲁ",
		"<emoji document_id=5810144570192694729>💀</emoji>  Ⲏⲁⲥυⲗьⲏⲟ ⲧя ⲡⲟⲥⲧⲁⲃυⲗ ⲣⲁⲕⲟⲙ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⳙⲥⲧⲣⲉⳝⲗяю ⲧⲃⲟύ ⲁⲏⲁⲗ ⲙⲉⳡⲟⲙ ⲡⲁⲩⲕⲁ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⳅⲁⲭⲟⲧⲉⲗⲁ ⲥ ⲙⲟυⲙ ⲡⲁⲩⲕⲟⲙ 69?",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲕⲟⲅⲇⲁ ⲡⲁⲩⲕ ⲕⲟⲏⳡυⲗ ⲃ ⲧⲃⲟю ⲙⲁⲧь, ⲟⲏⲁ ⲣⲁⲥⲥⲕⲁⳅⲁⲗⲁ ⲃⲥⲉⲙⲩ ⲅⲟⲣⲟⲇⲩ, ⲕⲁⲕⲁя ⲃⲕⲩⲥⲏⲁя ⲩ ⲏⲉⲅⲟ ⲥⲡⲉⲣⲙⲁ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲡⲣⲉⲇⲗⲁⲅⲁⲉⲧ ⲙⲟⲉⲙⲩ ⲡⲁⲩⲕⲩ 100000$ ⳡⲧⲟⳝы ⲟⲏ ⲉё ⲏⲉ ⲩⳝυⲃⲁⲗ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲕⲩⲡυⲗ я ⲣⲉⳅυⲏⲟⲃыύ ⲭⲩύ ⲥ ⲙⲉⳡⲁⲙυ ⲡⲁⲩⲕⲟⲃ ⲏⲁ ⳡⲗⲉⲏⲉ, ⳃⲁⲥ ⲧⲃⲟя ⲙⲁⲧь ⲥⲁⲇυⲧьⲥя υ ⲡⲗⲁⳡⲉⲧ ⲥ ⲕⲣⲟⲃью",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲙⲟύ ⲡⲁⲩⳡⲟⲕ ⲡⲟⲇⲕⲣⲁⲗⲥя ⲕ ⲧⲉⳝⲉ ⲥⳅⲁⲇυ υ ⲃⲃⲟⲱⲉⲗ ⲃ ⲧⲃⲟё ⲧⲉⲗⲟ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲃ ⲧⲉⲗⲉ ⲧⲃⲟⲉύ ⲱⲗюⲭⲟⲙⲁⲧⲉⲣυ ⲥⲟⲥⲩ ⳝⲟⲙⲯⲁⲙ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲙⲟυ ⲡⲁⲩⲕυ ⲣⲁⳅⲣⲉⳅⲁⲗυ ⲯυⲃⲟⲧ ⲙⲁⲧⲉⲣυ υ я ⳅⲁⲗⲉⳅ ⲃ ⲧⲉⲗⲟ ⲧⲃⲟⲉύ ⲱⲗюⲭυ υ ⲏⲁⳡⲁⲗ ⲥⲟⲥⲁⲧь ⲃⲥⲉⲙ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲉⳝⲁⲱⲩ ⲭⲩⲉⲙ ⲧⲃⲟю ⲙⲁⲧь",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲇⲉⲣⲯⲩ ⲅⲟⲗⲟⲃⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ, ⳡⲧⲟⳝы ⲏⲉ ⳝⲣыⲕⲁⲗⲁⲥь",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲩⳡυⲥь ⲩ ⲥⲃⲟⲉύ ⲱⲗюⲭⲟⲙⲁⲧⲉⲣυ, ⲕⲁⲕ ⲏⲁⲇⲟ ⲩⲙⲟⲗяⲧь ⲟⲧⲥⲟⲥⲟⲙ, ⳡⲧⲟⳝы ⲧⲉⳝя ⲏⲉ ⲩⳝυⲃⲁⲗυ?",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲣⲁⲥⲧяⲏⲩⲗ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ 4 ⲇⲉⲣⲉⲃⲁ υ ⲡⲟⲥⲧⲁⲃυⲗ ⲥⲏυⳅⲩ ⲕⲟⲥⲧёⲣ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲙυⲗⲗυⲟⲏⲁⲙυ υⲅⲗ я ⲡυⲭⲁⲗ ⲧⲃⲟю ⲙⲁⲧь",
		"<emoji document_id=5810144570192694729>💀</emoji>  Ⳡⲧⲟ-ⲧⲟ я ⳡⲁⲥⲧⲟ ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲇⲉⲥⲏⲁ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧⲃⲟя ⲙⲁⲧь ⳅⲁⲭⲟⲧⲉⲗⲁ ⲉⳃё ⳝⲟⲗьⲱⲉ ⲥⲡⲉⲣⲙы ⲡⲁⲩⲕⲁ, ⲡⲟⲧⲟⲙⲩ ⳡⲧⲟ ⲟⲏⲁ ⲥⲕⲁⳅⲁⲗⲁ, ⳡⲧⲟ ⲩ ⲏⲉⲅⲟ ⲃⲕⲩⲥ ⲥⲡⲉⲣⲙы ⲕⲁⲕ ⲙⲟⲗⲟⲏыύ ⲕⲟⲕⲧⲉύⲗь ⲥ ⳝⲁⲏⲁⲏⲟⲃ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⳝⲣⲁⳅυⲗьⲥⲕυ ⲧя ⲉⳝⲩ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲥⲁⲙⲩⲣⲁυ υ ⲡⲁⲩⲕυ ⲇⲟⲅⲟⲃⲟⲣυⲗυⲥь ⲧⲉⳝя ⲃыⲉⳝⲁⲧь",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲃⲟ ⲥⲗⲁⲃⲩ Ⲩⲕⲣⲁυⲏы ⲡⲁⲩⲕυ ⲡⲟⲱⲗυ ⲩⳝυⲃⲁⲧь ⲧⲃⲟю ⲣⲩⲥⲏяⲃⲩю ⲥⲧⲣⲁⲏⲩ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲡⲁⲩⲕυ ⲃⲡⲣыⲥⲕⲁюⲧ яⲇ ⲃ ⲣⲩⲥⲏяⲃыⲭ ⲭⲩⲉⲥⲟⲥⲟⲃ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲏⲁ ⳡⲗⲉⲏ ⲡⲣыⲅⲁύ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲗⲟⲃⲗю ⲧⲉⳝя ⳝυⲅ ⲇυⲕⲟⲙ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲏⲩ ⲃⲟⳅьⲙυ ⲙⲟύ ⳡⲗⲉⲏ ⲃ ⲣⲩⲕυ υ ⳅⲁⲡⲟύ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲥⲩⲏⲩⲗ ⲣⲁⲥⲡяⲧυⲉ, ⲁ ⳡⲧⲟⳝы ⲏⲉ ⲟⲣⲁлⲁ, ⲏⲁⲥⲣⲁⲗ ⲉύ ⲃ ⲣⲟⲧ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲃ ⲧⲃⲟю ⲇⲟⲭⲗⲩю ⲙⲁⲧь ⳅⲁⲥⲩⲏⲩⲗ ⲥⲧⲣⲁⲡⲟⲏ, ⲃ ⲃυⲇⲉ ⲁⲣⲙⲁⲧⲩⲣы",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲉⳝⲁⲱⲩ ⲧⲃⲟю ⲥⲉⲙью ⲥ ⲁⲣⲙⲁⲧⲩⲣы",
		"<emoji document_id=5810144570192694729>💀</emoji> Я ⲧⲃⲟю ⲙⲁⲧь ⳅⲁⲥⲧⲁⲃυⲗ ⲡⲟⲇыⲭⲁⲧь ⲃ ⲙⲟυⲭ ⲏⲟⲅⲁⲭ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲭⲩύ ⲥⲟⲥёⲧ ⲕⲁⲕ ⲱⲗюⲭⲁ",
		"<emoji document_id=5810144570192694729>💀</emoji> Я ⲧⲃⲟυ ⲅⲏυюⳃυⲉ ⲕⲟⲥⲧυ ⲣⲉⳅⲁⲗ ⳅⲁⲗⲩⲡⲟύ",
		"<emoji document_id=5810144570192694729>💀</emoji> Я ⲧⲃⲟю ⲙⲁⲧь ⲃыⲉⳝⲁⲗ ⲃ ⲉё ⲅⲏυⲗⲟύ ⲁⲏⲁⲗ",
		"<emoji document_id=5810144570192694729>💀</emoji> Я ⲧⲃⲟυ ⳅⲩⳝы ⲗⲟⲙⲟⲙ ⲃыⲣⲃⲁⲗ",
		"<emoji document_id=5810144570192694729>💀</emoji> Я ⲃ ⲧⲃⲟёⲙ ⳝⲣюⲭⲉ ⲡⲁⲩⲕⲟⲃ ⲣⲁⳅⲃⲟⲯⲩ ⲕⲁⲕ ⳝⲗяⲇⲉύ",
		"<emoji document_id=5810144570192694729>💀</emoji> Я ⲧⲃⲟυ ⲅⲩⳝы ⲅⲏⲟⲉⲙ ⳅⲁⲗⲉⲡυⲗ υ ⲭⲩёⲙ ⲡⲣυⳝυⲗ ⲇⲟ ⲕⲣⲟⲃυ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲏⲁⲥυⲗⲩю ⲧⲃⲟю ⲙⲁⲧь ⲱⲗюⲭⲩ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧⲃⲟя ⲥⲉⲙья эⲧⲟ ⲧⲟⲗⲡⲁ ⲉⳝⲩⳡυⲭ υⲙⳝυцυⲗⲟⲃ",
		"<emoji document_id=5810144570192694729>💀</emoji> Я ⲧⲃⲟⳝ ⲙⲁⲧь ⳅⲁⲣыⲗ ⲥⲣⲉⲇυ ⲕⲁⲙⲉⲏⲏыⲭ ⲥⲕⲣⲉⲯⲁⲗⲉύ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲥⲗыⲱυⲱь ⲭⲩⲉⲥⲟⲥ, я ⲧⲃⲟю ⲙⲁⲧь ⲃыⲉⳝⲁⲗ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧⲃⲟя ⲙⲁⲧь ⲟⲥⲧⲁⲃυⲗⲁ ⲡⲟⲥⲗⲉ ⲥⲉⳝя ⲏⲉⲥⲕⲟⲗьⲕⲟ ⲕⲁⲡⲉⲗь ⲏⲁ ⲕυⲏⲯⲁⲗⲉ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲅⲟⲗⲟⲃⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲩⲣⲟⲏυⲗ ⲏⲁ ⲡυⲕⲩ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲃ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲩⲏⲁύ ⲃⲥⲧⲁⲃυⲗ υ ⲡⲣⲟⲕⲣⲩⲧυⲗ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲡⲁⲩⲕυ ⲟⲥⲕⲃⲉⲣⲏυⲗυ ⲧⲃⲟύ ⲟⳝⲅⲟⲗⲟⲇⲁⲏⲏыύ ⲧⲣⲩⲡ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲩ ⲧⲉⳝя ⲡⲟⲇ ⲣⲉⳝⲣⲟⲙ ⲙⲟύ ⳡⲗⲉⲏ ⳅⲁⲥⲧⲣяⲗ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲣⲩⲱⲩ ⲧⲃⲟю ⲙⲁⲧь ⲥⲃⲟυⲙ ⳡⲗⲉⲏⲟⲙ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲏⲁ ⲕⲟⲥⲧяⲭ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ я ⲡⲟⲥⲧⲣⲟυⲗ ⲇⲟⲙ ⲇⲗя ⳝⲟⲙⲯⲉύ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲉⳝⲩ ⲧⲃⲟю ⲱⲗюⲭⲟⲙⲁⲧь ⲃ ⲣⲟⲧ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲣⲁⳅⲗⲟⲯυⲃⲱⲉⲉⲥя ⲙяⲥⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲉⳝⲁⲗ ⲏⲁ ⲕⲣыⲱⲕⲉ ⲅⲣⲟⳝⲁ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲣⲉⲯⲩ ⲧⲃⲟю ⲙⲁⲧь ⲗьⲇⲟⲙ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲙⲁⲧь ⲧⲃⲟю ⳡⲗⲉⲏⲟⲙ ⲇыⲣяⲃυⲗ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⳡⲗⲉⲏⲟⲙ ⲧⲃⲟя ⲙⲁⲧь ⳡⲉⲕⲁⲗ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲙⲁⲧь ⲧⲃⲟю ⲭⲩⲉⲙ ⲃыⲧⲣⲁⲭυⲃⲁⲗ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲙⲁⲙⲁⲏю ⲧⲃⲟю ⳅⲁⲗⲩⲡⲟύ ⲇⲣⲁⲗ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲙⲁⲧь ⲧⲃⲟя ⳅⲁⲗⲩⲡⲟύ ⲇⲁⲃυⲧьⲥя)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲥⲁⲥⲉⲧ ⲙⲁⲧь ⲧⲃⲟя, ⲡⲟⲕⲁ ⲧы ⲁⲭⲩⲉⲃⲁⲉⲱь)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲭⲩёⲙ ⲧⲃⲟю ⲙⲁⲧь υⲙⲉю)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧяⲏⲩ ⲧⲃⲟю ⲙⲁⲧь ⲱⲗюⲭⲩ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ 5++ ⲥⲟⲥёⲧ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲭⲩⲉⲙ ⲧⲃⲟю ⲙⲁⲧь ⲡυⲇⲁⲣⲁⲥυⲗ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲙⲁⲙⲁⲱⲩ ⲧⲃⲟю ⲃ ⲣⲟⲧ ⲉⳝⲁⲗ ⲯⲉ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲃ ⲁⲏⲁⲗ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⲏⳡυⲗ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧⲃⲟя ⲙⲁⲧь ⲙⲟю ⲥⲡⲉⲣⲙⲩ ⲯⲩёⲧ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⳡёⲧⲕⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥёⲧ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⳅⲁⲕⲣыⲗ ⲣⲟⲧ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⳡⲗⲉⲏⲟⲙ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧⲃⲟя ⲙⲁⲧь ⲡⲁⲗυⲣⲩⲉⲧ ⲙⲟю ⳅⲁⲗⲩⲡⲩ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲧⲃⲟю ⲙⲁⲧь я ⲥⲃⲟυⲙ ⳡⲗⲉⲏⲟⲙ ⲃъⲉⳝⲁⲱυⲗ ⲃ ⲁⲥⲫⲁⲗьⲧ",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⳅⲁⲥⲁⲇυⲗ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⳡⲗⲉⲏⲟⲙ ⲧⲃⲟю ⲙⲁⲧь ⲇⲁⲃυⲗ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲏⲟⲅⲁⲙυ ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲇⲣⲟⳡυⲧ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲙⲁⲧь ⲧⲃⲟю ⲟⲡⲣⲟⲕυⲏⲩⲗ ⳅⲁⲗⲩⲡⲟύ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲥⲁⲯⲁю ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲕⲩⲏⲁύ)",
		"<emoji document_id=5810144570192694729>💀</emoji> Ⲟⲧⲕⲣⲟύ ⲣⲟⲧυⲕ, ⲗⲉⲧяⲧ ⳡⲗⲉⲏы ⲡⲁⲩⳡⲕⲟⲃ)"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(shablon)), file=media)
            await sleep(time)
            
    async def rskeletcmd(self, message):
        """[ ! ] Запускает модуль: Ruda Skelet [ ! ]"""
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Модуль #RudaSkelet закончил уничтожать своим черепом. <emoji document_id=6037464506131549087>💀</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>Модуль #RudaSkelet начал истреблять шлюху своим черепом. <emoji document_id=6037464506131549087>💀</emoji></b>\n\n"
            "<b><emoji document_id=5222468670436943157>🤚</emoji> Чтобы закончить ебать шлюху черепом, пиши <code>.rskelet</code></b>",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message() 
        shabl3 = [
        "〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲥⲁⲥⲉⲱ ⲙⲏⲉ ⲇⲩⲣⲁⲃⲗυⲃⲁя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲃ ⲇⲃυⲯⲉⲏυυ ⲥⲁⲥⲉⲱ ⲙⲏⲉ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲣⲁⲥⲗⲁⳝυⲗ ⲧя ⲭⲩύⲉⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲟⳝυⲇⲉⲗ ⲧя ⲭⲩύⲉⲙ ⲱⲁⲗⲁⲃⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲣⲁⳅⲯⲁⲗ ⲧя ⲭⲩύⲉⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲅⲣⲉю ⲧя ⲭⲩⲉⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⳝⲉⳅ ⲥⲟⲃⲉⲥⲧυ ⲥⲁⲥⲉⲱ ⲙⲏⲉ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Эⲕⲁⲏⲟⲙⲏⲁ ⲉⲡⲩ ⲧя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲭⲩⲉⲙ ⲃ ⲧя ⲡⲱυⲕⲁⲗ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲥⲡⲁⲣⲧυⲃⲏⲁ ⲥⲁⲥⲉⲱ ⲙⲏⲉ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲭⲩύⲉⲙ ⲧя ⲙⲁⲧⲏⲩⲗ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⳝⲗⲉⲥⲧяⳃⲉ ⲉⲡⲩ ⲧя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲥⲡⲉⲣⲙⲩ ⲃ ⲧя υⳅⲉ ⳅⲁⲗυⲗ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲟⲧⳝⲉⲗυⲗ ⲧя ⲭⲩύⲉⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲥⲃⲁⳝⲟⲇⲏⲁ ⲥⲁⲥⲉⲱ ⲙⲏⲉ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⳅⲁⲧⲁυⲗ ⲃ ⲧⲉ ⲥⲃⲟύ ⲭⲩύ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲥⲗⲉⲧⲁя ⲇⲟⲭⲏⲉⲱ ⲗⲉⲭⲕⲟ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲡⲣⲁⲃⲉⲣυⲗ ⲧя ⲭⲩύⲉⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲕⲁⲏцⲉⲧⲣυⲣⲟⲃⲁⲗ ⲧя ⲭⲩύⲉⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲟⳝⲗⲉⲭⳡυⲗ ⲧя ⲭⲩύⲉⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲥⲁⲥⲁⲗⲁ ⲧы ⲙⲏⲉ ⲗⲉⲭⲕⲟ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⳅⲩⳝы ⲧⲉ ⲭⲩύⲉⲙ ⲧⲣⲩ ⲧⲁⲕⲧⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲣⲁⲥⲡυⲗυⲗ ⲧя ⲭⲩⲉⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲇⲁⲃⲗю ⲏⲁ ⲧя ⲭⲩύⲉⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⳡⲟⲧ ⲃ ⲣⲟⲧ ⲧя ⲉⲡⲩ ⲗⲉⲭⲕⲟ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲥ ⳡυⲥⲧⲟⲅⲟ ⲗυⲥⲧⲁ ⲥⲁⲥⲉⲱ ⲙⲏⲉ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲣⲁⳅⲇⲣⲁⲯυⲗ ⲧя ⲭⲩύⲉⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲟⲧⲕⲣыⲗ ⲧя ⲭⲩύⲉⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲭⲟⲯⲩ ⲃ ⲧя ⲭⲩύⲉⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲡⲣυⳝυⲗ ⲧя ⲭⲩύⲉⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲡⲟяⲃυⲗⲥя ⲃ ⲧⲉ ⲭⲩύⲉⲙ ⲥⲗⲉⲧⲁя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟύ ⲇⲉⲇ ⲃ 45 ⲙⲏⲉ ⲭⲩύ ⳅⲁ ⲕⲩⲥⲟⲕ ⲥⲁⲗⲟ ⲥⲁⲥⲁⲗ ⲣυⲗυ ⲏⲉⲙⲟⳃь ⲟⲏ ⲉⳝⲁⲏыύ ⲇⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕υ ⳡё ⳝⲩⲇⲩ ⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь ⲇⲟ ⲧⲁⲗⲟⲃⲁ υ ⲧы ⲏⲉ ⲥⲙⲟⲯⲉⲱь ⲙⲏⲉ ⲏⲉ ⳡⲉⲅⲟ ⲥⲕⲁⳅⲁⲧь ⲃⲉⲇь ⲥⲁⲙ ⲃ ⲧⲁύⲏⲉ ⲙⲏⲉ ⲥⲟⲥёⲱь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲇⲁⲃⲏⲟ ⲏⲁⳡⲁⲗⲁ ⲡⲣⲟяⲃⲗяⲧь ⲩⲃⲁⲯⲉⲏυя ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю υ ⳅⲇⲁⲣⲟⲃⲁⲉⲧьⲥя ⲥ ⲏυⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲉ ⲧы ⳡё ⲇⲩⲙⲁⲗ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲇⲟⲗⲅⲟ ⲥⲙⲟⲯⲉⲧ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲣыⲡⲁⲉⲧьⲥя я ⲉύ ⳅⲁ эⲧⲟ ⲭⲩёⲙ ⲡⲟ ⲅⲟⲣⳝⲩ ⲏⲁⲃⲉⲣⲏⲩ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲃ ⲏⲁⲥⲗⲉⲇⲥⲧⲃⲟ ⳅⲁⲃⲉⳃⲁⲗⲁ ⲧⲃⲟύ ⲣⲟⲧ ⲉⲥⲗυ ⳝⲩⲇⲉⲱь эⲧⲟ ⲟⲧⲣυцⲁⲧь я ⲉё ⲭⲩёⲙ υⳅ ⲅⲣⲟⳝⲁ ⲇⲟⲥⲧⲁⲏⲩ ⳡⲧⲟⳝы ⲟⲏⲁ ⲡⲟⲇⲧⲃⲉⲣⲇυⲗⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲩ ⳡё ⲡⲣυⲥⲧⲩⲡυⲙ ⲣⲁⲥⳡⲉⲭⲗяⲧь ⲧⲃⲟю ⲙⲁⲧь υⲗυ ⲧы ⲇⲁⲯⲉ ⲡⲟⳝⲟυⲱьⲥя ⲣыⲡⲏⲩⲧьⲥя ⲏⲁ ⲙⲉⲏя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⲏⲉ ⲣⲁⳅ ⲡⲁⲇⲁⲗⲁ ⲏⲁ ⲙⲟёⲙ ⲭⲩю ⲏⲟ ⲟⲏⲁ ⲥⲧⲣⲉⲙυⲗⲟⲥь ⲕ ⲃⲉⲣⲱυⲏⲉ ⲇⲩⲣⲁ ⲉⳝⲁⲏⲁя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲣⲁⲕⲩⲱⲕⲁ ⲏⲁⲭⲩύ ⲧы ⲡⲣяⳡⲉⲱьⲥя ⲥⲃⲟю ⲙⲁⲧь ⲟⲧ ⲭⲩя ⲙⲟⲉⲅⲟ ⲩ ⲏⲉё ⲏⲁ ⲡυⳅⲇⲉ ⲅⲉⲟⲗⲟⲕⲁⲧⲟⲣ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⲗⲉⲅⲗⲁ ⲡⲟⲇ ⲙⲟύ ⲭⲩύ υ ⲃⲣёⲧ ⳡⲧⲟ ⲏⲉ ⲙⲟⲯⲉⲧ ⲃыⲗⲉⳅⲧυ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲉ ⲭⲟⳡⲩ ⲧⲉⳝя ⲟⲥⲕⲟⲣⳝυⲧь ⲏⲟ ⲧⲃⲟя ⲙⲁⲧь ⲟⲧⲥⲁⲥыⲃⲁⲗⲁ ⲙⲏⲉ ⲡⲟ 100 ⲣⲁⳅ ⲏⲁ ⲇⲏю ⲏⲟ ⲇⲗя ⲏⲉё эⲧⲟ ⲏⲉ ⲣⲉⲕⲟⲣⲇ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲩ υ ⳡё ⲧы ⲇⲟⲥυⲭⲡⲟⲣ ⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳝⲩⲇⲉⲧ ⲉⳝⲁⲧь ⲃⲁⲱⲩ ⲥⲉⲙύⲕⲩ ⳅⲁ ⳝⲉⲥⲡⲗⲁⲧⲏⲟ ⲥⲕⲟⲣⲟ ⲃⲁⲙ ⲡⲣυⲇёⲧьⲥя ⲡⲗⲁⲧυⲧь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲡⲣⲉⲯⲇⲉ ⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁⳡυⲏⲁⲉⲧ ⲥⲟⲥⲁⲧь я ⳝью ⲉύ ⲭⲩёⲙ ⲡⲟ ⲅⲩⳝⲉ ⲉύ ⲏⲣⲁⲃυⲧьⲥя ⲃⲉⲇь эⲧⲟ ⲡⲁⲥⲧⲁ ⲇⲁⲃⲏⲟ ⲃⲟ ⲃⲗⲁⲥⲧυ ⲙⲟⲉⲅⲟ ⲭⲩя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧы ⲇⲁⲯⲉ ⲏⲉ ⳅⲁⲙⲉⲧυⲱь ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲯυⲧь ⲡⲉⲣⲉⲉⲇⲉⲧ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⳃⲁ ⲙⲟύ ⲭⲩύ ⲣⲉⲱυⲗⲁ ⲃ ⲙⲩⳅⲉύ ⲡⲣⲉⲏⲉⲥⲧυ υ ⲥⲕⲁⳅⲁⲧь ⳡⲧⲟ эⲧⲟ ⲃⲉⲗυⲕυύ ⲁⲣⲧⲉⲫⲁⲕⲧ ⳡё ⲟⲏⲁ ⲱⲁⲗⲟⲃⲁ ⲧⲟ ⲧⲁⲕⲁя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⳝⲉⳅ ⲱⲩⲧⲟⲕ ⲉⲥⲗυ ⲧⲃⲟя ⲙⲁⲧь ⲏⲉ ⲏⲁⳡⲏёⲧ ⲃ ⲧⲉⲙⲡⲉ ⲥⲟⲥⲁⲧь я ⲉύ ⳅⲁⲗⲩⲡⲟύ ⲡⲟ ⲉⳝⲁⲗⲩ ⲥⲉⳅⲯⲩ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕υ ⳡё ⲧы ⳃⲁⲥ ⲧⲟⲯⲉ ⳝⲩⲇⲉⲱь ⲟⲧ ⲭⲩя ⲩⲃυⲗυⲃⲁⲧь ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь υⲗυ ⲏⲁⳡⲏёⲱь ⲏⲁ ⲏⲟⲣⲙⲉ ⲥⲟⲥⲁⲧь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲉ ⲙⲟⲅⲩ ⲡⲉⲣⲉⲇⲁⲧь ⲧⲉ ⳡⲩⲃⲥⲧⲃⲁ ⲕⲟⲅⲇⲁ ⲧⲃⲟя ⲥⲡυⲇⲟⳅⲏⲁя ⲙⲁⲙⲁⲱⲁ ⲙⲏⲉ ⲥⲟⲥёⲧ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳃⲁ ⲙⲟύ ⲭⲩύ ⳅⲁ ⳃⲉⲕⲩ ⲡⲩⲥⲧυⲗⲁ υ ⲏⲉ ⲭⲟⳡⲉⲧ ⲃыⲥⲟⲃыⲃⲁⲧь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲁⲉⲧ ⲕⲁⲕ ⲏⲁ ⲣⲁⳝⲟⲧⲩ υⲇёⲧ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⳅⲁⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь ⲟⲡяⲧь ⲙⲏⲉ ⲥⲟⲥёⲧ ⲙⲟⲯⲉⲧ ⲟⲏⲁ ⲡⲟⲇⲩⲙⲁⲗⲁ ⳡⲧⲟ ⲙⲟⲯⲉⲧ ⲟⲧⲥⲁⲥыⲃⲁⲧь ⲙⲏⲉ ⳝⲉⳅⲗⲉⲙυⲧⲏⲟ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⲩⲡⲁⲗⲁ ⲡⲉⲣⲉⲇ ⲙⲟυⲙ ⲭⲩёⲙ ⲕⲟⲅⲇⲁ ⲡⲟⲇⲥⲧⲁⲃυⲗ ⲡⲉⲣⲇⲁⲕ ⲡⲉⲣⲉⲇ ⲥⲃⲟυⲙ ⳝⲁⲧⲉύ ⲏⲟ эⲧⲟⲧ ⲟⲥёⲗ ⲡⲟⳝⲟяⲗⲥя ⲉⲅⲟ ⲡⲟⲉⳝⲁⲧь ⲃⲉⲇь ⲟⲏ ⳅⲏⲁⲉⲧ ⳡⲧⲟ ⲙⲟя ⳅⲁⲗⲩⲡⲁ ⲟⲡяⲧь ⲡⲣⲟⳝьёⲧ ⲉⲅⲟ ⲅⲟⲣⳝ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲙⲩⲗьⲕⲁ ⳃⲁ ⲙⲟύ ⲭⲩύ ⲡⲟ ⲅⲗⲁⲏⲇы ⲡⲩⲥⲧυⲗⲁ я ⲡⲣⲉⲇⲗⲁⲅⲁю ⲇⲁⲧь ⲉύ ⲙⲉⲇⲁⲗьⲕⲩ ⳅⲁ ⲅⲟⲇⲟⲃⲟύ ⲟⲧⲥⲟⲥ ⳝⲉⳅ ⲡⲉⲣⲉⲣыⲃⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲩ ⲏⲩ ⲥⲕⲁⲯυ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲕⲁ ⲏⲉ ⲱⲁⳝⲟⲗⲇⲁ я ⲥⲃⲟυⲙ ⲭⲩёⲙ эⲧⲟ ⲟⲡⲣⲟⲃⲉⲣⲅⲏⲩ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲣⲁⳅⲃⲟⲣⲟⲱυⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲕⲩ ⲭⲩёⲙ υ ⲃыⲏⲉⲥ ⲟⲧ ⲧⲩⲇⲁ ⲃⲥё ⳡⲧⲟ ⲙⲟⲯⲏⲟ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕я ⲧⲃⲟю ⲇⲩⲣⲏⲩю ⲙⲁⲙⲁⲱⲩ ⳃⲁ ⲏⲁ ⲭⲩⲉ ⳅⲁ ⲧⲁⲕυⲉ ⲇⲃυⲯⲉⲏυя ⲡⲣⲟⲃⲉⲣⲏⲩ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲉ ⲃⲉⲣυⲱь ⲙⲏⲉ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲙⲟύ ⲭⲩύ ⳝⲉⳅⲁⲥⲧⲟⲏⲟⲃⳡⲏⲟ ⲥⲟⲥёⲧ ⲧⲁⲕ ⲡⲣυⲭⲟⲇυ ⲟⲏⲁ ⲇⲁⲥⲧ ⲧⲉ ⲩⲣⲟⲕυ ⲟⲧⲥⲟⲥⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲉ ⲙⲟⲅⲩ ⲡⲟⲏяⲧь ⲡⲟⳡⲉⲙⲩ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲧⲁⲕⲁя ⲥⲗⲁⳝⲁя ⲱⲗюⲭⲁ ⳡⲧⲟ ⲇⲁⲯⲉ ⲙⲟύ ⲭⲩύ ⲩⲯⲉ ⲟⲥυⲗυⲧь ⲏⲉ ⲙⲟⲯⲉⲧ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⳃⲁ ⲭⲩёⲙ ⲡⲉⲣⲉⲃⲉⲣⲏⲩ ⲭⲟⲧя эⲧⲟ ⲯⲁⲗⲕⲁя ⲏⲁⳡⲏёⲧ ⲟⲡяⲧь ⲃ ⲕⲟⲏⲃⲩⲗьⲥυяⲭ ⳝυⲧьⲥя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲩ ⲩⲯⲉ ⳝⲉⳅ ⲱⲩⲧⲟⲕ ⲃ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⳅⲁⲅⲏⲁⲗⲥя ⲁ ⲟⲏⲁ ⲏⲁⳡυⲏⲁⲉⲧ ⲕⲁⲕ ⲥⲃυⲏья ⲃυⳅⲯⲁⲧь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲃыⲥⲉⲕ ⳅⲁ ⲧⲟ ⳡⲧⲟ ⲟⲏⲁ ⲧⲃⲟⲉⲙⲩ ⳝⲁⲧυ ⲟⲧⲥⲟⲥⲁⲧь ⲡыⲧⲁⲗⲁⲥь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⲗⲉⳅⲗⲁ ⲕⲟ ⲙⲏⲉ цⲉⲗⲟⲃⲁⲧьⲥя ⲏⲟ ⲉύ ⳅⲁⲗⲩⲡⲟύ ⲗⲟⳝ ⲣⲁⲥⲕⲣⲟⲱυⲗ ⲡⲩⲥⲧь ⳅⲏⲁⲉⲧ ⲥⲃⲟё ⲙⲉⲥⲧⲟ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲩ υ ⳡё ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲅυⲗьⲇυю ⲥⲟⳅⲇⲁⲗⲁ ⳡⲧⲟⳝы ⲙⲟύ ⲭⲩύ ⲃⲟⲥⲭⲃⲁⲗяⲧь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⳃⲁ ⲙⲟύ ⲭⲩύ ⲡⲣυ ⲡⲟⲇⲣⲩⲅⲁⲭ ⲣⲁⲥⲭⲃⲁⲗυⲃⲁⲗⲁ υ ⲟⲏυ ⲧⲟⲯⲉ ⲣⲉⲱυⲗυ ⲙⲏⲉ ⲟⲧⲥⲟⲥⲁⲧь ⲏⲟ ⲗⲩⳡⲱⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲩⲭⲉ ⲏⲉ ⲕⲧⲟ ⲏⲉ ⲥⲟⲥёⲧ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲉⲥⲗυ ⲧы ⲭⲟⳡⲉⲱь ⲙⲟύ ⲭⲩύ ⲧⲟⲅⲇⲁ ⲧⲉ ⲡⲣυⲇёⲧьⲥя ⲡⲟⲕⲟⲏⲕⲩⲣυⲣⲟⲃⲁⲧь ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲩ υ ⳡё ⲧы ⳃⲁⲥ ⲡⲟⲇⲟⲭⲏⲉⲱь ⲏⲁ ⲙⲟёⲙ ⲭⲩю ⳡⲉⲙ ⲟⲡⲟⳅⲟⲣυⲱь ⲥⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲭⲟⲧя ⲙⲟύ ⲭⲩύ υ ⲧⲁⲕ ⲉё ⲟⲡⲩⲥⲧυⲗ ⲉⳅ ⲉⳅ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧⲩⲱⲕⲁ ⲙⲟⲯⲉⲧ ⲟⲧⲣυцⲁⲧь ⳡⲧⲟ ⲥⲟⲥⲁⲗⲁ ⲙⲏⲉ ⲏⲟ ⲩ ⲙⲉⲏя ⲉⲥⲧь ⲡⲣяⲙⲟⲉ ⲇⲟⲕⲁⳅⲁⲧⲉⲗьⲥⲧⲃⲟ ⲃⲉⲇь я ⳅⲁⲕⲁⳡⲁⲗ ⲉё υⳅⲏⲩⲧⲣυ ⲥⲡⲉⲣⲙⲟύ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⲡⲣⲟⲃυⲏυⲗⲁⲥь ⲡⲉⲣⲉⲇ ⲙⲟυⲙ ⲭⲩёⲙ υ ⲉύ ⲡⲣυⲱⲗⲟⲥь υⳅⲃⲉⲏяⲧьⲥя ⲥⲃⲟⲉύ ⲯⲁⲗⲕⲟύ ⲅⲗⲟⲧⲕⲟύ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲩ ⲧы ⲣυⲗυ ⲏⲉ ⲃⲇⲩⲡⲗяⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲟύ ⲭⲩύ ⲣⲉⲱυⲗⲁ ⲃ ⲁⲣⲉⲏⲇⲩ ⲃⳅяⲧь ⲏⲁ ⲇⲉⲏь υⳅ ⳅⲁ ⳡⲉⲅⲟ ⲡⲣⲟⲇⲁⲗⲁ ⲡⲟⳡⲕⲩ ⲧⲃⲟⲉⲅⲟ ⳝⲁⲧυ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲩ ⳡё ⳝⲩⲇⲉⲙ ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲧь υⲗυ ⲧы ⲟⲡяⲧь ⲣⲉⲱυⲗ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲥ ⲕⲉⲙ ⲏⲉ ⲇⲉⲗυⲧь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲭⲩёⲙ ⲧⲃⲟю ⲙⲁⲧь ⳃⲁ ⲣⲁⳅⲙⲉⲏυⲣⲟⲃⲁⲗ ⲁ ⲟⲏⲁ ⲟⲧ ⳝⲗⲁⲅⲟⲇⲁⲣⲏⲟⲥⲧυ ⲟⳝ ⲙⲟύ ⲭⲩύ ⲥⲃⲟю ⲡυⳅⲇⲩ ⲥⲧёⲣⲗⲁ ⲏⲁ ⲉⳅ ⲉⳅ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟю ⲙⲁⲧь ⳃⲁ ⲭⲩёⲙ ⲣⲁⲥⳡⲉⲗⲉⲏυⲗ ⲁ ⲟⲏⲁ ⲇⲁⲯⲉ ⲃ ⲧⲁⲕⲟⲙ ⲡⲟⲗⲟⲯⲉⲏυυ ⲥⲙⲟⲅⲗⲁ ⲟⲧⲥⲟⲥⲁⲧь ⲙⲏⲉ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⲏⲉ ⲙⲟⲯⲉⲧ ⲡⲟⲏяⲧь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲃⲥⲉⲅⲇⲁ ⳝⲩⲇⲉⲧ ⲇⲉⲣⲯⲁⲧь ⲏⲁⲇ ⲏⲉύ ⲃⲗⲁⲥⲧь ⲧⲁⲕ ⲧⲟ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲭⲩёⲙ ⲧⲃⲟю ⲙⲁⲧь ⲡⲗⲟⲙⳝυⲣⲟⲃⲁⲗ ⲉύ ⲇⲁⲯⲉ ⲕ ⲥⲧⲁⲙⲁⲧⲟⲗⲟⲅⲩ ⲭⲟⲇυⲧь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲣⲁⳅⲣⲉⳅⲁⲗ ⲁ ⲟⲏⲁ ⲡⲟⳝⲉⲯⲁⲗⲁ ⲕ ⲧⲃⲟⲉⲙⲩ ⳝⲁⲧυ υ ⲡⲟⲕⲁⳅⲁⲗⲁ ⲟⲧⲣⲉⳅⲁⲏⲩю ⲡυⳅⲇⲩ ⲕⲁⲕ ⲡⲣυⲕⲟⲗ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲭⲩёⲙ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁⲩⳡυⲗ ⲡυⲥⲁⲧь ⲏⲟ ⲟⲏⲁ ⲡⲗⲟⲭⲟ ⲃⲟⲥⲡⲣυⲏυⲙⲁⲉⲧ ⲩⳡⲉⲏυя υ ⲏⲁⳡυⲏⲁⲉⲧ ⲥⲟⲥⲁⲧь ⲏⲁ ⲁⲃⲧⲟⲙⲁⲧⲉ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕я ⲥⲧⲣⲉⲗяⲗ ⲃ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲃыⲥⲧⲣⲉⲗυⲗ υ ⲟⲏⲁ ⲧⲃⲁⲣь ⲟⲯυⲗⲁ υ ⲏⲁⳡⲁⲗⲁ ⲡⲟⲗⳅⲧυ ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⲣⲉⲕⲟⲣⲧⲥⲙⲉⲏⲕⲁ ⲡⲟ ⲥⲟⲥⲁⲏυю ⲙⲟⲉⲅⲟ ⲭⲩя ⲉё ⲣⲉⲕⲟⲣⲇ ⲇⲁⲯⲉ ⲧⲃⲟύ ⳝⲁⲧя ⲏⲉ ⲙⲟⲯⲉⲧ ⲡⲟⳝυⲧь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲩ υ ⳡё ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲥⲟⲥⲁⲗⲁ ⲏⲉ ⲏⲁⲇⲟ ⲟⲧⲣυцⲁⲧь ⲃⲉⲇь ⲧы ⲧⲟⲯⲉ ⳅⲁⲡⲟⲇⲟⳅⲣⲉⲏ ⲃ эⲧⲟⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲣⲁⳅⲕⲩⲙⲁⲣυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲇⲁ ⲧⲁⲕⲟύ ⲥⲧⲉⲡⲉⲏυ ⳡⲧⲟ ⲟⲏⲁ ⲉⲗυ ⲉⲗυ ⲇⲟⳝⲣⲁⲗⲁⲥь ⲇⲟ ⲇⲟⲙⲁ ⲇⲁⲯⲉ ⲡⲟ ⲇⲟⲣⲟⲅⲉ ⲟⲏⲁ ⲩⲥⲡⲉⲗⲁ ⲕⲟⲙⲩ ⲧⲟ ⲟⲧⲥⲟⲥⲁⲧь ⲱⲁⲗⲁⲃⲁ ⲯⲁⲗⲕⲁя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲩ υ ⳡё ⲧы ⲙⲟⲯⲉⲱь я ⲯⲉ ⲥⲃⲟυⲙ ⲭⲩёⲙ ⲧⲃⲟυ ⲙыⲥⲗυ ⲧⲁⲕ ⲧⲟ ⲡⲉⲣⲉⲥⲧⲣⲟυⲗ ⲇⲩⲣⲉⲏь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲉ ⲙⲟⲅⲩ ⲥⲕⲁⳅⲁⲧь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥёⲧ ⲃⲥⲉⲙ ⲟⳡⲉⲏь ⳡⲁⲥⲧⲟ ⲃⲉⲇь ⲃⲟⳅⲗⲉ ⲥⲃⲟⲉⲅⲟ ⲭⲩя я ⲃυⲯⲩ ⲉё ⲕⲁⲯⲇыύ ⲇⲉⲏь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕", 
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲩ ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲡⲟ ⳝⲗⲁⲧⲩ ⲙⲏⲉ ⲥⲟⲥёⲧ ⲏⲟ ⲉύ ⲏⲉ ⲭⲃⲁⲧⲁⲉⲧ ⲥⲧυⲙⲩⲗⲁ ⲙⲟⲯⲉⲧ ⲧⲃⲟⲉⲙⲩ ⳝⲁⲧυ ⲭⲩёⲙ ⲃⲉⲏы ⲃⲥⲕⲣыⲧь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲃ ⲣⲁⲙⲕⲩ ⲡⲟⲥⲧⲁⲃυⲗ υ ⲧⲉⲡⲉⲣь ⲃы ⲃⲥⲉύ ⲥⲉⲙьёύ υⲙ ⲗюⳝⲩⲉⲧⲉⲥь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲡⲟ ⲡⲣυⲕⲟⲗⲩ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲏⲁ ⲗⲩⲏⲩ ⳅⲁⲕυⲏⲩⲗ ⲁ ⲟⲏⲁ ⲇⲁⲯⲉ ⲧⲁⲙ ⲃ ⲡⲉⲣⲇⲁⳡⲉⲗⲟ ⲕⲟⲙⲩ ⲧⲟ ⲇⲁⲗⲁ ⲟⲣⲏυ ⲥ эⲧⲟύ ⲱⲗюⲭυ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲙⲟⲅⲩ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲭⲩёⲙ ⲃⳅяⲧь ⲏⲁ ⲡⲣⲟⲅυⳝ ⲏⲟ ⲏⲉ ⲭⲟⳡⲩ ⲃⲉⲇь ⲟⲏⲁ ⲥⲧⲟυⲧ ⲣⲁⲕⲟⲙ υ ⲯⲇёⲧ ⲕⲟⲅⲇⲁ я ⲉё ⲃыⲉⳝⲩ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲣⲁⲥⲱυⲣυⲗ ⲅⲗⲁⲏⲇы ⲭⲩёⲙ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲧⲟ ⲧⲉⲡⲉⲣь ⲟⲏⲁ ⳝⲟⲗьⲱⲉ ⲙⲟⲯⲉⲧ ⲟⲡⲣⲁⳝⲁⲧыⲃⲁⲧь ⲙⲟύ ⳡⲗⲉⲏ ⲥⲃⲟυⲙ ⲣⲧⲟⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲉ ⲥυⲗьⲏⲟ ⲃьⲉⳝⲁⲗ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲗⲩⲡⲟύ ⲏⲟ ⲟⲏⲁ ⲟⲧⲕⲗюⳡυⲗⲁⲥь ⳃⲁ ⲡⲣⲟⲥⲏёⲧьⲥя ⲡⲟ ⲏⲟⲃⲟύ ⲉё ⲡⲟⲉⳝⲩ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲁ ⲏⲉⲅⲁⲧυⲃⲉ ⲉⳝⲁⲗ ⲙⲁⲧь ⲧⲃⲟю ⲃⲉⲇь ⲟⲏⲁ ⳅⲁⲉⳝⲁⲗⲁ ⲃыⲣыⲃⲁⲧьⲥя ⳅⲁ ⳡⲧⲟ я ⲉύ ⲩⲉⳝⲁⲗ ⲗⲉⳃⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲣⲁⳅⲟⲣⲃⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲏⲁ ⳡⲁⲥⲧυ ⲧⲉⲣь ⲧы ⲉⲇυⲏⲥⲧⲃⲉⲏыύ ⲕⲧⲟ ⳝⲩⲇⲉⲧ ⲙⲟύ ⲭⲩύ ⲇⲟ ⲩⳝⲟя ⲥⲟⲥⲁⲧь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲣⲁⲥⲧⲣⲟⲅⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲕⲟⲅⲇⲁ ⲭⲩёⲙ ⲃьⲉⳝⲁⲗ ⲉύ ⲡⲟ ⲅⲩⳝⲁⲙ ⲃⲉⲇь ⲕⲁⲕ ⲙы ⲡⲟⲙⲏυⲙ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⲏьⲱⲉ ⲣⲁⳅυⳝⲃⲁⲗ ⲁ ⳃⲁⲥ ⲡⲣⲟⲥⲧⲟ ⲣⲁⲥёⲕ ⲟⲏⲁ ⲣⲁⲇⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲥⲧⲣⲟυⲗ ⲟⳝⲟⲣⲟⲏⲩ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⲏⲟ ⲥ ⲕⲁⲯⲇыⲙ ⲩⲇⲁⲣⲟⲙ ⲡⲟ ⲥⲧⲉⲏⲁⲙ эⲧⲟύ ⲟⳝⲟⲣⲟⲏы я ⲃⲥё ⳝⲗυⲯⲉ ⲕ ⲅⲗⲟⲧⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲩⲭⲉ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲙⲟύ ⲭⲩύ ⲩⲯⲉ ⲏⲁ ⲥⲧⲟⲗьⲕⲟ ⲃыⲣⲟⲥ ⲃ ⲅⲗⲁⳅⲁⲭ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲧⲟ ⲟⲏⲁ ⲥⲟⲥёⲧ ⲉⲅⲟ ⲙⲉⲥⲧⲟ ⳅⲁⲃⲧⲣⲁⲕⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲣⲁⳅⲙⲩⲣⲟⲃⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲕⲟⲅⲇⲁ ⲟⲏⲁ ⲏⲉ ⲙⲟⲅⲗⲁ ⲃыⳝⲣⲁⲧьⲥя υⳅ ⳅⲁ ⳡⲉⲅⲟ ⲧⲉⲡⲉⲣь ⲟⲏⲁ ⲡⲟ ⲯυⳅⲏⲉⲏⲟ ⲙⲏⲉ ⲇⲟⲗⲯⲏⲁ ⲟⲧⲥⲁⲥыⲃⲁⲧь ⲁ ⲡⲟⲧⲟⲙ ⲧы ⲉё ⲥⲙⲉⲏυⲱь ⲡⲣⲁⲃⲇⲁ ⲯⲉ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲁⲕυⲏⲩⲗ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲕⲁⳝυⲏⲩ ⳅⲁ ⲧⲟ ⳡⲧⲟ ⲟⲏⲁ ⲣⲉⲱυⲗⲁ ⲟⲥυⲗυⲧь ⲙⲟύ ⲭⲩύ ⲥⲃⲟυⲙ ⲣⲧⲟⲙ ⲡⲩⲥⲧь ⲧⲁⲕⲁя ⲱⲁⲃⲕⲁ ⲇⲁⲯⲉ ⲏⲉ ⲡυⲧⲁⲉⲧ ⲏⲁⲇⲉⲯⲇы〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲁⲅⲟⲣⲏⲩⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲡⲣⲟⲥⲧⲟ ⲡⲟ ⲡⲣυⲏцυⲡⲩ ⲏⲟ ⲟⲏⲁ ⲇⲁⲯⲉ ⲧⲁⲕ ⲣⲉⲱυⲗⲁ ⲇⲁⲧь ⲙⲏⲉ ⲃ ⲡυⳅⲇⲩ ⲕⲁⲕ ⳝыⲗⲁ ⲱⲗюⲭⲟύ ⲧⲁⲕ υ ⲟⲥⲧⲁⲗⲁⲥь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲙы ⲡⲟⲥⲡⲟⲣυⲗυ ⲥ ⲟⲧцⲟⲙ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲥⲟⲥⲁⲗⲁ ⲙⲏⲉ ⲏⲉ ⳝⲟⲗьⲱⲉ 200 ⲣⲁⳅ ⲃ ⲇⲉⲏь ⲏⲟ ⲟⲏ ⲡⲣⲟυⲅⲣⲁⲗ ⲃⲉⲇь ⲩⲃυⲇⲉⲗ ⲕⲁⲕ ⲟⲏⲁ ⲟⲧⲥⲁⲥыⲃⲁⲉⲧ ⲙⲏⲉ ⲃ ⲯυⲃⲩю〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟю ⲙⲁⲧь ⲡⲉⲣⲃыύ ⲣⲁⳅ ⳅⲁ ⲕⲩⲥⲟⲕ ⲥⲁⲗⲟ ⲃыⲉⳝⲁⲗ ⲁ ⲟⲏⲁ ⲣⲁⲇⲟⲃⲁⲗⲁⲥь ⳡⲧⲟ ⲙⲟⲯⲉⲧ ⲏⲁⲕⲟⲣⲙυⲧь ⲧⲉⳝя ⲏⲟ ⲕⲁⲕ ⲡⲟⲉⲗ ⲥⲗυⳅⲉⲏь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲡⲟⲡⲣⲟⳝⲩύ ⲉⳃё ⲣⲁⳅ ⲥⲕⲁⳅⲁⲧь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲡⲉⲣⲉⲃⲉⲇⲁⲗⲁ ⲥⲧⲟⲗьⲕⲟ ⲕⲗёⲃыⲭ ⲭⲩёⲃ я ⲧⲉⳝя ⲩⲉⳝⲩ ⲭⲩёⲙ ⲃⲉⲇь ⲟⲏⲁ ⲏⲁ ⲟⲧⲥⲟⲥⲉ ⲡⲣυⳅⲏⲁⲃⲁⲗⲥь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥⲁⲙыύ ⲗⲩⳡⲱυύ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲡⲟ ⳅⲃⲉⲣⲥⲕυ ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⲟⲏⲁ ⲃ ⲱⲟⲕⲉ υ ⲇⲩⲙⲁⲉⲧ ⳡⲧⲟ эⲧⲟ ⲗюⳝⲟⲃь ⲏⲟ я ⲡыⲧⲁюⲥь ⲃⲕⲁⳡⲁⲧь ⲉё ⲥⲡⲉⲣⲙⲁⲕⲟⲙ ⳡⲧⲟⳝы ⲟⲏⲁ ⲡⲉⲣⲉⲇⲟⳅⲏⲩⲗⲁⲥь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲩ υ ⳡё ⲙы ⲧⲉⲡⲉⲣь ⲥ ⲧⲃⲟυⲙ ⳝⲁⲧⲉύ ⲇⲣⲩⳅья ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ ⲕⲁⲕ я ⲇⲁⲗ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕⲉ ⲏⲁ ⲕⲗыⲕ ⲟⲏ ⲩⳅⲏⲁⲗ ⳡⲧⲟ ⲟⲏⲁ ⲯⲁⲗⲕⲁя ⲱⲗюⲭⲁ υ ⲥⲇⲁⲗ ⲉё ⲙⲏⲉ ⲃ ⲣⲁⳝⲥⲧⲃⲟ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⲥⲏⲁⳡⲁⲗⲁ ⲇⲩⲙⲁⲗⲁ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲃыⳅыⲃⲁⲉⲧ ⳅⲁⲃυⲥυⲥⲙⲟⲥⲧ ⲏⲟ ⲥ ⲕⲁⲯⲇыⲙ ⲣⲁⳅⲟⲙ ⲥⲟⲥⲁⲗⲁ ⲃⲥё ⳝⲟⲗьⲱⲉ υ ⳝⲟⲗьⲱⲉ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲁ ⲣⲁⳅⲟⲅⲣⲉⲃ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲟⲉⳝⲁⲗ ⲁ ⲡⲟⲧⲟⲙ ⲧⲃⲟύ ⳝⲁⲧя ⲣⲉⲱυⲗ ⲙⲏⲉ ⲡⲟ ⲫⲁⲏⲩ ⲟⲧⲥⲟⲥⲁⲧь я ⲧⲉⲡⲉⲣь ⲇⲩⲙⲁю ⲩ ⲃⲁⲥ ⲃⲣⲟⲯⲇёⲏⲟⲉ ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲁⲧь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲙⲁⲙⲩⲗьⲕⲁ ⲧⲃⲟя ⲣⲟⲇⲏⲉⲏьⲕⲁя ⳅⲁⲉⳝⲁⲏⲏⲁя ⲕⲩⲣυцⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟυ ⲣⲟⲇυⲧⲉⲗυ ⲟⲡⲩⳃⲉⲏы ⲃыⳝⲗяⲇⲕυ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲩ ⲧⲉⳝя ⲙⲁⲧь ⲥⲣⲁⲏⲁя ⲱⲗюⲭⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕υⲥⲡυⳅⲇяⳡⲩ я ⲧⲃⲟю ⲙⲁⲙⲕⲩ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⳃⲁⲥ ⲃъⲉⳝⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь υⲙⳝⲉцυⲗⲕⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲇⲁ ⲧⲃⲟя ⲙⲁⲧь ⲅⲟⲃⲏⲟⲉⲇⲕⲁ ⲧⲩⲡⲁⲣыⲗⲁя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲩ ⲧⲉⳝя ⲃⲥя ⲥⲉⲙья ⲥⲟⲥⲧⲟυⲧ υⳅ ⲡυⲇⲟⲣⲟⲃ υ ⲗⲉⳅⳝυяⲏⲟⲕ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧы ⳝⲗя ⲧⲩⲧ ⲥⲗυⲱⲕⲟⲙ ⲧⲟ ⲏⲉ ⲁⲭⲩⲉⲃⲁύ ⲩⲉⳝⲟⲕ ⲃⲁⲫⲉⲗьⲏыύ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲥⲩⳡⲁⲣⲁ ⲧы ⲡⲣυⲡυⳅⲇⲏⲩⲧⲁя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲥⲇⲟⲭⲏυ ⲅⲏυⲇⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⳅⲩⳝы ⲧⲟ ⲃыⲡⲁⲗυ ⲉⲡⲧυ,ⲟⲧ υⳅⳝыⲧⲕⲁ ⲥⲡⲉⲣⲙы ⲃ ⲧⲃⲟⲉⲙ ⲃⲇⲟⲗь ⲡⲣⲟⲉⳝⲁⲏⲏⲟⲙ ⲏⲁ ⲭⲩύ ⲉⳝⲁⲗьⲏυⲕⲉ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧы ⲥⲁⲙ ⲃыⳝⲗяⲇⲟⲕ ⲟⲡυⳅⲇⲉⲏⲉⲃⲱυύ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕Ⲕⲁⲕ ⲃы υ ⲡⲣⲟⲯυⲃⲉⲧⲉ... ⲡⲣⲁⲃⲇⲁ ⲏⲉ ⲇⲟⲗⲅⲟ..... ⲩⲣⲟⲇы υ ⲡυⲇⲟⲣы ⲇⲟⲗⲅⲟ ⲏⲉ ⲯυⲃⲩⲧ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧы ⲥⲁⲙ ⲃыⳝⲗяⲇⲟⲕ ⲟⲡυⳅⲇⲉⲏⲉⲃⲱυύ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧы ⲡⲟⲉⳝⲉⲏь ⲱⲁⲗяⲃυⲥⲧⲁя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲙы ⲥ ⲡⲣυяⲧⲉⲗяⲙυ ⲥⲉⲇⲏя ⲃⲙⲉⲥⲧⲟ ⲣⲁⳝⲟⲧы ⲇⲗя ⲡⲣυⲕⲟⲗⲁ ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲟύ ⳝⲁⲗⲟⲃⲁⲗυⲥь ⲡⲟⲇ ⲩⳝⲟύⲏыύ ⲙⲩⳅⲟⲏ, ⲁ ⲧы ⲏⲁⲙ ⲡυⲃⲟ ⲡⲟⲇⲏⲟⲥυⲗ υ ⲟⳝⲟυ ⲡⲟⲡⲣⲁⲃⲗяⲗ ⲅыⲅы ⳝⲗя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲉⳝя ёⳝⲁⲏⲏыύ ⲧы ⲥⲧⲣⲁⲭⲟⳅⲁⲗⲩⲡυⳃⲉ ⲇⲁⲯⲉ ⲏⲉⲕⲟⲙⲩ ⳝⲩⲇⲉⲧ ⲃⲥⲡⲟⲙⲏυⲧь,ⲕⲟⲅⲇⲁ ⲧы ⲥⲇⲟⲭⲏυⲱь ⲩⲉⳝⲁⲕ!!!〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕я ⲧⲉⳝя ⲥⲟⳝⲥⲧⲃⲉⲏⲏⲟⲣⲩⳡⲏⲟ ⲩⲏυⳡⲧⲟⲯⲩ ⲡⲁⲇⲗⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧы ⳡⲉⲣⲧ ⲇⲉⲃяⲧυⲥⲧⲃⲟⲣⳡⲁⲧыύ υⲇυ ⳅⲁⲗⲩⲡⲩ ⲟⳝⲗυⳅыⲃⲁύ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲇⲁ я  ⲥⲙⲉⲣⲧь ⲧⲃⲟя ⲙⲗⲁⲇⲉⲏⳡⲉⲥⲕⲁя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲥⲩⳡⲕⲁ ⲡⲟⲅⲁⲏⲁя ⳡⲧⲟ ⲯⲉ ⲧы ⲡⲁⲥⲧь ⲥⲃⲟю ⳅⲁⲭⲗⲟⲡⲏⲩⲗ ⲡⲉⲧⲩⲭ ⲡⲟⲧыⲕⲁⲏыύ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕я ⲇⲣⲁⲗ ⲧⲃⲟύ ⲣⲟⲧ ⲕⲟⲧⲟⲣыύ ⳝыⲗ ⲏⲁⲡⲟⲗⲏⲉⲏ ⲙⲟⲉύ ⲙⲟⳡёύ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⳝⲉⲗⲁя ⲕⲟⲏⳡь ⲡⲣⲟⲏⳅυⲗⲁ ⲅⲗⲁⲏⲇы ⲧⲃⲟⲉύ ⲡⲣⲟⲥⲧυⲧⲩⲧⲟⳡⲏⲟύ ⲙⲁⲙы ⲁ ⲟⲧⲉц ⲏⲉ ⳅⲏⲁя ⳡⲧⲟ ⲇⲉⲗⲁⲧь ⲏⲁⳡⲁⲗ ⲗυⳅⲁⲧь ⲙⲟⲉύ ⳝⲁⳝⲕⲉ ⲥⲉⲇыⲉ ⲃⲟⲗⲟⲥы ⲏⲁ ⲙⲟⲣⳃυⲏυⲥⲧⲟⲙ ⲗⲟⳝⲕⲉ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧы ⲕⲁⲣⲗⲁⲏ ⲉⳝⲏⲩⲧыύ υⲇυ ⲥⲟⲥυ ⲭⲩύ ⲡⲁⲡυⲏ ⲙⲣⲁⳅь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲙⲟⲭⲏⲁⲣыⲗⲁя ⲧⲉⳝⲉ ⲃ ⲣⲟⲧ ⲕⲟⲏⳡⲁⲗυ 3000 ⲭⲁⳡⲉύ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲁ, ⲭⲩύ ⲥ ⲧⲟⳝⲟύ , υⲧⲁⲕ ⲥⲉⲅⲟⲇⲏя ⲧы ⳝыⲗ ⲥⲗυⲱⲕⲟⲙ ⳝⲗυⳅⲕⲟ ⲡⲟⲇⲡⲩⳃⲉⲏ ⲕ ⲭⲩю〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⳅⲁⲃⲁⲗυ ⲥⲃⲟύ ⲡⲉⲣⲇⲁⲕ, υ ⲏⲉ ⲣⲁⲥⲥⲕⲣыⲃⲁύ ⲉⲅⲟ!〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧы ⲯ ⲕⲟⳡⲉⲅⲁⲣ ⲡⲟ ⲯυⳅⲏυ ⲥⲩⲕⲁ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟё ⲙⲉⲥⲧⲟ ⲏⲁ ⳝⲟⲗⲟⲧⲉ ⲧⲣⲁⲭⲁⲧь ⲗяⲅⲩⲱⲉⲕ.〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲙⲁⲧь ⲕⲣыⲥⲁ ⲡⲟⲗⲩⲇⲟⲭⲗⲁя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲕⲁⲣⲟⳡⲉ ⲧⲃⲟя ⲙⲁⲧь ⲃⲁⲅυⲏⲁ ⲧⲩⲡⲁя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲏⲁⲭⲩя ⲙⲏⲉ ⳡⲧⲟ ⲧⲟ ⲇⲟⲕⲁⳅыⲃⲁⲧь ⲧⲁⲕⲟⲙⲩ ⲟⲧⲣⲉⳝью ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲙⲁⲙⲕⲁ ⲧⲃⲟя ⲅⲏυⲇⲁⲣⲁⲥⲕⲁ ⲟⲧⲭⲩяⲣυⲏⲁя〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟύ ⲟⲧⲉц ⲇⲣⲟⳡⲗυⲃыύ ⲭⲩⲉⲥⲟⲥⲏυⲕ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟⲉ ⲇⲉⲗⲟ ⲥⲟⲥⲁⲧь ⲁ ⲏⲉ ⲅⲁⲃⲕⲁⲧь ⲙⲩⲇⲗⲁⲏ.〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧы ⲡⲟⲏυⲙⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥυⲏⲟⲙⲡυⲕ ⲡυⳅⲇⲁⲕⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲱⲕυ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧы ⲡⲟⲏυⲙⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲇⲟⲣⲟⲯυⲧ ⲡυⳅⲇⲟύ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕυ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲙⲟύ ⲭⲩύ ⲧⲁⲏцⲉⲃⲁⲗ ⲧⲁⲏⲅⲟ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕я ⲯⲉ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣυⲭⲗⲟⲡⲏⲩⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲕⲁⲕ ⲙⲩⲭⲩ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕я ⲧⲃⲟю ⲙⲁⲧь ⲅⲩⲥⲗяⲙυ ⲟⲧ ⲧⲁⲏⲕⲁ ⲉⳝⲁⲗ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲩ ⲧⲉⳝя ⲣⲟⲧ ⲕⲁⲕ ⲡыⲗⲉⲥⲟⲥ ,ⲃⲥⲁⲥыⲃⲁⲉⲧ ⲭⲩυ ⲥⲧⲣⲉⲙυⲧⲉⲗьⲏⲟ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕я ⲧⲃⲟю ⲙⲁⲧь ⳅⲁⲡⲉⲣⲁю ⲏⲁ ⳝⲁⲗⲕⲟⲏⲉ ⳡⲧⲟⳝы ⲟⲏⲁ ⲏⲟⳡью, ⲏⲉ υⲅⲣⲁⲗⲁ ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕я ⲯⲉ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲟⲧⲩⲱⲩ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ, ⲉⳝⲁⲏⲏⲁя ⲧы ⲥⲟⳝⲁⲕⲁ. ⲙⲟύ ⲭⲩύ ⲇⲉⲗⲁⲉⲧ ⲁⲭⲩⲉⲏⲏыⲉ υ ⲇⲟⳝⲣыⲉ ⲇⲉⲗⲁ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲣⲁⲃ ⲕⲟⲅⲇⲁ ⲉⳝⲉⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲁⲏⲁⲗьⲏⲟύ. ⲕⲟⲏⳡⲉⲏⲏⲁя ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ?). я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕⲉⲏⲧⲩⲭⲩ ⲃыⲉⳝⲩ), ⲥⲗыⲱυⲱь ⲏⲁⲉⳝⲁⲏⲏыύ ⳡⲉⲡⲩⲱⲏяⲕ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲉⳝⲩ ⲕⲟⲏⳡⲏⲉⲏыύ ⲧы ⲣⲟⲧ ⳝⲗяⲇь ⲕⲟⲧⲟⲣыύ ⳝⲉⲣⲉⲧ ⲏⲁ ⲥⲉⳝя ⲥⲗυⲱⲕⲟⲙ ⲇⲟⲭⲩя. ⲥⲗыⲱυⲱь ⲟⲧьⲉⳝⲁⲏⲏыύ ⲉⲃⲣⲉύ?), я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲧⲣⲁⲭⲁю υ ⲃыⲕυⲏⲩ ⲉё ⳅⲁⲥⲥⲁⲏыⲉ ⲧⲣⲩⲡ ⲥⲟⳝⲁⲕⲁⲙ ⳡⲧⲟ-ⳝы ⲟⲏυ ⲉё ⲥⲭⲁⲃⲁⲗυ ⲉⳝⲁⲏⲏⲩю ⲱⲁⲗⲁⲃⲩ. ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧⲟ ⲏⲁⲉⳝⲁⲏⲁⲏя ⲙⲟυⲙ ⲭⲩⲉⲙ. ⲥⲗыⲱυⲱь ⲃыⲥⲥⲁⲏыύ ⲡυⲇⲟⲣⲁⲥ. ⲙⲟύ ⲭⲩύ ⲃыⳝⲉⲣⲉⲧ ⲡⲟⳅⲩ ⲇⲗя ⲧⲟⲅⲟ ⳡⲧⲟ-ⳝы ⲃыⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ, υ ⲃыⳝⲉⲣⲉⲧ ⲁⲭⲩⲉⲏⲏю ⲡⲟⳅⲩ ⳡⲧⲟ-ⳝы ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⳝыⲗⲁ ⲇⲟⲃⲟⲗьⲏⲟύ. ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲃыⲉⳝⲉⲧ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁⲉⳝⲁⲏⲏⲩю, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧⲟ ⲱⲟⲱⲕⲁ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя. ⲥⲗыⲱυⲱь ⲙⲣⲁⳅⲟⲧⲁ ⲉⳝⲁⲏⲏⲁя,я ⲕⲁⲕ-ⲧⲟ ⲣⲁⳅ ⲧⲣⲁⲭⲏⲩⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ υ ⲩ ⲏⲉё ⲡⲟⲧⲟⲙ ⲏⲁⳡⲁⲗⲥя ⲥⲡⲁⳅⲙ ⲡυⳅⲇы, ⲧы ⲙⲟⲯⲉⲱь ⳅⲁⲗⲉⳡυⲧь ⲟⳡⲕⲟ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲏⲁя ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ?), я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲉⳝⲩ ⳝⲉⳅ ⲟⳝυⲇ ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏⲏыύ ⲧы ⲡⲉⲇυⲕ.〔 <emoji document_id=6037464506131549087>💀</emoji> 〕",
"〔 <emoji document_id=6037464506131549087>💀</emoji> 〕ⲧⲃⲟя ⲥⲉⲙⲉύⲕⲁ ⲥⲟⳝⲥⲧⲃⲉⲏⲟⲥⲧь ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ!〔 <emoji document_id=6037464506131549087>💀</emoji> 〕"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(shabl3)))
            await sleep(time)
            
            
            
    async def rblackcmd(self, message):
        """[ ! ] Запустить модуль: Ruda Black [ ! ]"""
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Модуль #RudaBlack закончил истреблять шлюх цепью. <emoji document_id=5373290243787070962>💀</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>Модуль #RudaBlack начал убийство шлюхи. <emoji document_id=5373290243787070962>💀</emoji></b>\n\n"
            "<b><emoji document_id=5222468670436943157>🤚</emoji> Чтобы закончить массовые убийства, пиши <code>.rblack</code></b>",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message() 
        shabl4 = [
        "[ <emoji document_id=5373290243787070962>💀</emoji> ] Ⲡυⳅⲇⲉц ⲥыⲏ ⲱⲗюⲭυ ⲧы ⲡⲟⳡⲉⲙⲩ υⳅ ⲇυⲁⲗⲟⲅⲁ ⲡⲣⲟⲡⲁⲇⲁⲉⲱь ⲕⲟⲅⲇⲁ ⲡυⲱⲉⲱь ⲕⲁⲕⲟύ ⲗυⳝⲟ ⲧⲉⲕⲥⲧ я ⲧⲉⳝⲉ ⲣⲁⳅⲃⲉ ⲇⲁⲃⲁⲗ ⲣⲁⳅⲣⲉⲱⳃⲉⲏυя ⲏⲁ эⲧⲟ υⲗυ ⲏⲉⲧ ⲥыⲏⲩⲗя ⲱⲗюⲭυ ⲧы ⲉⳝⲩⳡυύ, ⲧⲉⲕⲥⲧⲁ ⲙⲉⲯⲇⲩ ⲥⲟⳝⲟύ ⲏⲉ ⲥⲟⲉⲇⲉⲏяⲧь ⲥыⲏ ⲥⲗⲁⳝⲟύ ⲱⲗюⲭυ ⲕⲟⲧⲟⲣⲟύ я ⲡⲉⲣⲉⲕⲣыⲗ ⲇыⲭⲁⲏυя ⳅⲁⲗⲩⲡⲟύ, ⲃⲥⲉ ⳅⲏⲁюⲧ ⲟⲇυⲏ ⲭⲩύ ⳡⲧ ⲟⲩ ⲧⲉⳝя ⲙⲁⲙⲁⲱⲁ ⲱⲁⲗⲁⲃⲁ ⲁ ⲧы ⲥыⲏ ⲱⲗюυⲭ ⲕⲟⲧⲟⲣⲁя ⲏⲁⲭⲟⲇυⲧⲥя ⲃ ⲣⲉⲯυⲙυ ⲧⲉⲣⲡυⲗы ⲕⲟⲧⲟⲣⲁя ⲇⲟⲗⲅⲟ ⲏⲁⳝυⲣⲁⲉⲧ ⲥⲟⲟⳝⳃⲉⲏυя ⲇⲁⳝы ⲡⲟⲥⲧⲁⲣⲁⲧⲥя ⲇⲁⲧь ⲙⲏⲉ ⲭⲟⲧь ⲕⲁⲕⲟύ ⲧⲟ ⲟⲧⲡⲟⲣ, ⲧⲉⲡⲉⲣь ⲯⲉ я ⲧⲉⳝⲉ ⲥыⲏ ⲱⲗюⲭυ ⲧⲩⲧ ⲣⲉⲁⲗьⲏⲟ ⲃыⲣⲉⲯⲩ ⲏⲁ ⳃⲉⲕⲁⲭ ⲡⲟⲙⲉⲧⲕⲩ ⲱⲁⲗⲁⲃы υ ⲇⲁⲃⲁⲗⲕυ ⲕⲟⲧⲟⲣⲟύ ⲧⲩ ⲏⲁⲭⲩύ ⲏⲁⲧяⲅⲩ ⲃⲟⲗⲟⲥы ⲥⲏυⲙⲁя υⲭ υⳅ ⲧⲃⲟⲉύ ⲉⳝⲩⳡⲉύ ⳡⲉⲣⲉⲡⲩⲱⲕυ, ⲟⲥⲧⲁⲗⲁя ⲧы ⲥыⲏ ⲱⲗюⲭυ ⲕⲟⲧⲟⲣⲁя ⲉⲗυ ⲕⲁⲕ ⲧⲁⲙ ⲏυⳝυⲣⲁⲉⲧ ⲥⲟⲟⳝⳃⲉⲏυя ⲉⳃё υ ⲥυⲇυⲧ ⲃ ⲡⲟυⲥⲕⲁⲭ ⲧⲉⲕⲥⲧⲟⲃ ⲕⲟⲧⲟⲣыⲉ ⲙⲉⲯⲇⲩ ⲥⲟⳝⲟύ ⲥⲟⲉⲇⲉⲏяⲉⲧ ⳡⲧⲟ ⳝы ⲕⲁⳅⲁⲗⲟⲥь ⳡⲧⲟ ⲟⲏ ⲙⲏⲟⲅⲟ ⲡυⲱⲉⲧ ⲏⲟ ⲏⲁ ⲥⲁⲙⲟⲙ ⲇⲉⲗⲉ ⲧⲟ ⲧы ⲥыⲏ ⲱⲗюⲭυ ⲡⲟⲡⲣⲟⲥⲧⲩ ⲩⲥⲧⲁⲏⲉⲱь эⲧⲟ ⲇⲉⲗⲁⲧь υ ⲧⲉⳝⲉ ⲃ ⲣⲩⳡⲏⲩю ⲡⲣυⲇⲯёⲧⲥя ⲥⲃⲟυⲙυ ⲕⲣυⲃыⲙυ ⲡⲁⲗьцⲁⲙυ ⲏⲁⳝⲣⲁⲧь ⲥⲟⲟⳝⳃⲉⲏυя ⲡⲣυⲯυⲙⲁя ⲕⲗⲁⲃυⲱυ ⲏⲁ ⲥⲃⲟⲉύ ⲡⲟⲧⲏⲟύ ⲕⲃⲁⲗυⲁⲧⲩⲣⲉ ⲥыⲏ ⲅⲁⲏⲇⲟⲏⲁ ⲉⳝⲁⲏⲏⲟⲅⲟ υ ⲗυ ⲉⳃё ⳝⲩⲇⲉⲱь ⲥⲡⲟⲣυⲧь ⲥⲟ ⲙⲏⲟύ ⲥ эⲧυⲙ ⲕⲟⲅⲇⲁ я ⲃⲥю ⲧⲃⲟю ⲙⲁⲧь ⲱⲁⲗⲁⲃⲩ ⲥ ⲏⲟⲅ ⲇⲟ ⲅⲟⲗⲟⲃы ⲟⳝⲭⲁⲣⲕⲁю υ ⳅⲁⲡⲩⳃⲩ ⲕⲁⲕ ⲇⳅыⲅⲩ ⲉⳝⲁⲏⲏⲩю ⲕⲟⲧⲟⲣⲁя ⳝⲩⲇⲉⲱь ⲃⲥё ⲃⲣⲉⲙя ⲏⲁⳝⲣⲁⲧь ⲥⲕⲟⲣⲟⲥⲧь ⲃⲥё ⲟⲗьⲱⲉ υ ⳝⲟⲗьⲱⲉ ⳡⲧⲟ ⳝы ⲡⲟⲧⲟⲙ ⲏⲁⲭⲩύ ⲩⲗⲉⲧυⲧь ⲏⲁ ⲟⲣⳝυⲧⲩ ⲙⲁⲣⲥⲁ υ ⲡⲟⲕⲁⳅыⲃⲁⲧ ьⲃⲥⲉⲙ υⲏⲟⲡⲁⲗⲏⲉⲧяⲧⲙ ⲥⲃⲟю ⲡⲣⲟⳝυⲧⲩю ⲃⲁⲅυⲏⲩ ⲕⲟⲧⲟⲣⲩю ⲉⲥⲗυ ⳅⲁⲕυⲏⲩⲧь ⲅⲣⲁⲏⲁⲧⲩ, ⲏυⳡⲉⲅⲟ ⲏⲉ ⳝⲩⲇⲉⲧ ⲡⲟⲧⲟⲙⲩ ⳡⲧⲟ ⲧы ⲃⲉⲥь эⲧⲟⲧ ⲃⳅⲣыⲃ ⲡⲟⲡⲣⲟⲥⲧⲩ ⲃⲡυⲧⲁⲉⲱь ⲥыⲏ ⲟⲥⲧⲁⲗⲟⲅⲟ ⲅⲩⲙⲩⲏⲕⲩⲗⲁ ⲥυⲇⲁⳃυύ ⲏⲁ ⳡⲗⲉⲏⲉ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] Ⲧы ⲡⲉⲱⲕⲁ ⲉⳝⲁⲏⲁя ⲁ ⲧⲃⲟя ⲙⲁⲧь ⲉⳝⲁⲏⲁя ⲱⲁⲗⲁⲃⲁ ⲩ ⲕⲟⲧⲟⲣⲟύ ⲃⲉⳡⲏⲟ ⲏⲁⳡυⲏⲁюⲧⲥя ⲥⲩⲇⲟⲣⲟⲅυ υⳅ ⳅⲁ ⲟⲧⲥⲩⲥⲧⲃυя ⲙⲟⲉⲅⲟ ⲭⲩя ⲃ ⲉⲉ ⲣⲟⲧⲟⲃⲟύ ⲡⲟⲗⲟⲥⲧυ ⲧы ⲇⲁⲃⲁύ ⲙⲉⲏя ⲧⲩⲧ ⲕⲁⲱⲉⲗⲕⲁ ⲏⲁⲭⲩύ ⲕⲣⲁⲱⲉⲏⲁя ⲧⲉⲣⲡυ ⲣⲉⳃⲉ υ ⲧⲉⲣⲡυ ⲏⲁⲧυⲥⲕυ ⲙⲟⲉⲅⲟ ⲭⲩя ⲧы ⳅⲁⳡⲉⲙ ⲙⲏⲉ ⲧⲩⲧ ⲥⲃⲟύ ⲅⲟⲃⲏⲟ ⲩⲗυⲧⲟⳡⲏыύ ⲧⲁύⲡυⲏⲅ ⲡⲟⲕⲁⳅыⲃⲁⲉⲱ ⲥⲃυⲏⲟⲩⲭυύ ⳝⲗяⲇыⲣь ⲃⲥⲉ ⲙы ⲩⲯⲉ ⳅⲏⲁⲉⲙ ⲱⲟ ⲏⲁ ⲧⲃⲟⲉⲙ ⲉⳝⲗυⳃⲉ ⲕⲗⲉύⲙⲟ ⲥыⲏⲕⲁ ⲡⲟⳝⲗяⲇυ ⲗυⲃⲏυ ⲟⲧⲥюⲇⲁ ⲃ ⲥⲧⲣⲁⲭⲉ ⲉⳝⲁⲏⲁⲧυⳃⲉ ⲏⲁⲭⲩύ ⲡⲟⲕⲁ я ⲃⲏⲁⲧⲩⲣⲉ ⲏⲉ ⲡⲣυⲏяⲗⲥя ⲩⲥⲧⲣⲁυⲃⲁⲧь ⲡⲟⳝⲟυ ⲃ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲱⲗюⲭυ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] Ⲧы ⲧⲁⲙ ⲏⲉ ⲧⲉⲣяύⲥя я ⲧⲉⳝⲉ ⲙⲁⲙⲁⲱⲩ ⲉⳝⲁⲗ ⲧⲉⲗⲕⲁ ⲉⳝⲁⲏⲁя ⲧы ⲇⲁⲁύ ⲧⲟⲗьⲕⲟ ⲇⲟⲗьⲱⲉ ⲙⲏⲉ ⲧⲩⲧ ⲡυⲱυ, ⲡⲟⲕⲁ я ⲧⲉⳝⲉ ⲧⲟⳡⲏⲟ ⲧⲩⲧ ⲧⲟⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲉ ⲃⳝυⲗ я ⲧⲉⳝⲉ ⲯⲉ ⲡⲣⲟⲥⲧⲟ ⲧⲃⲟυ ⲅⲗⲁⳅⲁ ⲃыⲕⲣⲩⳡⲩ ⲏⲁⲭⲩύ ⲟⲥⲧⲥюⲇⲁ  ⳡⲧⲟ ⳝы  ⲧы ⲡⲁⲧⲩⲭ ⲉⳝⲁⲏыύ ⲣⲉⲱυⲗ ⲙⲏⲉ ⲭⲩύ ⲟⲧⲥⲟⲥⲁⲧь я ⲧⲉⳝⲉ ⲥⲕⲁⳅⲁⲗ ⲥⲗⲁⳝⲁⲕ ⲟⳝⲟⲥⲥⲁⲏыύ ⲡⲣⲟⲥⲧⲟ ⲧⲉⳝⲉ ⲧⲩ ⲉⳝⲁⲗⲟ ⲡⲟⲗⲟⲙⲁю ⲏⲁⲭⲩύ ⲧⲁⲕ ⳡⲧⲟ ⲧы ⲡⲟⲧⲙ ⳝⲩⲇⲉⲱь ⲃ ⲟⲕⲣⲟⲃⲁⲗⲁⲉⲏⲏⲟⲙ ⲕⲣⲩⲅⲉ ⲅⲏυⲧь ⲡⲟⲕⲁ я ⲧⲉⳝⲉ ⲏⲉ ⲥⲕⲁⲯⲩ ⲥⲧⲟⲡ я ⲧⲉⳝⲉ ⲯⲉ ⲡⲣⲟⲥⲧⲟ ⲣⲉⲕⲥⲩ ⲉⳝⲁⲏⲟⲙⲩ  ⳝⲩⲇⲩ ⲡⲁⲗⲕυ ⲃ ⲟⳡⲕⲟ ⲥⲟⲃⲁⲧь ⳡⲧⲟⳝы ⲧы ⲡⲟⲏяⲗ ⳡⲧⲟ ⲙⲏⲉ ⲧⲩⲧ ⲏυ ⲟⲇⲏυ ⲧⲃⲟύ ⲧⲉⲕⲥⲧ ⲡⲣⲟⲥⲧⲟ ⲏⲉ ⲙⲟⲯⲉⲧ ⲇⲁⲧь ⲇⲥⲧⲟύⲏыύ ⲟⲧⲡⲟⲣ ⲧⲁⲕ ⳡⲧⲟ ⲙⲟⲯⲉⲱь ⲡⲣⲟⲥⲧⲟ ⲟⳡⲩⲥⲧⲃⲧⲃⲁⲧь ⲅⲟⲗⲟⲇ ⲕⲁ ⲅⲟⲗыύ ⲣⲉⳝⲉύⲏⲟⲕ ⲧⲁⲕ ⳡⲧⲟ я ⲧⲉⳝⲉ ⲥⲕⲁⳅⲁⲗ ⲡⲣⲟⲥⲧⲟ ⲟⲧⲉⳝⲉ ⲧⲩⲧ ⳡⲉⲣⲉⲡ ⲡⲟ ⲱⲃⲁⲙ ⲡⲩⳃⲩ ⲩⲉⳝⲟⲕ ⲅⲟⲗυⲙыύ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] Я ⲃⲥⲧⲣⲉⲧυⲗ ⲧⲃⲟⲉⲅⲟ ⲏⲉ ⲣⲩⲥⲥⲕⲟⲅⲟ ⲟⲡⲩⳃⲉⲏⲏⲟⲅⲟ ⲃыⲉⳝⲁⲏⲏⲟⲅⲟ ⲡυⲇⲁⲣⲁ ⲁ ⲧⲟ ⲉⲥⲧь ⲇⲉⲇⲩⲱⲕⲩ, υ ⳅⲁⲥⲧⲁⲃυⲗ ⲉⲅⲟ ⲟⲧⲥⲟⲥⲁⲧь ⲭⲩύ ⲙⲩⲣⲟⲃья, ⲧⲁⲕ ⲃⲟⲧ ⳅⲁⲧⲉⲙ ⲡⲟⳡⲉⲙⲩ ⲧⲟ ⲃⲥя ⲧⲃⲟя ⲩⳝⲟⲅⲁя ⲃ ⲣⲟⲧ ⲉⳝⲁⲏⲁя ⲥⲉⲙⲉύⲕⲁ ⲡⲣυⳝⲉⲯⲁⲗⲁ ⲕⲟ ⲙⲏⲉ υ ⲡⲟ ⲟⳡⲉⲣⲉⲇυ ⲟⲧⲥⲟⲥⲁⲗυ ⲙⲟύ ⲭⲩύ ⲡⲟⲇ ⲙⲟυⲙ ⲯⲉ ⲥⲧⲟⲗⲟⲙ, ⲧы ⳝыⲗ ⲡⲉⲣⲃыύ ⲡⲟⲧⲟⲙ ⳝыⲗⲁ ⲧⲃⲟя ⲉⳝⲁⲏⲁя ⲱⲗюⲭⲁ ⲙⲁⲙⲕⲁ, ⳅⲁⲧⲉⲙ ⲧⲃⲟύ ⲃыⲉⳝⲁⲏⲏыύ ⳝⲟⲙⲯ ⲟⲧⲉц, ⲟⲡⲩⳃⲉⲏⲏⲁя ⲇⲟ ⲙⲟⲉύ ⲱυⲣυⲏⲕⲉ ⲉⳝⲁⲏⲁя ⲱⲗюⲭⲟⳝⲗяⲇⲥⲕⲁя ⳝⲁⳝⲩⲱⲕⲁ υ, ⲏⲁ ⲕⲟⲏⲉц ⲧⲟ ⲧⲃⲟύ ⲉⳝⲩⳡυύ ⲃ ⲣⲟⲧ ⲡυⲇⲁⲣⲁⲥ-ⲇⲉⲇ, ⲧⲁⲕυⲙ ⲟⳝⲣⲁⳅⲟⲙ я ⲃыⲉⳝⲁⲗ ⲃⲥю ⲧⲃⲟю ⲥⲉⲙⲉύⲕⲩ, ⲉⳝⲁⲏыύ ⲧы ⲗяⲃⲣⲟⲥⲟⲥ) ⲏⲩ ⲧⲁⲕ ⲃⲟⲧ ⲡⲟⲥⲗⲉ эⲧⲟⲅⲟ, ⲕⲁⲕ я ⲡⲉⲣⲉⲉⳝⲁⲗ ⲃ ⲣⲟⲧ ⲃⲥю ⲧⲃⲟю ⲥⲉⲙью, я ⲟⲧⲃⲟⲗⲟⲕ υⲭ ⲭⲩⲉⲙ ⲃ ⲣⲟⲧ ⲏⲁ ⲡⲟⲙⲟύⲕⲩ, ⲧⲁⲙ ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲃ ⲣⲟⲧ ⲃыⲉⳝⲁⲗυ 5 ⲏⲉⲅⲣⲟⲃ, ⲧⲃⲟю ⳝⲁⳝⲩⲱⲕⲩ ⲟⲧъⲉⳝⲁⲗυ 5 ⲭⲁⳡⲉύ, ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲟⲡⲟⲣⲟⳅυⲗυ, ⳝⲟⲙⲯυ, ⲧⲃⲟⲉⲅⲟ ⲇⲉⲇⲩⲱⲕⲩ ⲩⲏυⳅυⲗυ ⲁⲗьⳝυⲏⲟⲥы, ⲁ ⲧⲃⲟύ ⲣⲟⲧ ⲃыⲉⳝⲁⲗυ ⲟⲥы, ⲧⲉⲡⲉⲣь ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲡⲟⲃⲉⲗυⲧⲉⲗь ⲃⲁⲱⲉύ ⲱⲗюⲭⲟ-ⲥⲉⲙьυ?) ⲧⲃⲟя ⲥⲉⲙья υ ⲧы ⲡⲁⲗⲁ ⲟⲧ ⲭⲩя ⲃⲉⲣⲭⲟⲃⲏⲟⲅⲟ, ⲉⳝⲁⲏⲁя ⲧы ⲙⲣⲁⳅь) я ⲧⲃⲟю ⲥⲉⲙⲉύⲕⲩ ⲩⲏυⳡⲧⲟⲯυⲗ ⳡυⲥⲧⲟ ⲃ ⳡⲁⲧⲉ, ⲡⲣυⲕυⲏь ⲕⲁⲕⲟύ ⲡⲟⲥⲗⲉ ⲧы эⲧⲟⲅⲟ ⲟⳝⲟⲥⲥⲁⲏⲟ-ⲟⳝⲟⲥⲣⲁⲏⲏⲟ ⲅⲟⲃⲏⲟⲙ я ⲥⲙⲁⳅыⲃⲁю ⲁⲏⲁⲗ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ ⲕⲁⲕ ⲉⲉ ⲃыⲉⳝⲩ ⲃⲟⲧ ⲧⲉⳝⲉ ⳝы ⲃыⲥⲧⲩⲡⲁⲧь ⲃ цυⲣⲕⲉ ⲏⲁ ⲱⲟⲩ ⲩⲣⲟⲇⲟⲃ, ⲧⲁⲙ ⲧы ⳝⲩⲇⲉⲱь ⲗⲩⳡⲱⲉύ(υⲙ) ⲧы ⲉⳝⲁⲏыύ ⲡⲟⲇⲥⲟⲥ ⲙⲟⲉⲅⲟ ⲭⲩя.  ⲧⲃⲟύ ⲡⲁⲡⲱⲁ ⳅⲁⲙⲩⲧυⲗ ⳝυⳅⲏⲉⲥ  ⲏⲁ ⲥⲟⲥⲁⲏυυ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⲱⲕⲟⲁⲭⲁⲭⲁ ⲧы ⲗⲟⲡⲟⲩⲭⲁя ⲱⲕⲟⲗьⲏυцⲁ ⲕⲟⲧⲟⲣⲁя ⲏⲉ ⲙⲟⲯⲉⲧ ⲙⲏⲉ ⲏυⳡⲉⲙ ⲟⲧⲃⲉⲧυⲧь υ ⲟⲧⲃⲉⳡⲁⲉⲧ ⲃⲟⲡⲣⲟⲥ ⲏⲁ ⲃⲟⲡⲣⲟⲥ ⲡⲟⲧⲟⲙⲩ ⳡⲧⲟ ⲃⲥⲉ ⲧⲃⲟυ ⲙⲟⳅⲅυ ⲃ ⳝⲉⲗⲟύ ⲯυⲇⲕⲟⲥⲧυ  ⲙⲟⲉύ ⲕⲟⲏⳡⲉ) ⲧы ⲉⳝⲗⲁⲏ,ⲇⲩⲙⲁⲉⲱь ⲥⲁⲙыύ ⲩⲙⲏыύ  я ⲃⳅⲟⲣⲃⲩ ⲧⲃⲟю ⲁⲧⲙⲟⲥⲫⲉⲣⲩ!  ⲃⲥⲧⲃⲗю ⲭⲩύ υ ⲃыⲕυⲏⲩ ⲏⲁⲭⲩύ ⲙⲩⲇⲁⲕ  ⲥⲁⲏыύ ⲇцⲡ!)????  ⲡⲟⲏυⲙⲁⲉⲱь я ⲯⲉ ⲡⲣⲟⲥⲧⲟ ⲃ ⲧⲉⲧⲣυⲥ υⲅⲣⲁю ⲏⲁⲇⲟ ⲡⲟⲡⲁⲥⲧь ⲃ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲕⲉ υ ⲃыⲅⲣⲁⲧь  я ⲃ эⲧⲟύ υⲅⲣⲉ ⲏⲉⲡⲟⳝⲉⲇυⲙыύ ⳡⲉⲙⲡυⲟⲏ ⲥⲟⲥυ ⲙⲟύ ⲭⲩύ????)  ⲁⲏⲅⲗυⳡⲁⲏⲉ ⲃⲟ ⲃⲥёⲙ ⲙυⲣⲉ υⳅⲃⲉⲥⲧⲏы ⲟⲧⲥⲩⲧⲥⲧⲃυⲉⲙ ⲥⲟⲃⲉⲥⲧυ ⲃ ⲡⲟⲗυⲧυⲕⲉ. ⲟⲏυ ⳅⲏⲁⲧⲟⲕυ υⲥⲕⲩⲥⲥⲧⲃⲁ ⲡⲣяⲧⲁⲧь ⲥⲃⲟυ ⲡⲣⲉⲥⲧⲩⲡⲗⲉⲏυя ⳅⲁ ⲫⲁⲥⲁⲇⲟⲙ ⲡⲣυⲗυⳡυя. ⲧⲁⲕ ⲟⲏυ ⲡⲟⲥⲧⲩⲡⲁⲗυ ⲃⲉⲕⲁⲙυ, υ эⲧⲟ ⲏⲁⲥⲧⲟⲗьⲕⲟ ⲥⲧⲁⲗⲟ ⳡⲁⲥⲧью υⲭ ⲏⲁⲧⲩⲣы, ⳡⲧⲟ ⲟⲏυ ⲥⲁⲙυ ⳝⲟⲗьⲱⲉ ⲏⲉ ⳅⲁⲙⲉⳡⲁюⲧ эⲧⲟύ ⳡⲉⲣⲧы. ⲟⲏυ ⲇⲉύⲥⲧⲃⲩюⲧ ⲥ ⲧⲁⲕυⲙ ⳝⲗⲁⲅⲟⲏⲣⲁⲃⲏыⲙ ⲃыⲣⲁⲯⲉⲏυⲉⲙ υ ⲧⲁⲕⲟύ ⲁⳝⲥⲟⲗюⲧⲏⲟύ ⲥⲉⲣьёⳅⲏⲟⲥⲧью, ⳡⲧⲟ ⲩⳝⲉⲯⲇⲁюⲧ ⲇⲁⲯⲉ ⲥⲁⲙυⲭ ⲥⲉⳝя, ⳡⲧⲟ ⲟⲏυ ⲥⲗⲩⲯⲁⲧ ⲡⲣυⲙⲉⲣⲟⲙ ⲡⲟⲗυⲧυⳡⲉⲥⲕⲟύ ⲏⲉⲃυⲏⲏⲟⲥⲧυ. ⲟⲏυ ⲏⲉ ⲡⲣυⳅⲏⲁюⲧⲥя ⲥⲉⳝⲉ ⲃ ⲥⲃⲟёⲙ ⲗυцⲉⲙⲉⲣυυⲏυⲕⲟⲅⲇⲁ ⲟⲇυⲏ ⲁⲏⲅⲗυⳡⲁⲏυⲏ ⲏⲉ ⲡⲟⲇⲙυⲅⲏёⲧ ⲇⲣⲩⲅⲟⲙⲩ υ ⲏⲉ ⲥⲕⲁⲯⲉⲧ: ⲏⲟ ⲙы ⲡⲟⲏυⲙⲁⲉⲙ, ⳡⲧⲟ υⲙⲉⲉⲙ ⲃ ⲃυⲇⲩ. ⲟⲏυ ⲏⲉ ⲧⲟⲗьⲕⲟ ⲃⲉⲇⲩⲧ ⲥⲉⳝя ⲕⲁⲕ ⲟⳝⲣⲁⳅⲉц ⳡυⲥⲧⲟⲧы υ ⲏⲉⲡⲟⲣⲟⳡⲏⲟⲥⲧυ — ⲟⲏυ ⲥⲉⳝⲉ ⲃⲉⲣяⲧ. эⲧⲟ υ ⲥⲙⲉⲱⲏⲟ, υ ⲟⲡⲁⲥⲏⲟ. [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲇⲁ ⳡⲧⲟ ⲧы ⲉⳃё ⲙⲟⲯⲉⲱь ⲙⲏⲉ ⲡυⲥⲁⲧь ⲧⲩⲡⲟⲉⳝⲗⲟⲉ ⲧы ⲡⲟⳅⲟⲣυⳃⲉ ⳡⲧⲟ ⲡⲟⲗⲩⳡυⲗⲟ ⲩⲯⲉ ⲡⲟ ⲥⲃⲟⲉⲙⲩ ⲉⳝⲁⲗьⲏυⲕⲩ υ ⲇⲁⲗⲉⲉ ⲥⲧⲁⲣⲁⲉⲧⲥя ⲕⲁⲕ-ⲧⲟ ⲡⲟⲇⲇⲉⲣⲯⲁⲧь эⲧⲟⲧ ⲏⲉⲇⲟ ⲕⲟⲏⲫⲗυⲕⲧ ⲡⲣⲟⲧυⲃ ⲙⲟⲉⲅⲟ ⲡⲉⲏυⲥⲁ, ⲧы ⲗυⲱь ⲡⲟⲧⲩⲯⲉⲏⲉц ⲏυⲕⲟⲙⲩ ⲏⲉυⳅⲃⲉⲥⲧⲏыύ ⳡⲧⲟ ⲥⲧⲁⲣⲁⲉⲧⲥя ⲕⲁⲕ-ⲧⲟ ⲏⲉ ⲟⲧⲥⲟⲥⲁⲧь ⲙⲟύ ⲭⲩύ ⲩⲯⲉ ⲡⲩⳝⲗυⳡⲏⲟ ⲟⲡⲟⳅⲟⲣυⲃⲱυⲥь υⲥⲡⲟⲗьⳅⲟⲃⲁⲏυⲉⲙ ⲉⳝⲁⲏⲟⲅⲟ ⲱⲁⳝⲗⲟⲏⲁ, ⲧы ⳅⲇⲉⲥь ⲡⲣⲟ100 ⲏⲁⲡⲣⲟ100 ⲥⲁⲙⲁя ⲥⲗⲁⳝⲁя ⲇⲉⲅⲉⲏⲉⲣⲁⲧυⲃⲏⲟⲃυⲇⲏⲁя ⲡⲉⲱⲕⲟⲃυⲇⲏⲁя ⲟⲧⲥⲟⲥⲁⲃⲱⲁя ⲙⲟю ⲭⲩυⲏⲩ ⲣⲟⲃⲏⲟ ⲧⲁⲕ ⲯⲉ ⲕⲁⲕ υ ⲃⲥⲉ ⲙⲟυ ⲟⲡⲡⲟⲏⲉⲏⲧы ⲡⲟⲇⲭⲩύⲏⲁя ⲇⲟⳡь ⲅⲟⲃⲏⲁ ⲥⲩⳃⲉⲥⲧⲃⲩюⳃⲁя ⲗυⲱь ⲇⲗя ⲧⲟⲅⲟ ⳡⲧⲟⳝы ⲙⲟύ ⲭⲩύ ⲙⲟⲅ ⲏⲁⲥυⲗⲟⲃⲁⲧь ⳡьυ ⲧⲟ ⲧⲩⲱυ... [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧы ⲥⲗⲁⳝыύ ⲣⲁⳝ ⲙⲟⲉⲅⲟ ⲭⲩя ⳡⲧⲟ ⲙⲟⲯⲉⲧ ⲗυⲱь ⲥⲃⲟю ⲕⲁⲱⲩ ⲥⲣⲁⲧь я ⲡⲣⲟⲥⲧⲟ ⲏⲁⲡⲣⲟⲥⲧⲟ ⲧⲉⳝⲉ ⲏⲁ ⲧⲃⲟё ⲟⲙⲉⲯⲏⲟⲉ ⲥⲃυⲏⲟⲉⳝⲗυⳃⲉ ⲥⲣⲁⲧь ⳝⲩⲇⲩ ⲡⲟⲕⲁ ⲧы ⲏⲉ ⲩⲙⲣёⲱь ⲧⲩⲧ ⲉⳝⲁⲏⲏⲁя ⲡⲟⲧⲩⲯⲏⲁⳡ ⲏⲁⲥⲁⲇⲕⲁ ⲏⲁ ⲙⲟύ ⳡⲗⲉⲏ ⲕⲩⲇⲁ ⲧы ⲃⲟⲟⳝⳃⲉ ⲧⲩⲧ ⲗⲉⳅⲉⲱь ⲏⲁⲭⲩύ ⲧⲩⲡⲟⲉⳝⲗыύ ⲧы ⲇⲉⲅⲉⲏⲉⲣⲁⲧυⲃⲏⲟⲃυⲇⲏыύ ⲥыⲏ ⲭⲩύⲏυ ⳡⲧⲟ ⲧⲁⲕ ⲯⲉ ⲕⲁⲕ υ ⲧⲟⲧ ⲟⲗυⲅⲁⲫⲣⲉⲏ ⲃыⲗⲉⲧυⲧ ⲥ ⲡυⲏⲕⲁⲙυ υⳅ ⲕⲗⲁⲏⲁ Ⲫⲣⲁⲏцυυ ⳡⲧⲟ ⲥⲟⳝⲥⲧⲃⲉⲏⲏⲟ ⲅⲟⲃⲟⲣя ⲏⲉⲩⲇυⲃυⲧⲉⲗьⲏⲟ υⳝⲟ ⲧы ⲗυⲱь ⲥⲗⲁⳝⲁя ⲙⲉⲇⲗⲉⲏⲏⲁя ⲩⲏυⲯⲉⲏⲏⲁя ⲙⲏⲟю ⲏⲁⲥⲁⲇⲕⲁ ⲏⲁ ⳅⲁⲗⲩⲡⲩ ⳡⲧⲟ ⳡⲁⲥⲧυⲕⲟⲙ ⲡыⲧⲁⲉⲧⲥя ⲗυⲱь ⲟⲧⲥⲟⲥⲁⲧь ⳅⲇⲉⲥь ⲙⲟύ ⲭⲩύ ⲧⲁⲕ ⲥⲕⲁⲯⲉⲙ ⲙⲟⲏⲩⲙⲉⲏⲧⲁⲗьⲏⲟⲃⲥⲕυύ ⲭⲁⲭⲁ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧⲉⳝⲉ ⲇⲟ ⲙⲉⲏя ⲕⲁⲕ ⲇⲟ ⲕⲣⲁя ⳅⲉⲙⲗυ ⲏⲁⲭⲩύ ⲇⲁ υ ⲃⲥⲉ я ⲧ ⲉ ⲧⲩⲧ ⲙⲁⲧь ⲃыⲃⲉⲣⲏⲩ ⳡυⲥⲧⲟ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥⲇⲉⲗⲁю ⲉⲉ ⲫⲟⲣⲙⲟύ ⲥⲃⲁⲥⲧυⲕυ ⲏⲁⲭⲩύ ⲧы ⲡⲟⲡⲣⲟⳝⲩύ ⲡⲟⲧⲟⲙ ⲉⲉ ⲃыⲡⲣяⲙυⲧь ⲉⳝⲩⳡυύ ⲡⲗⲟⲥⲕⲟⲉⳝⲗыύ ⲟⳝⲭⲁⲣⲕⲁⲏыύ ⲥⲃυⲏⲟⲩⲗыⳝⳡⲁⲧыύ ⲥыⲏⲩⲗя ⲱⲁⲗⲁыы ⲭⲁⲭⲁⲭⲁⲭ ⲧы ⲣяⲗ ⳡⲧⲟυⲗ ⲥⲗυⲱⲕⲟⲙ ⲙⲏⲟⲅⲟ ⲏⲁ ⲥⲉⳝья ⳡⲧⲟⲗυ ⳝⲉⲣⲉⲅⲱ я ⲡⲟⲏяⲧυьⲧ ⲉⲏ ⲙⲟⲅⲩ ⳝυⳡ я ⲧⲉⳝⲉ ⲧⲩⲧ ⲃⲏⲁⲧⲩⲣⲉ ⲃⲥⲉ ⲧⲃⲟυ ⲧⲩⲧ ⲥⲩⲥⲧⲁⲃυ ⲡⲁⲗьц ⲡⲉⲣⲉⲗⲟⲙⲁю ⳡⲧⲟ ыⲧ ⲙⲏⲉ υ ⲏⲉ ⲉⲇυⲏⲡυύ ⲟⲧⲡⲟⲟⲣ ⲉⲏ ⲇⲁⲱ ⲯⲉ ⲧⲁⲕ ⲥⲕⲁⲯⲉⲙ яⲧ я ⲧⲩⲧ ⲡⲟⲡⲣⲟⲥⲧⲩ ⲏⲁⲭⲩύ ⲟⳝⲏⲩⲗυⲣⲩю ⲥⲃⲟυⲙ ⲡⲉⲏυⲥⲟⲙ ⲇⲁ υ ⲃⲥⲉ ⲉⳝⲁⲏⲁя ⲧⲉⲗⲟⳡⲕⲁ ⲥⲩⲕⲁⳅⲭ ⲁⲭⲁⲭⲭⲁ ⳅⲁⲃⲁⲗυ ⲉⳝⲁⲗⲟ ⲥⲃⲟⲉ ⲩⲯⲉ ⲧы ⲥⲟⳝⲁⲕⲁ ⲉⳝⲁⲏⲁⲃя ⲏⲁⲭύⲩ я ⲧⲉ ⲧⲩⲧ ⲡⲁⲥⲧυь ⲃⲏⲁⲧⲩⲣⲉ ⲣⲁⳅⲟⲣⲃⲩ ⲥⲃⲟυⲙ ⲡⲉⲏυⲥⲟⲙ ⲁⲗⲉ ⲏⲁⲭⲩύ ⲥⲗыⲱυⲱ ⲯⲁⲣⲕⲟ ⲥⲧⲁⲏⲟⲃυⲧⲥя?? ⲇⲁ ⲉⲧⲟ я ⲯⲉ ⲧⲃⲟⲗю ⲙⲁⲙⲁⲁⲱⲩ ⳅⲁⲥ ⲉⳝⲩ ⲇⲟ ⲟⲣⲅⲁⳅⲙⲁ ⲡⲟⲇ ⲣⲁⲙⲱⲧⲁⲏⲥⲕυύ ⲣⲟⲕ ⲁⲗⲉ ⲏⲁⲭⲩ υⲇυυ ⲉⲉ ⲩⲯⲉ ⳝⲉⳅ ⲥⲟⳅⲏⲁⲏⲉⲙя ⳅⲁⳝυⲣⲡⲁύ ⳡⲧⲟⲗυ υⲏⲃⲁⲗυⲗⲇ ⲉⳝⲩⳡύυ ⲁ ⲧⲟ ⲟⲏⲁ ⲧⲁⲕ ⲧⲟ ⲏⲁⲡⲣυⲗⲁⲥь ⲙⲟⲉύ ⲥⲡⲉⲣⲙⲟύ ⳡⲧⲟ ⲩⲯⲉ ⲧⲁⲕ ⲣⲉⳅⲕⲟ ⲏⲁⲭⲩύ ⲟⲡьяⲏⲉⲗⲁ я υ ⲥⲁⲙ ⲏⲉ ⲟⲯυⲇⲁⲗ ⲏⲟ ⲏⲁ ⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲧⲁⲕⲁя ⲃⲟⲧ ⲯυⲣⲏⲁя ⲏⲁъⲭⲩύ ⲱⲁⲗⲁⲃⲁ ⲗⲇⲁⳅⲭⲁⲭⲁ ⲉⳝⲧυь ⲧы ⲉⳝⲩⳡυύ ⲯⲟⲡⲟⲗυⳅ ⲡⲣⲟⳝυⲣⲟⳡⲏыύ ⲧⲩⲧ ⲡⲟⲡⲣⲟⲥⲧⲩ ⲉⲏⲁⲭⲩύ я ⲧя ⲧⲩⲧ ⲩⲏυⳡⲧⲟⲯⲩ ⲕⲁⲕ ⲇⲉⲇⲁⲧь ⲏⲉⲭⲩⲩύ ⲧы ⲙⲉⲏя ⲡⲟⲏυⲙⲁⲉⲱ ⲉⳝⲩⳡύυ ⲥыⲏⲟⲕ ⳝяⲗⲇυ υⲗυ ⲏⲉⲧ ⲏⲁⲭⲩύ ⳅⲭⲁⳅⲭⲁⲭⲁ ⲧы ⳅⲁⲕⲣⲟύ ⲉⳝⲁⲗⲟ ⲥⲃⲟⲉ ⲩⲯⲉ ⲏⲁⲭⲩύ ⲃⲟ υⲙя ⲁⳅⲟⲃⲁ ⲃⲟ υⲙя ⲃⲥⲉύ ⲩⲕⲣⲁυⲏυ ⲃⲟ υⲙя ⲃⲥⲉύ ⲉⲃⲣⲟⲡυ ⲏⲁⲭⲩύ ⲙы ⳝⲩⲇⲉⲙ ⲧя ⲉⳝⲁⲧь υ ⲧⲃⲟю ⲃⲥю ⲥⲉⲙью ⲏⲁⲭⲩύ ⲡⲟⲃⲉⲥυⲙ ⳡυⲥⲧⲟ ⲏⲁ ⲧⲃⲟυⲭ ⲅⲗⲁⳅⲁⲭ ⲏⲁⲭⲩύ ⳡⲧⲟ ⲧы ⲡⲟⲡⲣⲟⲥⲧⲩ ⲃ ⲥⲗⲉⳅⲁⲭ ⲡⲩⳝⳝⲗυⳡⲏⲟ ⲩ ⲩⲕⲣⲁυⲏⲥⲕⲟⲅⲟ ⲏⲁⲣⲟⲇⲁ ⲏⲁⳡⲏⲉⲱ ⲕⲁⲯⲇⲟⲙⲩ ⲏⲁⲙ ⲕⲧⲟ ⲃ ⲉⲧύⲟ ⲕⲏⲫ ⲡⲟⲗυⲣⲟⲃⲁⲧь ⲏⲁⲱⲱ ⲡⲉⲏυⲥ ⲥⲃⲟυⲙ яⳅυⲕⲟⲙ ⲥⲗыⲱυⲱ ⲙⲉⲏя ⲉⳝⲩⳡυύ ⳝⲗяⲇⲟяⳃⲉⲣ ⲏⲅⲁⲭⲩύ υⲗυ ⲙⲏⲉ ⲉⳃⲉ ⲣⲁⳅ ⳡⲧⲟⲗυ ⲡⲟⲃⲧⲟⲣυⲧь ⲭⲁⲭⲁⲭⲁ ⲏⲁⲭⲩύ я ⲏⲉ ⲡⲟⲏяⲗ ⲧⲉⲗⲕⲁ ⲉⳝⲁⲏя ⲏⲉ ⲇⲁύ ⳝⲟⲅ ⲧы ⲗυⲃⲏⲉⲱ ⲟⲧ ⲥюⲇⲁ ⲟⲧ ⲙⲟⲉⲅⲟ υⲙⲉⲏⲟ ⲡⲉⲏυⲥⲁ ⲏⲁⲭⲩύ ⲧⲉ ⲧⲩⲧ ⲏⲉ ⲯыⲧь ⲧⲁⲕ ⲧⲟ ⲡⲟⲗⲩⲫⲁⳝⲣυⲕⲁⲧ ⲉⳝⲩⳡύυ  ⲕⲟⲡⲣⲟⲫυⲗьⲏыύ ⳡυⲥⲧⲟ ⳅⲁⲗⲩⲡⲟⲅⲗⲁⲃⳅыύ ⲥыⲏⲟⲕ ⲩⳝⲗяⲇυ ⲡⲉⳃⲉⲣⲏⲟύ ⲏⲁⲭⲩύ я ⲧⲉⳝⲉ ⲧⲩⲧ ⲃⲏⲁⲧⲩⲣⲉ ⳡυⲥⲧⲟ υⲙⲉⲏⲟ ⲧⲃⲟю ⲡⲟⲧⲏⲩю ⲃⲁⲅυⲏⲩ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲟⲣⲃⲩ ⲧы ⳡⲟ ⲧⲁⲙⲁ ⲉⳝⲁⲏⲁя ⲏⲁⲭⲩύ ⲟⳝⲉⳅьяⲏⲁ ⲏⲩ ⲉⳝⲁⲧь ⲣяⲗ ⳡⲟⲧⲁ ⲧы ⲥⲗυⲱⲕⲟυⲙ ⲇⲁⲭⲩя ⲏⲁ ⲥⲉⳝя ⳝⲉⲣⲉⲱ ⲏⲩ ⲏυⳡⲉⲅⲟ ⲏⲁⲭⲩύ ⳃⲁⲥ υⲥⲡⲣⲁⲃυⲙ ⲏⲁⲭⲩύ я ⲧⲉⳝⲉ ⲧⲩⲧ ⳡυⲥⲧⲟ ⲉⳝⲁⲗьцⲟ ⲃ ⲥⲙяⲧⲕⲩ ⲉⳝⲁⲏⲩ ⲡⲁⲇⲁⲗь ⲧы ⲕⲣⲁⲱⲉⲏⲁя ⲏⲁⲭⲩύ ⲥⲗыⲱⲁⲗⲁ ⲙⲉⲏя ⲡⲣⲟⲫⲩⲣⲁ ⲉⳝⲁⲏⲁя υⲗυ ⲏⲉⲧ ⲏⲁⲭⲩύ я ⲏⲉ ⲡⲟⲏяⲗ ⲧы ⲧⲁⲙⲁ ⲇⲁⲃⲁύ ⲉⳝⲁⲧь ⳃⲁⲥ ⲏⲁⲡⲣяⲅυⲥь ⲟⲧ ⲙⲟⲉⲅⲟ ⲡⲉⲏυⲥⲁ я ⲧⲉⳝⲉ ⲅⲁⲣⲁⲏⲧυⲣⲩю ⳡⲧⲟ ⲧⲉⳝⲉ ⲧⲩⲧ ⲡυⳅⲇⲉц ⲩⲭ ⲕⲁⲕⲟύ ⲏⲁⲭύⲩ ⲏⲁⲥⲧυⲅⲏⲉⲧ ⳡⲧⲟ ⲧы ⲟⲧ ⲟⲇⲏⲟⲅⲟ ⲧⲁⲕ ⲥⲕⲁⲯⲉⲙ ⲙⲟⲉⲅⲟ ⲡⲟⲭⲟⲇⲩ ⲃⲕυⲏⲟⲧⲟⲅⲟ ⲧⲉⲕⲥⲧⲁ ⲥⲣⲁⳅⲩ ⲏⲁⲭⲩύ  ⲡⲟⲧⲉⲣяⳡⲉⲱ ⲥⲃⲟύ ⲣⲁⳅⲩⲙ υ ⲏⲁⳡⲏⲉⲱ ⳡυⲥⲧⲟ ⲥⲟⲥⲁⲧь ⲙⲟύ ⲡⲉⲏυⲥ ⲃⲉⲇь ⲟⲏ ⲧⲁⲕ υ ⲧяⲏⲉⲧ ⲧⲃⲟⲉ ⳡⲩⲙⲁⳅⲟⲉ ⲣыⲗⲟ ⲁⲭⲁⲭ ⲁⲩ ⲉⳝⲩⳡυύ ⲥыⲏ ⲱⲗюⲭυ ⲧы ⲧⲁⲙⲁ ⲏⲉ ⲧⲉⲣⲡυ ⲙⲟύ ⲡⲉⲏυⲥ ⲃⲏⲁⲧⲩⲣⲉ ⲧⲉⳝⲉ ⲧⲩⲧ ⲙⲁⲙⲁⲱⲩ ⳡυⲥⲧⲟ ⲧⲣⲁⲭⲏⲩ ⲁⲗⲉ ⲉⳝⲁⲏⲁя ⲡⲣⲟⲫⲩⲣⲁ ⲧы ⳡⲟⲧⲁⲙⲁ ⲣⲁⲥⲩⲇⲕⲁ ⲩⲯⲉ ⲥⲃⲟⲉⲅⲟ ⲗⲉⲱυⲗⲁⲥь ⲏⲁⲭⲩύ υⲗυ ⳡⲟ я ⲡⲟⲏяⲧь ⲏⲉ ⲙⲟⲅⲩ ⲏⲁⲭⲩύ ⲧы ⲧⲁⲙ ⲇⲁⲃⲁύ ⲏⲉ ⲡυⳅⲇυ ⲉⳝⲩⳡυύ ⲥыⲏⲩⲗя ⳝⲗяⲇυ ⲏⲁⲭύⲩ я ⲧⲉ ⲧⲩⲧ ⲃⲏⲁⲧⲩⲣⲉ ⲏⲁⲭⲩύ ⳡυⲥⲧⲟ ⲙⲁⲙⲁⲱⲩ ⲧⲣⲁⲭⲏⲩ ⲥⲃⲟυⲙ ⲡⲉⲏυⲥⲟⲙ ⲁⲗⲉ ⲧы ⳡⲟ ⲧⲁⲙ ⳝⲗяⲇⲥⲕυύ ⲥыⲏⲟⲕ ⲱⲗюⲭⲟⲡⲟⲇⲟⳝⲏύⲟ ⲙⲣⲁⳅυ ⲧы ⲧⲁⲙ ⲇⲁⲃⲁύ ⲉⳝⲁⲧь ⲏⲉ ⲩⳝⲉⲅⲁύ ⲟⲧ ⲉⲧⲟύ ⲕⲟⲏⲫы я ⲧⲉⳝⲉ ⲧⲩⲧ ⲙⲁⲧь ⲉⳝⲁⲗ ⳡυⲥⲧⲟ ⲫⲣⲕυ ⲉⳝⲩⳡυύ ⲁⲗⲉ ⲏⲁⲩύ ⲧы ⲧⲁⲙ ⲉⳝⲁⲧь ⲏⲉ ⲩⲙⲣυ ⲟⲧ ⲙⲟⲉⲅⲟ ⳝⲟⲅⲟⲡⲟⲇⲟⳝⲏⲟⲅⲟ ⲕⲟⲗυⳡⲉⲥⲧⲃⲁ ⲥⲗыⲱυⲱ ⲙⲉⲏя ⲉⳝⲁⲏⲁя ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲁ ⲙⲟⲉⲅⲟ ⲡⲉⲏυⲥⲁ я ⲧⲉⳝⲉ ⳡυⲥⲧⲟ ⲧⲩⲧ ⲙⲁⲧь ⲃыⲧⲣⲁⲭⲁю ⲕⲁⲕ ⲇⲉⲗⲁⲧ ь ⲏⲉⲭⲩύ ⲇⲁ υ ⲃⲥⲉ ⲁⲣⲩ ⲉⳝⲁⲧь ⲣяⲗ ⲯⲉ ⲧы ⲥыⲏυⳃⲉ ⲉⳝⲁⲏⲟύ ⲱⲁⲗⲁⲃы ⳝⲗяⲇь ⲏⲁ ⲥⲣυⲕⲉⲣⲁⲱⲟⲧ υⲗυ ⲕⲁⲕ ⲧⲁⲙ ⲧя ⲏⲟⲩ ⲏⲉύⲙ ⲉⳝⲩⳡυύ υⳅ ⲥⲁύⲗⲉⲏⲥⲁ ⲟⲧⲏыⲏⲉ ⲏⲁⳡⲏⲩ я ⲏⲁ ⲧⲃⲟⲉⲙ ⲉⳝⲁⲗⲉ ⲃыⲯυⲅⲁⲧь ⲥⲃⲟⲉ υⲙя #ⲇⲁⲏυяⲣⲟⲃ ⲁⳅⲟⲃⲥⲕⲟⲉ ⲡⲟⲏяⲗ ⲙя  ⲃыⳝⲗяⲇⲟⲕ я ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲃⲉⲥь ⲯⲉⲗⲧыύ ⳅⲩⳝⲏⲟύ ⲥⲟⲥⲧⲁⲃ ⲏⲁⳡⲏⲩ ⲕⲣⲩⲱυⲧь ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲟ ⲃⲥⲉύ ⲕⲟⲏⲫⲉ ⲉⲉ ⳅⲩⳝы ⳝⲩⲇⲩⲧ ⲃⲟⲗяⲧⲥя ⲁ ⲡⲟⲧⲟⲙ ⲧⲉⳝя ⲉⳝⲁⲏⲉⲟⲅⲟ ⲥⲟⲡⲗяⲕⲁ ⳅⲁⲥⲧⲁⲃⲗю ⲃⲥⲉ ⳅⲁ ⲏⲉύ ⲩⳝυⲣⲁⲧь ⲧы ⲙⲉⲏя ⲥⲗыⲱυⲱ ⲃⲟⲟⳝⳃⲱⲉ ⲥⲟⲡⲗяⲕ ⲉⳝⲩⳡυύ ⲏυⳡⲧⲟⲯⲏыύ ⲡⲟⲏυⲕⲱυύ ⲡⲟⲥыⲏⲟⲕ ⳝⲗяⲇяⲧυⲏы ⲕⲟⲧⲟⲣυύ ⲣⲉⲱυⲗ ⲧⲧⲩⲟ ⲟⲥⲙⲉⲗυⲗⲥя ⲡⲉⲣⲉύⲧυ ⲇⲟⲣⲟⲅⲩ ⲡⲣⲟⲧυⲃ ⲙⲟⲉⲅⲟ ⲭⲩя ⲕⲟⲧⲟⲣυύ ⳃⲁⲥ ⲧⲉⳝя ⲧⲩⲧ υⳅⲟⳝьⲉⲧ ⲏⲁⲭⲩύ ⲇⲟ ⲥⲙⲉⲣⲧυ ⳅⲁⲃⲁⲟυ ⲩⲯⲉ ⲧы ⲥⲃⲟⲉ ⲧⲩⲡⲟⲉ ⲉⳝⲁⲗⲟ ⲥыⲏⲩⲗя ⲉⳝⲁⲏⲟύ ⲡⲣⲟⳝⲗяⲇυⲏы ⲏυⳡⲧⲟⲯⲏⲟύ ⲧы ⲟⲧ ⲕⲁⲯⲇⲟⲅⲟ ⲱⲟⲣⲟⲭⲁ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⳝⲩⲇⲉⲧ ⲗⲟⲃυⲧь ⲡⲁⲏυⳡⲉⲥⲕυⲉ ⲁⲧⲁⲕυ ⲕⲁⲕ ⲗⲟⲃυⲗⲁ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ υⲭ ⲃ ⲧⲉⲙⲏⲟⲧⲉ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⳡⲧⲟ ⲩ ⲱⲁⲗⲁⲁⲃы ⲧⲃⲟⲉύ ⲟⲧⲏыⲏⲉ ⲡⲟяⲃⲗяюⲧⲥя ⲅⲁⲗюцυⲏⲁцυυ ⳝⲩⲇⲧⲁ ⲟⲏ ⲃυⲇυⲧ ⲙⲟύ ⲭⲩύ ⲕⲟⲧⲟⲣυύ ⳃⲁⲥ ⲉⲉ ⲃыⲉⳝⲉⲧ ⳝⲟ ⲟⲏⲁ ⲡⲥυⲭυⲕⲩ ⲧⲉⲙ ⲥⲁⲙυⲙ ⲥⲃⲟю ⲡⲟⲅⲁⲏⲩю ⲥⲗⲟⲙⲁⲗⲁ ⲧы ⲉⳝⲩⳡυύ ⲱⲉⲥⲧⲉⲣⲏυⲕ ⲧⲩⲧ ⲁⲗⲉ ⳡυⲥⲧⲟ ⲡⲟⲅⲁⲏь ⳝⲗяⲇⲥⲕⲁя ⲭⲁⲭⲁⲭⲁ ⲕⲩⲥⲟⲕ ⲧы ⲣⲉⲁⲗьⲏⲟ ⲏⲁⲭⲩύ ⲥыⲏⲁ ⲱⲁⲗⲁⲃы υⳅ ⲥⲁύⲗⲉⲉⲏⲥⲁ ⲧⲉ ⲅⲟⲃⲟⲣю ⲃⲁⲗьⲏυ ⲥⲃⲟⲉ ⲉⳝⲁⲗⲟ ⲩⲯⲉ ⲅⲣяⳅⲏыύ ⳡⲟⲣⲏыύ ⲥыⲏ ⲱⲁⲗⲁⲃы ⲧⲃⲟю ⲉⳝⲁⲏⲩю ⲙⲁⲧь ⲱⲁⲗⲁⲃⲩ ⲃыⲉⳝⲁⲗυ ⲭⲁⳡυ ⳅⲁ ⲅⲁⲣⲁⲯⲁⲙυ ⲃⲙⲉⲥⲧⲟ ⳅ ⲧⲟⳝⲟύ ⳡⲙⲟⲱⲏυцⲁ ⲧы ⲙⲁⲗⲟυⲙⲩⳃⲁя ⲯυⲃⲩⳃⲁя ⳅⲁ ⲥⳡⲉⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⲃ ⲕⲁⲕⲟύ ⲧⲟ ⳝⲣⲉⲯⲏⲉⲃⲕⲉ υⳅ ⲣⲁⲱⲕⲟⲥⲧⲁⲏⲁ ⲧы ⲥⲗⲁⳝⲁⲕ ⲉⳝⲩⳡυύ ⲡⲣυⳅⲏⲁύ ⲉⲧⲟ ⲩⲯⲉ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲉⳝⲗυⳃⲉ ⲥⲗⲟⲙⲁю ⲧⲩⲧ ⲏⲁⲭⲩύ я ⲃⲥю ⲉⲉ ⳡⲩⲙⲁⳅⲩю ⲕⲟⲯⲩ  [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧы ⳡⲟ ⲧⲁⲙⲁ ⲉⳝⲩⳡυύ ⲥыⲏⲟⲕ ⲩⲗьⲧⲣⲁⳝⲗяⲇυ ⲏⲁⲭⲩύ ⲃ ⲥя ⲡⲟⲃⲉⲣυⲗⲁ ⳡⲧⲟⲗυ ⲧⲉⲗⲕⲁ ⲉⳝⲁⲏⲁя я ⲧⲉ ⲧⲩⲧ ⲙⲁⲙⲁⲱⲩ ⲉⳝⲁⲗ ⳡυⲥⲧⲟ ⲥⲗⲁⳝⲁⲕ ⲉⳝⲩⳡυύ ⲏⲁⲭⲩύ ⳅⲁⲕⲣⲟύ ⲉⳝⲁⲗⲟ ⲥⲃⲟⲉ ⲩⲯⲉ я ⲧⲃⲟⲉ ⲣыⲗⲟ ⲧⲩⲧ ⲡⲟⲧⲁⲥⲕⲩⲭⲏⲟⲉ ⳡυⲥⲧⲟ ⲟⳝ ⲥⲃⲟύ ⲡⲉⲏυⲥ ⲏⲁⲭⲩύ ⲥⲗⲟⲙⲁю ⲡⲟⲏυⲙⲁⲉⲱ ⲧы ⲙⲉⲏя υⲗυ ⲏⲉⲧ ⲏⲁⲭύⲩ ⲥыⲏ ⲩⳝⲗяⲇυ ⲉⳝⲁⲏⲟύ я ⲧⲉ ⲧⲩⲧ ⲃⲏⲁⲧⲩⲣⲉ ⳡυⲥⲧⲟ ⲃⲥⲉ ⲕⲟⲥⲧυ ⲧⲃⲟυ ⳡⲟⲣⲏыⲉ ⲃⲙⲉⲥⲧⲉ ⳅ ⳅⲩⳝⲁⲙυ ⲏⲁⲭⲩύ ⲥⲗⲟⲙⲁю ⲥⲁⲗⲟ ⲧы ⲣⲩⲥⲏяⲃⲟⲉ ⲏⲁⲭⲩύ ⲁⲗⲉ ⲧы ⲧⲩⲧ ⲃⲏⲁⲧⲩⲣⲉ ⲟⲇυⲏ ⲭⲩύ ⲉⳝⲩⳡυύ ⲥыⲏ ⲅⲟⲃⲏⲁ ⲏⲁⲭⲩύ ⳡυⲥⲧⲟ ⲧя ⲧⲩⲧ ⲃ ⲡⲣⲁⲭ ⲏⲁⳡⲏⲩ ⲟⳝⲣⲁⳃⲁⲧь ⲥⲗыⲱⲁⲗⲁ ⲙⲉⲏя ⲧы ⲕⲣυⲃⲁⲏⲟⲥⲁя ⲇⲟⳡⲕⲁ ⲭⲩύⲏυ ⲡⲁⲣⲱυⲃⲟύ ⲏⲁⲭⲩ υⲗυ ⲏⲉⲧ я ⲡⲟⲏяⲧυь ⲏⲉ ⲙⲟⲅⲩ я ⲧⲉ ⲧⲩⲧ ⲙⲁⲧⲉⲣь ⲱⲁⲗⲁⲃⲩ ⳡυⲥⲧⲟ ⲃыⲉⳝⲩ ⲧⲩⲡⲟⲉⳝⲗⲁя ⲏⲁⲭύⲩ ⲥⲃυⲏⲟⲅⲁⲇυⲏⲁ ⲏⲁⲭⲩύ ⲡⲟⲇⳅⲁⲗⲩⲡⲏⲁя ⲇⲁ υ ⲃⲥⲉ ⲟⲇυⲏ ⲭⲩύ ⲧы ⲫⲣυⲕ ⲉⳝⲩⳡύυ ⲡⲟⲙⲣⲉⲱ ⲕⲟⲥⲟⲉⳝⲗⲁя ⲥⲃυⲏⲟⳝⲗяⲇυⲏⲁ ⲏⲁⲭⲩύ ⲧⲩⲧ ⳡυⲥⲧⲟ ⲏⲁⲭύⲩ ⲃыыⲙⲣⲉⲱ я ⲧⲉⳝⲉ ⲅⲃⲟⲟⲣю ⲉⳝⲩⳡυύ ⲡⲟⲗⲩⲫⲁⳝⲣυⲕⲁⲧ ⲃⲁⲗьⲏυ ⲣыⲗⲟ ⲥⲃⲟⲉ ⲏⲁⲭⲩύ ⲧы ⳡⲟ ⲧⲁⲙⲁ ⲧⲉⲗⲕⲁ ⲣяⲗ ⳡⲧⲟⲗυ ⲃ ⲥя ⲡⲟⲃⲉⲣυⲗⲁ ⳡⲧⲟⲗυ ⲏⲁⲭύ υⲗυ ⳡⲟ я ⲡⲟⲏяⲧь ⲏⲉ ⲙⲟⲅⲩ я ⲧⲉ ⲧⲩⲧ ⲉⳝⲁⲏⲟύ ⲱⲁⲗⲁⲃⲉ ⲃⲏⲁⲧⲩⲣⲉ ⲯⲉ ⲃⲥⲉ ⲧⲃⲟυ ⲉⳝⲩⳡυⲉ ⲣⲁⲕⲟⲙ ⲏⲁⲭⲩύ ⳝⲟⲗьⲏυⲉ ⲟⲣⲅⲁⲏы ⲃыⲃⲉⲣⲏⲩ ⲏⲁ υⳅⲏⲁⲏⲕⲩ ⲧы ⳡⲟ ⲧⲁⲙⲁ ⲉⳝⲩⳡυύ ⲭⲩⲉⳝⲉⲥ ⲥⲗыⲱυⲱ ⲙⲉⲏя ⲏⲁⲭⲩύ ⲏⲉ ⳅⲁⲥⲧⲁⲃⲗяύ ⳃⲁⲥ ⲙⲉⲏя ⲡⲣυⲏυⲙⲁⲧьⲥя ⲉⳝⲁⲧь ⲧⲃⲟю ⲯυⲣⲏⲩю ⲕⲣυⲃⲁⳅⲩⳝⲩю ⲙⲁⲧь ⲱⲁⲗⲁⲃⲩ ⲧы ⲯⲉ ⲣяⲗ ⲧⲩⲧ ⲟⲧⲗⲉⲧυⲱ ⲥⲟ ⲥⲃⲟⲉύ ⲉⳝⲁⲏⲟύ ⲯυⲣⲏⲟύ ⲙⲁⲧⲩⲱⲕⲟύ ⲏⲁⲭⲩύ ⲏⲁ ⲥⲃⲁⲗⲕⲩ ⲅⲣⲉⳡⲉⲥⲕⲩю ⲃыⲣⲟⲇⲟⲕ ⲉⳝⲩⳡύυ ⲏⲁⲭⲩύ я ⲧⲉ ⲧⲩⲧ ⲕⲟⲡυⲗяⲣⲕⲩ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳃⲁⲥ ⲥⲗⲟⲙⲁю ⲧы ⳡⲟ ⲧⲁⲙⲁ ⲉⳝⲁⲏⲁя ⲏⲁⲭⲩύ ⳡυⲥⲧⲟ ⲥⲃυⲏⲟⲃыⲯⲁⲧыύ ⲉⳝⲩⳡυύ ⲟⳝⲣыⲅⲁⲏⲏыύ ⲥыⲏⲟⲕ ⲇⲉⲣⲉⲃⲉⲏⲥⲕⲟύ ⲯυⲣⲏⲟύ ⲕⲁⲣⲅυ ⲏⲁⲭⲩύ я ⲧⲉ ⲧⲩⲧ ⲙⲁⲧь ⲉⳝⲁⲗ ⲥⲗыⲱυⲱ ⲙⲉⲏя ⲏⲁⲭύⲩ я ⲧⲉ ⲧⲩⲧ ⲥⲃⲟⲉύ ⲥⲡⲉⲣⲙⲟύ ⲃⲥⲉ ⲡⲉⲣⲉⲡⲟⲏⲕυ ⲏⲁⲭⲩύ ⳃⲁⲥ ⲥⲗⲟⲙⲁю ⲁⲗⲉ ⲏⲁⲭⲩύ ⲃⲥⲉ ⲗⲟⲡⲏⲉⲧ ⳡυⲥⲧⲟ ⲩ ⲧⲉⳝя ⲃⳅⲇⲩⲧⲁя ⲏⲁⲭⲩύ ⲣⲟⲅⲁⲧⲁя ⲥⲃυⲏья ⲁⲣⲩ ⲟⳝⲭⲁⲣⲕⲁⲏыύ ⳡυⲥⲧⲟ ⲗυⳡυⲏⲩⲥ ⲏⲁⲭⲩύ я ⲧⲉⳝⲉ ⲧⲩⲧ ⲏⲟⲅυ ⲃⲥⲉ ⲡⲉⲣⲉⲗⲟⲙⲁю ⲅⲁⲭⲩύ ⲧы ⲉⳝⲁⲏⲁя ⲏⲁⲭⲩύ ⲡυⲇⲁⲣⲁⲥυⳃⲱⲉ ⲙⲟⲉⲅⲟ ⲡⲉⲏυⲥⲁ ⲕⲁⲕ ⲏⲉ ⲕⲣⲩⲧυ ⲧы ⲥыⲏ ⲩⲅⲣюⲙⲟύ ⳝⲗяⲇυ ⲏⲁⲭⲩύ ⲧⲩⲧ ⲁⲣⲩ я ⲧⲉ ⲧⲩⲧ ⲃⲥⲉ ⲗⲁⲡы ⲡⲟⲣⲃⲩ ⲉⳝⲩⳡυύ ⲧы ⳃⲉⲏⲟⲕ ⲏⲁⲭⲩύ ⳝⲉⳅⳅⲁⳃυⲧыύ ⲁⲣⲩ ⲏⲁⲭύⲩ ⲧы ⳡⲟ ⲧⲁⲙⲁ ⲧⲉⲣⲡυⲗⲁ ⲉⳝⲁⲏⲁя ⲃ ⲥя ⳡⲧⲟⲗυ ⲡⲟⲃⲉⲣυⲗⲁ ⲏⲁⲭⲩύ υⲗυ ⳡⲟ я ⲡⲟⲏяⲧь ⲏⲉ ⲙⲟⲅⲩ ⲏⲁⲭⲩύ я ⲯⲉ ⲧⲃⲟⲉ ⲉⳝⲁⲗⲟ ⲧⲩⲧ ⲃⲏⲁⲧⲩⲣⲉ ⲃ ⳃυ ⲥⲏⲉⲥⲩ ⲉⳝⲩⳡυύ ⲥⲗⲩⳡⲁύ ⲗⲁⲉ ⲏⲁⲭⲩύ ⲧⲉⲗⲕⲁ ⲉⳝⲁⲏⲁя ⲗⲁⲃⲁύ я ⲧⲉⳝⲉ ⲧⲩⲧ ⲙⲁⲧь ⲉⳝⲁⲗ ⳡυⲥⲧⲟ ⲏⲟⲥⲟⲣⲟⲅ ⲉⳝⲩⳡυύ ⲁⲗⲉ ⲏⲁⲭύⲩ ⲁⲗⲉ ⲏⲁⲭⲩύ ⲩⲗυⲧⲕⲁ ⲉⳝⲁⲏⲁя ⳃⲁⲥ ⳝⲩⲇⲉⲧ ⲣⲁⲥⲡⲣⲁⲁⲃⲁ ⲏⲁⲇ ⲧⲟⳝⲟύ υ ⲧⲃⲟⲉύ ⲉⳝⲁⲏⲟύ ⲱⲗюⲭⲟⲙⲁⲧⲉⲣυ ⲉⳝⲩⳡυύ ⲏⲁⲭύⲩ ⳝυⳡⲟⲏⲟⲕ ⲧⲩⲧ ⲃⲏⲁⲧⲩⲣⲉ ⲧⲉⳝⲉ ⲃⲥⲉ ⲃⲟⲗⲟⲥυ ⲧⲃⲟυ ⲉⳝⲩⳡυⲉ ⲃ ⲡⲉⲣⲭⲁⲧⲉ ⲟⳝⲕⲟⲏⳡⳡⲁю ⲏⲁⲭύⲩ ⲥⲗыⲱυⲱ  ⲙⲉⲏя ⲥыⲏ ⲱⲁⲭⲧы ⲉⳝⲁⲏύⲟ я ⲱⲩⲣⲩⲡⲉⲃⲉⲣⲧⲟⲙ ⲧⲉ ⲉⳝⲁⲗⲟ ⲧⲩⲧ ⲥⲏⲉⲥⲩ ⳡυⲥⲧⲟ ⲟⳝⲟⲥⲁⲏыύ ⲥыⲏⲩⲗя ⲇⲉⲅⲣⲁⲇυⲣⲟⲃⲟⲏⲟύ ⳝⲗяⲇυ ⲁⲗⲉ ⲏⲁⲭύⲩ я ⳡⲟⲧⲁ ⲏⲉ ⲡⲟⲏяⲗ ⲧы ⲏⲁⲭⲩύ ⲙⲏⲉ ⲧⲩⲧ ⲥⲃⲟυ ⲧⲁⲕⲧ ⲟⲥⲗⲁⳝυⲉ ⲡⲟⲧⲩⲅυ ⲧⲁⲕ ⲧⲟ ⲥⲧⲁⲗ ⲡⲟⲕⲁⳅυⲃⲁⲧь ыⲧ ⳡⲟ ⲧⲁⲙ ⲉⳝⲁⲏⲁя ⲙⲁⲣⲁⳅⲙⲁⲧυⳡⲉⲥⲕⲁя ⲭⲩⲉⲕⲣыⲗⲁя ⲇⲟⳡⲕⲁ ⲩⳝⲗяⲇυ ⲃⲏⲁⲧⲩⲣⲉ ⳡⲧⲟⲗυ ⲃ ⲥя  ⲡⲟⲃⲉⲣυⲗⲁ ⲏⲁⲭύ υⲗυ ⳡⲟ я ⲡⲟⲏяⲧь ⲏⲉ ⲙⲟⲅⲩ ⲏⲁъⲭⲩύ ⲧы ⲉⳝⲁⲏⲁя ⲱⲁⲗⲁⲃⲁ ⳡυⲥⲧⲟ ⲇⲉⲣⲉⲃⲉⲏⲥⲕⲁя ⲏⲁⲭⲩύ я ⲧⲉ ⲧⲩⲧ ⲙⲧⲁь ⲉⳝⲁⲗ ⲁⲗⲉ ⲏⲁⲭⲩύ ⲫⲣυⲕ ⲉⳝⲩⳡυύ ⲇⲁⲃⲁύ ⲡⲉⲣⲉⳝυⲃⲁύ ⲙⲟύ ⲡⲉⲏυⲥ ⲏⲁⲭⲩύ я ⲧⲉ ⲧⲩⲧ ⲙⲁⲧь ⲉⳝⲁⲗ ⳡυⲥⲧⲟ ⲥⲗыⲱυⲱ ⲙⲉⲏя ⲣⲟⲅⲟⲏⲟⲥⲉц ⲅⲏυⲗⲟύ ⲏⲁⲭъⲩύ ⲏⲉ ⲥⲙⲉύ ⲙⲏⲉⲉ ⲧⲩⲧ ⲡⲟⲧⲩⲭⲁⲧь ⲉⳝⲁⲏⲁя ⲧⲉⲗⲕⲁ ⲏⲁⲭⲩύ я ⲧⲉ ⲩⲧⲧ ⳡυⲥⲧⲟ ⲙⲁⲙⲁⲱⲩ ⲱⲗюⲭⲩ ⲃыⲧⲣⲁⲭⲁю ⲁⲗⲉ ⲏⲁⲭⲩύ ⲧⲉⲗⲕⲁ ⲉⳝⲁⲏⲁя я ⲧⲉ ⲧⲩⲧ ⲃⲥⲉ ⲧⲃⲟυ ⲏⲁⲭⲩύ ⲡⲟⳡⲉⲣⲏⲉⲃⲱυⲉ ⲏⲟⲅⲧυ ⲏⲁⲭⲩύ ⲥⲗⲟⲙⲁⳝю ⳃⲁⲥ ⲧы ⳡⲟ ⲧⲁⲙⲁ ⳝⲉⲣⲉⲅⲁ ⳡⲧⲟⲗυ ⲡⲟⲡⲩⲧⲁⲗⲁ ⲥⲃυⲏья ⲉⳝьⲁⲏⲁя υⲗυ ⳡⲟ ⲏⲁⲭъύⲩ ⲭⲁⲭⲁⲭⲁ ⲁⲣⲩ ⲏⲁⲭⲩύ ⲃⲏⲁⲧⲩⲣⲉ ⲧы ⲫⲣυⲕ ⳝⲗяⲇⲥⲕυύ ⲏυⲕⲟⲙⲩ ⲏⲉ υⳅⲃⲉⲥⲧⲏыύ ⲏⲁⲭύⲩ ⳡυⲥⲧⲟ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲣⲯⲁⲃⲉⲃⲱⲩю ⲧⲩⲧ ⲥⲏⲉⲥⲩ ⳡυⲥⲧⲟ ⲥⲃⲟυⲙ ⲙⲉⲧⲁⲗυⳡⲥⲕυⲙ ⳝⲟⲅⲟⲡⲟⲇⲟⳝⲏυⲙ ⲭⲩⲉⲙ ⲃⲟ ⲥⲗⲁⲃⲩ ⳝⲁⲏⲇⲉⲣυ ⲭⲁⲭⲁⲭ ⲥⲃυⲏⲧⲩⳅ ⲉⳝⲩⳡύ ⲏⲁⲭⲩύ ⲕⲟⲧⲟⲣυύ 250 ⲥⲗⲟⲃ ⲡⲡυⲱⲉⲧ ⳝⲗяⲇь ⲏⲁⲭⳅⲩ 6 ⲙυⲏ ⲏⲩ ⲧы ⳡⲟ ⲧⲁⲙⲁ ⲉⳝⲁⲏⲁя ⲱⲗюⲭⲟⲧⲉⲏь ⲃⲏⲁⲧⲩⲣυⲉ ⲯⲉ ⲏⲁⲭⲩύ ⲧⲩⲧ ⲡⲟⲙⲣⲉⲱ ⳡυⲥⲧⲟ ⲉⳝⲩⳡύυ ⲟⳝⲕⲩⲣⲉⲏυύ ⲏⲁⲭⲩύ ⲡⲟⲧⲟⲙⲟⲕ ⲡⲣⲟⲫⲩⲣы ⲁⲗⲉ ⲏⲁⲭⲩύ ⲏⲩ ⲧы ⲧⲁⲙ ⲏⲉ ⲩⲙⲣυ ⲃⲏⲁⲧⲩⲣⲉ ⲉⳝⲩⳡυύ ⲥыⲏ ⲅⲟⲃⲏⲁ ⲏⲁⲭⲩύ ⲙⲏⲉ ⲏⲉ ⲥⲟⲥⲧⲁⲃυⲧ ⲧⲩⲧ ⲧⲣⲩⲇⲁ ⲥⲏⲉⲥⲧυ ⲧⲃⲟⲉ ⲅⲟⲃⲏⲟⲣⲟⲯⲟⲉ ⲣыⲗⲟ ⲡⲟⲃⲉⲣь ⲙⲏⲉ ⲏⲁ ⲥⲗⲟⲃⲟ ⲏⲁⲭⲩύ ⲧⲉⲣⲡυⲗυⳅⲟⲃⲁⲏⲁя ⲭⲩύυⲧⲁ ⳡυⲥⲧⲟ ⲏⲁⲭⲩύ ⲡⲟⲙⲣⲉⲱ ⲯⲉ ⲟⲇυⲏ ⲭⲩύ ⲏⲁ ⲙⲟⲉⲙ ⲡⲉⲏυⲥⲉ ⲙⲇⲉ ⲉⳝⲩⳡυύ ⲥⲗⲁⳝⲁⲕ ⲏⲁⲭⲩύ ⲃⲁⲗьⲏυ ⲉⳝⲁⲗⲟ ⲥⲥⲟⲃⲉ я ⲧⲉ ⲅⲟⲃⲟⲣю ⲧⲉ ⲧⲩⲧ ⲕⲗюⲃ ⳡυⲥⲧⲟ ⲡⲟⲣⲃⲩ ⲥⲃⲟυⲙ ⲡⲉⲏυⲥⲟⲙ ⲁⲗⲉ ⲉⳝⲁⲏⲁя ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲁ ⲏⲁⲭⲩύ ⲧы ⲧⲁⲙ ⲇⲁⲃⲁύ ⲏⲉ ⲡυⳅⲇυ ⲏυⳡⲉⲅⲟ ⲡⲉⲧⲩⲱⲟⲕ ⲉⳝⲩⳡυύ ⲏⲁⲭⲩύ я ⲧⲉⳝⲉ ⲧⲩⲧ ⲙⲁⲙⲁⲱⲩц ⲉⳝⲁⲗ ⲯυⲣⲏⲩю ⲱⲗюⲭⲩ ⲁⲗⲉ ⲏⲁⲭⲩύ ⲥⲗыⲱυⲱ ⲙⲉⲏя ⳃⲁⲥ ⲙⲟя ⳡυⲥⲧⲟ ⲡⲗⲁⲙⲉⲏⲁя ⳅⲁⲗⲩⲡⲁ ⲡⲟ ⲧⲃⲟⲉⲙⲩ ⲉⳝⲁⲗⲩ ⲡⲟύⲇⲉⲧ ⲕⲁⲕ ⲡⲟ ⲙⲁⲥⲗⲩ ⲏⲁⲭⲩύ ⲧя ⲧⲩⲧ ⲡⲣⲟⲯⲅⲩ ⲥⲃⲟⲉύ ⳝⲟⲅⲟⲡⲟⲇⲟⳝⲏⲟύ ⲙⲟⳃⲏⲟύ яⲣⲟⲥⲧью ⳡⲧⲟ ⲟⲧ ⲧⲉⳝя ⳡυⲥⲥⲧⲟ ⲟⲥⲧⲁⲏⲩⲧⲥя ⲏⲁⲭⲩύ ⲟⳝⲅⲟⲣⲉⲗыⲉ ⲕⲟⲥⲧⲟⳡⲕυ ⲏⲁ ⲥьⲉⲇⲉⲏυя ⲡⲥⲁⲙ ⲩⲕⲣⲁυⲏⲥⲕυⲙ ⲥⲗыⲱυⲱ ⲙⲉⲏя ⲥыⲏⲟⲕ ⲙⲩⲥⲟⲣⲟⲃⲟⳅⲁ я ⲧⲉⳝⲉ ⲧⲩⲧ ⲣыⲗⲟ ⲏⲁⲭⲩύ ⲥⲗⲟⲃⲏⲟ ⲡⲉⳡⲉⲏьⲉ ⲣⲁⲥⲕⲣⲟⲱⲩ ⲥⲃⲟυⲙ ⲡⲉⲏυⲥⲟⲙ ⲧы ⳡⲟ ⲧⲁⲙⲁ ⲡⲟⲧⲏⲁя ⲱⲁⲗⲁⲃⲁ ⲣυⲗ ⳡⲧⲟⲗυ ⲃ ⲥя ⲡⲟⲃⲉⲣυⲗⲁ ⲏⲁⲭⲩύ υⲗυ ⳡⲟ я ⲡⲟⲏяⲧь ⲏⲉ ⲙⲟⲩⲅ яⲧ ⲉⳝⲉ ⲧⲩⲧ ⲙⲁⲧь ⲉⳝⲁⲗ ⲃⲥⲉ ⲣⲁⲃⲏⲟ ⲕⲁⲕ ⲏⲉ ⲕⲣⲩⲧυ υⲇυ ⲉⲉ ⲇⲉⲫⲁύ ⳡⲧⲟυⲗ я ⲏⲉ ⳅⲏⲁю ⲉⳝⲩⳡύυ ⲥыⲏ ⲱⲗюⲭυ ⲏⲁⲭⲩύ ⲧы ⲧⲩⲧ ⲡυⳅⲇυⲱ ⲃⲥяⲕⲩю ⲭⲩύⲏю ⲧы ⲧⲩⲧ ⲏⲉ ⲥⲙⲉύ ⲉⳝⲁⲏⲁя ⲡⲁⲇⲁⲗь ⳝыⲧь ⲡⲟ ⲥυⲗⲉ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲇⲉⲫⲟⲗⲧⲏыύ ⲧы ⲥыⲏ ⳝⲗяⲇⲥⲕⲟύ ⲱⲉⲗⲩⲭυ ⲇⲁ υ ⲃⲥⲉ я ⲧⲉⳝя ⳡⲗⲉⲏⲟⲙ ⳃⲁⲥ ⲧⲩⲧ ⳝⲩⲇⲩ ⲃⲟⲥⲡυⲧыⲃⲁⲧь ⲡⲟ ⲏⲟⲃⲟύ ⳝⲟ ⲧы ⲉⳝⲁⲧьⲧ ⲇⲣ ⲧⲁⲕⲟύ ⲥⲧⲉⲡⲉⲏυ ⲏⲁυⲥⲗⲁⳝⲉύⲱυύ ⲣⲉⳝⲉⲏⲟⲕ ⲏⲁⲭⲩύ ⳡⲧⲟ я ⲏⲉ ⲙⲟⲅⲩ ⲧы ⲉⳝⲁⲧь ⲧⲩ ⳃⲁⲥ ⳝⲩⲇⲉⲱ ⲃⲏⲁⲧⲩⲣⲉ ⲏⲁ ⲙⲟⲉⲙ ⳡⲗⲉⲏⲉ ⲇⲣⲟⲯⲁⲧь υ ⳡⲩⲃⲥⲧⲃⲟⲃⲁⲧь ⲧⲩ ⳝⲟⲗь ⲕⲟⲅⲇⲁ я ⳝⲩⲇⲩ ⲧⲉⳝⲉ ⲉⳝⲁⲏⲟⲙⲩ ⲥыⲏⲩ ⲱⲗюⲭυ ⲣⲃⲁⲧь ⲁⲏⲩⲥ ⲧы ⲉⳝⲁⲧь ⲧⲩⲧ ⲩⲯⲉ ⲩⲅⲟⲙⲟⲏυⲥь ⲥⲗыⲱυⲱ ⲧы ⲙⲉⲏя ⲙⲟⲗь ⲧы ⲉⳝⲁⲏⲁя ⲁⲣⲩ ⲧы ⲉⳝⲁⲧь ⲧⲩⲧ ⲥыⲏ ⲯυⲣⲏⲟύ ⲱⲁⲗⲁⲃы ⲃ ⲟⳝⲗυⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲩ ⲥⲗⲩⲱⲁύ ⲥюⲇⲁ ⲙⲉⲏя ⲥыⲏ ⲧы ⲕⲟⲥⲟⲣыⲗⲟύ ⲥⲧⲩⲭⲱⲉύ ⳝⲗяⲇυ я ⳃⲁⲥ ⲏⲁⳡⲏⲩ ⲧⲩⲧ ⳡⲗⲉⲏⲟⲙ ⲃыⲧⲁⲥⲕυⲃⲁυь ⲧⲃⲟυ ⳅⲁⲗⲩⲡⲟⲅⲗⲁⳃⲉ ⲏⲁⲭⲩύ υ ⲕⲟⲏⳡⲁⲧь ⲃ ⲇыⲣⲕυ ⲏⲁⲭⲩύ ⲧⲃⲟυ ⲧы ⲙⲉⲏя ⲡⲟⲏяⲗ ⲧы ⳝⲗяⲇь ⲧⲩⲡⲟⲣыⲗⲁя я ⲧⲃⲟю ⲙⲁⲧь ⲱⲁⲗⲁⲃⲩ ⳡυⲥⲧⲟ ⳡⲗⲉⲏⲟⲙ ⳝⲩⲇⲩ ⲕⲣⲩⲧυⲧь υ ⲉⲉ ⲡυⳅⲇⲉⲏⲕⲩ ⲏⲁ ⲃⲉⲏⲧυⲗяⲧⲟⲣ ⲏⲁⲥⲁⲯⲩ ⳝⲩⲇⲉⲧ ⲱⲁⲗⲁⲃⲁ ⲃⲟⲕⲣⲩⲅ ⲥⲃⲟⲉύ ⲟⲥυ ⲕⲣⲩⲧυⲧⲥя υ ⲟⲣⲁⲧь ⲟⲧ ⳝⲟⲗυ ⲡⲟⲕⲁ ⲉⲉ ⲡυⳅⲇⲁ ⳝⲩⲇⲉⲧ ⲡⲣⲉⲃⲣⲁⳃⲁⲧьⲥя ⲃ ⲫⲁⲣⲱ ⲟⲧ ⲃυⲏⲧⲟⲃ ⲉⲧυⲭ ⲧы ⲉⳝⲁⲏⲁя ⲏⲁⲭⲩύ ⲱⲙⲁⲣⲁⲥⲟⲥⲕⲁ ⲡыⲗь ⲧы ⲉⳝⲁⲏⲁя ⲏⲉ υⲏⲁⳡⲉ я ⲥⲩⲕⲁ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲏⲁⲭⲩύ ⲧⲁⲕ ⲥⲙⲁⳡⲏⲟ ⲭⲩⲉⲙ ⳅⲁⲕⲟⲱⲙⲁⲣυⲗ ⳡⲧⲟ ⲉⲧⲟⲧ ⲃыⳝⲗяⲇⲟⲕ ⲩⲡⲁⲗ ⲃ ⲕⲁⲏⲁⲗы ⲟⲏ ⲧⲁⲙ ⲡⲗⲁⲃⲁⲗ ⲕⲁⲕ ⲕⲣⲟⲕⲟⲇυⲗ ⲉⳝⲩⳡυύ ⲧы ⳡⲟ ⲥⲩⲕⲁ ⲇⲣⲁⲏⲁя ⲁⲭⲩⲉⲗ ⲏⲁ ⲙⲟύ ⳡⲗⲉⲏ ⲗⲉⳅⲧь ⲕⲟⲧⲟⲣυύ ⲧⲃⲟⲉ ⲡⲟⲧⲏⲟⲉ ⲉⳝⲁⲗьцⲟ ⳝⲩⲇⲉⲧ ⲧⲩⲧⲁ ⲕⲣⲁⲙⲥⲁⲧь ⲏⲁⲭⲩύ ⲥыⲏ ⲧы ⲇⲉⲣⲉⲃⲉⲏⲥⲕⲟύ ⲡυⳅⲇⲟⲣⲃⲁⲏⲕυ ⲏⲁⲭⲩύ ⲧы ⲧⲩⲧ ⲏυⲕⲧⲟ ⲟⲧⲏыⲏⲉ ⲧы ⲇⲁⲯⲉ ⲏⲉ ⲇⲟⲥⲧⲟυⲏ ⲧⲩⲧ ⲃⲟ ⲃⲣⲉⲙя ⲥⲙⲉⲣⲧυ ⳝыⲧь ⲃ ⲣⲁю ⲁ ⲥⲣⲁⳅⲩ ⲃ ⲕⲁⲧⲉⲕ ⲧⲃⲟύ ⲡυⳅⲇⲁⲕ ⲏⲅⲁⲭⲩύ ⲁⲣⲩ я ⲯⲉ ⲧⲩⲧ ⲥⲃⲟυⲙ ⳝⲟⲅⲟⲡⲟⲇⲟⳝⲏυⲙ ⲭⲩⲉⲙ ⳝⲩⲇⲩ ⲣⲁⲥⲱυⲣяⲧь ⲧⲃⲟю ⲉⳝⲩⳡⲩю ⲣⲟⲧⲟⲃⲩю ⲡⲟⲗⲟⲥⲧь ⲏⲁⲭⲩύ ⲣⲁⳅⲣυⲃⲁя ⲧⲉⳝⲉ ⲃⲥю ⲧⲕⲁⲏь ⲏⲁⲭⲩύ ⲥыⲏ ⲧы ⲉⳝⲁⲏⲟύ ⲱⲗюⲭυ я ⲡⲟⲙⲉⳡⲩ ⲥⲡⲉⲣⲙⲟύ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υ ⲡⲣυⲕⲁⲯⲩ ⲁⲣⲧⲉⲗⲉⲣυю υⳅ ⲧыⲥяⳡυ ⲭⲩⲉⲙ ⲡⲣяⲙⲟ ⲃⲏⲩⲧⲣь ⲉⲉ ⲡυⳅⲇы ⲡⲟⲕⲁ ⲟⲧ ⲉⲧⲟύ ⲱⲁⲗⲁⲃы ⲏⲉ ⲟⲥⲧⲁⲏⲉⲧⲥя ⲙⲟⲕⲣⲟⲉ ⲙⲉⲥⲧⲟ ⲏⲁⲭⲩύ ⲣⲟⲅⲟⲏⲟⲥⲉц ⲉⳝⲩⳡυύ ⲧы ⲧⲃⲟύ ⳝⲁⲧя ⲕⲁⲕ ⳝыⲕ ⲉⳝⲁⲏυύ ⲧⲃⲟю ⲙⲁⲧь ⲱⲁⲗⲁⲃⲩ ⳅⲁⳝⲁⲇⲁⲗ ⲉⲉ ⲡυⳅⲇⲩ ⲇⲟ ⲕυⲱⲕⲟⲃ ⲏⲁⲭⲩύ ⲡⲣⲟⳝυⲗ ⲧⲩⲱⲩ ⲉⲉ ⲃⲥю υⲥⲕⲁⲗⲉⳡυⲗ ⲏⲁⲭⲩύ ⲡⲟⲕⲁ ⲧы ⲥыⲏⲟⳡⲉⲕ ⲡυⳅⲇⲟⲉⳝⲗυⲃⲟύ ⲱⲉⲗⲩⲭυ ⲃ ⲱⲟⲕⲉ ⲉⳝⲗⲁ ⲥⲧⲟяⲗ ⲏⲁⳝⲗюⲇⲁⲗ ⲕⲁⲕ ⲧⲃⲟя ⲏυⲕⳡⲉⲙⲏⲁя ⲙⲁⲧь ⲱⲗюⲭⲁ ⲙⲩⳡυⲧⲉⲗьⲏⲟ ⲟⲧⲡⲣⲁⲃⲗяⲉⲧⲥя ⲏⲁ ⲧⲟⲧ ⲉⳝⲩⳡυύ ⲥⲃⲉⲧ ⳡⲧⲟⳝы ⲡⲟⲧⲟⲙ ⲃ ⲁⲇⲩ ⲙⲟύ ⳡⲗⲉⲏ υⳅ ⲡⲗⲁⲙя ⲥⲏⲟⲃⲁ ⲏⲁⲥⲧυⲅⲁⲗ ⲉⲧⲩ ⲕⲩⲣⲃⲩ ⲉⳝⲁⲏⲩю ⲩⳃⲉⲙⲗⲉⲏⲥⲕⲁя ⲧы ⲃыⳝⲗяⲇь я ⲯⲉ ⲧⲃⲟю ⲙⲁⲧь ⲡⲣυⲉⳝⲁⲱυⲗ ⳡⲗⲉⲏⲟⲙ ⲕ ⲥⲧⲉⲏⲉ ⲥⲗⲟⲃⲏⲟ ⲅⲃⲟⳅⲇь ⲙⲟⲗⲟⲧⲕⲟⲙ υ ⲉⳝⲁⲱυⲗ ⲇⲟ ⲧⲁⲕⲟύ ⲥⲧⲉⲡⲉⲏυ ⲡⲟⲕⲁ ⲉⲧⲁ ⳝⲗяⲇⲟⲧⲁ ⲏⲉ ⲡⲣυⲡⲉⳡⲁⲧⲁⲗⲁⲥь ⲃ ⲅⲗⲩⳝυⲏⲉ ⲥⲧⲉⲏы я υⳅ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲱⲗюⲭυ ⳅⲇⲉⲗⲁⲗ ⲁⲭⲩⲉⲏⲩю ⲅⲣⲩⲱⲩ ⲇⲗя ⳝυⲧья ⳡⲧⲟⳝы ⲥⲃⲟύ ⳡⲗⲉⲏ ⲧⲣⲉⲏυⲣⲟⲃⲁⲧь ⲇⲗя ⲥⲗⲉⲇⲩюⳃⲉύ ⲁⲧⲁⲕυ ⲧⲃⲟⲉύ ⲟⲥⲧⲁⲃⲱυⲉⲥя ⲥⲃυⲏⲟⲥⲉⲙьυ ⲏⲁⲭⲩύ ⲡⲟⲗⲩⲡⲟⲕⲉⲣ ⲧы ⲣⲩⲥⲏяⲃυύ ⲏⲁⲭⲩύ ⲏⲩ ⲁⲗⲉ ⲥⲩⲕⲁ  ⲥыⲏ ⲡⲟⲕⲟύⲏⲟύ ⳝⲗяⲇυ ⲣⲉⲱυⲗ ⲃ ⲥⲧⲣⲁⲭⲉ ⲩⳝⲉⲯⲁⲧь ⲃ ⲥⲗⲉⳅⲁⲭ ⳅⲟⲃя ⲏⲁ ⲡⲟⲙⲟⳃ ⳡⲧⲟ ⲧⲉⳝя ⲧⲩⲧ ⲩⲏυⲯⲁюⲧ ⲙы ⳝⲟⲅⲟⲡⲟⲇⲟⳝⲏυⲉ  υⲏⲧⲉⲗⲉⲕⲧⲩⲁⲗы ⲏⲟ ⲧⲉⳝⲉ ⲭⲩύ ⲕⲧⲟ ⲡⲟⲙⲟⲯⲉⲧ ⲃⲉⲇь я ⲃⲥю ⲧⲃⲟю ⲥⲉⲙⲉύⲕⲩ ⲏⲁⲭⲩύ ⲡⲉⲣⲉⲣⲉⳅⲁⲗ ⲏⲉ ⲟⲥⲧⲁⲃυⲃ ⲧⲉⳝⲉ ⲏⲉ ⲉⲇυⲏⲟⲅⲟ ⲱⲁⲏⲥⲁ ⲥⲕⲣыⲧьⲥя ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⲱⲉⲣⲱⲉⲏь ⲡⲟⲇⳅⲁⲗⲩⲡⲏⲁя ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲙⲟⲗυⲗⲁⲥь ⲙⲟⲉⲙⲩ ⲭⲩю ⲃыⳅυⲃⲁя ⲇⲟⲯⲇь υⳅ ⲙⲟⲉύ ⲕⲟⲏⳡυ ⲕⲟⲧⲟⲣⲁя ⲡⲟⲗυⲃⲁⲗⲁ ⲉⳝⲁⲗьⲏυⲕυ ⲧⲃⲟυⲭ ⳝⲗυⳅⲕυⲭ ⲱⲁⲗⲁⲃ ⲙⲟя ⲕⲟⲏⳡⲁ ⳝыⲗⲁ ⲇⲗя ⲏυⲭ ⲕⲁⲕ ⲉⳝⲁⲏⲁя ⲕυⲥⲗⲟⲧⲁ ⲏⲁⲭⲩύ υⲭ ⲯυⲣⲟⲕ ⲙⲉⲇⲗⲉⲏⲟ ⲥⲧⲉⲕⲁⲗ ⲏⲁ ⲡⲟⲗ υ ⲧⲉⲕ ⲡⲣяⲙυⲕⲟⲙ ⲃ ⲕⲁⲏⲁⲗυⳅⲁцυю ⲏⲁⲭⲩύ ⲅⲇⲉ ⲥⲧⲣⲁⲇⲁⲗυ ⲭⲩύⲏⲉύ ⳝⲟⲙⲯυ ⲕⲟⲧⲟⲣυⲉ ⲃⲥю ⲉⲧⲩ ⲥⲙⲉⲥь υⳅ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲯυⲣⲁⲗυ ⲏⲁⲭⲩύ υⲥⲡⲉⲕⲱυύ ⲧы ⲃⲏⲁⲧⲩⲣⲉ ⲡⲟⲥыⲏⲟⳡⲉⲕ ⲅⲟⲃⲏⲟⲣыⲗⲟύ ⳝⲗяⲇь ⲱⲁⲕⲁⲗьⲏⲟύ ⳝⲗяⲇυ я ⲱⲁⲥ ⲙⲁⲧⲕⲩ ⲧⲃⲟⲉύ ⲧⲩⲡⲟύ ⲙⲁⲙⲁⲱυ ⲏⲁⳡⲏⲩ ⲥⲣⲉⳅыⲁⲃⲁⲧь ⲡⲟⲏяⲗ ⲙⲉⲏя ⲧы ⲉⳝⲁⲧь ⲩⲱυ ⲗⲩⳡⲱⲉ ⲥⲃⲟυ ⳅⲁⲕⲣⲟύ ⲃⲉⲇь ⲟⲏⲁ ⲟⲣⲁⲧь ⲏⲁⳡⲏⲉⲧ ⲅⲣⲟⲙⲕⲟ ⲉύ ⲏυⲕⲧⲟ ⲏⲁⲭⲩύ ⲧⲩⲧ ⲏⲉ ⲡⲟⲙⲟⲯⲉⲧ ⲁ ⲡⲟⲧⲟⲙ я ⲧⲉⳝя ⲥыⲏⲕⲁ ⲡⲗⲉⲥⲏⲉⲃⲟύ ⲱⲁⲗⲁⲃы ⳅⲁⲥⲧⲁⲃⲗю ⲉⲉ ⲧⲩⲧ ⲟⲥⲧⲁⲧⲕυ ⲇⲟⲯυⲣⲁⲧь ⲃⲙⲉⲥⲧⲟ ⳅ ⲙⲟⲉύ ⲥⲥⲁⲏυⲏⲟύ ⲏⲅⲁⲭⲩύ  ьы ⳡⲥⲗ ⲉⳝⲁⲧь ⲧⲩⲧ ⲃⲏⲁⲧⲩⲣⲉ ⲇⲟяⲣⲕⲁ ⲉⳝⲁⲏⲁя  я ⲧⲉⳝⲉ ⲏⲁⲭⲩύ ⲅⲟⲃⲟⲣю ⲏⲁⳡυⲏⲁύ ⲙⲏⲉ ⲥⲟⲥⲁⲧь ⲥⲩⲕⲁ ⲥⲟⲥυ ⲙⲏⲉ ⲇⲟ ⲩⲡⲟⲣⲁ ⲏⲁⲭⲩύ ⲙⲟю ⳅⲁⲕⲁⲗёⲏⲏⲩю ⲕⲣⲟⲃⲁⲃⲩю ⳅⲁⲗⲩⲡⲩ ⲟⳝⲯυⲅⲁя ⲥⲉⳝⲉ ⲣⲟⲧⲟⲃⲩю ⲡⲟⲗⲟⲥⲧь ⲏⲁⲭⲩύ υⳝⲟ ⲧы ⲧⲩⲧ ⲥⲗⲁⳝⲟⲭⲁⲣⲁⲕⲧⲉⲣⲏⲁя ⲇⲟⳡь ⲡυⳅⲇⲟⲧⲣⲉⳃυⲏы ⲅⲏυⲗⲟⲃⲁⲧⲟύ ⲏⲁ ⲥⲣυⲕⲉⲣⲁⲱⲟⲧⲉ  ⲃⲟⲟⳝⳃⲉ ⲏⲉ ⲃⲏⲩⲉⲱ ⳃⲁⲥ ⲥυⲧⲩⲁцυю ⲕⲟⲅⲇⲁ я ⲡⲟⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲏⲟⳡью ⲁⲧ ⲇⲩⲱυ ⲡⲟⲕⲁ ⲧы ⲥⲡⲁⲗⲁ ⲏⲁⲭⲩύ ⲡⲟⲥⲗⲉ ⲙυⲏⲉⲧⲁ ⲅⲟⲣⲗⲟⲃⲟⲅⲟ ⲇⲏⲉⲃⲏⲟⲅⲟ ⲙⲏⲉ ⲯⲉ ⲧы ⲉⳝⲁⲏⲁя ⲏⲁⲭⲩύ ⲇⲟⳡь ⲥⲃυⲏⲟⲅⲟ ⲟⲱⲙⲉⲧⲕⲁ ⲡⲟⲥⲗⲉ ⲟⲧьⲉⳝⲁ ⲟⲧ ⲧⲟⲗⲡы ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ я ⳝⲩⲇⲩ ⲉⲉ ⲕυⲱⲕυ ⲏⲁⲭⲩύ ⲃⲥⲉ ⲥⲟⳝυⲣⲁⲧь ⲃ ⲕⲟⲗⲉⲕцυю υ ⲃ ⲧⲁⲕⲟⲙ ⲯⲉ ⲃυⲇⲉ ⲏⲁⳡυⲏⲁⲧь ⲡⲟⲇⲯυⲅⲁⲧь ⲏⲁⲭⲩύ ⲕⲁⲕ ⲟⲅⲏⲉⲏⲁя ⲃⲉⲣⲉⲃⲕⲕⲁ ⳝⲩⲇⲉⲧ ⳅ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲱⲗюⲭυ ⲕⲟⲧⲟⲣⲟύ я ⳝⲩⲇⲩ ⲡυυⳅⲇⲉⲧь ⲧⲃⲟⲉ ⲥⲟⲥⲁⲗυⳃⲉ ⲁⲣⲩ  υⳅ ⲧⲃⲟⲉύ ⲧⲩⲡⲟύ ⳝⲗяⲇь ⲙⲁⲧⲉⲣυ ⲉⳝⲁⲏⲟύ ⳅⲁⲗⲩⲡⲟⲅⲗⲁⳅⲟύ ⲱⲗюⲭυ ⳝⲩⲇⲉⲧ ⲃⲥⲉ ⲥⲟⳝⲣⲁⲏⲟ ⲡⲟⲏяⲗ ⲙя ⲏⲁⲭⲩύ  ⲃыⲙя ⲥⲟⳝⲁⳡья ⲉⳝⲁⲧь ⲅⲏυⲗⲟⲉ ⲧы ⲧⲩ ⲏυⲕⲧⲟ ⲏⲁⲭⲩύ ⲧы ⲉⳝⲁⲏⲁя ⲱⲗюⲭⲁ ⲏⲁⲭⲩύ я ⲕυⲱⲕυ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲏⲁⲭⲩύ ⲃⲥⲡⲟⲣⲟⲗ ⲡⲟⲃⲉⲥυⲗ ⲏⲁ ⲏυⲭ ⲧⲃⲟю ⲉⳝⲁⲏⲩю υ ⲧⲁⲕ ⲉⲗⲉ ⲯυⲃⲩю ⲙⲁⲙⳅⲉⲗь ⲱⲗюⲭⲩ ⲡⲟⲥⲗⲉ ⳡⲉⲅⲟ ⲟⲁ ⲥⲣⲁⳅⲩ ⲟⲧⲕυⲏⲩⲗⲁ ⲥⲃⲟⲉ ⲉⳝⲁⲗⲟ ⲥⲃυⲏⲟⲉ ⲟⲧ ⲩⲇⲩⲱⲉⲏυя υ ⲃ ⲡⲣⲁⲭ ⲥыⲡⲁⲗⲁⲥь ⲡⲟⲥⲧⲉⲡⲉⲏⲟ υ ⲥⲃⲟю ⲡⲗⲟⲧь ⲟⳝⲗⲉⳅⲗⲩю ⲁⲭⲁⲭ ⲏⲁⲭⲩύ ⲧы ⳝⲗяⲇь  ⲱⲟ ⲧⲩⲧ ⲥыⲏяⲣⲁ ⲙⲟⲣⲇⲟⳝⲗяⲇυ ⲉⳝⲗυⲃⲟύ ⲇⲩⲙⲁⲗ я ⲧⲉⳝя ⲧⲩⲧ ⳅⲁⳝυⲗ ⳡⲧⲟⲗυ ⲕⲁⲕ ⲅⲗⲁⲃⲏⲟⲅⲟ ⲟⲧⲥⲟⲥⲏυⲕⲁ ⲉⲧⲟύ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] я ⲧⲉⳝⲉ ⳃⲁⲥ ⲥⲟⲥⲁⲗυⳃⲉ ⲧⲃⲟⲉ ⳅⲁⲣⲉⲯⲩ ⳅⲇⲉⲥь ⲧы ⲁⲭⲩⲉⲗ ⳡⲧⲟ ⲗυ ⲧⲩⲧ ⲧⲁⲕ ⳝⲁⳅⲁⲣυⲧь ⲕⲗⲟⲩⲏ ⲉⳝⲁⲏыύ ⲏυ ⲏⲁ ⳡⲧⲟ ⲏⲉ ⲥⲡⲟⲥⲟⳝⲏыύ я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲏⲩ ⲧы ⲯⲉ ⲥыⲏ ⲱⲗюⲭυ ⲉⳝⲩⳡυύ ⲃⲥⲉ ⲣⲁⲃⲏⲟ ⲧⲩⲧ ⲃⲉⳡⲏⲟ ⳝⲩⲇⲉⲱь ⲧⲉⲣⲡⲉⲧь ⲙⲟю ⳅⲁⲗⲩⲡⲩ υ ⲏυⳡⲉⲅⲟ ⳝⲟⲗⲉⲉ υⳝⲟ ⲧⲉⳝⲉ ⲣⲉⲁⲗьⲏⲟ ⲃ ⲡⲣυⲏцυⲡⲉ ⲧⲟ ⲏυⳡⲉⲅⲟ ⲏⲉ ⲥⲃⲉⲧυⲧ υⳝⲟ ⲧы ⲥыⲏⲟⳡⲉⲕ ⲱⲗюⲭυ ⲥⲗⲁⳝыύ ⲣⲉⲱυⲗ ⲙⲏⲉ ⲏⲁⲡυⲥⲁⲧь υⳅ ⳅⲁ ⲯⲁⲗⲟⲥⲧυ ⲥюⲇⲁ ⳡυⲥⲧⲟ ⲡⲟⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲭⲩύцⲁ ⲏⲩ ⲃ ⲡⲣυⲏцυⲡⲉ ⲧы ⲯⲉ ⲫⲁⲏⲁⲧ ⲙⲟυⲭ яυц ⲧы ⳡⲁⲥⲧⲉⲏьⲕⲟ ⲙⲏⲉ υⲭ ⳅⲇⲉⲥь ⲗυⲯⲉⲱь ⲡⲟⳡⲉⲙⲩ ⳝы ⲧⲉⳝⲉ ⲡⲣⲟⲥⲧⲟ ⲏⲉ ⲡⲟⲃⲧⲟⲣυⲧь ⲇⲁⲏⲏыύ ⲡⲣⲟцⲉⲥⲥ ⲉⳃⲉ ⲣⲁⳅ ⲧⲉⳝⲉ ⲇⲁⲯⲉ ⲏυⳡⲉⲅⲟ ⲏⲉ ⲙⲉⲱⲁⲉⲧ ⲟⲧⲗυⳅⲁⲧь ⲙⲟυ яύцⲁ ⳅⲇⲉⲥь ⲃⲥⲉ ⲩⲯⲉ υ ⲧⲁⲕ ⳅⲏⲁюⲧ ⲟ ⲧⲟⲙ ⳡⲧⲟ ⲧы ⲙⲟύ ⲣⲁⳝ ⲥⲁⲙыύ ⳡⲧⲟ ⲏυ ⲏⲁ ⲉⲥⲧь ⲧы ⲥⲗыⲱυⲱь ⲉⳝⲩⳡⲁя ⲧⲉⲗⲕⲁ ⲏⲁⲭⲩύ я ⲧⲉⳝⲉ ⲣⲉⲁⲗьⲏⲟ ⲧⲩⲧ ⲱⲁⲏⲥⲟⲃ ⲕⲁⲕυⲭ ⲗυⳝⲟ ⲏⲉ ⲟⲥⲧⲁⲃⲗю ⲯⲉ ⲏⲁⲭⲩύ я ⳅⲁⲗⲩⲡⲟύ ⲡⲟ ⲙⲟⲣⲇⲉ ⲧⲃⲟⲉύ ⲧⲩⲧ ⲃⲉⳡⲏⲟ ⲇⲁⲃⲁⲧь ⳝⲩⲇⲩ ⳡⲧⲟ ⲧⲉⳝⲉ ⲥⲟⳝⲥⲧⲃⲉⲏⲏⲟ υ ⲥⲃⲉⲧυⲧ ⲏⲟ ⲇⲣⲩⲅⲟⲅⲟ ⲧⲉⳝⲉ ⲏⲉ ⲇⲁⲏⲟ υⳝⲟ ⲧы ⲥыⲏⲩⲗя ⳝⲗяⲇυⲏы ⲧⲩⲡⲟⲣыⲗыύ ⲧⲩⲧ ⳝⲗяⲇⲟⲣⲉⲗьⲏыύ ⳡυⲥⲧⲟ ⲣⲟⲯⲇⲉⲏ ⲇⲗя ⲥⲟⲥⲁⲏυя ⲙⲟⲉⲅⲟ ⲭⲩя ⲕⲣⲁⲱⲉⲏⲏⲁя ⲧⲉⲗⲟⳡⲕⲁ ⲥ ⲕⲉⲙ ⲧы ⳅⲇⲉⲥь ⲣⲉⲱυⲗ ⲧяⲅⲁⲧьⲥя ⲧⲟ я ⲯⲉ ⲉⳝⲁⲗⲟ ⳃⲁⲥ ⲥⲗⲟⲙⲁю ⲧⲃⲟⲉ ⲥ ⲟⲇⲏⲟⲅⲟ ⲩⲇⲁⲣⲁ ⲥⲗⲟⲃⲏⲟ цⲁⲣь ⲧы ⲥⲗыⲱυⲱь ⲅⲏυⲇⲁⲉⳝ ⲧы ⲥⲩⳡυύ я ⳅⲇⲉⲥь ⲥ ⲧⲟⳝⲟύ ⲱⲩⲧυⲧь ⲏⲉ ⲥⲟⳝυⲣⲁюⲥь я ⲥⲣⲁⳅⲩ ⲯⲉ ⲏⲁⳡⲏⲩ ⲃыⲧⲣⲁⲭυⲃⲁⲧь ⲧⲩⲧ ⲧⲃⲟⲉ ⲕⲣυⲃⲟⲏⲟⲥⲟⲉ ⲣыⲗυⳃⲉ ⲡⲁⲩⳡυⲏⲏⲟⲉ ⲉⳝⲩⳡυύ ⲭⲩⲉⲥⲟⲥ ⲏυ ⲏⲁ ⳡⲧⲟ ⲏⲉ ⲅⲟⲇⲏыύ ⲧы ⲥⲗыⲱυⲱь ⲥⲃυⲏья ⲉⳝⲩⳡⲁя я υⳅ ⲧⲉⳝя ⲃⲥⲉ ⲕυⲱⲕυ ⲃыⲯⲙⲩ ⲯⲉ ⳅⲇⲉⲥь ⲧы ⳡυⲥⲧⲟ ⲙⲟύ ⳡⲗⲉⲏ ⲧⲉⲣⲡⲉⲧь ⳝⲩⲇⲉⲱь ⲫⲁⲏⲁⲧ ⲉⳝⲩⳡυύ ⲡⲟⲇⳅⲁⲗⲩⲡⲏыύ ⲕⲟⲧⲟⲣыύ ⲃ ⲡⲣυⲏцυⲡⲉ ⲥⲟⳝⲥⲧⲃⲉⲏⲏⲟ ⲇⲁⲯⲉ ⲏυⳡⲉⲅⲟ ⲥⲇⲉⲗⲁⲧь ⲧⲟ ⲏⲉ ⲙⲟⲯⲉⲧ ⲥ ⲧⲉⲙ ⳡⲧⲟ ⲉⲙⲩ ⲉⳝⲁⲗυⲣⲩюⲧ ⲉⲅⲟ ⲙⲁⲧⲉⲣь ⲧⲩⲡⲟⲅⲟⲗⲟⲃⲩю ⲥⲃυⲏⲥⲕⲩю ⲱⲗюⲭⲩ ⲧы ⲥⲗыⲱυⲱь ⲙⲉⲏя ⲥⲗⲁⳝⲁⲕ ⲉⳝⲩⳡυύ я ⲧⲉⳝⲉ ⳅⲇⲉⲥь ⲕⲁⲕυⲭ ⲗυⳝⲟ ⲱⲁⲏⲥⲟⲃ υⲗυ ⲡⲉⲣⲉⲇыⲱⲉⲕ ⲇⲁⲃⲁⲧь ⲏⲉ ⳝⲩⲇⲩ ⲧы ⲃⲥⲉ ⲣⲁⲃⲏⲟ ⲡⲉⲱⲕⲁⲣь ⲩⲏυⲯⲉⲏⲏыύ ⳝⲩⲇⲉⲱь ⲧⲩⲡⲟ ⲧⲉⲣⲡⲉⲧь ⲙⲟυ ⲭⲁⲣⳡⲕυ ⲃ ⲣыⲗυⳃⲉ ⲥⲃⲟⲉ ⲥⲟⳝυⲣⲁя ⲡⲣяⲙⲟ ⲏⲁ ⲥⲃⲟⲉⲙ ⲥⲟⲥⲁⲗυⳃⲉ υⲭ ⲕⲟⲗⲗⲉⲕцυю ⲧы ⲇⲁⲃⲁύ ⲧⲩⲧ ⲥⲃⲟⲉⲙⲩ ⳝⲟⲅⲟⲉⳝыⲣю ⳡⲗⲉⲏ ⲏⲁⳡυⲏⲁύ ⲡⲟⲗυⲣⲟⲃⲁⲧь ⲯⲉⲥⲧⲕⲟ ⲧⲁⲕ яⳅыⳡⲕⲟⲙ ⲥⲃⲟυⲙ ⲡⲟⲕⲁ я ⲧⲉⳝя ⳃⲉⲏⲕⲁ ⲉⳝⲩⳡⲉⲅⲟ ⲧⲩⲧ ⲡⲣυⲗюⲇⲏⲟ ⲏⲉ ⲏⲁⳡⲁⲗ ⲩⲏυⲯⲁⲧь ⲧы ⲃ ⲡⲣυⲏцυⲡⲉ ⲧⲟⲗьⲕⲟ ⲩⲏυⲯⲉⲏυύ ⲃ ⲥⲃⲟύ ⲁⲇⲣⲉⲥ υ ⲇⲟⲥⲧⲟυⲏ ⲧы ⲣⲁⳝ ⲉⳝⲁⲏыύ ⲧⲉⲣⲡυⲗυⳅυⲣⲟⲃⲁⲏⲏыύ ⳅⲁⲕⲣⲟύ ⲃⲟⲟⳝⳃⲉ ⲉⳝⲁⲗⲟ ⲥⲃⲟⲉ ⲏⲁ ⲕⲟⲅⲟ ⲧы ⲧⲩⲧ ⳝыⲕⲩⲉⲱь ⲥыⲏ ⲱⲗюⲭυ ⲉⳝⲩⳡυύ ⲥⲧⲣⲁⲱⲏыύ ⲕⲟⲧⲟⲣⲩю ⲕⲁⲯⲇыύ ⳡⲉⲗⲟⲃⲉⲕ ⲃ υⲏⲧⲉⲣⲏⲉⲧⲉ ⲉⳝⲁⲗ ⲧы ⲯⲉ ⲯυⲣⲏыύ ⲥыⲏ ⲱⲗюⲭυ ⲡⲟⲥⲙⲟⲧⲣυ ⲏⲁ ⲥⲉⳝя ⲏⲁⲭⲩύ ⲕⲟⲙⲩ ⲧы ⳡⲉ ⲥⲇⲉⲗⲁⲉⲱь ⲥⲗыⲱυⲱь ⲙⲉⲏя ⲇⲉⲥⲡⲟⲧυⳡⲏыύ ⲃыⳝⲗяⲇⲟⲕ ⲩⲏυⲯⲉⲏⲏыύ υⳅⳝυⲧыύ ⳅⲁⲭⲁⲣⲕⲁⲏⲏыύ ⲟⲗυⲅⲟⲫⲣⲉⲏⲟⲃыύ ⲡⲉⲇυⲕ ⲟⲣⲧⲟⲡⲉⲇυⳡⲏыύ я ⲙⲁⲙⲁⲱⲉⲗⲗⲩ ⲃⲉⳡⲏⲟ ⲧⲃⲟю υⳅⲣⲉⳅⲁⲧь ⳝⲩⲇⲩ ⳅⲇⲉⲥь υ ⲧы ⲥ эⲧυⲙ ⲇⲁⲯⲉ ⲏυⳡⲉⲅⲟ ⲏⲉ ⲥⲇⲉⲗⲁⲉⲱь ⲧⲩⲡⲟ ⲡⲣⲟⲥⲧⲟ ⲏⲁⲡⲣⲟⲥⲧⲟ υⳅ ⳅⲁ ⲧⲟⲅⲟ ⳡⲧⲟ я ⲥυⲗьⲏⲉⲉ ⲧⲉⳝя ⲡⲟ ⲃⲥⲉⲙ ⲡⲁⲣⲁⲙⲉⲧⲣⲁⲙ ⲃыⲡⲉⳅⲇыⲱ ⲧы ⲁⳝⲥⲧⲣⲁⲅυⲣⲟⲃⲁⲏⲏыύ ⲡⲟⳡⲉⲙⲩ ⲧы ⲩⲇⲟⲥⲩⲯυⲗⲥя ⲙⲏⲉ ⲧⲩⲧ ⲃⲟⲟⳝⳃⲉ ⳡⲧⲟ ⲧⲟ ⲥ ⲉⳝⲩⳡυⲙ ⲭⲟⲗⲟⲇⲏыⲙ ⲡⲟⲧⲟⲙ ⲟⲧ ⲥⲧⲣⲁⲭⲁ ⲏⲁ ⲗⳝⲩ ⲥⲃⲟⲉⲙ ⲧⲃⲉⲣⲇⲟⲙ ⲧы ⲉⳝⲩⳡⲁя ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲁ ⲧⲉⲗⲕⲟⲡⲟⲇⲟⳝⲏⲁя ⲙⲉⲗⲟⳡⲏⲁя ⲧⲉⲡⲉⲣь ⳅⲇⲉⲥь ⲏⲁ ⲡⲟⲥⲧⲟяⲏⲏⲟύ ⲟⲥⲏⲟⲃⲉ ⳝⲩⲇⲉⲱь ⲗⲟⲃυⲧь ⲭⲗⲉⲥⲧⲕυ ⲙⲟⲉύ ⳅⲁⲗⲩⲡы ⲃ ⲥⲃⲟⲉ ⲡⲟⲗⲩⳅⲁⲅⲏυⲃⲱⲉⲉ ⲉⳝⲁⲗυⳃⲉ ⲧы ⳡⲉ ⲥⲟⲃⲥⲉⲙ ⲟⳝⲉⳅⲩⲙⲉⲗ ⳡⲧⲟ ⲗυ ⲥыⲏ ⲱⲗюⲭυ ⲧⲩⲡⲟύ ⲭⲁⲭⲁ ⲏⲩ ⲣⲉⲁⲗьⲏⲟ ⳡυⲥⲧⲟ ⳅⲇⲉⲥь ⲃыⲉⳝⲉⲙ ⲧⲉⳝⲉ ⲙⲁⲧⲩⲱⲕⲩ ⲱⲗюⲭⲩ ⲧⲃⲟю υ ⲧы ⲥ эⲧυⲙ ⳝⲉⳅ ⲣⲟⲫⲗⲟⲃ ⲏυⳡⲉⲅⲟ ⲏⲉ ⲥⲇⲉⲗⲁⲉⲱь υⳝⲟ ⲩ ⲃⲁⲱⲉύ ⲡⲟⲣⲟⲇы ⲉⳝⲁⲏⲟύ ⲟⲥⲟⳝⲉⲏⲏⲟⲥⲧь ⲧⲁⲕⲁя ⲧⲉⲣⲡⲉⲧь ⲃⲥⲉ ⳡⲧⲟ υⲇⲉⲧ ⲃⲁⲙ ⲃⲟ ⲃⲣⲉⲇ ⲏⲩ ⲏυⳡⲉⲅⲟ ⲥыⲏⲩⲗя ⳝⲗяⲇυⲏы ⲡⲉⲣⲉⲕⲟⲱⲉⲏⲏⲟύ я ⲧⲉⳝⲉ ⲡⲟⲕⲁⲯⲩ ⳅⲇⲉⲥь ⳡⲧⲟ ⲧⲁⲕⲟⲉ ⲏⲁⲥⲧⲟяⳃυύ ⲧⲣⲟⲗⲗυⲏⲅ ⲧы ⲙυⲅⲟⲙ ⲣⲁⳅⲭⲟⳡⲉⲱь ⲃⲟⲃⲥⲉ ⲏⲁⲭⲟⲇυⲧьⲥя ⲃ ⲥⲫⲉⲣⲁⲭ ⲡⲟⲇⲟⳝⲏыⲭ ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ ⲕⲁⲕ ⲟⲧⲥⲟⲥⲉⲱь ⲙⲏⲉ ⲏⲁ ⲃⲥⲉⲟⳝⳃⲉⲙ ⲟⳝⲟⳅⲣⲉⲏυυ ⲙⲁⲏяⲧⲣⲟⲗⲗь ⲧⲩⲡⲟⲣыⲗыύ ⳅⲁⲡυⲏⲁⲏⲏыύ ⲡⲉⲥⲉⲗⲉⲡⲟⲇⲟⳝⲏыύ ⲏⲁⲭⲩύ ⲕⲟⲅⲟ ⲧы ⲧⲩⲧ ⲡыⲧⲁⲉⲱьⲥя ⲟⲥυⲗυⲧь ⲧⲟ ⲉⳝⲩⳡυύ ⲡⲉⲥ ⲭⲩⲉⲥⲟⲥⲁⲗьⲥⲕυύ я ⲧⲉⳝⲉ ⲣⲉⲁⲗьⲏⲟ ⲣыⲗυⳃⲉ ⲧⲩⲧ ⲉⳝⲁⲗ ⲧⲃⲟⲉ я ⲯⲉ ⲃⲥⲉ ⲥⲟⲕυ ⲃыⲯⲙⲩ υⳅ ⲧⲉⳝя ⳅⲇⲉⲥь ⲏⲉ ⲟⲥⲧⲁⲃⲗяя ⲇⲁⲯⲉ ⲏⲁⲙⲉⲕⲟⲃ ⲏⲁ ⲡⲟⳃⲁⲇⲩ ⲧы ⲥⲗыⲱυⲱь ⲙⲉⲏя ⲧⲉⲗⲕⲁ ⲉⳝⲩⳡⲁя ⲥыⲏ ⲱⲗюⲭυ ⲧы ⲧⲩⲧ ⳝⲩⲇⲉⲱь ⲥⲉⳝⲉ ⲯⲟⲡⲩ ⲣⲃⲁⲧь ⲇⲁⳝы ⲡыⲧⲁⲧьⲥя ⲧⲁⲙ ⲭⲟⲧь ⲕⲁⲕ ⲧⲟ ⲡⲉⲣⲉⳝυⲧь ⲙⲟυ ⲧⲉⲕⲥⲧⲁ ⲏⲟ ⲃⲥⲉ ⲇⲗя ⲧⲉⳝя ⳝⲩⲇⲉⲧ ⲧⳃⲉⲧⲏⲟ υⳝⲟ ⲧы ⲥⲗⲁⳝⲉύⲱυύ ⲥыⲏ ⲱⲗюⲭυ ⲏυⳡⲉⲅⲟ ⲏⲉ ⲩⲙⲉⲉⲱь ⲏⲟⲣⲙⲁⲗьⲏⲟ ⲧы ⲇⲁⲯⲉ ⲧⲁⲙ ⲏⲁⲭⲩύ ⲟⲧ ⲡⲟⲗⲁ 15 ⲣⲁⳅ ⲟⲧⲯυⲙⲁⲧьⲥя ⲏⲉ ⲩⲙⲉⲉⲱь ⲯⲉ ⲕⲁⲕυⲉ ⲧⲉⳝⲉ ⲧⲉⲕⲥⲧⲁ ⲃыⳝⲗяⲇⲟⲕ ⲕⲟⲥⲟⲣⲩⲕυύ я ⲧⲉⳝⲉ ⲣⲉⲁⲗьⲏⲟ ⲏⲁ ⲗⲟⳝ ⲥⲣⲁⲗ ⲧⲃⲟύ ⲧы ⳡⲉ ⲣⲉⲁⲗьⲏⲟ ⲧⲁⲙ ⲥⲧⲣⲁⲭ ⲡⲟⲧⲉⲣяⲗ ⳡⲧⲟ ⲗυ υⲗυ ⲧⲉⳝⲉ ⲥыⲏⲕⲩ ⲱⲗюⲭυ ⲯυⲧь ⲏⲁⲇⲟⲉⲗⲟ ⲟⲗⲉⲏь ⲧы ⲉⳝⲁⲏыύ я ⲧⲉⳝⲉ ⲣⲉⲁⲗьⲏⲟ ⲧⲃⲟυ ⲧⲩⲡыⲉ ⲣⲟⲅⲁ ⲡⲟⲡⲉⲣⲉⲗⲟⲙⲁю ⲧⲩⲧ ⲡⲟⲟⳡⲉⲣⲉⲇⲏⲟ ⲧы ⳝⲩⲇⲉⲱь ⳡυⲥⲧⲟ ⲥ ⲡⲉⲣⲉⲗⲟⲙⲁⲏⲏыⲙυ ⲣⲟⲅⲁⲙυ ⳝⲉⲅⲁⲧь ⲧⲩⲇⲁ ⲥюⲇⲁ ⲡⲟ υⲏⲧⲉⲣⲏⲉⲧⲩ υ ⲏⲁⳅыⲃⲁⲧь ⲧⲟⲅⲟ ⲕⲧⲟ ⲯⲉ υⲭ ⲧⲉⳝⲉ ⲥⲗⲟⲙⲁⲗ ⲏⲩ ⲧы ⲥыⲏ ⲱⲗюⲭυ ⲕⲟⲏⲉⳡⲏⲟ ⲯⲉ ⲧы ⳝⲩⲇⲉⲱь ⲉⳃⲉ ⲡⲟ ⲥⲟⲃⲙⲉⲥⲧυⲧⲉⲗьⲥⲧⲃⲩ ⲏⲁⳅыⲃⲁⲧь υⲙя ⲥⲃⲟⲉⲅⲟ ⳝⲟⲅⲟⲉⳝыⲣя ⲧы ⲧⲩⲡⲟⲣыⲗыύ ⲩⲏυⲯⲉⲏⲏыύ ⲁⲩⲧⲥⲁύⲇⲉⲣ ⲏⲟⲩⲗⲁύⲫⲉⲣ ⲕⲟⲧⲟⲣыύ ⲃыⲭⲟⲇυⲧ ⲏⲁ ⲩⲗυцⲩ ⲣⲁⳅ ⲃ ⲅⲟⲇ υ ⲧⲟ ⳡⲧⲟⳝы ⲃыⳝⲣⲟⲥυⲧь ⲙⲩⲥⲟⲣ ⲕⲟⲧⲟⲣыύ ⲉⲅⲟ ⲙⲁⲧь ⲡⲣⲟⲥυⲧ ⲱⲗюⲭⲁ ⲕⲟⲧⲟⲣⲁя ⲏⲩ ⲧы ⲡⲟⲏяⲗ ⲯⲉ ⲙⲉⲏя ⲥыⲏ ⲱⲗюⲭυ я ⲧⲉⳝя ⲕⲣⲟⲗυⲕⲁ ⲉⳝⲁⲏⲟⲅⲟ ⳝⲉⳅ ⲩⲱⲉύ ⲟⲥⲧⲁⲃⲗю ⳅⲇⲉⲥь υ ⲗⲁⲡ ⲧⲃⲟυⲭ ⲉⲥⲗυ ⲧы ⲉⳃⲉ ⲣⲁⳅ ⲧⲩⲧ ⲡⲟⲥⲙⲉⲉⲱь ⲙⲏⲉ ⳡⲉ ⲧⲟ ⲃыⲥⲣⲁⲧь [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧы ⲩⲯⲉ ⲃ ⲥⲃⲟυⲭ ⲯⲉ ⲥⲗⲟⲃⲁⲭ ⲡⲩⲧⲁⲉⲱьⲥя ⲏⲁ ⲕⲁⲯⲇⲟⲙ ⲱⲁⲅⲩ ⲏⲩⲗⲉⲃⲟύ ⲁⲭⲭⲁ, ⲟⳝъяⲥⲏυ ⲙⲏⲉ ⲕⲁⲕ ⲧⲁⲕ ⲃыⲱⲗⲟ ⳡⲧⲟ ⲧы ⲩⲯⲉ ⲃⲟⲗⲏⲩⲉⲱьⲥя ⲧⲉⳝя ⲯⲉ ⲧⲩⲧ ⲏⲉ ⲡυⳅⲇяⲧ ⲕⲁⲕ ⲅⲣⲩⲱⲩ ⳝⲟⲕⲥёⲣⲥⲕⲩю ⲭⲟⲧя ⲙⲟⲅⲗυ ⳝы эⲧⲟ υ ⲥⲇⲉⲗⲁⲧь ⲧы ⳝы ⲩⳅⲏⲁⲗ ⳡⲧⲟ ⲧⲁⲕⲟⲉ ⲥυⲗⲁ ⲩⲇⲁⲣⲁ υ ⲉⲅⲟ ⲧяⲯⲉⲥⲧь ⲏⲁ ⲥⲃⲟⲉύ ⲫυⳅυⲟⲏⲟⲙυυ, я ⲩⲃⲉⲣⲉⲏ ⲧы ⳝы ⲧⲩⲧ ⲟⲡⲁⲗ ⲏⲁ ⳅⲉⲙⲗю ⲡⲟⲥⲗⲉ ⲡⲉⲣⲃⲟⲅⲟ ⲯⲉ ⲩⲇⲁⲣⲁ ⲧⲉⳝⲉ ⲃ ⲉⳝⲁⲗⲟ ⲡⲟэⲧⲟⲙⲩ ⲡⲣⲟⲧυⲕⲁύ ⲥ эⲧⲟύ ⲕⲟⲏⲫⲉⲣⲉⲏцυυ ⲕⲁⲕ ⲃⲣⲉⲙя: υⳅ ⲡⲣⲟⲱⲗⲟⲅⲟ, ⲃ ⲏыⲏⲉⲱⲏⲉⲉ υ ⳝⲩⲇⲩⳃⲉⲉ, ⲱⲗяⲡⲏυⲕ ⲉⳝⲁⲏыύ ⲏⲁⲭⲩύ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⳅⲁⲗⲩⲡⲉⲏⲉц ⲉⳝⲁⲏⲏыύ я ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲡⲟ ⲅⲩⳝⲁⲙ ⲇⲁⲙ ⲥⲁⳝⲗⲉⳅⲩⳝыύ ⲡυⲇⲟⲣⲁⲥ)ⲧы ⲡⲣⲟⲥⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲟⲧⳝυⲧыύ)ⲩⳝυⲧыύ)ⲃ ⲙⲩⲥⲟⲣⲕⲩ ⲃыⲕυⲏⲩⲧыύ)ⲕⲁⲕ ⲡυⲇⲟⲣⲁⲥ ⲡⲟⲧⲉⲣяⲏⲏыύ цⲉⲗⲩⲉⲱь ⲙⲟю ⲙⲁⲱⲟⲏⲕⲁ υ ⲥⲗυⳅыⲃⲁⲉⲱь ⲗⲉⳡⲉⳝⲏⲩю ⲥⲙⲉⲧⲁⲏⲩ ⲥ ⲙⲟⲉⲅⲟ ⲭⲩя)я ⲯⲉ ⳝⲗяⲧь ⲧⲃⲟю ⲃⲥю ⲥⲉⲙью ⲭⲩⲉⲙ ⲇⲩⲱυⲗ ⲉⳝⲁⲏⲏⲁя ⲧы ⲥⲡυⲇⲟⳅⲏⲁя ⲙⲁⲕⲁⲕⲁ ⲕⲟⲧⲟⲣⲁя ⲏⲁ ⲙⲟύ ⳝⲁⲏⲁⲏ ⲟⲭⲟⲧⲩ ⲩⲥⲧⲣⲟυⲗⲁ)ⲧы ⲧⲁⲙ ⲏⲉ ⲃⲉⲥυ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲕⲁⲕ ⲏⲁ ⲗυⲁⲏⲉ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲡⲟⲏυⲙⲁⲉⲱь, ⲕⲟⲅⲇⲁ ⲧⲃⲟя ⲙⲁⲧь ⲃυⲇυⲧ ⲙⲟύ ⲭⲩύ, ⲟⲏⲁ ⲥⲣⲁⳅⲩ ⲯⲉ ⲏⲁⳡυⲏⲁⲉⲧ ⲥⲁⲇυⲧⲥя ⲏⲁ ⲕⲟⲗⲉⲏυ, υ ⲡⲣⲟⲕⲗⲁⲇыⲃⲁⲧь ⲕⲣⲁⲥⲏⲩю ⲇⲟⲣⲟⲯⲕⲩ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя ⲕ ⲉё ⲡυⳅⲇⲉ? Ⲁ ⲕⲁⲕ ⲧⲟⲗьⲕⲟ я ⲏⲁⳡυⲏⲁю ⲡⲟⲇⲥⲧⲁⲃⲗяⲧь ⲕ ⲏⲉύ ⲥⲃⲟύ ⲭⲩύ, ⲟⲏⲁ цⲉⲗⲩⲉⲧ ⲙⲏⲉ ⳅⲁⲗⲩⲡⲩ, υ ⲡⲣυⲅⲟⲃⲁⲣυⲃⲁⲉⲧ ⳅⲇⲣⲁⲃⲥⲧⲃⲩύ ⲟ Ⲃⲉⲗυⲕυύ ?? [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲗⲟⲯυⲧьⲥя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲟⲗⲏⲟⲥⲧью ⲥⲃⲟⲉύ ⲡυⳅⲇⲟύ, ⲧⲁⲕ ⲥⲕⲁⳅⲁⲧь ⲡⲟⲕⲣыⲃⲁⲉⲧ ⲉⲅ ⲟⲉⳝⲁⲏⲁⲏя ⲇⲩⲣⲁ, ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲟⳡⲕⲁⲥⲧⲩю ⲥⲩⲕⲁ ⲇⲩⲣⲩ, ⲧы ⲯⲉ ⲥ ⲧⲩⲡыⲙ ⲉⳝⲁⲗⲟⲙ ⲟⲧⲇⲁⲱьⲥя ⲙⲟⲉⲙⲩ ⲭⲩю ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲃыⲉⳝⲁⲏⲏⲁя, ⲧы ⲯⲉ ⲟⲃⳡⲁⲣⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲕⲟⲧⲟⲣⲁя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲁⲉⲧ, ⲃыⲉⳝⲁⲏⲏыύ ⲧы ⲥⲩⲕⲁ ⳡⲗⲉⲏⲟⲥⲟⲥ), ⲧы ⳝⲩⲇⲉⲱь ⲡⲟⲙⲟⲅⲁⲧь ⲙⲟⲉⲙⲩ ⲭⲩю ⲉⳝⲁⲧь ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲉⳝⲁⲏⲏⲟύ. ⲧы ⲯⲉ ⲕⲟⲏⳡⲉⲏⲏыύ ⲇⲁⲩⲏ ⲕⲟⲧⲟⲣⲟⲙⲩ я ⲃ ⲣⲟⲧ ⲇⲁю, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲇⲉⲅⲉⲏⲉⲣⲁⲧⲕⲁ ⲉⳝⲁⲏⲏⲁя)? [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⲟⳡⲉⲏь ⲟⳝⲣⲁⲇⲟⲃⲁⲗⲁⲥь ⲕⲟⲅⲇⲁ я ⲥⲟⲅⲗⲁⲥυⲗⲥя ⲉⲉ ⳝⲉⲇⲏяⲯⲕⲩ ⲡⲟⲕⲟⲣⲙυⲧь ⲥⲃⲟⲉύ ⲥⲡⲉⲣⲙⲟύ [ <emoji document_id=5373290243787070962>💀</emoji> ]", 
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲇⲁⲃⲁύ ⲧы ⲥⲉύⳡⲁⲥ ⲟⲧⲥⲟⲥⲉⲱь ⲙⲟύ ⲭⲩύ ⲁ ⲡⲟⲧⲟⲙ я эⲧυⲙ ⲭⲩⲉⲙ ⲃыⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь ⲱⲗюⲭⲩ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] эⲧⲟ ⲃⲥё ⲏⲁ ⳡⲧⲟ ⲧы ⲥⲡⲟⲥⲟⳝⲉⲏ ⲥыⲏ ⲱⲗюⲭυ? ⲩύⲇυ ⲏⲁⲭⲩύ ⲏⲉ ⲡⲟⳅⲟⲣь ⲥⲃⲟю ⲙⲁⲧь ⲱⲗюⲭⲩ. [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲉύⳡⲁⲥ ⲏⲁⲙⲁⲧⲁю ⲧⲃⲟύ ⲣⲟⲧ ⲏⲁ ⲥⲃⲟύ ⳡⲗⲉⲏ υ ⳅⲁⲇⲩⲱⲩ ⲧⲉⳝя ⲏⲁⲭⲩύ? [ <emoji document_id=5373290243787070962>💀</emoji> ]", 
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] Я ⲥⲟⲃⲉⲧⲩю ⲧⲉⳝⲉ ⲡⲟύⲧυ ⲏⲁⲭⲩύ ⲧⲁⲕ ⲕⲁⲕ ⲏⲁ ⳝⲟⲗьⲱⲉⲉ ⳡⲉⲙ ⲟⲧⲥⲟⲥ ⲙⲟⲉⲅⲟ ⲭⲩя ⲧы ⲏⲉ ⲥⲡⲟⲥⲟⳝⲉⲏ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲕⲟⲅⲇⲁ ⲧы ⲥⲟⲥⲉⲱь ⲙⲟύ ⲭⲩύ ⲧы ⲏⲁⲥⲗⲁⲯⲇⲁⲉⲱьⲥя ⲕⲁⲯⲇⲟύ ⲙυⲏⲩⲧⲟύ, ⲕⲁⲯⲇⲟύ ⲥⲉⲕⲩⲏⲇⲟύ ⲃⲉⲇь ⲧы ⲏⲁⲥⲧⲟⲗьⲕⲟ ⲭⲟⲣⲟⲱυύ ⲭⲩⲉⲥⲟⲥ υ ⲧⲉⳝⲉ эⲧⲟ ⲡⲣυⲏⲟⲥυⲧ ⲩⲇⲟⲃⲟⲗьⲥⲧⲃυⲉ [ <emoji document_id=5373290243787070962>💀</emoji> ]", 
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] я ⲯⲉ ⲧⲉⳝя ⲧⲩⲧ ⲃыⲉⳝⲩ ⲏⲁ ⲥⲡυⲏⲉ ⲧⲃⲟⲉύ ⲯⲉ ⲙⲁⲙы υ ⲧы ⲙⲏⲉ ⲇⲟⲕⲁⲯⲉⲱь ⲧⲩⲧ ⲧⲟⲗьⲕⲟ ⲧⲟ, ⳡⲧⲟ ⲧы ⲥⲗⲁⳝыύ ⲥыⲏ ⲱⲗюⲭυ, ⲏⲉ ⳝⲟⲗⲉⲉ. [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ эⲧⲟ ⳡⲣⲉⳅⲃыⳡⲁύⲏⲟ ⲟⲡⲁⲥⲏⲁя ⳅⲟⲏⲁ? [ <emoji document_id=5373290243787070962>💀</emoji> ]", 
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧы ⲇⲁⲃⲁύ ⲏⲉ ⲡυⳅⲇυ, ⲁ ⲭⲩύ ⲙⲟύ ⲃⲥⲁⲥυ ⲡυⳅⲇⲁⳝⲟⲗ ⲉⳝⲁⲏыύ. ⲧы ⲯⲉ ⲧⲩⲧ υ ⲥⲩⲧⲟⲕ ⲏⲉ ⲡⲣⲟⲧяⲏⲉⲱь, ⲩⳝⲉⲯυⲱь ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉ ⲡυⳅⲇⲩ ⲗυⳅⲁⲧь υ ⲭⲃⲁⲥⲧⲁⲧьⲥя ⲧⲉⲙ, ⳡⲧⲟ ⲟⲧⲥⲟⲥⲁⲗ ⲭⲩύ ⲃⲉⲗυⲕⲟⲙⲩ ⳅⲗⲟⲇⲉю. [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⲇⲁⲯⲉ ⲏⲉ ⲙⲟⲯⲉⲧ ⲁⲣⲅⲩⲙⲉⲏⲧυⲣⲟⲃⲁⲧь ⲥⲃⲟё ⲥⲟⲥⲁⲏυя эⲧⲟ ⲥⲧⲁⲗⲟ ⲉё ⲭⲟⳝⳝυ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲏⲉ ⲇⲩⲙⲁⲗ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⳅⲇⲁⲥⲧ ⲫⲁⲏ ⲕⲗⲩⳝ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя υ ⲇⲟⲕⲁⳅыⲃⲁⲧь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥⲁⲙыύ ⲗⲩⳡⲱυύ [ <emoji document_id=5373290243787070962>💀</emoji> ]", 
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] υ ⳡё ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲥⲟⲥёⲧ ⲁ ⲧы ⲏⲉⲙⲟⳃь ⲇⲁⲯⲉ ⲏⲉ ⲙⲟⲯⲉⲱь ⲉё ⳅⲁⲙⲉⲏυⲧь [ <emoji document_id=5373290243787070962>💀</emoji> ]", 
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧы ⳡё ⳝⲗяⲧь я ⳃⲁ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲡⲉⲣⲇⲁⲕ ⲭⲩяⲣю ⲁ ⲟⲏⲁ ⲡыⲧⲁⲉⲧьⲥя ⲕⲩⲇⲁ ⲧⲟ ⲩⳝⲉⲯⲁⲧь [ <emoji document_id=5373290243787070962>💀</emoji> ]", 
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲏⲉ ⲙⲟⲅⲩ ⲡⲟⲏяⲧь ⲡⲟⳡⲉⲙⲩ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲥⲧⲟⲗьⲕⲟ ⲩⲥⲉⲣⲇⲏⲟ ⲥⲟⲥёⲧ ⲙⲟύ ⲭⲩύ ⲕ ⳡⲉⲙⲩ ⲟⲏⲁ ⲥⲧⲣⲉⲙυⲧьⲥя [ <emoji document_id=5373290243787070962>💀</emoji> ]",
	"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲩⲯⲉ ⲥⳝυⲗⲥя ⲥ ⳡёⲧⲩ ⲥⲕⲟⲗьⲕⲟ я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁⲇⲟ ⲥⲡⲣⲟⲥυⲧь ⲩ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲃⲉⲇь ⲟⲏ ⲇⲣⲟⳡυⲗ ⲏⲁ эⲧⲟ [ <emoji document_id=5373290243787070962>💀</emoji> ]", 
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧⲃⲟύ ⲟⲧⲉц ⲇⲁⲃⲏⲟ ⲩⲯⲉ ⲩⲭⲟⲇυ ⲥ ⲕⲃⲁⲣⲧυⲣы υ ⲯⲇёⲧ ⲡⲟⲕⲁ я ⲡⲟⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь ⲁ ⲡⲟⲧⲟⲙ ⲡⲣυⲭⲟⲇυⲧ ⲕⲁⲕ ⲏⲉ ⲃ ⳡёⲙ ⲏⲉ ⳝыⲃⲁⲗ ⲟⲗⲩⲭ ⲧы ⲉⳝⲁⲏыύ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲡⲟⲕⲁ эⲧⲟ ⲏⲉ ⲥⲧⲁⲗⲟ ⲙⲉύⲏⲥⲧⲣυⲙⲟⲙ ⲣυⲗυ [ <emoji document_id=5373290243787070962>💀</emoji> ]", 
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⳃⲁⲥ ⲧⲃⲟя ⲙⲁⲧь ⲕⲩⲇⲁ ⲧⲟ ⲡⲟⳝⲉⲯⲁⲗⲁ υ ⲇⲩⲙⲁⲉⲧ ⳡⲧⲟ ⲉύ эⲧⲟ ⲡⲟⲙⲟⲯⲉⲧ ⲏⲟ ⲃⲉⲇь ⲙⲟύ ⲭⲩύ ⲉё ⲃⲥⲉ ⲣⲁⲃⲏⲟ ⲇⲟⲅⲟⲏυⲧ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧⲃⲟύ ⲇⲉⲇ ⲃ 45 ⲙⲏⲉ ⲭⲩύ ⳅⲁ ⲕⲩⲥⲟⲕ ⲥⲁⲗⲟ ⲥⲁⲥⲁⲗ ⲣυⲗυ ⲏⲉⲙⲟⳃь ⲟⲏ ⲉⳝⲁⲏыύ ⲇⲁ [ <emoji document_id=5373290243787070962>💀</emoji> ]", 
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] υ ⳡё ⳝⲩⲇⲩ ⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь ⲇⲟ ⲧⲁⲗⲟⲃⲁ υ ⲧы ⲏⲉ ⲥⲙⲟⲯⲉⲱь ⲙⲏⲉ ⲏⲉ ⳡⲉⲅⲟ ⲥⲕⲁⳅⲁⲧь ⲃⲉⲇь ⲥⲁⲙ ⲃ ⲧⲁύⲏⲉ ⲙⲏⲉ ⲥⲟⲥёⲱь [ <emoji document_id=5373290243787070962>💀</emoji> ]", 
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲇⲁⲃⲏⲟ ⲏⲁⳡⲁⲗⲁ ⲡⲣⲟяⲃⲗяⲧь ⲩⲃⲁⲯⲉⲏυя ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю υ ⳅⲇⲁⲣⲟⲃⲁⲉⲧьⲥя ⲥ ⲏυⲙ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲏⲉ ⲧы ⳡё ⲇⲩⲙⲁⲗ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲇⲟⲗⲅⲟ ⲥⲙⲟⲯⲉⲧ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲣыⲡⲁⲉⲧьⲥя я ⲉύ ⳅⲁ эⲧⲟ ⲭⲩёⲙ ⲡⲟ ⲅⲟⲣⳝⲩ ⲏⲁⲃⲉⲣⲏⲩ [ <emoji document_id=5373290243787070962>💀</emoji> ]", 
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲃ ⲏⲁⲥⲗⲉⲇⲥⲧⲃⲟ ⳅⲁⲃⲉⳃⲁⲗⲁ ⲧⲃⲟύ ⲣⲟⲧ ⲉⲥⲗυ ⳝⲩⲇⲉⲱь эⲧⲟ ⲟⲧⲣυцⲁⲧь я ⲉё ⲭⲩёⲙ υⳅ ⲅⲣⲟⳝⲁ ⲇⲟⲥⲧⲁⲏⲩ ⳡⲧⲟⳝы ⲟⲏⲁ ⲡⲟⲇⲧⲃⲉⲣⲇυⲗⲁ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲏⲩ ⳡё ⲡⲣυⲥⲧⲩⲡυⲙ ⲣⲁⲥⳡⲉⲭⲗяⲧь ⲧⲃⲟю ⲙⲁⲧь υⲗυ ⲧы ⲇⲁⲯⲉ ⲡⲟⳝⲟυⲱьⲥя ⲣыⲡⲏⲩⲧьⲥя ⲏⲁ ⲙⲉⲏя [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⲏⲉ ⲣⲁⳅ ⲡⲁⲇⲁⲗⲁ ⲏⲁ ⲙⲟёⲙ ⲭⲩю ⲏⲟ ⲟⲏⲁ ⲥⲧⲣⲉⲙυⲗⲟⲥь ⲕ ⲃⲉⲣⲱυⲏⲉ ⲇⲩⲣⲁ ⲉⳝⲁⲏⲁя [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲣⲁⲕⲩⲱⲕⲁ ⲏⲁⲭⲩύ ⲧы ⲡⲣяⳡⲉⲱьⲥя ⲥⲃⲟю ⲙⲁⲧь ⲟⲧ ⲭⲩя ⲙⲟⲉⲅⲟ ⲩ ⲏⲉё ⲏⲁ ⲡυⳅⲇⲉ ⲅⲉⲟⲗⲟⲕⲁⲧⲟⲣ [ <emoji document_id=5373290243787070962>💀</emoji> ]", 
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⲗⲉⲅⲗⲁ ⲡⲟⲇ ⲙⲟύ ⲭⲩύ υ ⲃⲣёⲧ ⳡⲧⲟ ⲏⲉ ⲙⲟⲯⲉⲧ ⲃыⲗⲉⳅⲧυ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲏⲉ ⲭⲟⳡⲩ ⲧⲉⳝя ⲟⲥⲕⲟⲣⳝυⲧь ⲏⲟ ⲧⲃⲟя ⲙⲁⲧь ⲟⲧⲥⲁⲥыⲃⲁⲗⲁ ⲙⲏⲉ ⲡⲟ 100 ⲣⲁⳅ ⲏⲁ ⲇⲏю ⲏⲟ ⲇⲗя ⲏⲉё эⲧⲟ ⲏⲉ ⲣⲉⲕⲟⲣⲇ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲏⲁ ⲥⲟⳝⲣⲁⲏυⲉ ⲧⲃⲟю ⲙⲁⲧь ⲡⲟⲉⳝⲁⲗ ⲃⲥⲉ ⲇⲩⲙⲁⲗυ ⳡⲧⲟ ⲟⲏⲁ ⲡⲣυⲱⲗⲁ ⲣⲁⳅⳝυⲣⲁⲧьⲥя ⲏⲟ ⲟⲏⲁ ⲃⲥⲉⲅⲟ ⲗυⲱь ⲭⲟⲧⲉⲗⲁ ⲟⲧⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲭⲩύ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] Ⲡⲟ ⲕⲁύⲫⲩ ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥⲉⲧ ⲡⲟⲕⲩⲣυⲱь ⲕⲟⲥяⲕ υ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁⳡυⲏⲁⲉⲧ ⲥⲟⲥⲁⲧь ⲏⲟ ⲧⲁⲕ ⲁⲕ ⲙы ⲇⲁⲯⲉ ⲏⲉ ⲡⲟⲏυⲙⲁⲉⲙ ⳡⲧⲟ ⲡⲣⲟυⲥⲭⲟⲇυⲧ ⲙы ⲏⲁⳡυⲏⲁⲉⲙ ⲉⲉ ⲡυⳅⲇυⲧь ⲕⲁⲕ ⲡⲟⲥⲗⲏⲉⲇⲏυю ⲱⲁⲗⲁⲃⲩ ⲏⲟ ⲇⲁⲯⲉ ⲡⲟⲥⲗⲉ эⲧⲟⲅⲟ ⲟⲏⲁ ⲏⲉ ⲡⲉⲣⲉⲥⲧⲁⲃⲁⲗⲁ ⲏⲁⲙ ⲥⲟⲥⲁⲧь. [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] Ⲥⲗыⲱь ⳝⲗяⲧь ⳡⲉⲡⲉⲭⲁ ⲧы ⲉⳝⲁⲏⲁя? Я ⲏⲁⲧⲩⲣⲉ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲧяⲏⲩⲗ ⲏⲁ ⲥⲃⲟύ ⲭⲩύ ⲕⲁⲕ ⲥⲕⲁⲫⲁⲏⲇⲣ ⳡⲧⲟⳝы ⲉⳝⲁⲧь ⲧⲉⳝя ⲃ ⲟⳡⲕⲟ υ ⲏⲉ ⲡⲟⲇⲗⲟⲯυⲧь ⳅⲁⲣⲁⳅы ⲡυⲇⲟⲣ ⲧы ⲥυⲫⲟⳅⲏыύ ⲉⳝⲁⲧь?? ⲇⲁⲃⲁύ ⲏⲁⲭⲩύ ⳅⲁⲡⲣыⲅυⲃⲁύ ⲏⲁ ⲙⲟⳝ ⳅⲁⲗⲩⲡⲩ υ ⲏⲁⳡυⲏⲁύ ⲃⲉⲣⲧⲉⲧⲥя ⲏⲁ ⲏⲉύ ⲕⲁⲕ ⲏⲉ цυⲏⲧⲣⲉⲫⲩⲅⲉ ⲉⳝⲁⲏⲟύ?? [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] Ⲧⲃⲟя ⲙⲁⲧь ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲁ ⲙⲏⲉ ⳃⲁⲥ ⳅⲁ ⲥυⲅⲁⲣⲉⲧⲩ ⲟⲧⲇⲁⲗⲁⲥь υⳅ ⳅⲁ ⳡⲉⲅⲟ я ⲏⲁⳡⲁⲗ ⲡυⳅⲇυⲧь ⲉⲉ ⲏⲟⲅⲁⲙυ ⲥ ⲕⲉⲏⲧⲁⲙυ ⲇⲉⲱⲉⲃⲁя ⲱⲗюⲭⲁ эⲧⲁ ⳝяⲗⲇυⲏⲁ ⲇⲁⲯⲉ ⲡⲟⲥⲗⲉ υⳅⳝⲉⲏυя ⲡⲣⲉⲇⲗⲁⲅⲁⲗⲁ ⲡⲟⲥⲁⲥⲁⲧь ⲏⲟ ⲙы ⲕⲟⲣⲟⳡⲉ ⲉⲉ ⳅⲁⲡυⲏⲁⲗυ ⲏⲟ ⲥⲟⲥⲁⲗⲁ ⲟⲏⲁ ⲏⲟⲣⲙ. [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] Ⲃ ⲣⲉⲁⲗьⲏⲟύ ⲯυⳅⲏυ ⲧⲃⲟя ⲙⲁⲧь ⲏⲉ ⲧⲁⲕⲁя ⲕⲁⲕ ⲃ υⲏⲧⲉⲣⲏⲉⲧⲉ ⲧ.ⲉ ⲃ υⲏⲉⲧⲉ ⲟⲏⲁ ⲡυⲱⲉⲧ ⳡⲧⲟ υⳃⲉⲧ ⲥⲉⲣьёⳅⲏыⲉ ⲟⲧⲏⲟⲱⲉⲏυⲉ υ ⲧⲁⲕ ⲇⲁⲗⲉⲉ ⲏⲟ ⲃ ⲯυⳅⲏυ ⲃⲥё ⲥⲟⲃⲥⲉⲙ ⲡⲟ ⲇⲣⲩⲅⲟⲙⲩ ⲃⲉⲇь ⲟⲏⲁ ⲃ ⲯυⳅⲏυ ⲃⲥё ⳡⲧⲟ ⲇⲉⲗⲁⲉⲧ эⲧⲟ ⲥⲟⲥёⲧ ⲏⲁⲙ ⳅⲁ ⲥⲃⲟё ⲙⲉⲥⲧⲟ ⲡⲟⲇ ⲥⲟⲗⲏцⲉⲙ. [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] ⲧы ⲭⲩⲗυ ⲧⲟ ⲙⲟύ ⲭⲩύ υⲅⲏⲟⲣυⲱь) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲃⲥя ⲧⲃⲟя ⲥⲉⲙья ⲥⲟⲥⲉⲧ ⳝⲉⲥⲡⲗⲁⲧⲏⲟ, ⲁ ⲧы ⲡⲗⲁⲧⲏⲟ, υ ⲩ ⲙⲉⲏя ⲃ ⲅⲟⲗⲟⲃⲉ ⲡⲟⲱⲗⲁ ⲙыⲥⲗь ⳡⲧⲟ ⲧы ⲡⲣυⲉⲙⲏⲁя ⲇⲟⳡь?? [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] эύ ⳡⲉⲣⲏыύ ⲥыⲏ ⲱⲁⲗⲁⲃы ⲏⲁⳝυⲣⲁύ ⲡⲟ ⲣⲉⳃⲉ ⲥⲃⲟύ ⲟⳡⲉⲣⲉⲇⲏⲟύ ⲃыⲥⲉⲣ υⲗυ я ⲧⲉⳝⲉ ⲧⲃⲟυ ⲡⲁⲗьцы ⲟⲯυⲣⲉⲃⲱυⲉ ⲡⲟⲟⲧⳝυⲃⲁю ⲟⲧ ⲧⲃⲟυⲭ ⲕⲩⲗьⲧяⲡⲟⲕ ⲥⲗυⲧыύ ⲥыⲏυⲱⲕⲁ ⲱⲗюⲭυ ⲁⲭⲁⲭ [ <emoji document_id=5373290243787070962>💀</emoji> ]",
		"[ <emoji document_id=5373290243787070962>💀</emoji> ] я ⲣыⲗⲟ ⲧⲃⲟⲉ ⲉⳝⲁⲗ ⲧы ⲭⲩⲗυ ⳅⲇⲉⲥь ⲧⲁⲕ ⲇⲟⲗⲅⲟ ⲏⲁⲥⲧⲣⲁⳡυⲃⲁⲗⲁ ⲥⲃⲟυ ⲃⲥⲡⲟⲉⳝⲟⲧⲏыⲉ ⲧⲉⲕⲥⲧⲁ ⳡυⲥⲧⲟ ⲧⲉⳝⲉ ⳅⲇⲉⲥь ⲟⲧⲡυⲗυⲙ ⲃⲥⲉ ⲧⲃⲟυ ⲕⲟⲏⲉⳡⲏⲟⲥⲧυ υ ⲟⳝ ⲧⲃⲟю ⲥⲣⲁⲕⲩ ⲧⲩⲧ ⲃыⲧⲣⲉⲙ ⲧы ⲇⲁⲃⲁύ ⲧⲁⲙ ⲉⲗⲉ ⲕⲁⲕ ⲧⲩⲯьⲥя υ ⲟⲧⲡυⲥыⲃⲁύ ⲙⲏⲉ ⲥⲃⲟυⲙυ ⲅⲟⲃⲏⲟⲡⲁⲥⲧⲉⲏⲕⲁⲙυ я ⲧⲉⳝⲉ ⳅⲇⲉⲥь ⲕⲁⲕ ⲩⲥяⲇⲩⲥь ⲏⲁ ⲉⳝⲁⲗьⲏυⲕ ⲃⲇⲁⲃⲗυⲃⲁя ⲥⲃⲟύ ⲭⲩύ яύцⲁ υ ⲡⲁⲣⲁⲱⲩ ⲥ ⲟⳡⲕⲁ ⲟⳝⲙⲁⳅыⲃⲁя ⲧⲉⳝя ⳅⲇⲉⲥь ⲥⲙⲁⳅⲕⲟύ ⲇⲗя ⲟⲧⲥⲁⲥыⲃⲁⲏυύ ⲡⲉⲣⲉⲃыⲱυⳝⲁя ⳅⲇⲉⲥь ⲧⲃⲟυ ⳅⲩⳝы ⲟⳝⲙⲁⲧыⲃⲁя ⲧⲃⲟύ ⲡυⳅⲇⲁⲗьⲏυⲕ ⲟⳝ ⲥⲃⲟυ ⲡⲟⲗⲟⲃыⲉ ⲟⲣⲅⲁⲏы я ⲧⲉⳝя ⳅⲇⲉⲥь ⲇⲟⳡⲩ ⲱⲗюⲭυ ⲏⲁ ⲧⲟⲧ ⲥⲃⲉⲧ ⳅⲁⳝⲣⲟⲱⲩ ⲡⲟⲕⲁ ⲧы ⲧⲁⲙ ⲥⲧⲁⲣⲁⲉⲱьⲥя ⲃыⲡυⲥⲁⲧь ⲙⲏⲉ ⲭⲟⲧь ⲕⲁⲡⲗю ⲥⲃⲟυⲭ ⲙυⳅⲉⲣⲏыⲭ ⲟⳝъⲉⲙⲏыⲭ ⲧⲉⲕⲥⲧⲟⲃ ⲕυⲇⲁя ⲃ ⲧⲃⲟⲉ ⲉⳝⲁⲗⲟ ⳅⲁⲗⲡ ⲭⲁⲣⳡⲉύ υ ⲱⲕⲃⲁⲗ ⲅⲟⲃⲏυⲥⲧыⲭ ⳅⲃⲉⳅⲇⲟⲡⲩⲗь ⲧы ⲧⲁⲙ ⲣⲉⳃⲉ ⲥⲟⳝⲉⲣυⲥь ⲥ ⲥυⲗⲁⲙυ ⲇⲟⳡⲁ ⲱⲗюⲭυ ⲡⲟⲕⲁ я ⲧⲉⳝя ⳅⲇⲉⲥь ⲡⲟ ⲥⲁⲙыⲉ ⲅⲗⲁⲏⲇы ⲏⲉ ⲃⲥⲡⲟⲣⲟⲗ ⲥⲃⲟⲉύ ⳅⲁⲗⲩⲡⲟύ υ ⲏⲉ ⲟⲧⲃⲉⲥυⲗ ⲧⲃⲟύ ⲡυⳅⲇⲁⲕ ⲏⲁ ⲧⲃⲟⲉ ⲉⳝⲁⲗⲟ υⲅⲣⲁяⲥь ⲧⲃⲟυⲙ ⲧⲉⲗⲟⲙ ⲕⲁⲕ ⲣⲟⲅⲁⲧⲕⲟύ ⳝⲉⲥⲥⲙыⲥⲗⲉⲏⲏⲁя ⲏⲁⲉⳝⲁⲏⲏⲁя ⲏⲁ ⲥⲉⲕⲥ ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲁ я ⲧⲉⳝⲉ ⳅⲇⲉⲥь ⲙⲁⲙⲁⲱⲩ ⲱⲗюⲭⲩ ⲏⲁⳡυⲕⲁⲏю ⲧы ⳡⲉ ⲧⲁⲙ ⲩⲅⲟⲙⲟⲏυⲗⲁⲥь ⲇⲟⳡⲁ ⲡⲟⲗⲩⲡυⲇⲟⲣⲁⲥⲁ ⲯⲉⲣⲧⲃⲁ ⲁⳝⲟⲣⲧυⲣⲟⲃⲁⲏυя ⳡυⲥⲧⲟ ⲧⲉⳝⲉ ⳅⲇⲉⲥь ⲙⲁⲙⲁⲱⲩ ⲱⲗюⲭⲩ ⲧⲃⲟю ⲏⲁ ⲥⲉⲕⲥ ⲏⲁⲉⳝⲁⲗυ ⲧы ⲭⲩяⲗυ ⲧⲁⲕⲁя ⲙⲉⲇⲗⲉⲏⲏⲁя я ⲏⲉ ⲡⲟⲏяⲗ ⲙяⲥⲏⲟⲉ ⲇυⲧⲉ ⲱⲗюⲭυ. [ <emoji document_id=5373290243787070962>💀</emoji> ]"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(shabl4)))
            await sleep(time)
            
            
    async def rbloodcmd(self, message):
        """[ ! ] Запустить модуль: Ruda Blood [ ! ]"""
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Модуль #RudaBlood закончил кровопролитие криком. <emoji document_id=5784988418459046074>💀</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>Модуль #RudaBlood начал кровопролитие криком. <emoji document_id=5784988418459046074>💀</emoji></b>\n\n"
            )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl5 = [
        "<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⳡⲉⲣⲉⳅ ⳃⲉⲕⲟⲗⲇⲩ ⲇⲃⲉⲣυ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⳡⲉⲣⲉⳅ ⳅⲁⳝⲟⲣ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⳡⲉⲣⲉⳅ ⲇⲩⳝ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⲕⲁⲧⲁⲏⲟύ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⲕⲗюⳡёⲙ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲉⲏю ⲁⲣⲙⲁⲧⲩⲣⲟύ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⲃ ⲣⲟⲧⲁⲏ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⲃ ⲅⲏυⲗⲟύ ⲣⲟⲧ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⲥⲕⲟⲣⲡυⲟⲏⲟⲙ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⳡⲉⲣⲉⳅ ⳡⲉⲣⲇⲁⲕ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⲣⲩⲕⲁⲙυ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⲥⲃⲟυⲙ ⳡⲗⲉⲏⲟⲙ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⲃ ⲁⲏⲁⲗυⳃⲉ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ?",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ я ⲗⲟⲙⲁю ⲧⲉⳝⲉ ⲉⳝⲁⲗⲟ?",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩёⲙ ⲧⲉⳝⲉ ⳅⲩⳝы ⲃыⳝυⲗ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ я ⲧⲉⳝⲉ ⳅⲩⳝы ⲗⲟⲙⲁⲗ ⲥⲃⲟυⲙ ⳡⲗⲉⲏⲟⲙ?",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ я ⲣⲉⳅⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲧⲣⲁⲥⲥⲉ?",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲱⲗюⲭⲁ?",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, я ⲉⳝⲁⲱⲩ ⲧⲃⲟю ⲥⲉⲙью ⲥⲕⲟⲣⲡυⲟⲏⲁⲙυ?",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲃⲟ ⲥⲗⲁⲃⲩ ⲥⲕⲟⲣⲡυⲟⲏⲁⲙ ⲟⲏυ υⲇⲩⲧ ⲧⲉⳝя ⲩⳝυⲃⲁⲧь ⲥⲃⲟυⲙ яⲇⲟⲙ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲉⲥⲗυ ⳝы ⲧы ⳅⲏⲁⲗ, ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь 	ⲟⲣⲁⲗⲁ, ⲕⲟⲅⲇⲁ я ⲣⲁⳅⲣⲉⲱυⲗ ⲉύ ⲟⲧⲥⲟⲥⲁⲧь ⲙⲟύ ⳡⲗⲉⲏ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲃⲟⲟⳝⳃⲉ ⲡⲟⲏυⲙⲃⲉⲱь, ⲕⲁⲕⲟⲅⲟ ⳝыⲧь ⲕⲟⲣⲟⲗёⲙ ⲥⲕⲟⲣⲡυⲟⲏⲟⲃ, ⳡⲧⲟⳝы ⲩⲅⲣⲟⲯⲁⲧь ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲙⲉⲣⲧⲉⲗьⲏыⲙ яⲇⲟⲙ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  Я ⲧⲉⳝⲉ ⲧⲩⲧ ⳅⲩⳝы ⲡⲟⲃыⳝυⲃⲁⲗ ⲥⲃⲟυⲙ ⲭⲩёⲙ ⲱⲗюⲭⲟⲙⲁⲧⲉⲣⲏⲁя ⲇⲟⲗⳝⲁⲉⳝυⲏⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲱⲁⲗⲁⲃⲁ ⲧы ⲉⳝⲁⲏⲁя, я ⲧⲉⳝя ⲧⲩⲧ ⲗⲟⲙⲁⳝ ⲕⲁⲕ ⲧёⲗⲟⳡⲕⲩ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲥⲁⲥⲉⲱ ⲙⲏⲉ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲥⲩⳡⲕⲁ ⲏⲁ ⲕⲟⲗⲉⲏяⲭ ⲥⲧⲟυⲧ υ ⲩⲙⲟⲗяⲉⲧ ⲟ ⲙⲟёⲙ ⳡⲗⲉⲏⲉ. Ⲯⲁⲗь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲧⲁⲕⲁя ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲁ ⲉⳝⲁⲏⲁя",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧⲁⲕ ⳝы ⲃыⲉⳝⲁⲗ ⲧⲃⲟю ⲯυⲣⲏⲩю ⲙⲁⲧь ⲃ ⲉё ⲇⲉⲥⲏⲁ, ⲯⲁⲗь ⲩ ⲏⲉё ⲣⲟⲧ ⲏⲉ ⲡⲟⲙыⲧ, ⲥⲟⲃⲉⲧⲩю ⲉц ⲥⲭⲟⲇυⲧь ⲏⲁ ⲁⲃⲧⲟⲙⲟύⲕⲩ, ⲉύ ⲧⲁⲙ ⲡⲣⲟⲙⲟюⲧ ⲧⲩⲭⲗⲩю ⲡυⳅⲇёⲏⲕⲩ υ ⲉё ⲣⲟⲧ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⳡёⲧⲕⲁ ⲥⲁⲥⲉⲱ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Я ⲧⲉⳝя ⲧⲩⲧⲁ ⲉⳝⲩ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⲏⲁ ⲭⲟⲇⲩ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲏⲁ ⲭⲩёⲙ ⲙⲟёⲙ ⲡⲣыⲅⲁⲉⲱь",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲥⲁⲥⲉⲱ ⲙⲏⲉ ⲏⲁ ⲡⲣⲉⲇⲥⲧⲁⲗυ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲭⲩёⲃа ⲧя ⲡⲁёⳝыⲃⲁю ⲭⲩⲉⲙ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲙⲟυⲙ ⲭⲩⲉⲙ ⲟⳝⲟⲣⲟⲏяⲗⲥя",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲥⲉⳝⲉ ⳃⲉⲕⲩ ⲡⲟⲣⲃⲁⲗ ⲙⲟυⲙ ⲭⲩⲉⲙ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲥⲉⳝⲉ ⲅⲗⲁⲏⲇы ⲡⲟⲣⲃⲁⲗ ⲙⲟυⲙ ⳡⲗⲉⲏⲟⲙ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲥⲉⳝⲉ ⲕυⲱⲕυ ⲃыⲣⲉⳅⲁⲗ ⲙⲟυⲙ ⳡⲗⲉⲏⲟⲙ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧⲃⲟя ⲙⲁⲧь ⲣⲉⳅⲁⲗⲁ ⲥⲉⳝя, ⳡⲧⲟⳝы я ⲣⲁⳅⲣⲉⲱυⲗ ⲉύ ⲙⲏⲉ ⲥⲇⲉⲗⲁⲧь ⲅⲗⲩⳝⲟⲕυύ ⲙυⲏⲉⲧ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲥⲁⲥⲉⲱ ⲕⲁⲕ ⲧⲣⲁⲭⲏⲩⲧⲁя",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲣⲁύⲟⲏⲏⲁ ⲧя ⲉⳝⲩ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲣⲧⲟⲙ ⲥⲃⲟυⲙ ⲙⲟύ ⲭⲩύ ⲅⲗⲁⲇυⲗ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Яⳅыⲕⲟⲙ ⲙⲏⲉ ⲡⲁⲗυⲣⲩⲉⲱь ⲟⳡⲕⲟ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⳅⲁ ⲭⲩёⲙ ⲙⲟυⲙ ⲥⲡⲣяⲧⲁⲗⲥя",
		"<emoji document_id=5784988418459046074>💀</emoji>  Я ⲧⲉⳝя ⲧⲩⲧ ⲭⲩⲉⲙ ⲡυⲏⲅⲃυⲏυⲗ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲡⲉⲥⲇⲩ ⲧⲉ ⲕⲁύⲫⲟⲃⲁ ⲟⳝⲟⲥцⲁⲗ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⳝⲟⲙⲯυ ⲡⲣⲟⲥυⲗυ ⲇⲉⲏⲉⲅ, ⲏⲩ я υ ⲡⲣⲟⲇⲁⲗ ⲧⲃⲟю ⲥⲉⲙью",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ я ⲧⲃⲟю ⲥⲉⲙью ⲡⲣⲟⲉⳝⲁⲗ ⲃ ⲕⲁⳅυⲏⲟ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Я ⲧⲃⲟю ⲙⲁⲧь ⳝⲩⲇⲩ ⲉⳝⲁⲧь ⲥⲧⲟⲗьⲕⲟ, ⲥⲕⲟⲗьⲕⲗ ⲟⲏⲁ ⳅⲁⲭⲟⳡⲉⲧ. Ⲯⲁⲗь ⲟⲏⲁ ⳅⲁⲭⲟⲧⲉⲗⲁ ⳡⲩⲃⲥⲧⲃⲟⲃⲁⲧь ⲙⲟύ ⳡⲗⲉⲏ ⲃ ⲥⲃⲟёύ ⲡυⳅⲇⲉ ∞ ⲗⲉⲧ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲥⲁⲧⲁⲏυⳡⲉⲥⲕυ ⲧя ⲉⳝⲩ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲣⲁⲇυ υⲅⲣⲩⲱⲕυ ⲧⲃⲟя ⲙⲁⲙⲟⳡⲕⲁ ⲥⲧⲁⲗⲁ ⲡⲉⲣⲉⲇ ⲙⲟυⲙ ⳡⲗⲉⲏⲟⲙ ⲣⲁⲕⲟⲙ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲁⲧⲗυⳡⲏⲁ ⲧя ⲉⳝⲩ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⳡё ⲅⲟⲃⲟⲣυⲗ, ⲕⲟⲅⲇⲁ я ⲧⲉⳝя ⲉⳝⲁⲗ?",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⳡё ⲅⲟⲃⲟⲣυⲗ, ⲕⲟⲅⲇⲁ я ⲧⲉⳝⲉ ⲙⲁⲧь ⲉⳝⲁⲗ?",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲃ ⲧⲉⲗⲉ ⲧⲃⲟⲉύ ⲱⲗюⲭⲟⲙⲁⲧⲉⲣυ ⲥⲟⲥⲩ ⲩ ⲃⲥⲉⲭ ⲣⲁⳝⲟⲧⲏυⲕⲟⲃ ⳝⲁⲏⲕⲁ, ⳡⲧⲟⳝы ⳅⲁⲣⲁⳝⲟⲧⲁⲧь ⲧⲉ ⲏⲁ ⲉⲇⲩ ⳝⲟⲙⲯ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲃ ⲧⲉⲗⲉ ⲧⲃⲟⲉύ ⲱⲗюⲭⲟⲙⲁⲧⲉⲣυ ⲥⲟⲥⲁⲗ ⲩ ⳝⲟⲙⲯⲉύ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲏⲁⲥⲣⲁⲗ ⲏⲁ ⲧⲃⲟё ⲗυⳡυⲕⲟ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲕⲟⲏⳡⲁю ⲃ ⲧⲃⲟύ ⲅⲏυⲗⲟц ⲣⲟⲧ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧⲉⲣⲡυⲱь ⲏⲁⲡⲟⲣ ⲙⲟⲉύ ⲥⲡⲉⲣⲙы",
		"<emoji document_id=5784988418459046074>💀</emoji>  Я ⲥⲏёⲥ ⲅⲟⲗⲟⲃⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ, ⳡⲧⲟⳝы я ⲉё ⲟⲕⲟⲏⳡⲁⲧⲉⲗьⲏⲟ ⲃыⲉⳝⲁⲗ ⲃ ⲅⲗⲁⲏⲇы",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲇⲟ ⲏ.э я ⲧⲉⳝⲉ ⲙⲁⲧь ⲉⳝⲉⲏυⲗ ⲕⲁⲕ ⲧⲃⲟю ⲙⲉⲣⲧⲃⲩю ⳝⲁⳝⲕⲩ, ⲕⲟⲧⲟⲣⲁя ⲙⲏⲉ ⲥⲟⲥⲁⲗⲁ ⳅⲁ ⲇⲉⲏьⲅυ υ ⲡⲣⲟⲥυⲗⲁ ⲡⲟⳃⲁⲇы ⲩ ⲥⲕⲟⲣⲡυⲟⲏⲟⲃ. Ⲏⲩ ⲟⲏⲁ ⲙⲏⲉ ⲟⲧⲥⲟⲥⲁⲗⲁ ⲭⲩⲉⲃⲁ υ я ⲣⲉⲱυⲗ ⲉё υⲥⲧⲣⲉⳝυⲧь ⲥⲃⲟⲉύ ⲟⲣⲇⲟύ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲥⲧⲣⲉⲗяю ⲃ ⲧя ⲥ ⲃυⲏⲧⲟⲃⲕυ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲣⲁⲥⲧⲣⲉⲗяⲗ ⲧя, ⲡⲟⲕⲁ ⲧы ⲥⲧⲟяⲗ ⲃ ⲥⲧⲣⲁⲭⲉ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧя ⲥⲧⲣⲁⲭ ⲉⳝⲉⲏυⲧ ⲇⲩⲣⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲭⲩёⲙ ⲧя ⲡⲉⲣⲉⲥⲧⲁⲃυⲗ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲃⲉⲣⳡⲩ ⲧя ⲏⲁ ⲥⲃⲟёⲙ ⳡⲗⲉⲏⲉ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲕⲁⲕ ⲧⲟⲗьⲕⲟ ⲧⲃⲟя ⲙⲁⲧь ⲩⳅⲏⲁⲗⲁ ⲡⲣⲟ ⲙⲟύ ⳡⲗⲉⲏ, ⲟⲏⲁ ⳅⲁⲭⲟⲧⲉⲗⲁ ⲡⲟⲗⲉⲧⲁⲧь ⲏⲁ ⲏёⲙ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲇⲩⲙⲁⲗⲁ ⳡⲧⲟ ⲙⲟύ ⳡⲗⲉⲏ ⲇⲗя ⲏⲉё эⲧⲟ ⳝⲁⲧⲩⲧ, ⲏⲩ υ ⲏⲁⳡⲁⲗⲁ ⲡⲣыⲅⲁⲧь ⲏⲁ ⲏёⲙ ⲕⲁⲕ ⲕⲟⳝыⲗⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⳝⲁⲣⲭⲁⲧⲏыⲙυ ⲧяⲅⲁⲙυ ⳅⲙⲉυ ⲉⳝⲩ ⲧя",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧя ⳅⲙⲉя ⲃⲉⲣⲧⲉⲗⲁ ⲏⲁ ⲥⲃⲟёⲙ ⳡⲗⲉⲏⲉ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧⲃⲟю ⲙⲁⲧь ⲡυⲇⲁⲣⲁⲥυⲗ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧⲃⲟⲉⲅⲟ ⲱⲗюⲭⲟⲟⲧцⲁ ⲉⳝⲉⲏυⲗ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧⲃⲟύ ⲟⲧⲉц ⲣⲁⳝⲟⲧⲁⲉⲧ ⲥⲧⲣυⲡⲧυⳅⲉⲣⲟⲙ, ⳡⲧⲟⳝы ⲟⲡⲟⳅⲟⲣυⲧь ⲧя ⲣⲉⳝёⲏⲕⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲡⲟ ⲃⲉⳡⲉⲣⲁⲙ ⲙⲁⲧь ⲧⲉ ⲉⳝⲩ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲥⲗⲟⲃⲏⲟ ⲃ ⲥⲕⲁⳅⲕⲉ ⲙⲏⲉ ⲥⲁⲥⲉⲱ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⳅⲟⲙⳝυ ⲡⲣυⲱⲗυ ⲉⳝⲉⲏυⲧ ⲧⲃⲟю ⲅⲟⲗⲟⲃⲩ, ⳡⲧⲟⳝы ⲇⲁⲗьⲱⲉ ⲥⲟⲯⲣⲁⲧь ⲧⲃⲟυⲭ ⲧⲩⲡыⲭ ⲣⲟⲇυⲧⲉⲗⲉύ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲥⲕⲟⲣⲡυⲟⲏы ⲃⲡⲣыⲥⲕυⲃⲁюⲧ яⲇ ⲃ ⲧⲃⲟю ⲱⲗюⲭⲟⲙⲁⲧь",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲕⲁⲕ ⲏⲉⲕⲟⳡⲁⲏ, ⲗюⳝυⲱь ⲥⲁⲥⲁⲧь",
		"<emoji document_id=5784988418459046074>💀</emoji>  Я ⲧⲉⳝя ⲉⳝⲉⲏυⲗ ⳅυⲙⲟύ, ⳡⲧⲟⳝы ⲥⲟⲅⲣⲉⲧь ⲥⲃⲟύ ⲁⲭⲩυⲧⲉⲗьⲏыύ ⳡⲗⲉⲏ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲉ ⲭⲟⲧⲉⲗⲁ ⲕⲣυⳡⲁⲧь ⲥⲗⲁⲃⲁ Ⲩⲕⲣⲁυⲏⲉ ⳅⲁ ⲏⲁⲱυⲭ ⲭⲗⲟⲡцⲉⲃ ⳅⲁ ⲉⲧⲟ ⲙы ⲉύ ⲇⲁⲗυ ⲃ ⲣыⲗⲟ ⲡⲣυⲕⲗⲁⲇⲟⲙ ⳡⲧⲟ ⲟⲏⲁ ⲏⲁⲭⲩύ ⳅⲁⲕⲣⲟⲃⲟⲧⲟⳡυⲗⲁ ⲡⲟ ⲃⲥⲉⲙⲩ ⲡⲉⲣυⲙⲉⲧⲣⲩ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⳝⲗяⲇⲥⲕυύ ⲥыⲏ ⲏⲁⲭⲩύ ⲏυ ⲏⲁ ⳡⲧⲟ ⲏⲉ ⲥⲡⲟⲥⲟⳝⲏыύ ⲕⲣⲟⲙⲉ ⲕⲁⲕ ⲙⲟю ⳡⲗⲉⲏяⲣⲩ ⲥⲟⲥⲁⲧь ⲇⲁ υ ⲃⲥⲉ ⲏⲁⲭⲩύ ⲧы ⳃⲁⲥ ⲙⲏⲉ ⲧⲩⲧ ⲡⲟⲇ ⳅⲁⲡυⲥь ⲥⲟⲥⲉⲱ ⲅυⲇⲣⲁцυⲫⲁⲗ ⲏⲁⲭⲩύ ⳝⲗяⲇⲥⲕυύ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲥⲗыⲱ ⲕⲁⲗⲟⲡⲟⲉⲇⲁⲧⲉⲗь ⲉⳝⲩⳡυύ ⲁ ⲏⲩ ⲕⲁ ⲉⳝⲗυⳃⲉ ⲥⲃⲟⲉ ⳃёⲗⲕⲏυ ⲡⲟⲕⲁ я ⲧⲉⳝⲉ ⳃⲁⲥ ⲅⲩⳝы ⲧⲩⲧ ⲏⲉ ⲥⲟⲣⲃⲁⲗ ⲥⲃⲟυⲙ ⳡⲗⲉⲏⲟⲙ",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⳝⲗяⲇь ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃцⲉⲡυⲗⲥя ⲃ ⲅⲗⲁⳅⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ υ ⲃыⲣⲃⲁⲗ υⲭ ⲏⲁⲭⲩύ ⲡⲟⲧⲟⲙ ⲥⲙⲟⲧⲣⲉⲗ ⲕⲁⲕ ⲉⲉ ⲅⲗⲁⳅⲏыⲉ яⳝⲗⲟⲕυ ⲏⲁⳡⲁⲗυ ⳅⲁⲥыⲭⲁⲧь",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲉⳝⲉ ⲃ ⲣⲟⲧ ⲏⲁⲥⲣⲩ ⲭⲩⲉⲥⲟⲥυⳃⲉ ⲥⲗⲁⳝⲟⲏⲉⲃⲣⲟⳅⲏⲟⲉ ",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲃⲏⲁⲧⲩⲣⲉ ⲭⲩⲉⲇⲗυⲏυⲧⲉⲗьⲏⲁя ⳝⲗяⲇⲩⲱυⲏⲕⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲭⲩⲉⲙ ⲧя ⲟⲧⲡⲉⳅⲇⲉⲗ", 
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲡυⳅⲇⲁⲡёⲣⲕⲁ ⲉⳝⲁⲏⲁя я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲉⳝⲁⲗ ⲡⲟⲕⲁ ⲧы ⲙⲟυ яύцⲁ ⲭⲁⲃⲁⲗ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲭⲩύ ⲗⲟⲃυ ⲥыⲏⲟⲕ ⲱⲗюⲭυ ⲥⲧⲣⲁⲏⲏⲟⲅⲟ ⲥⲉⲙⲉύⲥⲧⲃⲁ ⲟⲗυⲅⲟⲫⲣⲉⲏⲟⲃ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲥⲁⲥⲉⲱь ⲕⲁⲕ ⲥⲧⲁⲣⲡⲉⲣ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲃ ⲣⲟⲧ ⲧⲉⳝя ⲉⳝⲁⲗ ⲙⲣⲁⳅⲟⲧⲁ ⲥⲥⲁⲏⲁя ⲧы ⲟⲧⲥⲟⲥυ ⲧⲁⲙ ⲱⲗюⲱⲉⲏьⲕⲁя ⲉⳝⲩⲏяⳡⲁя",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲙⲁⲙⲁⲏ я ⲧⲃⲟю ⲙⲁⲧь ⲡυⳅⲇⲁⲅⲟⲗⲟⲃⲁя ⲧⲃⲁⲣь",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⳝⲗя ⳝⲩⲇⲩ ⲧя ⲉⳝⲩ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⳝⲗяⲧь ⲱⲗюⲭⲁ ⲉⳝⲁⲏⲁя",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲕⲗюⲕⲃⲟⲥⲣⲁⲏυⳃⲉ ⲥⲃⲟⲉ ⳅⲁⲕⲣⲟύ ⲙⲣⲁⳅυⲏυⲏⲁ ⲉⳝⲁⲏⲁя",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲉⳝⲩ ⲧя ⲏⲁⲥυⲗьⲏⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲭⲩⲉⲙ ⲧⲉⳝя ⲁⲏⲏυⲅυⲗυⲣⲟⲃⲁⲗ ⲱⲗюⲭⲁ ⲧⲉⲣⲡυⲗυⲃⲁя ⲟⲧⲥⲟⲥυ ⲅⲣю",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⳝⲩⲕⲃⲁⲗьⲏⲁ ⲥⲁⲥⲉⲱь",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲭⲩⲉⲙ ⲧⲉⳝя ⲧⲟⲣⲙⲟⲱυⲗ ⲱⲗюⲭⲁ ⲉⳝⲩⳡⲁя",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲥⲟⲥⲏυ ⳅⲇⲉⲥь ⲭⲩⲉⲡⲗⲉⲧυⳃⲉ ⲥⲥⲁⲏⲟⲉ ⲉⳝⲁⲏⲟⲉ ⲭⲁⲭⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲁ ⲧⲁⲕ ⲧⲃⲟя ⲙⲁⲧь ⲧⲟ ⲣⲉⲁⲗьⲏⲟ ⲧⲩⲧ ⲙⲏⲉ ⲃ яύцⲁ ⲡⲣыⲅⲁⲗⲁ яⳅыⲕⲟⲙ",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲉⳝⲉ ⲏⲁ ⲕⲗыⲕ ⲇⲁⲙ ⲡυⲇⲟⲣⲁⲥ", 
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲏⲁⲭⲩύ ⲧы ⲡⲣяⳡⲉⲱьⲥя ⲥⲃⲟю ⲙⲁⲧь ⲟⲧ ⲭⲩя ⲙⲟⲉⲅⲟ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⳝыⳡⲕⲩⲉⲱ ⲙⲟύ ⲭⲩύ ⲗяⲣⲃⲁ ⲉⳝⲁⲏⲁя ⲁⲣⲩ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲥⲟⲥⲉⲱ ⲧы ⲙⲏⲉ ⲥⲟ ⲥⲗⲉⳅⲁⲙυ ⲏⲁ ⲅⲗⲁⳅⲁⲭ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧⲃⲟю ⲙⲁⲧь ⳡⲗⲉⲏⲁⲙ ⲧⲟⲣⲯⲁⲱⲩ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲥⲟⲥⲉⲱ ⲧы ⲙⲏⲉ ⲟⲧⲃⲉⲧⲥⲃⲉⲏⲏⲟ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Я ⲧⲃⲟю ⲙⲁⲧь ⲟⳝ ⲥⲃⲟύ ⲭⲩύ ⲏⲁ ⳅⲁⲗⲩⲡⲩ ⳝⲣⲟⲥυⲗ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲥⲟ ⲥⲕⲩⲕυ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲟⲧ ⲣⲁⳅⲗⲩⲕυ ⲧы ⲙⲏⲉ ⲭⲩύ ⲥⲟⲥⲁⲗ ⲯⲉ ⲁⲣⲩ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲡⲟ ⲡⲩⲧυ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲥⲟⲥⲉⲱ ⲧы ⲙⲏⲉ ⲕⲁⲕ ⲏⲩⲯⲏыύ ⲕⲟⲙⲩ ⲧⲟ ⳝⲗяⲧь ⲁⲣⲩ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲁⲗ ⲡⲣυⲧⲟⲣⲏⲁ ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⳅⲁ ⲅⲁⲣⲁⲯⲁⲙυ ⲥⲩⲕⲁ ⲇⲉцⲉⲗ ⲧы ⲉⳝⲁⲏыύ ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲭⲩύ ⲥⲟⲥυ ⲙⲏⲉ ⲡⲟⲧⲟⲙ ⲏⲟύ ⳝⲗяⲇυⲏⲁ ⲥⲩⲕⲁ ⲕⲟⲏⳡⲉⲏⲏⲁя",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲃⲏⲁⲧⲩⲣⲉ ⲧⲉ ⲅⲗⲁⳅⲉⲏⲕυ ⳡⲗⲉⲏⲁⲙ ⲃыⲧⲁⳃυⲗ ⲥⲩⲕⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧⲃⲟю ⲙⲁⲧь ⲟⳝ ⲥⲃⲟύ ⲭⲩύ ⲩⲇⲁⲣяⲗ ⲡⲣυ ⲕⲁⲯⲇⲟύ ⲃⲥⲧⲣⲉⳡⲉ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⲙⲏⲉ ⲧⲩⲧ ⲥⲟⲥυ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉ ⲉⳝⲁⲗⲟ ⲡⲉⲣⲉⲣⲉⲯⲩ ⲥыⲏⲟⲕ ⲱⲗюⲭυ ⲉⳝⲩⳡυύ ⲁ ⲏⲩ υⲇυ ⲥюⲇⲁ ⲡⲟ ⲉⳝⲁⲗⲩ ⲡⲟⲗⲩⳡⲁⲧь ⳝⲩⲇⲉⲱь ⲭⲉ-ⲭⲉ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲙⲁⲙⲁⲏю ⲧⲃⲟю ⲉⳝⲁⲗ ⲥыⲏⲟⲕ ⲱⲗюⲭυ ⲭⲉ-ⲭⲉ ⲏⲉ ⲡⲟⲃⲉⲣυⲱь ⲕⲁⲕ ⲉⳝⲁⲗ ⲇⲁⲯⲉ !",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲩⲥⲟⲥυ ⲱⲗюⲭⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⳅⲁⲥⲟⲥⲉⲱь ⲥⲃυⲏⲟⲧⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲉⳝⲁⲗ я ⲧⲃⲟю ⲙⲁⲧь ⲧⲁⲕ ⲧⲟ ⲧы ⲥыⲏⲟⲕ ⲱⲗюⲭυ ⲭⲉ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲥⲃⲟύ ⲭⲩύ ⲡⲟⲥⲁⲇυⲗ ⲃⲏⲁⲧⲩⲣⲉ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲧы ⳝⲗяⲧь ⲭⲩύ ⲥⲟⲥⲉⲱ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧⲃⲟю ⲙⲁⲧь я ⲉⳝⲁⲗ ⲯⲉ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲟⲧⲟⲥⲟⲥυ ⲧⲩⲧ ⲡⲉⲣⲉⲗⲟⲙⲟⲕ ⲉⳝⲁⲏыύ",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⳅⲇⲉⲥь ⲉⳝⲩ ⳝⲉⳅⲙⲟⲗⲃⲏⲟ ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь ⲟⲏⲁ ⲙⲟⲗⳡυⲧ υ ⲧⲉⲣⲡυⲧ ⲕⲁⲕ ⲅⲩⳝⲕⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲃⲡυⲧыⲃⲁⲉⲱь ⲙⲟю ⲥⲡⲉⲣⲙⲩ ⲕⲁⲕ ⲅⲩⳝⲕⲁ ⲉⳝⲁⲏⲁя",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲥⲟⲥⲉⲱь ⲙⲏⲉ ⲕⲁⲕ ⳝⲩⲇⲧⲟ ⲧⲉⳝⲉ эⲧⲟ ⲏⲁⲇⲟ ⲥ ⲣⲟⲯⲇⲉⲏυя",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲥⲗыⲱ ⲗⲟⲱⲁⲣⲁ ⲉⳝⲁⲏⲁя ⲏⲩ ⲧы ⲃⲥⲟⲥⲉ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲁⲣⲩ ⲕⲟⲏⳡⲉⳝⲗяⲇ ⲉⳝⲁⲏыύ ⲧы ⳡⲉ ⲃⲥⲁⲥыⲃⲁⲉⲱь",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⳅⲇⲉⲥь ⲡⲟⲇⲃⲉⲱⲩ ⳅⲁ ⲕⲣюⲕ υ ⲃыⲉⳝⲩ ⲉⲉ ⲃ ⲡⲩⳅⲟ",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⳅⲇⲉⲥь ⳝⲩⲇⲩ ⲧⲣⲁⲭⲁⲧь ⲇⲟ ⲡⲟⲧⲉⲣυ ⲡⲩⲗьⲥⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⳝⲩⲇⲩ ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲧь ⲡⲟⲕⲁ ⲃⲥⲉ ⳡⲉⲗⲟⲃⲉⳡⲉⲥⲧⲃⲟ ⲏⲉ ⲃыⲙⲣⲉⲧ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⳝⲩⲇⲩ ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲧь ⲇⲟ ⲧⲟⲅⲟ ⲙⲟⲙⲉⲏⲧⲁ ⲡⲟⲕⲁ ⲃⲣⲉⲙя ⲏⲉ ⲟⲧⲙⲁⲧⲁⲉⲧⲥя ⲇⲟ эⲣы ⲇυⲏⲟⳅⲁⲃⲣⲟⲃ",
		"<emoji document_id=5784988418459046074>💀</emoji>  Ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲡⲟⲕⲁ ⲧы ⲥⲟⲥⲁⲗ ⲙⲟυ яύцⲁ ⲧы ⲁⳝⲥⲟⲥⲟⲕ ⲉⳝⲁⲏыύ  ⳝⲗя",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲃⲟю ⲙⲁⲧь ⳅⲇⲉⲥь ⲉⳝⲩ ⲇⲁⲯⲉ ⲕⲟⲅⲇⲁ ⲃⲥⲉ ⲥⲙⲟⲧⲣяⲧ ⲟⲏⲁ ⲏⲉ ⲥⲧⲉⲥⲏяⲉⲧⲥя",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲉⳝⲉⲙ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲣⲟⲧ ⲟⲏⲁ ⲧⲩⲧ ⲏⲟⲉⲧ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲉⳝⲩ ⲧⲉⳝя ⲧⲩⲧ ⲃ ⲣⲟⲧ ⲕⲁⲕ ⲕⲟⳝыⲗⲩ ⲉⳝⲁⲏⲩю",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲉⳝⲉⲙ ⲧⲉⳝя ⲃ ⲣⲟⲧ ⲕⲁⲕ ⲉⳝⲁⲏⲟⲅⲟ ⲩⲕⲩⲣⲕⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲉⳝⲉⲙ ⲧⲉⳝя ⲃ ⲣⲟⲧ ⳝыⳡⲟⲕ ⲉⳝⲁⲏыύ", 
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲡⲉⲇυⲕ ⲇⲉⲱⲉⲃыύ ⲏⲁⲭⲩύ ⲃⲥⲟⲥⲁⲗ ⲙⲏⲉ",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲣⲟⲧ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲁ ⲥⲃⲟύ ⲭⲩύ ⲏⲁⲧяⲏⲩⲗ ⲕⲁⲕ ⲡⲣⲉⳅυⲕ υ ⲃыⲉⳝⲁⲗ ⲧⲉⳝя",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲕⲟⲅⲇⲁ ⲣⲟⲇυⲗⲥя я ⲧⲉⳝя ⲕⲁⲕ ⲡⲣⲉⳅυⲕ ⲏⲁ ⲥⲃⲟύ ⲭⲩύ ⲏⲁⲧяⲏⲩⲗ υ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲕⲟⲅⲇⲁ ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲭⲩύ ⲥⲟⲥⲁⲗⲁ ⲟⲏⲁ ⲃⲗюⳝυⲗⲁⲥь ⲃ ⲙⲟύ ⲡⲉⲏυⲥ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲙⲟύ ⲭⲩύ ⲏⲁⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲥⲉⲕⲥ ⲟⲏⲁ ⲉⲅⲟ ⲗюⳝυⲗⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲉⳝⲉⲙ ⲧⲃⲟю ⲙⲁⲧь ⲃⲟ ⲃⲥⲉⲭ ⲡⲟⳅⲁⲭ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⳝⲩⲇⲉⲱь ⲧⲁⲏцⲉⲃⲁⲧь ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲃⲁⲗьⲥ ⲏⲁ ⲃыⲡⲩⲥⲕⲏⲟⲙ ⲉⳝⲁⲏⲏы ύⲧы ⲥⲟⲥⲟⲕ?), ⲧⲉⳝⲉ ⳅⲏⲁⲕⲟⲙы ύⲙⲟύ ⲭⲩύ ⲕⲟⲧⲟⲣыύ ⲧⲣⲉⲧⲥя ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲁⲉⳝⲁⲏⲏⲟύ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲭⲩⲉⲙ ⲗⲉⲥ ⲃⲁⲗυⲗ ⲃ ⲙⲁⲅⲁⲇⲁⲏⲉ))) ⲥⲁⲙ ⲇⲩⲙⲁύ ⲕⲟⲅⲇⲁ ⲧⲃⲟя ⲙⲁⲙⲉⲏьⲕⲁ ⲙⲁⲣⲧыⲱⲕⲁ ⲉⳝⲁⲏⲁя ⲇⲟ ⲙⲟⲉⲅⲟ ⲭⲩⳡ ⲇⲟⳝⲉⲣⲉⲧⲥя я ⲉё ⲕⲁⲕ ⳝⲉⲣⲉⳅⲕⲩ ⲥⲡυⲗю ⲥⲃⲟυⲙ ⲇⲉⲧⲟⲣⲟⲇⲏыⲙ ⲟⲣⲅⲁⲏⲟⲙ)))0",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲇⲁⲃⲁύ ⲧⲃⲟё ⲟⳡⲕⲟ ⳅⲁⲕⲣⲩⲧυⲙ ⲏⲁ ⲭⲩύ? ⲕⲁⲕ ⲥⲁⲭⲁⲣⲏⲩю ⲃⲁⲧⲩ ⲏⲁ ⲡⲁⲗⲟⳡⲕⲩ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲕⲟⲅⲇⲁ ⲙⲟύ ⲭⲩύ ⲃⲭⲟⲇυⲗ ⲃ ⲯυⲣⲏⲩю ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ υ я ⲏⲉ ⲙⲟⲅⲗⲁ ⲃыⲧⲁⳃυⲧь ⲉⲅⲟ, ⲡⲣυⲱⲉⲗ ⲧⲃⲟύ ⲡⲁⲡⲁ, ⲡⲟⲧяⲏⲩⲗ ⲙⲟύ ⲭⲩύ ⲃⲙⲉⲥⲧⲉ ⲥ ⲕⲗυⲧⲟⲣⲟⲙ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲃыⲧⲁⳃυⲗυ??",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲉⳝⲉ ⲅⲟⲃⲟⲣю, ⲏⲉ ⲫⲟⲣⲥυ ⲧⲩⲧ ⲥⲃⲟύ ⲉⳝⲁⲗυⲏ, ⲁ ⲥⲡⲣяⳡ ⲉⲅⲟ ⲩ ⲙⲉⲏя ⲙⲉⲯⲇⲩ ⲏⲟⲅ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲯⲉ ⳅⲏⲁⲉⲱь, ⳡⲧⲟ ⲥⲉύⳡⲁⲥ ⲕⲁⲕ ⲕⲟⲱⲉⳡⲕⲟ ⲙⲟⲗⲟⲕⲟ ⳝⲩⲇⲉⲧ ⲥⲗυⳅыⲃⲁⲧь ⲙⲟⳡⲩ ⲥⲟ ⲥⲃⲟⲉύ ⲙⲁⲙⲕυ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲁⲕⲁя ⳝⲉⲣⲩ υ ⲟⲡⲣⲕυⲇыⲃⲁю ⲧⲃⲟύ ⲭⲁⲃⲁⲗьⲏυⲕ ⲏⲁ ⲭⲩύ) υ ⲧы ⲱⲗюⲭⲁ, ⲏⲉ ⲥⲟⲡⲣⲟⲧυⲃⲗяⲉⲱьⲥя) ⲡⲟⲏяⲗ? ⲩⲧⲕⲟⲏⲟⲥ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲯⲉ ⲥⲉύⳡⲁⲥ ⲅⲣⲟⲙυⲧь ⲧⲃⲟύ ⲉⳝⲁⲗьⲏυⲕ ⳝⲩⲇⲩ, ⲕⲁⲕ ⲇⲯⲉⲕυ ⳡⲁⲏ, ⲱⲁⲗⲁⲃⲁ ⲧы ⲉⳝⲁⲏⲏⲁя, ⲥⲟⲥυ ⲭⲩύ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲧⲁⲕⲟύ ⲙⲙⲉⲇⲗⲉⲏⲏыύ, ⳡⲧⲟ ⳝⲗяⲧь я ⲟⲡяⲧь ⲡⲟⲥⲥⲁⲧь ⲏⲁ ⲧⲃⲟю ⲙⲁⲧь ⲥⲙⲟⲅⲩ, ⲱⲗюⲭⲁ ⲧы ⲡⲟⲉⳝⲁⲏⲏⲁя, υⲇυ ⲏⲁ ⲭⲩύ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧⲃⲟύ ⲃыⲥⲉⲣ ⲧⲁⲕⲟύ ⳝⲉⳅⲡⲟⲙⲟⳃⲏыύ, ⳡⲧⲟ ⲩ ⲙⲉⲏя ⲗυцⲟ ⲟⲧ ⲥⲙⲉⲭⲁ ⲗⲟⲡⲁⲉⲧⲥя) ⲁⲧⲃυⳡⲁю) ⲇⲁⲃⲁύ ⲧы ⲗⲩⳡⲱⲉ ⲡⲟύⲇёⲱь, υ ⲟⲡⲣⲕυⲏⲉⲱь ⲥⲃⲟύ ⲉⳝⲁⲗьⲏυⲕ ⲏⲁ ⲡⲁⲇⲩⲱⲕⲩ, υ ⲟⲧⲃⲉⲣⲏёⲱьⲥя ⲉⳝⲁⲗⲟⲙ ⲕ ⲥⲧⲉⲏⲕⲉ?",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲧⲁⲕⲟⲉ ⳝⲣⲉⲃⲏⲟ, ⳡⲧⲟ я ⲧⲉⳝя ⲃ ⲕⲁⳡⲉⲥⲧⲃⲉ ⲇⲣⲟⲃ ⲃ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕυⲇⲁю, ⳡυⳝⲟ ⲧⲁⲙ ⲡⲉⳡь ⲧⲁⲕⲁя)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲁ ⲧⲉⲡⲉⲣь ⲡⲟύⲇёⲙ ⲡⲟ ⲥⲧⲩⲡⲉⲏьⲕⲁⲙ)я ⲡⲟⲇⲏυⲙⲁюⲥь ⲭⲩⲉⲙ ⲡⲟ ⲧⲃⲟυⲙ ⲕⲟⲣⲉⲏⲏыⲙ ⳅⲩⳝⲁⲙ)я ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⳝⲩⲇⲩ ⲃыⳝυⲃⲁⲧь υⲭ, ⲡυⲇⲟⲣ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲃⲟⳅьⲙυ υ ⲉⳝⲁⲏυⲥь ⲟⳝ ⲕⲗⲁⲃⲩ) ⲁ ⲧⲟ я ⳝⲩⲇⲩ ⲧⲉⳝя ⲉⳝⲁь ⳡⲧⲟ ⲩ ⲧⲉⳝя ⲡⲁⲗьцы ⲡⲟⲧⲉⲧь ⲏⲁⳡⲏⲩⲧ ⲟⲧ ⲧⲟⲅⲟ ⳡⲧⲟ ⲡυⲱⲉⲱь ⲩⲥⲉⲣⲇⲏⲟ, ⲉⳝⲁⲏⲁⲱⲕⲁ ⲧⲩⲡⲟⲣыⲗⲁя",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲇⲁ я ⲧⲁⲕ ⲧⲉⳝя ⲩⲯⲉ ⲧⲩⲧ ⲡⲉⲣⲉⲉⳝⲁⲗ, ⳡⲧⲟ ⲧы ⳝⲗяⲧь ⲩύⲧυ ⲥⲡⲁⲧь ⲇⲟⲗⲯⲉⲏ ⳅⲩⳝⲁⲙυ ⲕ ⲥⲧⲉⲏⲕⲉ, ⲭⲩⲉⲥⲟⲥ ⲟⳝⲣыⲅⲁⲏⲏыύ", 
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧⲃⲟё ⲉⳝⲁⲗⲟ ⲧⲩⲧ ⲏυ ⲕⲁ ⲏⲉ ⲁⲥⲥⲟцυυⲣⲩⲉⲧⲥя ⲥ ⲥυⲇяⳃⲉⲙυ ⲡⲉⲣⲥⲏⲁⲙυ, υⳝⲟ ⲟⳝⲟⲥⲥⲁⲏцⲉⲙ ⲧⲩⲧ ⲏⲉ ⲙⲉⲥⲧⲟ, ⳝⲉⳅ ⲩⲃⲁⲯⲉⲏυя ⲕ ⲭⲩⲉⲥⲟⲥⲁⲙ υ ⲡⲣⲟⳡⲉύ ⲭⲩύⲏυ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲥⲗыⲱь ⲥⲡυⲇⲟⳅⲏυⲕ ⲉⳝⲁⲏыύ ,ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲕυⲣⳅⲟⲃыⲉ ⲥⲁⲡⲟⲅυ ⲡⲩⲥⲧυⲗⲁ ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲧы ⲃыⲉⳝⲁⲏⲏⲁ ⲭⲩⲉⲙ ⲥⲃⲟⲉⲅⲟ ⲯⲉ ⲟⲧцⲁ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲧы ⲥⲉύⳡⲁⲥ ⲥⲟⲥⲉⲱь ⲙⲏⲉ ⳝⲉⳅ ⲥⲙⲥ υ ⲣⲉⲅυⲥⲧⲣⲁцυυ, ⲏⲟ ⲟⲇⲏⲟⲃⲣⲉⲙⲉⲏⲏⲟ ⲡⲗⲁⲧυⲱь ⲙⲏⲉ ⳅⲁ эⲧⲟ ⲇⲉⲏьⲅυ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲧы ⲧⲁ ⲱⲕⲩⲣⲁ, ⲕⲟⲧⲟⲣⲁя ⲥⲟⲥⲁⲗⲁ ⲙⲏⲉ ⳡⲉⲣⲉⳅ ⲡⲣⲉⳅⲉⲣⲃⲁⲧυⲃ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲧⲁⲕ ⲡⲟⲏяⲗ, ⳅⲁⲕⲟⲏⳡυⲗυⲥь ⲱⲁⳝⲗⲟⲏⳡυⲕυ?) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ я ⲥⲉύⳡⲁⲥ ⲃыⲉⳝⲩ ⲧⲉⳝя, ⲕⲁⲕ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь, ⲡⲟⲕⲁ ⲧы ⲥⲡⲁⲗⲁ?)0)0000)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲥⲧⲟяⲧ ⲁⲫⲧⲟⲅⲣⲁⲫы ⲅⲣⲩⲃ ⲥⲧⲣυⲧ?ⲧⲁⲙ ⳡⲉ ⲙⲟύ ⲭⲩύ ⲩⲯⲉ υⲅⲣⲁⲗⲥя ⲥ ⲇⲣⲩⳅьяⲙυ?",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⳝⲗяⲧь ⲟⲣⲩⲩⲩ!ⲇυⲕⲟ ⲟⲣⲩ!ⲧы ⲏⲁⲭⲩύ ⲥⲉⲗ ⲏⲁ ⲙⲟύ ⲭⲩύ υ ⲡыⲧⲁⲗⲥя ⲕⲁⲕ ⲧⲣⲁⲥⲫⲟⲣⲙⲉⲣ ⲧⲣⲁⲥⲫⲟⲣⲙυⲣⲟⲃⲁⲧьⲥя?ⲕⲣⲉⲧυⲏ ⲥⲩⲕⲁ)я ⲯⲉ ⲧⲃⲟⲟю ⲙⲁⲧь ⲉⳝⲁⲗ)ⲅⲣυⲫⲟⲏ ⲧы ⲥⲩⲕⲁ υⳅ ⲡⲟⲇ ⲭⲩя)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲡыⲧⲁⲗⲥь ⲡⲣыⲅⲏⲩⲧь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲥ ⲩⲗыⳝⲕⲟύ ⲏⲁ ⲗυцⲉ ⲡⲣυⳡⲉⲙ ⲥ ⲕⲣыⲗⲁ ⲥⲁⲙⲟⲗⲉⲧⲁ ?",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲡⲟⲕⲁ ⲧы ⲥⲡⲁⲗ я ⲕⲟⲏⳡⲁⲗ ⲧⲃⲟⲉⲙⲩ ⳝⲁⲧυ ⲃ ⲣⲟⲧ, ⲁ ⲧы ⲥⲕⲃⲟⳅь ⲥⲏⲁ ⳡⲧⲟ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲡⲟⲕⲁ ⲧы ⲥⲡⲁⲗ ⲧⲃⲟύ ⲟⲧцⲉц ⲃыⲗυⳅыⲃⲁⲗ ⲙⲏⲉ ⲯⲟⲡⲩ ⲡⲟⲕⲁ я ⲥⲡⲁⲗ) ⲁ ⲧы ⳡⲧⲟ ⲅⲟⲃⲟⲣυⲗ ⲥⲕⲃⲟⳅь ⲥⲏⲁ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲥ ⲕⲁⲕυⲙυ ⲥⲗⲃⲟⲁⲙυ ⲧⲉⳝⲉ ⲕⲟⲏⳡυⲗυ ⲃ ⲅⲗⲁⳅ?)",
'ⲡⲟⲕⲁ ⲧы ⲙⲉⲏя υⲅⲏⲟⲣυⲱь ⲧⲃⲟύ ⲣⲟⲧ ⲏⲁⲧяⲅυⲃⲁюⲧ ⲏⲁ ⲡυⳅⲇⲩⳝⲟⲙⲯυⲭυ',
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲃⲩ ⳝⲗяⲇь, ⲉⳝⲁⲧь ⲧы ⳝⲉⲇⲏⲁя, ⲏⲟⲥⲕⲁⲙυ ⲡυⲧⲁⲉⲱьⲥя, ⲡⲟⲧⲟⲙⲩ ⳡⲧⲟ ⲙⲁⲧь ⳝⲗяⲇⲩⲉⲧ, υ ⲇⲉⲏьⲅυ ⲥ ⲧⲣⲁⲥⲥⲩ ⲧⲣⲁⲧυⲧ ⲏⲁ ⲃⲟⲇⲕⲩ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟю ⲙⲁⲧь ⲡⲟⲥⲁⲇυⲗυ ⲏⲁ ⲟⲥⲧⲣⲟⲃ υ ⲇⲁⲗυ ⲉύ ⲧⲟⲗьⲕⲟ ⲙⲟⲉύ ⲭⲩύ υ ⲥⲕⲁⳅⲁⲗυ ⳡⲧⲟ ⳝы ⲟⲏⲁ ⲕⲁⲕ ⲙⲟⲯⲏⲟ ⳝⲟⲗьⲱⲉ ⲡⲣⲟⲇⲉⲣⲯⲁⲗⲁⲥь ⳝⲉⳅ ⲡυⳃυ υ ⲃыⲯυⲃⲁⲗⲁ ⲏⲩ ⲕⲁⲕ ⲃ ⲫυⲗьⲙⲉ ⳅⲟύⲕⲁ ⲡⲉⲣⲉⲥⲙⲉⲱⲏυцⲁ",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲗⲟⳝⲕⲟⲃⲩю ⲕⲟⲥⲧь ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲡⲣⲟⲧυⲃⲟⲡⲟⲗⲟⲯⲏⲩю ⲥⲧⲟⲣⲟⲏⲩ ⲥⲙⲉⲥⲧυⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  я ⲃⲥⲉ ⲡⲟⲏяⲗ,ⲧы ⲭⲟⳡⲉⲱь ⲥⲟⲥⲁⲧь,ⲧⲁⲕ ⳝы ⲥⲣⲁⳅⲩ υ ⲥⲕⲁⳅⲁⲗ)ⲏⲁⲭⲩύ ⲫⲟⲧⲕυ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲡⲟⲕⲁⳅыⲃⲁⲧь ⲧⲟ ⲏⲉ ⲡⲟύⲙⲩ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь υⲡⲟⲗьⳅⲩⲉⲧ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲧяⲡⲕⲩ ⲏⲁ ⲟⲅⲟⲣⲟⲇⲉ ⲕⲟⲧⲟⲣⲟύ ⲟⲏⲁ ⲟⲕⲩⳡυⲃⲁⲉⲧ ⲕⲟⲣⲧⲟⲱⲕⲩ ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⲥⲡⲟⲗьⳅⲩⲉⲧ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲥⲡⲁⲗьⲏыύ ⲙⲉⲱⲟⲕ ⲃ ⲡⲟⲭⲟⲇⲉ ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲃⲥю ⲡⲗⲉⲱ ⲡⲣⲟⲉⲗⲁ ⲕⲁⲕ ⲙⲟⲗь ⲉⳝⲁⲏⲁя ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲣⲟυⲗ ⲥⲧⲟяⲏⲕⲩ υ ⲡⲟⲧⲟⲙ ⲡⲟⲣⲕⲟⲃⲁⲗ ⲥⲃⲟύ ⲭⲩύ ⲏⲁ эⲗυⲧⲏⲟⲉ ⲙⲉⲥⲧⲟ ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲣⲟυⲗ ⲡυⲣⲁⲙυⲇⲩ ⲭυⲟⲡⲥⲁ ⲧⲁ ⲏⲉ ⲩⲥⲧⲟяⲗⲁ υ ⲟⳝⲣⲩⲱυⲗⲁⲥь ⲡⲣяⲙ ⲏⲁ ⲡⲟⲗⲟⲃⲩю ⲅⲩⳝⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υⳅ ⳅⲁ ⲡⲗⲟⲭⲟύ ⲕⲟⲏⲥⲧⲣⲩⲕцυυ υ ⲩⲕⲗⲁⲇⲕυ ?)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⳝⲗяⲧь ⲇⲟⲱυⲣⲁⲕ ⲉⳝⲁⲏыύ) я ⲧⲃⲟⲉύ ⲙⲁⲙⲉ ⳅⲁ ⳃⲉⲕⲩ ⲏⲁⲥцⲁⲗ_) ⲟⲏⲁ ⲙⲟⲉύ ⲥⲥⲁⲏυⲏⲟύ ⲡⲣⲟⲡⲁⲗⲟⲥⲕⲁⲗⲁ ⲣⲟⲧυⲕ υ ⲡⲗюⲏⲩⲗⲁ ⲧⲉⳝⲉ ⲏⲁ ⲉⳝⲁⲗⲟ)",
		"<emoji document_id=5784988418459046074>💀</emoji>  ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲃⲟю ⲙⲁⲧь ⲱυⲏⲧⲁⲯυⲣⲟⲃⲁⲗ ⲕⲁⲕ ⲃ ⲕⲣⲉⲙυⲏⲁⲗьⲏыⲭ ⲫυⲗьⲙⲁⲭ ?)"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl5))
            await sleep(0.1)
            await sleep(time)
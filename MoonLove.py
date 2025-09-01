# █ █ ▀ █▄▀ ▄▀█ █▀█ ▀    ▄▀█ ▀█▀ ▄▀█ █▀▄▀█ ▄▀█
# █▀█ █ █ █ █▀█ █▀▄ █ ▄  █▀█  █  █▀█ █ ▀ █ █▀█
#
#              © Copyright 2022
#
#          https://t.me/hikariatama
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://img.icons8.com/emoji/256/000000/waxing-crescent-moon.png
# meta developer: @hikarimods
# scope: hikka_only
# scope: hikka_min 1.1.7

from telethon.tl.types import Message

from .. import loader, utils

FRAMES = [
    "🌘🌗🌖🌕🌔🌓🌒\n🌙❤️❤️🌙❤️❤️🌙\n❤️💓💓❤️💓💓❤️\n❤️💓💓💓💓💓❤️\n🌙❤️💓💓💓❤️🌙\n🌙🌙❤️💓❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌘🌗🌖🌕🌔🌓🌒",
    "🌗🌖🌕🌔🌓🌒🌘\n🌙❤️❤️🌙❤️❤️🌙\n❤️💓💓❤️💓💓❤️\n❤️💓💓💗💓💓❤️\n🌙❤️💓💓💓❤️🌙\n🌙🌙❤️💓❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌗🌖🌕🌔🌓🌒🌘",
    "🌖🌕🌔🌓🌒🌘🌗\n🌙❤️❤️🌙❤️❤️🌙\n❤️💓💗❤️💗💓❤️\n❤️💓💗💗💗💓❤️\n🌙❤️💓💗💓❤️🌙\n🌙🌙❤️💓❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌖🌕🌔🌓🌒🌘🌗",
    "🌕🌔🌓🌒🌘🌗🌖\n🌙❤️❤️🌙❤️❤️🌙\n❤️💗💗❤️💗💗❤️\n❤️💗💗💗💗💗❤️\n🌙❤️💗💗💗❤️🌙\n🌙🌙❤️💗❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌕🌔🌓🌒🌘🌗🌖",
    "🌔🌓🌒🌘🌗🌖🌕\n🌙❤️❤️🌙❤️❤️🌙\n❤️💗💗❤️💗💗❤️\n❤️💗💗💖💗💗❤️\n🌙❤️💗💗💗❤️🌙\n🌙🌙❤️💗❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌔🌓🌒🌘🌗🌖🌕",
    "🌓🌒🌘🌗🌖🌕🌔\n🌙❤️❤️🌙❤️❤️🌙\n❤️💗💖❤️💖💗❤️\n❤️💗💖💖💖💗❤️\n🌙❤️💗💖💗❤️🌙\n🌙🌙❤️💗❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌓🌒🌘🌗🌖🌕🌔",
    "🌒🌘🌗🌖🌕🌔🌓\n🌙❤️❤️🌙❤️❤️🌙\n❤️💖💖❤️💖💖❤️\n❤️💖💖💖💖💖❤️\n🌙❤️💖💖💖❤️🌙\n🌙🌙❤️💖❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌒🌘🌗🌖🌕🌔🌓",
    "🌘🌗🌖🌕🌔🌓🌒\n🌙❤️❤️🌙❤️❤️🌙\n❤️💖💖❤️💖💖❤️\n❤️💖💖💓💖💖❤️\n🌙❤️💖💖💖❤️🌙\n🌙🌙❤️💖❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌘🌗🌖🌕🌔🌓🌒",
    "🌗🌖🌕🌔🌓🌒🌘\n🌙❤️❤️🌙❤️❤️🌙\n❤️💖💓❤️💓💖❤️\n❤️💖💓💓💓💖❤️\n🌙❤️💖💓💖❤️🌙\n🌙🌙❤️💖❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌗🌖🌕🌔🌓🌒🌘",
] * 3 + [  # It's shit, I know. But it's the easiest solution tho
    "💓",
    "💗",
    "💖",
]


@loader.tds
class MoonLoveMod(loader.Module):
    """Interesting animation with hearts and moons"""

    strings = {"name": "MoonLove"}

    async def moonlovecmd(self, message: Message):
        """[text] - Love you to the moon"""
        m = await self.animate(
            message,
            FRAMES,
            interval=0.3,
            inline=False,
        )
        await m.edit(utils.get_args_raw(message) or "❤️")

    async def moonloveicmd(self, message: Message):
        """[text] - Love you to the moon [Inline]"""
        m = await self.animate(
            message,
            FRAMES,
            interval=0.3,
            inline=True,
        )
        await m.edit(utils.get_args_raw(message) or "❤️")
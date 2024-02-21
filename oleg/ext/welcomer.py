# MIT License
#
# Copyright (c) 2023-Present Shinshi Developers Team
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from typing import Any

from hikari.channels import PermissibleGuildChannel
from hikari.guilds import Member, Guild

from oleg.framework.bot import Bot


class Welcomer:
    __cache: dict[str, dict[str, Any]] = {}

    def __init__(self, bot: Bot, guild: Guild) -> None:
        self.bot = bot
        channels: dict[str, PermissibleGuildChannel] = {
            "RU": guild.get_channel(bot.config["welcomer"]["channels"]["russian"]),
            "EN": guild.get_channel(bot.config["welcomer"]["channels"]["english"]),
        }  # TODO: Typing
        messages: dict = {
            "RU": bot.config["welcomer"]["messages"]["russian"],
            "EN": bot.config["welcomer"]["messages"]["english"],
        }
        self.__cache.update(channels=channels, messages=messages)

    @classmethod
    async def welcome(cls, bot: Bot, member: Member, language: str) -> None:
        language: str = language.upper()
        channels: dict = cls.__cache["channels"]
        messages: dict = cls.__cache["messages"]
        if channels.get(language) is None or messages.get(language) is None:
            raise ValueError(f"Language '{language}' is None")
        await channels.get(language).send(
            content=messages.get(language).format(
                emoji=bot.cache.get_emoji(bot.config["emojis"]["join"]),
                member=member.mention,
            ),
            user_mentions=True,
        )

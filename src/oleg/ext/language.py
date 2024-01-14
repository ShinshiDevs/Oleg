# MIT License
#
# Copyright (c) 2023-Present "Shinshi Developers Team"
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

from hikari.guilds import Member, Role, Guild

from oleg.framework.bot import Bot


class Language:
    __cache: dict[str, dict[str, Any]] = {}

    def __init__(self, bot: Bot, guild: Guild) -> None:
        roles: dict[str, Role] = {
            "RU": guild.get_role(bot.config["roles"]["languages"]["russian"]),
            "EN": guild.get_role(bot.config["roles"]["languages"]["english"]),
        }
        self.__cache.update(roles=roles)

    @classmethod
    async def set(cls, member: Member, language: str) -> None:
        language: str = language.upper()
        if cls.__cache["roles"].get(language) is None:
            raise ValueError(f"Language '{language}' is None")
        await member.add_role(cls.__cache["roles"][language])

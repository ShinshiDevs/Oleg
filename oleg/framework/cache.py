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
from logging import getLogger
from typing import TYPE_CHECKING, cast

from cachetools import LFUCache
from hikari.guilds import Member
from hikari.impl.cache import CacheImpl
from hikari.impl.config import CacheComponents, CacheSettings
from hikari.impl.gateway_bot import GatewayBot

if TYPE_CHECKING:
    from logging import Logger

MESSAGE_CACHE_SIZE: int = 1_000
DM_CHANNEL_CACHE_SIZE: int = 0
MEMBER_CACHE_SIZE: int = 1_000


class Cache(CacheImpl):
    def __init__(self, app: GatewayBot) -> None:
        settings = CacheSettings(
            components=(
                CacheComponents.ME
                | CacheComponents.GUILD_CHANNELS
                | CacheComponents.GUILD_THREADS
                | CacheComponents.GUILDS
                | CacheComponents.ROLES
                | CacheComponents.EMOJIS
            ),
            max_messages=MESSAGE_CACHE_SIZE,
            max_dm_channel_ids=DM_CHANNEL_CACHE_SIZE,
        )
        super().__init__(app, settings=settings)
        self.__members: LFUCache[tuple[int, int], Member | None] = LFUCache(
            MEMBER_CACHE_SIZE
        )
        self.__app: GatewayBot = cast(GatewayBot, app)
        self.__logger: Logger = getLogger("cache")

    def clear_safe(self) -> None:
        self.__members.clear()
        self.clear_messages()
        self.clear_dm_channel_ids()

    def clear(self) -> None:
        self.clear_safe()
        super().clear()

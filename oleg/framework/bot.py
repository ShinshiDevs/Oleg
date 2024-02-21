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
from concurrent.futures import ThreadPoolExecutor
from os import environ
from typing import Any

from hikari.impl.gateway_bot import GatewayBot
from hikari.intents import Intents
from orjson import dumps, loads

from oleg import __version__
from oleg.framework.cache import Cache
from oleg.utils.humanize_version import humanize_version


class Bot(GatewayBot):
    def __init__(self, executor: ThreadPoolExecutor, config: dict[str, Any]) -> None:
        self.__cache = Cache(self)
        self.__config = config
        super().__init__(
            token=environ.get("OLEG_DISCORD_TOKEN"),
            executor=executor,
            cache_settings=self.cache.settings,
            dumps=dumps,
            loads=loads,
            logs="DEBUG",
            intents=(Intents.GUILDS | Intents.GUILD_MEMBERS),
        )

    @property
    def cache(self) -> Cache:
        return self.__cache

    @property
    def _cache(self) -> Cache:
        return self.__cache

    @_cache.setter
    def _cache(self, ot) -> None:
        pass

    @property
    def config(self) -> dict[str, Any]:
        return self.__config

    @property
    def version(self) -> str:
        return humanize_version(__version__)

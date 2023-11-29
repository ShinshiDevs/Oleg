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
from typing import Sequence
from os import getenv

from dotenv.main import load_dotenv

from hikari.impl.gateway_bot import GatewayBot
from hikari.intents import Intents
from hikari.presences import Status
from hikari.impl.config import CacheSettings, CacheComponents

from crescent.client import Client
from miru.bootstrap import install

__all__: Sequence[str] = "base_bot"
load_dotenv("../.env", override=True)

if __name__ == "__main__":
    base_bot: GatewayBot = GatewayBot(
        token=getenv("OLEG_DISCORD_TOKEN"),
        intents=Intents.ALL,
        banner=None,
        auto_chunk_members=False,
        cache_settings=CacheSettings(
            components=(
                CacheComponents.ME
                | CacheComponents.GUILD_CHANNELS
                | CacheComponents.GUILD_THREADS
                | CacheComponents.GUILDS
                | CacheComponents.ROLES
            ),
            max_dm_channel_ids=0,
            max_messages=100,
        ),
    )

    install(base_bot)

    client: Client = Client(
        base_bot,
        default_guild=getenv("OLEG_MAIN_GUILD"),
    )
    client.plugins.load_folder("oleg.plugins")

    try:
        base_bot.run(
            status=Status.IDLE,
            enable_signal_handlers=True,
            shard_count=1,
            check_for_updates=True,
            propagate_interrupts=True,
        )
    except KeyboardInterrupt:
        exit(0)

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
from typing import cast

from crescent.commands.decorators import command
from crescent.context.context import Context
from crescent.plugin import Plugin

from oleg import __version__
from oleg.framework.bot import Bot

plugin = Plugin[Bot, None]()


@plugin.include
@command(description="Information about me")
async def about(context: Context) -> None:
    bot: Bot = cast(Bot, context.app)
    await context.respond(
        content="\n".join(
            [
                f"{bot.cache.get_emoji(bot.config['emojis']['logo'])} "
                "I'm Oleg, a service bot to provide the server with all the features it needs.",
                "Some stats:",
                f"- **{sum(bot.cache.get_guild(guild).member_count for guild in bot.cache.get_guilds_view())}** users",
                f"- Latency **{round(bot.heartbeat_latency * 1000, 1)}ms**",
                f"- Current version [`{bot.version}`]"
                f"(<https://github.com/ShinshiDevs/Oleg/blob/main/CHANGELOG.md#version-{__version__[0]}{__version__[1]}{__version__[2]}>)",
                "I'm an open-source project of [Shinshi Developers Team](<https://github.com/ShinshiDevs/Oleg>), "
                "licensed under MIT. I'll be glad to help you!",
            ]
        ),
    )

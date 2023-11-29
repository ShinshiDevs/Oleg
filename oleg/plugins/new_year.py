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
from datetime import datetime, timedelta

from hikari.impl.gateway_bot import GatewayBot
from hikari.channels import PermissibleGuildChannel

from crescent.plugin import Plugin
from crescent.ext.tasks import loop

from humanize.time import precisedelta
from humanize.i18n import activate, deactivate

from __main__ import base_bot
from oleg.variables import EN_NEW_YEAR_CHANNEL_ID, RU_NEW_YEAR_CHANNEL_ID

plugin: Plugin = Plugin[GatewayBot, None]()
new_year: datetime = datetime(day=1, month=1, year=(datetime.now().year + 1))
base_bot: GatewayBot = base_bot


async def update_en_channel(channel: PermissibleGuildChannel) -> None:
    humanized_timedelta: str = precisedelta(format="%0.0f", value=(new_year - datetime.now()), minimum_unit="days")
    await channel.edit(name=f"🎄 {humanized_timedelta}")


async def update_ru_channel(channel: PermissibleGuildChannel) -> None:
    activate("ru_RU")
    humanized_timedelta: str = precisedelta(format="%0.0f", value=(new_year - datetime.now()), minimum_unit="days")
    await channel.edit(name=f"🎄 {humanized_timedelta}")
    deactivate()


@plugin.include
@loop(timedelta(hours=1))
async def task() -> None:
    en_channel: PermissibleGuildChannel = await base_bot.rest.fetch_channel(EN_NEW_YEAR_CHANNEL_ID)
    ru_channel: PermissibleGuildChannel = await base_bot.rest.fetch_channel(RU_NEW_YEAR_CHANNEL_ID)
    await update_en_channel(en_channel)
    await update_ru_channel(ru_channel)

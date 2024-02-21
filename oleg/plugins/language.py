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
from crescent.commands.decorators import command
from crescent.commands.groups import Group
from crescent.context.context import Context
from crescent.events import event as event_decorator
from crescent.plugin import Plugin
from hikari.components import ButtonStyle
from hikari.events.shard_events import ShardReadyEvent
from hikari.guilds import Guild, Member
from hikari.permissions import Permissions
from miru.button import Button
from miru.events import ComponentInteractionCreateEvent
from miru.view import View

from oleg.ext.language import Language
from oleg.ext.welcomer import Welcomer
from oleg.framework.bot import Bot

plugin = Plugin[Bot, None]()
group = Group("init", default_member_permissions=Permissions.ADMINISTRATOR)


@plugin.include
@event_decorator
async def cache_load_on_shard_con(event: ShardReadyEvent) -> None:
    main_guild: Guild = await event.app.rest.fetch_guild(
        plugin.app.config["guilds"]["main"]
    )
    Language(plugin.app, main_guild)
    Welcomer(plugin.app, main_guild)


@plugin.include
@event_decorator
async def button(event: ComponentInteractionCreateEvent) -> None:
    await event.context.defer()
    member: Member = event.member
    match event.custom_id.replace("choice_", ""):
        case "ru":
            await Language.set(member, "RU")
            await Welcomer.welcome(plugin.app, member, "RU")
        case "en":
            await Language.set(member, "EN")
            await Welcomer.welcome(plugin.app, member, "EN")


@group.child
@plugin.include
@command()
async def locale(context: Context) -> None:
    await context.channel.send(
        components=(
            View()
            .add_item(
                Button(
                    label="Русский",
                    emoji="🇷🇺",
                    custom_id="choice_ru",
                    style=ButtonStyle.SECONDARY,
                )
            )
            .add_item(
                Button(
                    label="English",
                    emoji="🇬🇧",
                    custom_id="choice_en",
                    style=ButtonStyle.SECONDARY,
                )
            )
        )
    )
    await context.respond(content="✅", ephemeral=True)

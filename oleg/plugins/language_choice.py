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
from dataclasses import dataclass
from logging import Logger, getLogger
from random import choice
from typing import Final

from hikari.components import ButtonStyle
from hikari.guilds import Guild, Role, Member
from hikari.impl.gateway_bot import GatewayBot
from hikari.events.shard_events import ShardConnectedEvent
from hikari.channels import GuildTextChannel, TextableGuildChannel, PartialChannel

from crescent.plugin import Plugin
from crescent.events import event as base_event
from crescent.commands.hooks import hook
from crescent.commands.decorators import command
from crescent.context.context import Context

from miru.view import View
from miru.button import Button
from miru.events import ComponentInteractionCreateEvent

from oleg.hooks import is_owner
from oleg.variables import (
    EMOJI_POOL_GUILD_ID,
    GENERAL_GUILD_ID,
    RUSSIAN_CHANNEL_ID,
    ENGLISH_CHANNEL_ID,
    RUSSIAN_ROLE_ID,
    ENGLISH_ROLE_ID,
    JOIN_MEMBER_EMOJI_ID,
    RUSSIAN_WELCOMES,
    ENGLISH_WELCOMES,
)

_log: Logger = getLogger(__name__)
plugin: Plugin = Plugin[GatewayBot, None]()
setattr(plugin, "resources", None)


@dataclass
class Resources:
    general_guild: Guild
    join_emoji: str
    russian_chat: PartialChannel
    english_chat: PartialChannel
    russian_role: Role | None = None
    english_role: Role | None = None


@plugin.include
@base_event
async def on_connect(event: ShardConnectedEvent) -> None:
    emojis_pool_guild: Final[Guild] = await event.app.rest.fetch_guild(EMOJI_POOL_GUILD_ID)

    resources = Resources(
        general_guild=await event.app.rest.fetch_guild(GENERAL_GUILD_ID),
        join_emoji=str(
            await event.app.rest.fetch_emoji(emojis_pool_guild, JOIN_MEMBER_EMOJI_ID)
        ),
        russian_chat=await event.app.rest.fetch_channel(RUSSIAN_CHANNEL_ID),
        english_chat=await event.app.rest.fetch_channel(ENGLISH_CHANNEL_ID),
    )

    resources.russian_role = resources.general_guild.get_role(RUSSIAN_ROLE_ID)
    resources.english_role = resources.general_guild.get_role(ENGLISH_ROLE_ID)

    setattr(plugin, "resources", resources)
    _log.info("Initialized all base information")


@plugin.include
@base_event
async def on_button_click(event: ComponentInteractionCreateEvent) -> None:
    await event.context.defer()
    member: Member = event.member
    resources: Resources = getattr(plugin, "resources")
    if event.custom_id == "choice_ru":
        await event.app.rest.add_role_to_member(
            resources.general_guild, member, resources.russian_role
        )
        await resources.russian_chat.send(
            content=(
                f"{resources.join_emoji} "
                + choice(RUSSIAN_WELCOMES).format(member.mention)
            ),
            user_mentions=True,
        )
    if event.custom_id == "choice_en":
        await event.app.rest.add_role_to_member(
            resources.general_guild, member, resources.english_role
        )
        await resources.english_chat.send(
            content=(
                f"{resources.join_emoji} "
                + choice(ENGLISH_WELCOMES).format(member.mention)
            ),
            user_mentions=True,
        )


@plugin.include
@hook(is_owner)
@command(name="initl", description="Init a language choice message")
class Command:
    async def callback(self, context: Context) -> None:
        channel: GuildTextChannel | TextableGuildChannel = context.channel
        view: View = View()
        view.add_item(
            Button(
                label="English",
                emoji="🇬🇧",
                custom_id="choice_en",
                style=ButtonStyle.SECONDARY,
            )
        )
        view.add_item(
            Button(
                label="Русский",
                emoji="🇷🇺",
                custom_id="choice_ru",
                style=ButtonStyle.SECONDARY,
            )
        )
        await channel.send(content=None, components=view)
        return await context.respond(content="✅", ephemeral=True)

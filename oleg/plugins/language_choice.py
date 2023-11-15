from dataclasses import dataclass
from logging import getLogger

from crescent import Plugin, event as base_event, hook, command, Context
from hikari import (
    Guild,
    Role,
    Member,
    GuildTextChannel,
    TextableGuildChannel,
    GatewayBot,
    ButtonStyle,
    PartialChannel,
)
from hikari.events import ShardConnectedEvent
from miru import View, Button
from miru.events import ComponentInteractionCreateEvent

from oleg.hooks import is_owner
from oleg.variables import (
    GENERAL_GUILD_ID,
    RUSSIAN_CHANNEL_ID,
    ENGLISH_CHANNEL_ID,
    RUSSIAN_ROLE_ID,
    ENGLISH_ROLE_ID,
)

_log = getLogger(__name__)
plugin: Plugin = Plugin[GatewayBot, None]()
setattr(plugin, "resources", None)


@dataclass
class Resources:
    general_guild: Guild
    russian_chat: PartialChannel
    english_chat: PartialChannel
    russian_role: Role | None = None
    english_role: Role | None = None


@plugin.include
@base_event
async def on_connect(event: ShardConnectedEvent) -> None:
    resources = Resources(
        general_guild=await event.app.rest.fetch_guild(GENERAL_GUILD_ID),
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
    if event.custom_id == "choice_en":
        await event.app.rest.add_role_to_member(
            resources.general_guild, member, resources.english_role
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

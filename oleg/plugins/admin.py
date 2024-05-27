import io
import typing

from aurum.commands import SlashCommand
from aurum.commands.decorators import sub_command
from aurum.ext.plugins import Plugin
from aurum.interactions import InteractionContext
from hikari.files import Bytes
from hikari.permissions import Permissions

from oleg.utils.zip import create_memory_zip

plugin = Plugin("admin", default_member_permissions=Permissions.ADMINISTRATOR)


@plugin.include
class PruneCommand(SlashCommand):
    def __init__(self) -> None:
        super().__init__(
            name="prune",
        )

    @sub_command(name="emojis")
    async def prune_emojis(self, context: InteractionContext) -> None:
        deleted_emojis: typing.Dict[str, bytes] = {}
        await context.defer(ephemeral=True)
        if guild := context.interaction.get_guild():
            for emoji in guild.get_emojis().values():
                await context.bot.rest.delete_emoji(guild, emoji)
                deleted_emojis[
                    f"{emoji.name}.{emoji.extension or "webp"}"
                ] = await emoji.read()
            emojis_zip: io.BytesIO = await create_memory_zip(deleted_emojis)
            await context.edit_response(
                content=f"Removed **{len(deleted_emojis.keys())} emojis** ✅",
                attachment=Bytes(emojis_zip, f"{guild.id}-emojis.zip"),
            )

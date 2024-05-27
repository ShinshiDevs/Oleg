from os import getenv
from pathlib import Path

from aurum.client import Client
from aurum.enum.sync_commands import SyncCommandsFlag
from aurum.ext.plugins import PluginIntegration
from colorlog import DEBUG, basicConfig
from hikari.impl import GatewayBot

from oleg.dotenv import load_dotenv

load_dotenv()
basicConfig(
    level=DEBUG,
    format="%(log_color)s %(asctime)s %(bold)s%(levelname)-8s%(reset)s%(log_color)s %(bold)s%(name)s%(reset)s%(log_color)s %(message)s",
    datefmt="%y-%m-%d %H:%M:%S",
)

if not (token := getenv("OLEG_DISCORD_TOKEN")):
    raise Exception("No token")
bot = GatewayBot(
    token,
    banner=None,
)
client = Client(
    bot,
    sync_commands=SyncCommandsFlag.DEBUG,
    integrations=[PluginIntegration(base_directory=Path("oleg", "plugins"))],
)

if __name__ == "__main__":
    bot.run()

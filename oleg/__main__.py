from os import getenv

from crescent import Client
from dotenv import load_dotenv
from hikari import GatewayBot, Intents, Status
from miru.bootstrap import install

load_dotenv(override=True)

if __name__ == "__main__":
    base_bot: GatewayBot = GatewayBot(
        token=getenv("DISCORD_TOKEN"), intents=Intents.ALL, banner=None
    )
    install(base_bot)
    client: Client = Client(base_bot)
    client.plugins.load_folder("oleg.plugins")
    try:
        base_bot.run(status=Status.IDLE)
    except KeyboardInterrupt:
        exit(0)

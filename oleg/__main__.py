from os import getenv

from dotenv import load_dotenv
from hikari import GatewayBot, Intents, Status
from crescent import Client

load_dotenv(override=True)

if __name__ == "__main__":
    base_bot: GatewayBot = GatewayBot(
        token=getenv('DISCORD_TOKEN'),
        intents=Intents.ALL,
        banner=None
    )
    client: Client = Client(base_bot)
    try:
        base_bot.run(status=Status.IDLE)
    except KeyboardInterrupt:
        exit(0)

# Copyright (c) 2023-Present Shinshi Developers Team
# Apache-2.0 License from Shinshi Avela.
import asyncio
import sys

import uvloop


# from hikari
def setup_event_policy() -> None:
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    else:
        uvloop.install()

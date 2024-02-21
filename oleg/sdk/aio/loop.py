# Copyright (c) 2023-Present Shinshi Developers Team
# Apache-2.0 License from Shinshi Avela.
import asyncio
import warnings


# from hikari
def setup_loop() -> asyncio.AbstractEventLoop:
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            loop = asyncio.get_event_loop_policy().get_event_loop()
        if not loop.is_closed():
            return loop
    except RuntimeError:
        pass
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop

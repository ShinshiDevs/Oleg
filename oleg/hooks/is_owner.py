from os import getenv

from crescent import Context, HookResult


async def is_owner(context: Context) -> HookResult:
    if str(context.user.id) in getenv("OWNER_IDS").split(","):
        return HookResult(exit=False)
    return HookResult(exit=True)

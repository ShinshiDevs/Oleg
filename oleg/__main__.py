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
import sys
from concurrent.futures.thread import ThreadPoolExecutor
from os import environ
from pathlib import Path

from crescent.client import Client
from miru.bootstrap import install as install_miru

from oleg.framework.bot import Bot
from oleg.framework.data import Data
from oleg.framework.environment import Environment
from oleg.sdk.aio import setup_event_policy, setup_loop
from oleg.sdk.dotenv import load_dotenv

# entry point
if __name__ != "__main__":
    sys.exit(0)

executor = ThreadPoolExecutor(max_workers=10)
_, loop = setup_event_policy(), setup_loop()
loop.set_default_executor(executor)

# environment
environment = Environment()

# load dotenv file
if load_dotenv(f"{environment.root_path}/.env") is False:
    raise RuntimeError(".env file doesn't loaded correctly")

data = Data(environment.root_path, "resources", "config.json")
bot = Bot(ThreadPoolExecutor(), data.file)

# TODO: rework this part.
#   I very hate load plugins from path and this strategy of loading.
#   Maybe, we can make analogue of system from Shinshi Avela, but very simple version.
client = Client(bot, tracked_guilds=[int(environ.get("OLEG_MAIN_GUILD"))])
client.plugins.load_folder(str(Path("oleg", "plugins")))
install_miru(bot)

try:
    loop.run_until_complete(bot.start())
    loop.run_forever()
except KeyboardInterrupt:
    sys.exit(0)

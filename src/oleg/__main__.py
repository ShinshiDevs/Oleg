# MIT License
#
# Copyright (c) 2023-Present "Shinshi Developers Team"
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
from concurrent.futures.thread import ThreadPoolExecutor
from os import environ
from pathlib import Path

from crescent.client import Client
from dotenv.main import load_dotenv
from miru.bootstrap import install as install_miru

from oleg.framework.bot import Bot
from oleg.framework.data import Data
from oleg.framework.environment import Environment

load_dotenv("../.env", override=True)

if __name__ == "__main__":
    environment = Environment()
    executor = ThreadPoolExecutor(thread_name_prefix="oleg_")
    bot = Bot(executor, Data(environment.root_path, "data", "config.json").file)
    install_miru(bot)
    client = Client(bot, tracked_guilds=[int(environ.get("OLEG_MAIN_GUILD"))])
    client.plugins.load_folder(str(Path(environment.root_path, "plugins")))
    bot.run()

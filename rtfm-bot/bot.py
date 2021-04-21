import discord
import warnings
import configparser
from discord.ext import commands


EXTENSIONS = ["jishaku", "cogs.event", "cogs.misc"]

intents = discord.Intents.all()  # New in version 1.5
warnings.filterwarnings("ignore", category=DeprecationWarning)

CONFIG = configparser.ConfigParser()
CONFIG.read("config.ini")


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=CONFIG["bot"]["PREFIX"], intents=intents
        )

        self.color = 0x2F3136
        self.config = CONFIG

        for cog in EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception as exc:
                print(f"{cog} {exc.__class__.__name__}: {exc}")

    async def on_resumed(self):
        print("Resumed...")

    async def close(self):
        await super().close()

    def run(self):
        super().run(self.config["bot"]["TOKEN"], reconnect=True)

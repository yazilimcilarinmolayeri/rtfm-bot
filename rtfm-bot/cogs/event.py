import discord
from discord.ext import commands
from discord import Status, ActivityType


def setup(bot):
    bot.add_cog(Event(bot))


class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            "\ndiscord.py version: {}\n{} (ID: {})\n".format(
                discord.__version__, self.bot.user, self.bot.user.id
            )
        )

        await self.bot.change_presence(
            activity=discord.Activity(
                type=ActivityType.watching,
                name=self.bot.config["bot"]["STATUS"],
            ),
            status=Status.idle,
        )

    @commands.Cog.listener(name="on_message")
    async def on_chat(self, message):
        author = message.author

        if author.bot:
            return

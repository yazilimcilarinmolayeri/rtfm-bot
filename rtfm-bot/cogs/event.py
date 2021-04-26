import discord
from discord.ext import commands
from better_profanity import profanity
from discord import Status, ActivityType


def setup(bot):
    bot.add_cog(Event(bot))


class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.invite_code = "9P5HvT9nPD"
        profanity.load_censor_words_from_file("blacklist.txt")
        self.invite_address = "https://discord.com/invite/{}".format(self.invite_code)

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

    @commands.Cog.listener(name="on_message")
    async def on_invite(self, message):
        content = message.content.lower()

        if content.startswith("davet") or content.startswith("invite"):
            invite = await self.bot.fetch_invite(self.invite_address)
            await message.reply(invite.url)

    @commands.Cog.listener(name="on_message")
    async def on_badword(self, message):
        author = message.author
        channel = message.channel

        if author.bot:
            return

        if profanity.contains_profanity(message.content):
            await message.reply("-_-")

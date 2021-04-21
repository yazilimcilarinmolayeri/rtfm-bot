import json
import discord
from discord.ext import commands


with open("rtfm.json") as file:
    RTFM_DATA = json.load(file)


def setup(bot):
    bot.add_cog(Misc(bot))


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loads_rtfm_commands()

    def loads_rtfm_commands(self):
        for name, rule in RTFM_DATA["rules"].items():
            command = commands.Command(
                name=name,
                func=Misc.rtfm_command,
            )
            command.rule = rule
            command.cog = self

            self.rtfm.add_command(command)

    @commands.group(invoke_without_command=True)
    async def rtfm(self, ctx, command=None):
        embed = discord.Embed(color=self.bot.color)
        embed.title = "YMY Raconu"
        # embed.set_image(url="https://i.imgur.com/b5tPhBd.png")
        embed.description = "\n".join(
            ["{}. {}".format(n, r) for n, r in RTFM_DATA["rules"].items()]
        ) + "\n\n{}".format(RTFM_DATA["advices"])

        await ctx.send(embed=embed)

    async def rtfm_command(self, ctx):
        embed = discord.Embed(color=self.bot.color)
        embed.title = "Kural {}".format(ctx.command.name)
        embed.description = ctx.command.rule

        await ctx.send(embed=embed)

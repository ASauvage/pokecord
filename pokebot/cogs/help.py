import json
import discord
import logging
from discord.ext import commands
from .. import PokeBot


class Help(commands.Cog):
    def __init__(self, bot: PokeBot):
        self.bot = bot

        with open(self.bot.path + "help.json", 'r') as file:
            self.help = json.load(file)

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("cogs/help loaded")

    @commands.command()
    async def help(self, ctx: commands.Context, command=None):
        embed = discord.Embed(title=self.bot.user,  description="\n\n", color=0xE60012)
        embed.set_thumbnail(url=self.bot.user.avatar)
        embed.set_footer(text="By DilanDuck#4014")

        if command:
            try:
                embed.add_field(
                    name=self.bot.settings['discord']['prefix'] + self.help[command]['title'],
                    value=self.help[command]['description'], inline=False)

                await ctx.send(embed=embed)
            except KeyError:
                await ctx.channel.send(f"No command {command} found")
        else:
            for value in self.help.values():
                embed.add_field(name=self.bot.settings['discord']['prefix'] + value['title'],
                                value=value["description"], inline=False)

            await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    async def version(self, ctx: commands.Context):
        try:
            with open(self.bot.path + "changelog.txt", 'r') as file:
                content = file.read()
        except FileNotFoundError:
            content = "No changelog found"

        embed = discord.Embed(title="Game Bot Advance", description=f"V{self.bot.settings['version']}", color=0x221188)
        embed.set_thumbnail(url=self.bot.user.avatar)
        embed.set_footer(text="By DilanDuck#4014")

        embed.add_field(name="Emulation of Game Boy's game on public discord server and multiple minigames",
                        value="Developed with Python3",
                        inline=False)
        embed.add_field(name="Changelogs:",
                        value=content)

        await ctx.channel.send(embed=embed)
        await ctx.message.delete()


async def setup(bot: PokeBot):
    await bot.add_cog(Help(bot))
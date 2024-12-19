import json
import enum
import discord
import logging
from discord.ext import commands
from .. import PokeBot, VERSION
from ..common import get_commands_list


class Help(commands.Cog):
    help_commands: dict = get_commands_list()
    help_commands_enums: enum.Enum = enum.Enum('HELP_COMMANDS_ENUMS', {x: x for x in help_commands})

    def __init__(self, bot: PokeBot):
        self.bot = bot

        with open(self.bot.path + "commands.json", 'r') as file:
            self.help = json.load(file)

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f'cogs/{__name__} loaded')

    @commands.hybrid_command(name="help", with_app_command=True, description=help_commands['help']['description'])
    @discord.app_commands.describe(command="(optional) The command name")
    async def help(self, ctx: commands.Context, command: help_commands_enums = None):
        embed = discord.Embed(title=self.bot.user,
                              description=f"`Bot Prefix: {self.bot.settings['discord']['prefix']}`", color=0xE60012)
        embed.set_thumbnail(url=self.bot.user.avatar)
        embed.set_footer(text=f"By {self.bot.developper.display_name}")

        if command:
            embed.add_field(name=command.value,
                            value="__Description__: {}\n__Parameter(s)__:\n- {}\n__Guild Only__: {}\n__Extras__: {}".format(
                                self.help_commands[command.value]['description'],
                                '\n- '.join(self.help_commands[command.value]['parameters']) if self.help_commands[command.value][
                                    'parameters'] else 'No parameter',
                                self.help_commands[command.value]['guild_only'],
                                self.help_commands[command.value]['extras'] if self.help_commands[command.value][
                                    'extras'] else 'No extra informations.'
                            ),
                            inline=False)
        else:
            for name, value in self.help_commands.items():
                embed.add_field(name=name,
                                value=value["description"],
                                inline=False)

        await ctx.reply(embed=embed, ephemeral=True)

    @commands.hybrid_command(name="version", with_app_command=True, description=help_commands['version']['description'])
    async def version(self, ctx: commands.Context):
        try:
            with open(self.bot.path + "changelog.txt", 'r') as file:
                content = file.read()
        except FileNotFoundError:
            content = "No changelog found"

        embed = discord.Embed(title=self.bot.user, description=f"V{VERSION}", color=0x221188)
        embed.set_thumbnail(url=self.bot.user.avatar)
        embed.set_footer(text=f"https://github.com/ASauvage")

        embed.add_field(name="Gotta catch them all!!",
                        value=f"Developed with Python by {self.bot.developper.mention}",
                        inline=False)
        embed.add_field(name="Changelogs:",
                        value=content)

        await ctx.reply(embed=embed)


async def setup(bot: PokeBot):
    await bot.add_cog(Help(bot))

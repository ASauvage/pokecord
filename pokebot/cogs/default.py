import discord
import logging
from discord.ext import commands
from .. import PokeBot


class Default(commands.Cog):
    def __init__(self, bot: PokeBot):
        self.bot = bot




async def setup(bot: PokeBot):
    await bot.add_cog(Default(bot))

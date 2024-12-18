import discord
import logging
from discord.ext import commands
from datetime import date
from .. import PokeBot


class Default(commands.Cog):
    def __init__(self, bot: PokeBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f'cogs/{__name__} loaded')

    @commands.hybrid_command(name="create_my_card", with_app_command=True, description="Create your trainer card and start playing")
    async def create_my_card(self, ctx: commands.Context):
        # todo features teams like poke go
        embed = discord.Embed(title=f'{ctx.author.name} joined the {"red"} team!',
                              description='', color=0x221188)
        embed.set_thumbnail(url=ctx.author.avatar)
        embed.set_footer(text=f'Pokémon trainer since {date.today().strftime("%d/%m/%y")}')

    @commands.hybrid_command(name="card", with_app_command=True, description="Inspect trainer cards")
    @discord.app_commands.describe(trainer="(optional) The trainer id")
    async def card(self, ctx: commands.Context, trainer: discord.User):
        # todo check if account exist
        embed = discord.Embed(title=trainer.name,
                              description='', color=0x221188)
        embed.set_thumbnail(url=trainer.avatar)
        embed.set_footer(text=f'Pokémon trainer since {date.today().strftime("%d/%m/%y")}')


async def setup(bot: PokeBot):
    await bot.add_cog(Default(bot))

import discord
import logging
from discord.ext import commands
from datetime import date
from enum import Enum
from .. import PokeBot
from ..mongodb import MongoCon
from ..common import TrainerNotFound, get_commands_list


class Default(commands.Cog):
    help_commands: dict = get_commands_list()

    def __init__(self, bot: PokeBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f'cogs/{__name__} loaded')

    @commands.hybrid_command(name="create_my_card", with_app_command=True, description=help_commands['create_my_card']['description'])
    async def create_my_card(self, ctx: commands.Context):
        # todo features teams like poke go
        team = "red"
        if not MongoCon().is_trainer_exist(trainer_id=ctx.author.id):
            embed = discord.Embed(title=f'{ctx.author.name} joined the {team.capitalize()} team!',
                                  description='', color=self.bot.settings['gamerules']['teams'][team])
            embed.set_thumbnail(url=ctx.author.avatar)
            embed.set_footer(text=f'Pokémon trainer since {date.today().strftime("%d/%m/%y")}')

            MongoCon().create_trainer(trainer_id=ctx.author.id, trainer_team=team)
        else:
            embed = discord.Embed(title='You already have an acount',
                                  description='', color=0x221188)
        await ctx.reply(embed=embed, ephemeral=True)

    @commands.hybrid_command(name="card", with_app_command=True, description=help_commands['card']['description'])
    @discord.app_commands.describe(trainer="(optional) The trainer id")
    async def card(self, ctx: commands.Context, trainer: discord.User = None):
        if not trainer:
            trainer = ctx.author

        trainer_data = MongoCon().get_trainer_info(trainer_id=trainer.id)
        if not trainer_data:
            raise TrainerNotFound(trainer.id)

        embed = discord.Embed(title=f'{trainer.name} - Lvl. {trainer_data["trainer_lvl"]['lvl']}',
                              description=f'stats:\n - {"\n - ".join(f"{key}: {value}" for key, value in trainer_data["stats"].items())}',
                              color=self.bot.settings['gamerules']['teams'][trainer_data['trainer_team']])
        embed.set_thumbnail(url=trainer.avatar)
        embed.set_footer(text=f'Pokémon trainer since {trainer_data['register_since']}')

        await ctx.reply(embed=embed, ephemeral=True)


async def setup(bot: PokeBot):
    await bot.add_cog(Default(bot))

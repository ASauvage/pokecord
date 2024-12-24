import discord
import logging
from discord.ext import commands
from .. import PokeBot
from ..mongodb import MongoCon
from ..common import TrainerNotFound, get_commands_list


class Trainer(commands.Cog):
    help_commands: dict = get_commands_list()

    def __init__(self, bot: PokeBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f'cogs/{__name__} loaded')

    @commands.hybrid_command(name="bagpack", with_app_command=True, description=help_commands['bagpack']['description'])
    async def bagpack(self, ctx: commands.Context):
        bagpack = MongoCon().get_inventory(trainer_id=ctx.author.id)

        if not bagpack:
            raise TrainerNotFound(ctx.author.id)

        file = discord.File(fp=f"files/bagpack.png", filename=f"bagpack.png")
        embed = discord.Embed(title='Your bagpack contain',
                              description=f' - {"\n - ".join(f"{key}: {value}" for key, value in bagpack.items())}', color=0x221188)
        embed.set_thumbnail(url='attachment://bagpack.png')

        await ctx.reply(embed=embed, file=file, ephemeral=True)

# todo
# - team
# - pc
# - inventory


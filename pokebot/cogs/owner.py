import discord
import logging
from discord.ext import commands
from .. import PokeBot


class Owner(commands.Cog):
    def __init__(self, bot: PokeBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f'cogs/{__name__} loaded')

    @commands.hybrid_command(name="sync", with_app_command=True, description="Sync commands with discord (Owner only)")
    @commands.has_permissions(administrator=True)
    async def sync(self, ctx: commands.Context):
        if await self.bot.is_owner(ctx.author):
            logging.info(f"command(s) syncronisation")
            try:
                synced = await self.bot.tree.sync()
                await ctx.reply(f"Synced {len(synced)} command(s)")
                logging.info(f"Synced {len(synced)} command(s)")
            except Exception as e:
                await ctx.reply(e.__str__())
        else:
            raise commands.MissingPermissions(missing_permissions=['owner'])

    @commands.hybrid_command(name="find_user", with_app_command=True, description="Find a person's profile from their id")
    @discord.app_commands.describe(user="The user id")
    @commands.has_permissions(administrator=True)
    async def find_user(self, ctx: commands.Context, user: discord.User):
        await ctx.reply(user.mention)


async def setup(bot: PokeBot):
    await bot.add_cog(Owner(bot))

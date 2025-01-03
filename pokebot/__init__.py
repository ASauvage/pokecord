import os
import yaml
import discord
import logging
from discord.ext import commands
from datetime import date
from .common import TrainerNotFound


MAJOR_VERSION = 1
MINOR_VERSION = 0
PATCH_VERSION = 0
VERSION = '.'.join((str(MAJOR_VERSION), str(MINOR_VERSION), str(PATCH_VERSION)))


class PokeBot(commands.Bot):
    def __init__(self):
        # Variable
        self.path = os.path.dirname(__file__) + "/"
        with open(self.path + 'settings.yaml', 'r') as yaml_file:
            self.settings = yaml.load(yaml_file, Loader=yaml.FullLoader)
        self.developper = None

        # Intents
        intents = discord.Intents.default()
        intents.message_content = True
        intents.messages = True
        intents.dm_messages = True
        intents.reactions = True

        # Logging
        os.makedirs(self.path + 'logs', exist_ok=True)
        logging.basicConfig(filename=f"./logs/{date.today()}.log",
                            level=logging.INFO,
                            format="%(asctime)s [%(levelname)s] %(message)s")

        super().__init__(command_prefix=self.settings['discord']['prefix'],
                         help_command=None,
                         intents=intents,
                         application_id=self.settings['discord']['application_id'],
                         tree_cls=discord.app_commands.CommandTree)

    async def on_ready(self):
        logging.info(f'[{__name__}] Logged in as {self.user}')
        print(f'[{__name__}]logged in as {self.user}')

        self.developper = await self.fetch_user(187529417176645632)

        await self.change_presence(status=discord.Status.online)

    async def setup_hook(self):
        logging.info("Loading cogs...")
        for filename in os.listdir(os.path.dirname(__file__) + "/cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")

    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f"Error: Missing Required Argument // {error}", ephemeral=True)
            logging.info(f"Error: MissingRequiredArgument // {error}")
        elif isinstance(error, commands.BadArgument):
            await ctx.reply(f"Error: Bad Argument // {error}", ephemeral=True)
            logging.info(f"Error: Bad Argument // {error}")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply(f"Error: Missing Permissions// {error}", ephemeral=True)
            logging.info(f"Error: Missing Permissions // {error}")
        elif isinstance(error, commands.ChannelNotReadable):
            await ctx.reply(f"Error: Channel Not Readable // {error}", ephemeral=True)
            logging.info(f"Error: Channel Not Readable // {error}")
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.reply(f"Sorry {ctx.author.mention}, but your not allowed to use this command in private message", ephemeral=True)
            logging.info(f"Error : No Private Message // {error}")
        elif isinstance(error, commands.PrivateMessageOnly):
            await ctx.reply(f"Sorry {ctx.author.mention}, but your not allowed to use this command in servers", ephemeral=True)
            logging.info(f"Error : Private Message Only // {error}")
        elif isinstance(error, TrainerNotFound):
            await ctx.reply("No trainer found for this ID", ephemeral=True)
            logging.info(f"Error : No Trainer Found // {error}")
        else:
            logging.info(f"Error: Unknown // {error}")

    def startbot(self, token: str = None):
        if not token:
            token = self.settings['discord']['token']

        self.start(token)

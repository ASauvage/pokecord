import os
import yaml
import discord
import logging
from discord.ext import commands
from datetime import date


MAJOR_VERSION = 1
MINOR_VERSION = 1
VERSION = '.'.join((str(MAJOR_VERSION), str(MINOR_VERSION)))


class PokeBot(commands.Bot):
    def __init__(self):
        logging.basicConfig(filename=f"./logs/{date.today()}.log",
                            level=logging.INFO,
                            format="%(asctime)s [%(levelname)s] %(message)s")

        with open(os.path.dirname(__file__) + 'settings.yaml', 'r') as json_file:
            self.settings = yaml.load(json_file, Loader=yaml.FullLoader)

        self.path = os.path.dirname(__file__) + "/"
        self.logchannel = None

        # Intents
        intents = discord.Intents.default()
        intents.message_content = True
        intents.messages = True
        intents.dm_messages = True
        intents.reactions = True

        super().__init__(command_prefix=self.settings['discord']['prefix'], help_command=None, intents=intents)

    async def on_ready(self):
        logging.info("[main.py] Logged in as {0.user}".format(self))
        print("[main.py]logged in as {0.user}".format(self))

        await self.change_presence(status=discord.Status.online)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send(f"Error: Missing Required Argument // {error}")
            await ctx.message.delete()
            logging.info(f"Error: MissingRequiredArgument // {error}")
        elif isinstance(error, commands.BadArgument):
            await ctx.channel.send(f"Error: Bad Argument // {error}")
            await ctx.message.delete()
            logging.info(f"Error: Bad Argument // {error}")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(f"Error: Missing Permissions// {error}")
            await ctx.message.delete()
            logging.info(f"Error: Missing Permissions // {error}")
        elif isinstance(error, commands.ChannelNotReadable):
            await ctx.channel.send(f"Error: Channel Not Readable // {error}")
            await ctx.message.delete()
            logging.info(f"Error: Channel Not Readable // {error}")
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.channel.send(
                f"Sorry {ctx.author.mention}, but your not allowed to use this command in private message")
            logging.info(f"Error : No Private Message // {error}")
        else:
            logging.info(f"Error: Unknown // {error}")

    def run_pokebot(self, token: str = None):
        if not token:
            token = self.settings['discord']['token']

        for filename in os.listdir(os.path.dirname(__file__) + "/cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename[:-3]}")

        self.start(token)


def get_settings():
    with open(os.path.dirname(__file__) + 'settings.yaml', 'r') as json_file:
        return yaml.load(json_file, Loader=yaml.FullLoader)

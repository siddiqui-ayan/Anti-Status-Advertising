from discord.ext import commands
import os, discord
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('token')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

if __name__ == "__main__":
    for i in os.listdir('./src'):
        if i.endswith('.py'):
            bot.load_extension(f'src.{i.split(".py")[0]}')
    bot.run(token)
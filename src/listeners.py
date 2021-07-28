import json, discord
from discord.ext import commands

class Listeners(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.config = json.load(open('config.json'))
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot made by @MysteriousK69 and !MisuteriasuKe#6969 on GitHub and Discord respectively.")
        print(f'Logged in as {self.bot.user} || {self.bot.user.id}')

    @commands.Cog.listener()
    async def on_member_join(self, e: discord.Member):
        logs = self.bot.get_channel(self.config['logs'])
        for i in self.config['blacklist']:
            status = e.activities
            for x in status:
                if type(x) == discord.activity.CustomActivity:
                    try:
                        if x.name.lower().find(i.lower()) != -1:
                            await logs.send(embed=discord.Embed(title='Member found status advertising!', description=f'I found {e.mention} ({e.id}) status advertising. Their status is "{x}", what triggered the bot is "{i}"'))
                            break
                    except AttributeError:
                        break
                break
    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        logs = self.bot.get_channel(self.config['logs'])
        e = msg.author
        for i in self.config['blacklist']:
            status = e.activities
            for x in status:
                if type(x) == discord.activity.CustomActivity:
                    try:
                        if x.name.lower().find(i.lower()) != -1:
                            await logs.send(embed=discord.Embed(title='Member found status advertising!', description=f'I found {e.mention} ({e.id}) status advertising. Their status is "{x}", what triggered the bot is "{i}"'))
                            break
                    
                    except AttributeError:
                        break
                break

def setup(bot):
    bot.add_cog(Listeners(bot))
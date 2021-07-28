import json, discord
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.config = json.load(open('config.json'))

    @commands.command()
    async def search(self, ctx: commands.Context):
        logs = self.bot.get_channel(self.config['logs'])
        await ctx.send(f"Please wait, searching all members. The results will go in <#{self.config['logs']}>.\n**Please note that this may take a while.**")
        for e in self.bot.get_all_members():
            for i in self.config['blacklist']:
                status = e.activities
                for x in status:
                    if type(x) == discord.activity.CustomActivity:
                        if x.name.lower().find(i.lower()) != -1:
                            await logs.send(embed=discord.Embed(title='Member found status advertising!', description=f'I found {e.mention} ({e.id}) status advertising. Their status is "{x}", what triggered the bot is "{i}"'))
                            break
def setup(bot):
    bot.add_cog(Commands(bot))
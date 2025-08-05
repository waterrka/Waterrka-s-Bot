import disnake
from disnake.ext import commands

class MessageSend(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="message")
    async def message(self, ctx):
        embed = disnake.Embed(
            title="Test",
            description="test test test"
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MessageSend(bot))
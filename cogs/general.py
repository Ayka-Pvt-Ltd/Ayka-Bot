import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # WELCOME USER
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    #Hello
    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

    # CLEAR COMMAND
    @commands.command()
    async def clear(self, ctx , amount=1):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def ping(self,ctx):
        await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))


def setup(client):
    client.add_cog(General(client))

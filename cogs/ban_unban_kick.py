import discord
from discord.ext import commands


class KickUnbanBan(commands.Cog):
    """docstring for KickUnbanBan"""

    def __init__(self, client):
        self.client = client

    # Kick
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *,reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked')

    #Ban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member: discord.Member, *,reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been banned')

    #Unban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,*,member):
        banned_users = await ctx.guild.bans()

        member_name , member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name,user.discriminator) == (member_name,member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{member} has been unbanned ")



def setup(client):
    client.add_cog(KickUnbanBan(client))

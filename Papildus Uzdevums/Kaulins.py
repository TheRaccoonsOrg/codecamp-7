from discord.ext import commands
import random
class Kaulins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send("Hello, fellow Raccoon {member.mention}.")
    
    @commands.group()
    async def met(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid command. Try again!")

    @met.command(name="monetu")
    async def met_monetu(self, ctx):
        await ctx.send(random.randint(0, 1))

    @met.command(name="kaulinu")
    async def met_kaulinu(self, ctx):
        await ctx.send(random.randint(1, 6))
    
    @met.command(name="custom")
    async def custom_roll(self, ctx, sides: int):
        await ctx.send(random.randint(1, sides))

async def setup(bot):
    await bot.add_cog(Kaulins(bot))
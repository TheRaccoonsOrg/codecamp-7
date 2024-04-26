#importejam asyncio lai varētu izmantot asinhronās funkcijas
import asyncio
import nest_asyncio

import discord
from discord.ext import commands
from Secret import TOKEN

from Kaulins import Kaulins

nest_asyncio.apply()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#Notiks, ja bots ir paladies bez problēmām
@bot.event
async def on_ready():
    print("Bot is ready and running!")

@bot.command()
#test ir komandas nosaukums
async def test(ctx):
    await ctx.send("Hello World!")

#Ar "name" varam izveleties komandas nosaukumu
@bot.command(name="ping")
async def loti_gars_komandas_nosaukums(ctx, reizes:int = 1):
    for i in range(reizes):    
        await ctx.send("pong")
# !ping 5

#Izveidojam komandu grupu
@bot.group(name="mod")
async def mod_grupa(ctx):
    #Ja tiek izsaukta nepareiza apakskomanda
    if ctx.invoked_subcommand is None:
        await ctx.send("Invalid command. Try again!")

#pievienojam apakskomandu grupai
@mod_grupa.command()
async def ping(ctx, user):
    await ctx.send("Ping " + user)
# !mod ping @user

@bot.command()
async def info(ctx):
    #Iegūstam servera informāciju
    servera_nosaukums = ctx.guild.name
    servera_dalibnieki = ctx.guild.member_count
    servera_roles = ctx.guild.roles

    servera_roles_str = ""
    #Parveidojam roles uz tiaki role nosaukumiem
    for role in servera_roles:
        servera_roles_str += role.name + "\n"

    #Izveidojam zinu
    zina = f"*Servera nosaukums*: {servera_nosaukums}\n*Servera dalibnieki*: {servera_dalibnieki}\n*Servera roles*: {servera_roles_str}"

    await ctx.send(zina)


@bot.command()
async def info_advanced(ctx):
    servera_nosaukums = ctx.guild.name
    servera_dalibnieki = ctx.guild.member_count
    servera_roles = ctx.guild.roles

    servera_roles_str = ""

    for role in servera_roles:
        servera_roles_str += role.name + "\n"

    #Izveidojam embed tipa ziņu
    embed = discord.Embed(title="Servera informācija", description="Informācija par serveri", color=0x00ff00)
    
    #Pievienojam nepieciešamos laukus
    embed.add_field(name="Servera nosaukums", value=servera_nosaukums, inline=False)
    embed.add_field(name="Servera dalibnieki", value=servera_dalibnieki, inline=False)
    embed.add_field(name="Servera roles", value=servera_roles_str, inline=False)

    await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.send("Bot is shutting down!")
    await bot.close()
        
#Izveidojam asinhronu funkciju, lai varētu pievienot Cog
async def main():
    await bot.load_extension("Kaulins")
    await bot.run(TOKEN)

#Palaižam asinhrono funkciju
asyncio.run(main())
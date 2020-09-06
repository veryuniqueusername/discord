import discord
import math
import random
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='$')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}ms'.format(round(bot.latency, 2)))

@bot.command()
async def list(ctx):
    check_role = get(ctx.message.guild.roles, name='TigerWolf')
    if check_role in ctx.author.roles:
        x = ctx.guild.members
        for member in x:
            await ctx.send(member.name)
    else:
        await ctx.send("gitgud")

@bot.command()
async def kick(ctx):
    check_role = get(ctx.message.guild.roles, name='TigerWolf')
    if check_role in ctx.author.roles:
        x = ctx.guild.members
        y = random.randint(0, len(x) - 1)
        z = x[y]
        r = z.roles
        while len(r) != 1:
            x = ctx.guild.members
            y = random.randint(0, len(x) - 1)
            z = x[y]
            r = z.roles
            print("not non")
            print(z)
        else:
            await ctx.send("non")
            await z.kick()
        await ctx.send(z.mention)
    else:
        await ctx.send("gitgud")

bot.run('NzUxOTAwMDc4NTc0NDAzNzI1.X1PzhA.sXgdEtbNHMtSUxPx5j1h2MkXATc')
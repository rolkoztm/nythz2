import discord
import os
import datetime
import inspect
import sqlite3
import jishaku
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or("'"))
bot.remove_command("help")

@bot.event
async def on_ready():
    print("zyje!!!!!!!!!!!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content.endswith("<@!723210798146781230") or message.content.endswith("<@723210798146781230>"):
        okok = discord.Embed(
            color = 0x000000,
            title = "**Ping ping i ping!!**",
            description = f"<a:twitch:719972173799751682> **{message.author.mention} Jolo, widze że nie znasz mojego prefixu czy coś.\nMój prefix na serwerze `{message.author.guild}` to: `'`.\nLista komend jest pod komendą `'jak`.**"
        )
        okok.set_footer(text="Zapraszam na mój serwer support!!", icon_url=message.author.avatar_url)
        okok.timestamp=datetime.datetime.utcnow()
        await message.channel.send(embed=okok)
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction("<a:nei:719868753214570557>")

@bot.command(aliases=["load"])
@commands.is_owner()
async def załaduj(ctx, okk):
  bot.load_extension(f"cogs.{okk}")
  await ctx.send(f"> **Załadowano cogs `{okk}` pomyślnie**")

@bot.command(aliases=["unload"])
@commands.is_owner()
async def odładuj(ctx, okk):
  bot.unload_extension(f"cogs.{okk}")
  await ctx.send(f"> **Odładowano cogs `{okk}` pomyślnie**")

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

bot.load_extension("jishaku")

@bot.command(name='eval', pass_context=True)
@commands.is_owner()
async def eval_(ctx, *, command):
    res = eval(command)
    if inspect.isawaitable(res):
        await ctx.send(await res)
    else:
        await ctx.send(res)

@eval_.error
async def eval__error(ctx, error):
    await ctx.send(f"**Error!**\nTraceback: `{error}`")

bot.run("tu daj token downie")

import discord
import datetime
import sqlite3
import asyncio
from discord.ext import commands

class Automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.guild_permissions.manage_messages:
            return
        if not message.author.guild_permissions.manage_messages:
            if "discord.gg/" in message.content or "https://discord.gg/" in message.content:
                db = sqlite3.connect('main.sqlite')
                cur = db.cursor()
                cur.execute(f"SELECT user_id FROM amod WHERE guild_id = {message.guild.id}")
                res = cur.fetchone()
                if res is None:
                    return
                elif res is not None:
                    await message.delete()
                    await message.channel.send("nununu reklamowanie sie?")

    @commands.command(aliases=["auto-mod"])
    async def automod(self, ctx):
        if ctx.message.author.guild_permissions.manage_guild:
            db = sqlite3.connect('main.sqlite')
            cur = db.cursor()
            cur.execute(f"SELECT user_id FROM amod WHERE guild_id = {ctx.guild.id}")
            res = cur.fetchone()
            if res is None:
                sql = ("INSERT INTO amod(user_id, guild_id) VALUES(?,?)")
                val = (ctx.author.id, ctx.guild.id)
                cur.execute(sql, val)
                db.commit()
                await ctx.send("<a:tia:719868701205332012> **`Automod włączony pomyślnie.`**")
            elif res is not None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Automod jest już włączony.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
        else:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Nie masz wystarczających uprawnień.\nWymagane: `MANAGE GUILD`.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)

    @commands.command(aliases=["auto-mod-off", "automod-off"])
    async def automodoff(self, ctx):
        if ctx.message.author.guild_permissions.manage_guild:
            db = sqlite3.connect('main.sqlite')
            cur = db.cursor()
            cur.execute(f"SELECT user_id FROM amod WHERE guild_id = {ctx.guild.id}")
            res = cur.fetchone()
            if res is None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Automod nie był włączony.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
            elif res is not None:
                sql = f"DELETE FROM amod WHERE guild_id = {ctx.guild.id}"
                cur.execute(sql)
                db.commit()
                await ctx.send("<a:tia:719868701205332012> **`Automod wyłączony pomyślnie.`**")
        else:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Nie masz wystarczających uprawnień.\nWymagane: `MANAGE GUILD`.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)

def setup(bot):
    bot.add_cog(Automod(bot))
    print("zaladowano Automod")

import discord
import datetime
import sqlite3
import asyncio
from discord.ext import commands

class Log(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["logi"])
    async def logs(self, ctx, k:discord.TextChannel=None):
        if ctx.message.author.guild_permissions.manage_guild:
            if k is None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Poprawne użycie: `logs (kanał)`.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
            elif k is not None:
                db = sqlite3.connect('main.sqlite')
                cur = db.cursor()
                cur.execute(f"SELECT channel_id FROM logs WHERE guild_id = {ctx.guild.id}")
                res = cur.fetchone()
                if res is None:
                    sql = ("INSERT INTO logs(channel_id, guild_id) VALUES(?,?)")
                    val = (k.id, ctx.guild.id)
                    cur.execute(sql, val)
                    db.commit()
                    await ctx.send(f"<a:tia:719868701205332012> **`Kanał logów został ustawiony na:`** {k.mention}")
                elif res is not None:
                    er = discord.Embed(
                        color=0xff4545,
                        title="**Error...**",
                        description="<a:nei:719868753214570557> **|** *Logi są już ustawione na tym serwerze.*"
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

    @logs.error
    async def logs_error(self, ctx, error):
        er = discord.Embed(
            color=0xff4545,
            title="**Error...**",
            description="<a:nei:719868753214570557> **|** *Nie znalazłem takiego kanału.*"
        )
        er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
        er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        er.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=er)

    @commands.command(aliases=["logs-off"])
    async def logsoff(self, ctx):
        if ctx.message.author.guild_permissions.manage_guild:
            db = sqlite3.connect('main.sqlite')
            cur = db.cursor()
            cur.execute(f"SELECT channel_id FROM logs WHERE guild_id = {ctx.guild.id}")
            res = cur.fetchone()
            if res is None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Logi nie były włączone.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
            elif res is not None:
                sql = f"DELETE FROM logs WHERE guild_id = {ctx.guild.id}"
                cur.execute(sql)
                db.commit()
                await ctx.send("<a:tia:719868701205332012> **`Wyłączono logi!`**")
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
    bot.add_cog(Log(bot))
    print("zaladowano Logs")

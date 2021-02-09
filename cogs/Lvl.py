import discord
import os
import time
import inspect
import sqlite3
import math
import datetime
from discord.ext import commands

class lvl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        else:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT user_id FROM levels WHERE user_id = {message.author.id}")
            result = cursor.fetchone()
            if result is None:
                sql = ("INSERT INTO levels(user_id, exp, lvl) VALUES(?,?,?)")
                val = (message.author.id, 2, 0)
                cursor.execute(sql, val)
                db.commit()
            else:
                cursor.execute(f"SELECT user_id, exp, lvl FROM levels WHERE user_id = {message.author.id}")
                result1 = cursor.fetchone()
                exp = int(result1[1])
                sql = ("UPDATE levels SET exp = ? WHERE user_id = ?")
                val = (exp + 2, str(message.author.id))
                cursor.execute(sql, val)
                db.commit()

                cursor.execute(f"SELECT user_id, exp, lvl FROM levels WHERE user_id = {message.author.id}")
                result2 = cursor.fetchone()
                xp_start = int(result2[1])
                lvl_start = int(result2[2])
                xp_end = math.floor(5 * (lvl_start ^ 2) + 50 * lvl_start + 100)
                if xp_end < xp_start:
                    sql = ("UPDATE levels SET lvl = ? WHERE user_id = ?")
                    val = (int(lvl_start + 1), str(message.author.id))
                    cursor.execute(sql, val)
                    db.commit()
                    sql = ("UPDATE levels SET exp = ? WHERE user_id = ?")
                    val = (0, str(message.author.id))
                    cursor.execute(sql, val)
                    db.commit()
                    cursor.execute(f"SELECT user_id FROM lvloff WHERE guild_id = {message.guild.id}")
                    result123 = cursor.fetchone()
                    if result123 is None:
                        await message.channel.send(f"{message.author.mention} // Gz!! Zdobyłeś nowy globalny poziom!! (`{lvl_start + 1}`)")
                    elif result123 is not None:
                        return

    @commands.command(aliases=["glvl-off"])
    async def gleveloff(self, ctx):
        if ctx.message.author.guild_permissions.manage_guild:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT user_id FROM lvloff WHERE guild_id = {ctx.guild.id}")
            result = cursor.fetchone()
            if result is None:
                sql = ("INSERT INTO lvloff(user_id, guild_id) VALUES(?,?)")
                val = (ctx.author.id, ctx.guild.id)
                cursor.execute(sql, val)
                db.commit()
                dn = discord.Embed(
                    color=0xabff96,
                    title="**Succes!**",
                    description="<a:tia:719868701205332012> **|** *Pomyślnie `wyłączono` Global lvl system.*"
                )
                dn.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731955375464775790/image0.gif")
                dn.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                dn.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=dn)
            elif result is not None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Globalny lvl system był już `wyłączony` na tym serwerze.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
        else:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Nie masz uprawnień `manage_guild`.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)

    @commands.command(aliases=["glvl-on"])
    async def glevelon(self, ctx):
        if ctx.message.author.guild_permissions.manage_guild:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT user_id FROM lvloff WHERE guild_id = {ctx.guild.id}")
            result = cursor.fetchone()
            if result is None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Globalny lvl system był już `włączony` na tym serwerze.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
            elif result is not None:
                sql = f"DELETE FROM lvloff WHERE guild_id = {ctx.guild.id}"
                cursor.execute(sql)
                db.commit()
                dn = discord.Embed(
                    color=0xabff96,
                    title="**Succes!**",
                    description="<a:tia:719868701205332012> **|** *Pomyślnie `włączono` Global lvl system.*"
                )
                dn.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731955375464775790/image0.gif")
                dn.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                dn.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=dn)
        else:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Nie masz uprawnień `manage_guild`.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)

def setup(bot):
    bot.add_cog(lvl(bot))
    print("zaladowano Lvl")

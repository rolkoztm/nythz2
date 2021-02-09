import discord
import os
import time
import requests
import random
import inspect
import datetime
import sqlite3
from discord.utils import get
from discord.ext import commands

class Wel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        db = sqlite3.connect('main.sqlite')
        cur = db.cursor()
        cur.execute(f"SELECT channel_id FROM wel WHERE guild_id = {member.guild.id}")
        res = cur.fetchone()
        if res is None:
            return
        else:
            db = sqlite3.connect('main.sqlite')
            cur = db.cursor()
            cur.execute(f"SELECT msg FROM wel WHERE guild_id = {member.guild.id}")
            res1 = cur.fetchone()
            osoby = len(list(member.guild.members))
            oznacz = member.mention
            imie = member.name
            serwer = member.guild

            xd = str(res1[0]).format(osoby = osoby, oznacz = oznacz, imie = imie, serwer = serwer)

            yhym = self.bot.get_channel(id=int(res[0]))
            await yhym.send(xd)

    @commands.command(aliases=["pow-off"])
    async def powoff(self, ctx):
        db = sqlite3.connect('main.sqlite')
        cur = db.cursor()
        if ctx.message.author.guild_permissions.manage_guild:
            cur.execute(f"SELECT channel_id FROM wel WHERE guild_id = {ctx.guild.id}")
            res1 = cur.fetchone()
            if res1 is None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Powitanie nie było włączone.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
            elif res1 is not None:
                sql = f"DELETE FROM wel WHERE guild_id = {ctx.guild.id}"
                cur.execute(sql)
                db.commit()
                dn = discord.Embed(
                    color=0xabff96,
                    title="**Succes!**",
                    description=f"<a:tia:719868701205332012> **|** *Powitanie zostało wyłączone.*"
                )
                dn.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731955375464775790/image0.gif")
                dn.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                dn.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=dn)
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

    @commands.command(aliases=["pow-kanał", "pow-kanal"])
    async def powkanal(self, ctx, k:discord.TextChannel=None):
        if ctx.message.author.guild_permissions.manage_guild:
            if k is None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Poprawne użycie: `pow-kanał (kanał)`.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
            elif k is not None:
                db = sqlite3.connect('main.sqlite')
                cur = db.cursor()
                cur.execute(f"SELECT channel_id FROM wel WHERE guild_id = {ctx.guild.id}")
                res = cur.fetchone()
                if res is None:
                    sql = ("INSERT INTO wel(channel_id, guild_id) VALUES(?,?)")
                    val = (k.id, ctx.guild.id)
                    cur.execute(sql, val)
                    db.commit()
                    dn = discord.Embed(
                        color=0xabff96,
                        title="**Succes!**",
                        description=f"<a:tia:719868701205332012> **|** *Kanał powitalny został ustawiony na: {k.mention}.*"
                    )
                    dn.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731955375464775790/image0.gif")
                    dn.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                    dn.timestamp=datetime.datetime.utcnow()
                    await ctx.send(embed=dn)
                elif res is not None:
                    sql = ("UPDATE wel SET channel_id = ? WHERE guild_id = ?")
                    val = (k.id, ctx.guild.id)
                    cur.execute(sql, val)
                    db.commit()
                    dn = discord.Embed(
                        color=0xabff96,
                        title="**Succes!**",
                        description=f"<a:tia:719868701205332012> **|** *Kanał powitalny został zmieniony na: {k.mention}.*"
                    )
                    dn.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731955375464775790/image0.gif")
                    dn.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                    dn.timestamp=datetime.datetime.utcnow()
                    await ctx.send(embed=dn)
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

    @powkanal.error
    async def powkanal_error(self, ctx, error):
        er = discord.Embed(
            color=0xff4545,
            title="**Error...**",
            description="<a:nei:719868753214570557> **|** *Nie znalazłem tego kanału.*"
        )
        er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
        er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        er.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=er)

    @commands.command(aliases=["pow-text", "pow-tekst"])
    async def powtext(self, ctx, *, k):
        if ctx.message.author.guild_permissions.manage_guild:
            if k is None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Poprawne użycie: `pow-text (tekst)`.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
            elif k is not None:
                db = sqlite3.connect('main.sqlite')
                cur = db.cursor()
                cur.execute(f"SELECT msg FROM wel WHERE guild_id = {ctx.guild.id}")
                res = cur.fetchone()
                if res is None:
                    sql = ("INSERT INTO wel(msg, guild_id) VALUES(?,?)")
                    val = (k, ctx.guild.id)
                    cur.execute(sql, val)
                    db.commit()
                    dn = discord.Embed(
                        color=0xabff96,
                        title="**Succes!**",
                        description=f"<a:tia:719868701205332012> **|** *Text powitalny został ustawiony na: `{k}`.*"
                    )
                    dn.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731955375464775790/image0.gif")
                    dn.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                    dn.timestamp=datetime.datetime.utcnow()
                    await ctx.send(embed=dn)
                elif res is not None:
                    sql = ("UPDATE wel SET msg = ? WHERE guild_id = ?")
                    val = (k, ctx.guild.id)
                    cur.execute(sql, val)
                    db.commit()
                    dn = discord.Embed(
                        color=0xabff96,
                        title="**Succes!**",
                        description=f"<a:tia:719868701205332012> **|** *Text powitalny został zmieniony na: `{k}`.*"
                    )
                    dn.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731955375464775790/image0.gif")
                    dn.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                    dn.timestamp=datetime.datetime.utcnow()
                    await ctx.send(embed=dn)
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
    bot.add_cog(Wel(bot))
    print("zaladowano Welcome")

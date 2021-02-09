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

class Arole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        db = sqlite3.connect('main.sqlite')
        cur = db.cursor()
        cur.execute(f"SELECT role FROM arole WHERE guild_id = {member.guild.id}")
        res = cur.fetchone()
        if res is None:
            return
        elif res is not None:
            siema = str(res[0])
            role = get(member.guild.roles, name=siema)
            await member.add_roles(role)

    @commands.command(aliases=["auto-role", "a-role"])
    async def arole(self, ctx, xd:discord.Role=None):
        if ctx.message.author.guild_permissions.manage_guild:
            if xd is None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Poprawne użycie: `auto-role (rola)`.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
            elif xd is not None:
                db = sqlite3.connect('main.sqlite')
                cur = db.cursor()
                cur.execute(f"SELECT role FROM arole WHERE guild_id = {ctx.guild.id}")
                res = cur.fetchone()
                if res is None:
                    sql = ("INSERT INTO arole(role, guild_id) VALUES(?,?)")
                    val = (xd.name, ctx.guild.id)
                    cur.execute(sql, val)
                    db.commit()
                    dn = discord.Embed(
                        color=0xabff96,
                        title="**Succes!**",
                        description=f"<a:tia:719868701205332012> **|** *Rola {xd.mention} będzie nadawana nowym członkom.*"
                    )
                    dn.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731955375464775790/image0.gif")
                    dn.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                    dn.timestamp=datetime.datetime.utcnow()
                    await ctx.send(embed=dn)
                elif res is not None:
                    er = discord.Embed(
                        color=0xff4545,
                        title="**Error...**",
                        description="<a:nei:719868753214570557> **|** *Autorole jest już włączony na tym serwerze, możesz ją wyłączyć komendą `auto-role-off`.*"
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

    @arole.error
    async def arole_error(self, ctx, error):
        er = discord.Embed(
            color=0xff4545,
            title="**Error...**",
            description="<a:nei:719868753214570557> **|** *Nie znalazłem tej roli.*"
        )
        er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
        er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        er.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=er)

    @commands.command(aliases=["auto-role-off", "a-role-off"])
    async def aroleoff(self, ctx):
        if ctx.message.author.guild_permissions.manage_guild:
            db = sqlite3.connect('main.sqlite')
            cur = db.cursor()
            cur.execute(f"SELECT role FROM arole WHERE guild_id = {ctx.guild.id}")
            res = cur.fetchone()
            if res is not None:
                sql = f"DELETE FROM arole WHERE guild_id = {ctx.guild.id}"
                cur.execute(sql)
                db.commit()
                dn = discord.Embed(
                    color=0xabff96,
                    title="**Succes!**",
                    description=f"<a:tia:719868701205332012> **|** *wyłączono autorole.*"
                )
                dn.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731955375464775790/image0.gif")
                dn.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                dn.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=dn)
            elif res is None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Autorole nie była włączona na tym serwerze.*"
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

def setup(bot):
    bot.add_cog(Arole(bot))
    print("zaladowano Autorole")

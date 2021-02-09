import discord
import datetime
import sqlite3
import asyncio
from discord.ext import commands

class Antyraid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.guild_permissions.manage_messages:
            return
        if not message.author.guild_permissions.manage_messages:
            if "@everyone" in message.content or "@here" in message.content:
                db = sqlite3.connect('main.sqlite')
                cur = db.cursor()
                cur.execute(f"SELECT user_id FROM antyr WHERE guild_id = {message.guild.id}")
                res = cur.fetchone()
                if res is None:
                    return
                elif res is not None:
                    await message.delete()
                    await message.author.ban(reason="Ban z powodu wykrycia raidu. ~ Nythz")
                    await message.guild.owner.send("Wykryłem raid na twoim serwerze! lecz te osoby zostały zbanowane przezemnie :)")
                    cur.execute(f"SELECT channel_id FROM modlog WHERE guild_id = {message.guild.id}")
                    res1 = cur.fetchone()
                    lol = discord.Embed(
                        title="**Szczegóły Bana:**",
                        description=f"<:ban:723881510054395990> {message.author.mention} *został zbanowany!!*\n\n> **Z serwera: `{message.guild}`**\n\n> **Powód: `Ban z powodu wykrycia raidu. ~ Nythz`**",
                        color=0xff4545
                    )
                    lol.set_thumbnail(url=message.author.avatar_url)
                    lol.set_footer(text=f"Nythz™#6222  •  (723210798146781230)", icon_url="https://cdn.discordapp.com/avatars/723210798146781230/6b957852da78a592a0bfb3430bbcf9eb.webp?size=1024")
                    lol.timestamp = datetime.datetime.utcnow()
                    if res1 is None:
                        await message.channel.send(embed=lol)
                    elif res1 is not None:
                        jnt = int(res1[0])
                        xd = self.bot.get_channel(id=jnt)
                        await xd.send(embed=lol)
                        await message.guild.owner.send(f"Szczegóły: <#{jnt}>")
                        try:
                            await message.author.send(embed=lol)
                        except:
                            return

    @commands.command(aliases=["anty-raid"])
    async def antyraid(self, ctx):
        if ctx.message.author.guild_permissions.manage_guild:
            db = sqlite3.connect('main.sqlite')
            cur = db.cursor()
            cur.execute(f"SELECT user_id FROM antyr WHERE guild_id = {ctx.guild.id}")
            res = cur.fetchone()
            if res is None:
                sql = ("INSERT INTO antyr(user_id, guild_id) VALUES(?,?)")
                val = (ctx.author.id, ctx.guild.id)
                cur.execute(sql, val)
                db.commit()
                await ctx.send("<a:tia:719868701205332012> **`Antyraid włączony pomyślnie.`**")
            elif res is not None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Antyraid jest już włączony.*"
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

    @commands.command(aliases=["anty-raid-off", "antyraid-off"])
    async def antyraidoff(self, ctx):
        if ctx.message.author.guild_permissions.manage_guild:
            db = sqlite3.connect('main.sqlite')
            cur = db.cursor()
            cur.execute(f"SELECT user_id FROM antyr WHERE guild_id = {ctx.guild.id}")
            res = cur.fetchone()
            if res is None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Antyraid nie był włączony.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
            elif res is not None:
                sql = f"DELETE FROM antyr WHERE guild_id = {ctx.guild.id}"
                cur.execute(sql)
                db.commit()
                await ctx.send("<a:tia:719868701205332012> **`Antyraid wyłączony pomyślnie.`**")
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
    bot.add_cog(Antyraid(bot))
    print("zaladowano Antyraid")

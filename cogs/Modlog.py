import discord
import datetime
import sqlite3
from discord.ext import commands

class Modlog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["mod-log"])
    async def modlog(self, ctx, k:discord.TextChannel=None):
        if ctx.message.author.guild_permissions.manage_guild:
            if k is None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Poprawne użycie: `modlog (kanał)`.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
            elif k is not None:
                db = sqlite3.connect('main.sqlite')
                cur = db.cursor()
                cur.execute(f"SELECT channel_id FROM modlog WHERE guild_id = {ctx.guild.id}")
                res = cur.fetchone()
                if res is None:
                    sql = ("INSERT INTO modlog(channel_id, guild_id) VALUES(?,?)")
                    val = (k.id, ctx.guild.id)
                    cur.execute(sql, val)
                    db.commit()
                    dn = discord.Embed(
                        color=0xabff96,
                        title="**Succes!**",
                        description=f"<a:tia:719868701205332012> **|** *Kanał modlogów został ustawiony na: {k.mention}.*"
                    )
                    dn.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731955375464775790/image0.gif")
                    dn.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                    dn.timestamp=datetime.datetime.utcnow()
                    await ctx.send(embed=dn)
                elif res is not None:
                    er = discord.Embed(
                        color=0xff4545,
                        title="**Error...**",
                        description="<a:nei:719868753214570557> **|** *Modlog jest już ustawiony na tym serwerze, możesz ją wyłączyć komendą `modlog-off`.*"
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

    @modlog.error
    async def modlog_error(self, ctx, error):
        er = discord.Embed(
            color=0xff4545,
            title="**Error...**",
            description="<a:nei:719868753214570557> **|** *Nie znalazłem tego kanału.*"
        )
        er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
        er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        er.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=er)

    @commands.command(aliases=["modlog-off"])
    async def modlogoff(self, ctx):
        if ctx.message.author.guild_permissions.manage_guild:
            db = sqlite3.connect('main.sqlite')
            cur = db.cursor()
            cur.execute(f"SELECT channel_id FROM modlog WHERE guild_id = {ctx.guild.id}")
            res = cur.fetchone()
            if res is None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Modlog nie był ustawiony na tym serwerze.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
            elif res is not None:
                sql = f"DELETE FROM modlog WHERE guild_id = {ctx.guild.id}"
                cur.execute(sql)
                db.commit()
                dn = discord.Embed(
                    color=0xabff96,
                    title="**Succes!**",
                    description=f"<a:tia:719868701205332012> **|** *Modlog został wyłączony.*"
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
    bot.add_cog(Modlog(bot))
    print("zaladowano Modlog")

import discord
import sqlite3
import os
import datetime
from discord.ext import commands

class Prof(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["profil-stwórz", "profil-stworz", "profil-create", "profile-stwórz", "profile-stworz", "profile-create"])
    async def profil_create(self, ctx, use, majl, ig1=None, fb1=None):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT username, mail, ig, fb FROM prof WHERE user_id = {ctx.author.id}")
        res = cursor.fetchone()
        if res is None:
            sql = ("INSERT INTO prof(username, mail, ig, fb, user_id) VALUES(?,?,?,?,?)")
            val = (use, majl, ig1, fb1, ctx.author.id)
            cursor.execute(sql, val)
            db.commit()
            dn = discord.Embed(
                color=0xabff96,
                title="**Succes!**",
                description="<a:tia:719868701205332012> **|** *Pomyślnie `stworzono` twój profil.*"
            )
            dn.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731955375464775790/image0.gif")
            dn.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            dn.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=dn)
        if res is not None:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Masz już profil, możesz usunąć komendą `profile-delete`.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)

    @profil_create.error
    async def profil_create_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Poprawne użycie: `profile-create (username) (mail) [IG] [fb]`*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)

    @commands.command(aliases=["profil-usuń", "profil-usun", "profil-delete", "profile-usuń", "profile-usun", "profile-delete"])
    async def profil_usun(self, ctx):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT username FROM prof WHERE user_id = {ctx.author.id}")
        res = cursor.fetchone()
        if res is None:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *`Nie` masz profilu, więc nie mam co usuwać.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)
        if res is not None:
            sql = f"DELETE FROM prof WHERE user_id = {ctx.author.id}"
            cursor.execute(sql)
            db.commit()
            dn = discord.Embed(
                color=0xabff96,
                title="**Succes!**",
                description="<a:tia:719868701205332012> **|** *Pomyślnie `usunięto` twój profil.*"
            )
            dn.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731955375464775790/image0.gif")
            dn.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            dn.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=dn)

    @commands.command(aliases=["profile"])
    async def profil(self, ctx, k:discord.Member=None):
        if k is None:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT username, mail, ig, fb FROM prof WHERE user_id = {ctx.author.id}")
            res = cursor.fetchone()
            if res is None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *`Nie` masz profilu, aby go stworzyć użyj komendy `profile-create`.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
            elif res is not None:
                use = str(res[0])
                mail = str(res[1])
                ig = str(res[2])
                fb = str(res[3])

                cursor.execute(f"SELECT exp, lvl FROM levels WHERE user_id = {ctx.author.id}")
                result1 = cursor.fetchone()

                gl = str(result1[1])
                gxp = str(result1[0])

                cursor.execute(f"SELECT odznaka FROM odz WHERE user_id = {ctx.author.id}")
                res123 = cursor.fetchone()
                if res123 is None:
                    profil = discord.Embed(
                        color = ctx.author.color,
                        description = f"**Ogólne info:**\n\n> Username: `{use}`\n> Mail: `{mail}`\n> Instagram: `{ig}`\n> Facebook: `{fb}`\n\n**Statystyki:**\n\n> Globalny level: `{gl}`\n> Globalny exp: `{gxp}`\n\n**Odznaki:**\n\n<a:thebest:719278648930205761> - Użytkownik Bota"
                    )
                    profil.set_author(name=f"Profile: {ctx.author}", icon_url=ctx.author.avatar_url)
                    profil.set_thumbnail(url=ctx.author.avatar_url)
                    profil.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                    profil.timestamp=datetime.datetime.utcnow()
                    await ctx.send(embed=profil)
                elif res123 is not None:
                    odz = str(res123[0])
                    profil = discord.Embed(
                        color = ctx.author.color,
                        description = f"**Ogólne info:**\n\n> Username: `{use}`\n> Mail: `{mail}`\n> Instagram: `{ig}`\n> Facebook: `{fb}`\n\n**Statystyki:**\n\n> Globalny level: `{gl}`\n> Globalny exp: `{gxp}`\n\n**Odznaki:**\n\n{odz}\n <a:thebest:719278648930205761> - Użytkownik Bota\n"
                    )
                    profil.set_author(name=f"Profile: {ctx.author}", icon_url=ctx.author.avatar_url)
                    profil.set_thumbnail(url=ctx.author.avatar_url)
                    profil.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                    profil.timestamp=datetime.datetime.utcnow()
                    await ctx.send(embed=profil)
        elif k is not None:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT username, mail, ig, fb FROM prof WHERE user_id = {k.id}")
            res = cursor.fetchone()
            if res is None:
                er = discord.Embed(
                    color=0xff4545,
                    title="**Error...**",
                    description="<a:nei:719868753214570557> **|** *Ten użytkownik `Nie` ma profilu, aby go stworzyć niech użyje komendy `profile-create`.*"
                )
                er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
                er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                er.timestamp=datetime.datetime.utcnow()
                await ctx.send(embed=er)
            elif res is not None:
                use = str(res[0])
                mail = str(res[1])
                ig = str(res[2])
                fb = str(res[3])

                cursor.execute(f"SELECT exp, lvl FROM levels WHERE user_id = {k.id}")
                result1 = cursor.fetchone()

                gl = str(result1[1])
                gxp = str(result1[0])

                cursor.execute(f"SELECT odznaka FROM odz WHERE user_id = {k.id}")
                res123 = cursor.fetchone()
                if res123 is None:
                    profil = discord.Embed(
                        color = ctx.author.color,
                        description = f"**Ogólne info:**\n\n> Username: `{use}`\n> Mail: `{mail}`\n> Instagram: `{ig}`\n> Facebook: `{fb}`\n\n**Statystyki:**\n\n> Globalny level: `{gl}`\n> Globalny exp: `{gxp}`\n\n**Odznaki:**\n\n<a:thebest:719278648930205761> - Użytkownik Bota"
                    )
                    profil.set_author(name=f"Profile: {k}", icon_url=k.avatar_url)
                    profil.set_thumbnail(url=k.avatar_url)
                    profil.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                    profil.timestamp=datetime.datetime.utcnow()
                    await ctx.send(embed=profil)
                elif res123 is not None:
                    odz = str(res123[0])

                    profil = discord.Embed(
                        color = ctx.author.color,
                        description = f"**Ogólne info:**\n\n> Username: `{use}`\n> Mail: `{mail}`\n> Instagram: `{ig}`\n> Facebook: `{fb}`\n\n**Statystyki:**\n\n> Globalny level: `{gl}`\n> Globalny exp: `{gxp}`\n\n**Odznaki:**\n\n{odz}\n <a:thebest:719278648930205761> - Użytkownik Bota\n"
                    )
                    profil.set_author(name=f"Profile: {k}", icon_url=k.avatar_url)
                    profil.set_thumbnail(url=k.avatar_url)
                    profil.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
                    profil.timestamp=datetime.datetime.utcnow()
                    await ctx.send(embed=profil)

def setup(bot):
    bot.add_cog(Prof(bot))
    print("zaladowano Prof")

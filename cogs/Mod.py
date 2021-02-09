import discord
import datetime
import sqlite3
import asyncio
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, osoba: discord.Member=None, *, powod='Brak'):
        if not osoba:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Poprawne użycie: `kick (osoba) [powód]`*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)
            return

        if osoba == ctx.author:
            await ctx.send('Nie możesz wywalić **siebie**!')

        if ctx.message.author.guild_permissions.kick_members:
            await osoba.kick(reason=powod)
            kkk = discord.Embed(
                color=0xfc5603,
                title="**Szczegóły Kicku:**",
                description=f"<:kick:723882528452378624> {osoba.mention} *został wyrzucony!!*\n\n> **Z serwera: `{ctx.guild}`**\n\n> **Powód: `{powod}`**"
            )
            kkk.set_thumbnail(url=osoba.avatar_url)
            kkk.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            kkk.timestamp = datetime.datetime.utcnow()
            db = sqlite3.connect('main.sqlite')
            cur = db.cursor()
            cur.execute(f"SELECT channel_id FROM modlog WHERE guild_id = {ctx.guild.id}")
            res = cur.fetchone()
            if res is None:
                await ctx.send(embed=kkk)
            elif res is not None:
                jnt = int(res[0])
                yhym = self.bot.get_channel(id=jnt)
                await yhym.send(embed=kkk)
                await ctx.send(f"<a:tia:719868701205332012> **`Szczegóły Kicku:`** <#{jnt}>.")
            try:
                await osoba.send(embed=kkk)
            except:
                return
        else:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Nie masz wystarczających uprawnień.\nWymagane: `KICK MEMBERS`.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)

    @kick.error
    async def kick_error(self, ctx, error):
        er = discord.Embed(
            color=0xff4545,
            title="**Error...**",
            description="<a:nei:719868753214570557> **|** *Nie mam uprawnień lub nie mogę znaleźć tego użytkownika.\nUpewnij się że jestem wyżej niż ten członek.*"
        )
        er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
        er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        er.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=er)


    @commands.command()
    async def ban(self, ctx, osoba: discord.Member=None, *, powod='Brak'):
        if not osoba:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Poprawne użycie: `ban (osoba) [powód]`*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)
            return

        if osoba == ctx.author:
            await ctx.send('Nie możesz zbanować **siebie**!')

        if ctx.message.author.guild_permissions.ban_members:
            await osoba.ban(reason=powod)
            kkk = discord.Embed(
                color=0xff4545,
                title="**Szczegóły Bana:**",
                description=f"<:ban:723881510054395990> {osoba.mention} *został zbanowany!!*\n\n> **Z serwera: `{ctx.guild}`**\n\n> **Powód: `{powod}`**"
            )
            kkk.set_thumbnail(url=osoba.avatar_url)
            kkk.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            kkk.timestamp = datetime.datetime.utcnow()
            db = sqlite3.connect('main.sqlite')
            cur = db.cursor()
            cur.execute(f"SELECT channel_id FROM modlog WHERE guild_id = {ctx.guild.id}")
            res = cur.fetchone()
            if res is None:
                await ctx.send(embed=kkk)
            elif res is not None:
                jnt = int(res[0])
                yhym = self.bot.get_channel(id=jnt)
                await yhym.send(embed=kkk)
                await ctx.send(f"<a:tia:719868701205332012> **`Szczegóły Ban:`** <#{jnt}>.")
            try:
                await osoba.send(embed=kkk)
            except:
                return
        else:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Nie masz wystarczających uprawnień.\nWymagane: `BAN MEMBERS`.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)

    @ban.error
    async def ban_error(self, ctx, error):
        er = discord.Embed(
            color=0xff4545,
            title="**Error...**",
            description="<a:nei:719868753214570557> **|** *Nie mam uprawnień lub nie mogę znaleźć tego użytkownika.\nUpewnij się że jestem wyżej niż ten członek.*"
        )
        er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
        er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        er.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=er)

    @commands.command(aliases=["purge", "czyść", "kasuj"])
    async def clear(self, ctx, amount:int):
        if ctx.message.author.guild_permissions.manage_messages:
            all = amount + 1
            await ctx.channel.purge(limit=all)
            ok = discord.Embed(
                color=0xfcba03,
                title="**Czyszczenie chatu ...**",
                description=f"<a:tia:719868701205332012> `SUKCES!` wyczyszczono `{amount}` wiadomości."
            )
            ok.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            ok.timestamp = datetime.datetime.utcnow()
            msg = await ctx.send(embed=ok)
            await asyncio.sleep(1)
            await msg.add_reaction("🕛")
            await asyncio.sleep(1)
            await msg.add_reaction("🕒")
            await asyncio.sleep(1)
            await msg.add_reaction("🕕")
            await asyncio.sleep(1)
            await msg.add_reaction("🕘")
            await asyncio.sleep(1)
            await msg.add_reaction("👋")
            await asyncio.sleep(1)
            return await msg.delete()
        else:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Nie masz wystarczających uprawnień.\nWymagane: `MANAGE MESSAGES`.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Poprawne użycie: `clear (ilość)*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)

def setup(bot):
    bot.add_cog(Mod(bot))
    print("zaladowano Mod")

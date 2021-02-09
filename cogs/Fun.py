import discord
import os
import time
import requests
import random
import inspect
import datetime
import sqlite3
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["cat"])
    async def kot(self, ctx):
        zdj = requests.get("https://some-random-api.ml/img/cat").json()["link"]
        e = discord.Embed(
            title = "**Twój Kotecek!**",
            description="<:smile:719414224698474566> *Słodziaczek, UwU*",
            color = 0x9ef2ff
        )
        e.set_image(url=zdj)
        e.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        e.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=e)

    @commands.command()
    async def panda(self, ctx):
        zdj = requests.get("https://some-random-api.ml/img/panda").json()["link"]
        e = discord.Embed(
            title = "**Twoja Panda!**",
            description="<:PandaLove:729444681553019071> *Słodki, prawda? OwO*",
            color = 0xe7ff5c
        )
        e.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        e.timestamp=datetime.datetime.utcnow()
        e.set_image(url=zdj)
        await ctx.send(embed=e)

    @commands.command(aliases=['dog'])
    async def pies(self, ctx):
        zdj = requests.get("https://some-random-api.ml/img/dog").json()["link"]
        e = discord.Embed(
            title = "**Twój Piesio!**",
            description="<:doggie:687285940506722327> *Słodziak, co nie? TwT*",
            color = 0xabffca
        )
        e.set_image(url=zdj)
        e.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        e.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=e)

    @commands.command(aliases=['fox'])
    async def lis(self, ctx):
        zdj = requests.get("https://some-random-api.ml/img/fox").json()["link"]
        e = discord.Embed(
            title = "**Twój Lisio!**",
            description="<:fox4:724319548643213394> *Słodki czy raczej groźny? QwQ*",
            color = 0xffc363
        )
        e.set_image(url=zdj)
        e.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        e.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=e)

    @commands.command(aliases=["pogłaszcz"])
    async def pat(self, ctx, k:discord.Member=None):
        if k is None:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Podaj osobę którą chcesz pogłaskać.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)
        elif k.id == ctx.author.id:
            await ctx.send("He? Chcesz pogłaskać **samego siebie**?")
        elif k is not None:
            zdj = requests.get("https://some-random-api.ml/animu/pat").json()["link"]
            e = discord.Embed(
                color = 0x9500ff
            )
            e.set_author(name=f"{ctx.author} pogłaskał/a {k}", icon_url=ctx.author.avatar_url)
            e.set_image(url=zdj)
            e.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=e)

    @commands.command(aliases=["przytul"])
    async def hug(self, ctx, k:discord.Member=None):
        if k is None:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Podaj osobę którą chcesz przytulić.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)
        elif k.id == ctx.author.id:
            await ctx.send("C O? Chcesz przytulić **samego siebie**?")
        elif k is not None:
            zdj = requests.get("https://some-random-api.ml/animu/hug").json()["link"]
            e = discord.Embed(
                color = 0x7dffeb
            )
            e.set_author(name=f"{ctx.author} przytulił/a {k}", icon_url=ctx.author.avatar_url)
            e.set_image(url=zdj)
            e.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=e)

    @commands.command(aliases=['pika'])
    async def pikachu(self, ctx):
        zdj = requests.get("https://some-random-api.ml/img/pikachu").json()["link"]
        e = discord.Embed(
            title = "**Pika Pika?**",
            color = 0xffff29
        )
        e.set_image(url=zdj)
        e.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        e.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=e)

    @commands.command(aliases=["heks"])
    async def hex(self, ctx, kolor):
        e = discord.Embed(
            title = f"**Hex #{kolor}**",
            color = discord.Colour.red()
        )
        e.set_image(url=f'https://some-random-api.ml/canvas/colorviewer?hex={kolor}')
        e.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        e.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=e)

    @hex.error
    async def hex_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Zapomniałeś o hexie.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)

    @commands.command(aliases=["uderz"])
    async def slap(self, ctx, k:discord.Member=None):
        if k is None:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Podaj osobę którą chcesz uderzyć.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)
        elif k.id == ctx.author.id:
            await ctx.send("Hm? Czy napewno chcesz uderzyć **samego siebie**?")
        elif k is not None:
            zdj = requests.get("http://api.nekos.fun:8080/api/slap").json()["image"]
            e = discord.Embed(
                color = 0xff6542
            )
            e.set_author(name=f"{ctx.author} uderzył {k}", icon_url=ctx.author.avatar_url)
            e.set_image(url=zdj)
            e.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=e)

    @commands.command(aliases=["połaskocz"])
    async def tickle(self, ctx, k:discord.Member=None):
        if k is None:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Podaj osobę którą chcesz połaskoczyć.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)
        elif k.id == ctx.author.id:
            await ctx.send("xD? **Samego siebie** będziesz łaskotał?")
        elif k is not None:
            zdj = requests.get("http://api.nekos.fun:8080/api/tickle").json()["image"]
            e = discord.Embed(
                color = 0xa1ffb4
            )
            e.set_author(name=f"{ctx.author} połaskotał/a {k}", icon_url=ctx.author.avatar_url)
            e.set_image(url=zdj)
            e.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=e)

    @commands.command(aliases=["pocałuj"])
    async def kiss(self, ctx, k:discord.Member=None):
        if k is None:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Podaj osobę którą chcesz pocałować.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)
        elif k.id == ctx.author.id:
            await ctx.send("xD? **Samego siebie** będziesz pocałować? lmao.")
        elif k is not None:
            zdj = requests.get("http://api.nekos.fun:8080/api/kiss").json()["image"]
            e = discord.Embed(
                color = 0xff69c3
            )
            e.set_author(name=f"{ctx.author} pocałował/a {k}", icon_url=ctx.author.avatar_url)
            e.set_image(url=zdj)
            e.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=e)

    @commands.command(aliases=["sup"])
    async def supreme(self, ctx, *, y=None):
        if y is None:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Podaj `tekst`, np: `supreme siemka`.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)
        elif y is not None:
            b = y.replace(" ","%20")

            wi = f"https://api.alexflipnote.dev/supreme?text={b}"
            h = discord.Embed(
                title = '**Supreme:**',
                color = 0x00b959
            )
            h.set_image(url=wi)
            h.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            h.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=h)

    @commands.command(aliases=["fakt"])
    async def fact(self, ctx, *, y=None):
        if y is None:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Podaj `tekst`, np: `fact siemka`.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)
        elif y is not None:
            b = y.replace(" ","%20")

            wi = f"https://api.alexflipnote.dev/facts?text={b}"
            h = discord.Embed(
                title = '**Fact:**',
                color = 0x82c3ff
            )
            h.set_image(url=wi)
            h.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            h.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=h)

    @commands.command()
    async def drake(self, ctx, y, k):
        b = y.replace(" ", "%20")
        ccc = k.replace(" ", "%20")
        wi = f"https://api.alexflipnote.dev/drake?top={b}&bottom={ccc}"
        h = discord.Embed(
            title = '**Drake:**',
            color = 0xff8521
        )
        h.set_image(url=wi)
        h.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        h.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=h)

    @drake.error
    async def drake_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Poprawne użycie: `drake (tekst) (tekst)`.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)

    @commands.command(aliases=["ph"])
    async def pornhub(self, ctx, y, k):
        b = y.replace(" ", "%20")
        ccc = k.replace(" ", "%20")
        wi = f"https://api.alexflipnote.dev/pornhub?text={b}&text2={ccc}"
        h = discord.Embed(
            title = '**pornhub:**',
            color = 0x000000
        )
        h.set_image(url=wi)
        h.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        h.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=h)

    @pornhub.error
    async def pornhub_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Poprawne użycie: `pornhub (tekst) (tekst)`.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)

    @commands.command()
    async def dum(self, ctx, y, k):
        b = y.replace(" ", "%20")
        ccc = k.replace(" ", "%20")
        wi = f"https://api.alexflipnote.dev/didyoumean?top={b}&bottom={ccc}"
        h = discord.Embed(
            title = '**Did you mean:**',
            color = 0x000000
        )
        h.set_image(url=wi)
        h.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        h.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=h)

    @dum.error
    async def dum_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Poprawne użycie: `dum (tekst) (tekst)`.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)

    @commands.command(aliases=["achv"])
    async def achievement(self, ctx, *, y=None):
        if y is None:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Podaj `tekst`, np: `achievement siemka`.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)
        elif y is not None:
            b = y.replace(" ","%20")

            wi = f"https://api.alexflipnote.dev/achievement?text={b}"
            h = discord.Embed(
                title = '**Achievement:**',
                color = 0xa8a8a8
            )
            h.set_image(url=wi)
            h.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            h.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=h)

    @commands.command(aliases=["ugryź"])
    async def bite(self, ctx, k:discord.Member=None):
        if k is None:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Podaj osobę którą chcesz ugryźć.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)
        elif k.id == ctx.author.id:
            await ctx.send("xD? **Samego siebie** będziesz gryzł?")
        elif k is not None:
            zdj = requests.get("https://some-random-api.ml/animu/bite").json()["link"]
            e = discord.Embed(
                color = 0xe6e6e6
            )
            e.set_author(name=f"{ctx.author} ugryzł/a {k}", icon_url=ctx.author.avatar_url)
            e.set_image(url=zdj)
            e.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=e)

    @commands.command()
    async def skin(self, ctx, *, skin=None):
        if skin is None:
            er = discord.Embed(
                color=0xff4545,
                title="**Error...**",
                description="<a:nei:719868753214570557> **|** *Podaj nick osoby z mc.*"
            )
            er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
            er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            er.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=er)
        elif skin is not None:
            e = discord.Embed(
                title = f"**Skin W Mc Gracza: {skin}**",
                color = 0xf5ff66
            )
            e.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            e.timestamp=datetime.datetime.utcnow()
            e.set_image(url=f'https://minecraftskinstealer.com/api/v1/skin/render/fullbody/{skin}')
            await ctx.send(embed=e)

    @commands.command(aliases=["mem"])
    async def meme(self, ctx):
        zdj = requests.get("https://some-random-api.ml/meme").json()["image"]
        napis = requests.get("https://some-random-api.ml/meme").json()["caption"]
        e = discord.Embed(
            color = 0xb0ffd9,
            title= f"**{napis}**"
        )
        e.set_image(url=zdj)
        e.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        e.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=e)

    @commands.command()
    async def nosacz(self, ctx):
        zdj = requests.get("http://servicesedward.tk:2095/api/nosacz").json()["image"]
        e = discord.Embed(
            title = f"**Hue Hue Nosacz:**",
            color = discord.Colour.green()
        )
        e.set_image(url=zdj)
        e.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        e.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=e)

    @commands.command(aliases=["awatar", "avek", "awek"])
    async def avatar(self, ctx, *, k: discord.Member = None):
        if k is None:
            ok = discord.Embed(
                title=f"{ctx.author}:",
                color=discord.Color.red()
            )
            ok.set_image(url=ctx.author.avatar_url)
            ok.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            ok.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=ok)
        elif k is not None:
            ok = discord.Embed(
                title=f"{k}:",
                color=discord.Color.red()
            )
            ok.set_image(url=k.avatar_url)
            ok.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            ok.timestamp=datetime.datetime.utcnow()
            await ctx.send(embed=ok)

def setup(bot):
    bot.add_cog(Fun(bot))
    print("zaladowano Fun")

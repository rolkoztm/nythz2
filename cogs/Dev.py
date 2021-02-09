import discord
import os
import time
import inspect
import datetime
import sqlite3
from discord.ext import commands

start_time = time.time()

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ping", "users", "uptime", "guilds", "guild", "p", "g", "u"])
    @commands.is_owner()
    async def guildy(self, ctx):
        ok = len(self.bot.guilds)
        g = len(self.bot.users)
        nope = round(self.bot.latency*1000)

        member = ctx.author

        current_time = time.time()

        difference = int(round(current_time - start_time))

        text = str(datetime.timedelta(seconds=difference))

        ok = discord.Embed(
            color=0x070000,
            title="Dev Info",
            description=f"Serwery: `{ok}`\nUżytk: `{g}`\nPing: `{nope}`\nUptime: `{text}`"
        )
        try:
            await ctx.send(embed=ok)
        except discord.HTTPException:
            await member.send("uptime: " + text)

    @commands.command(aliases=["status1"])
    @commands.is_owner()
    async def presence1(self, ctx, *, okk):
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=f"{okk}"))
        await ctx.send("Już dzbanie")

    @commands.command(aliases=["status2"])
    @commands.is_owner()
    async def presence2(self, ctx, *, okk):
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{okk}"))
        await ctx.send("Już dzbanie")

    @commands.command(aliases=["status3"])
    @commands.is_owner()
    async def presence3(self, ctx, *, okk):
        await self.bot.change_presence(activity=discord.Activity(type=1, name=f'{okk}', url='https://twitch.tv/twitch'))
        await ctx.send("Już dzbanie")

    @commands.command(aliases=["add-badges"])
    @commands.is_owner()
    async def add_badges(self, ctx, k:discord.Member, *, ok):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT odznaka FROM odz WHERE user_id = {k.id}")
        res = cursor.fetchone()
        if res is None:
            sql = ("INSERT INTO odz(odznaka, user_id) VALUES(?,?)")
            val = (ok, k.id)
            cursor.execute(sql, val)
            db.commit()
            await ctx.send("Nadano odznake")
        elif res is not None:
            sql1 = ("UPDATE odz SET odznaka = ? WHERE user_id = ?")
            val1 = (ok, k.id)
            cursor.execute(sql1, val1)
            db.commit()
            await ctx.send("Dodano odznake")

    @commands.command(aliases=["remove-badges"])
    @commands.is_owner()
    async def remove_badges(self, ctx, k:discord.Member):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT odznaka FROM odz WHERE user_id = {k.id}")
        res = cursor.fetchone()
        if res is None:
            await ctx.send("ta osoba nie ma odznak wiec co mam usunac")
        elif res is not None:
            sql1 = f"DELETE FROM odz WHERE user_id = {k.id}"
            cursor.execute(sql1)
            db.commit()
            await ctx.send("usunieto odznaki")

    @commands.command()
    @commands.is_owner()
    async def hdprofile(self, ctx, id=None):
        if id is None:
            await ctx.send("podaj id")
        elif id is not None:
            db = sqlite3.connect('main.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT username FROM prof WHERE user_id = {id}")
            res = cursor.fetchone()
            if res is None:
                await ctx.send("ta osoba nie ma profilu bruhh")
            elif res is not None:
                sql = f"DELETE FROM prof WHERE user_id = {id}"
                cursor.execute(sql)
                db.commit()
                await ctx.send("DONE")

def setup(bot):
    bot.add_cog(Dev(bot))
    print("zaladowano Dev")

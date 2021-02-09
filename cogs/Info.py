import discord
import os
import datetime
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["osoba-info", "user-info", "whois", "osoba", "ui"])
    async def user(self, ctx, k:discord.Member=None):
        if k is None:
            roles = [role for role in ctx.author.roles]
            ok = discord.Embed(
                color = ctx.author.color,
                title = "**User Info**",
                description = f"*Info na temat użytkownika:* **{ctx.author}**"
            )
            ok.add_field(name="**ID:**", value=f"`{ctx.author.id}`", inline=False)
            ok.add_field(name="**Link do pobrania awataru:**", value=f"**[`Kliknij tu`]({ctx.author.avatar_url})**", inline=False)
            ok.add_field(name="**Data utworzenia konta:**", value="`" + ctx.author.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC") + "`", inline=False)
            ok.add_field(name="**Data dołączenia na serwer:**", value="`" + ctx.author.joined_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC") + "`", inline=False)
            ok.add_field(name="**Liczba Ról:**", value=f"`{len(roles)}`", inline=False)
            ok.add_field(name="**Najwyższa Rola:**", value=ctx.author.top_role.mention, inline=False)
            ok.add_field(name="**Czy to bot:**", value=f"`{ctx.author.bot}`", inline=False)
            ok.set_thumbnail(url=ctx.author.avatar_url)
            ok.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            ok.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=ok)
        else:
            roles = [role for role in k.roles]
            ok = discord.Embed(
                color = k.color,
                title = "**User Info**",
                description = f"*Info na temat użytkownika:* **{k}**"
            )
            ok.add_field(name="**ID:**", value=f"`{k.id}`", inline=False)
            ok.add_field(name="**Link do pobrania awataru:**", value=f"**[`Kliknij tu`]({k.avatar_url})**", inline=False)
            ok.add_field(name="**Data utworzenia konta:**", value="`" + k.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC") + "`", inline=False)
            ok.add_field(name="**Data dołączenia na serwer:**", value="`" + k.joined_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC") + "`", inline=False)
            ok.add_field(name="**Liczba Ról:**", value=f"`{len(roles)}`", inline=False)
            ok.add_field(name="**Najwyższa Rola:**", value=k.top_role.mention, inline=False)
            ok.add_field(name="**Czy to bot:**", value=f"`{k.bot}`", inline=False)
            ok.set_thumbnail(url=k.avatar_url)
            ok.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
            ok.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=ok)

    @user.error
    async def user_error(self, ctx, error):
        er = discord.Embed(
            color=0xff4545,
            title="**Error...**",
            description="<a:nei:719868753214570557> **|** *Nie znalazłem tego użytkownika.*"
        )
        er.set_thumbnail(url="https://cdn.discordapp.com/attachments/730775180590186556/731941086649385100/image0.gif")
        er.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        er.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=er)

    @commands.command(aliases=["serwer", "server-info", "serwer-info"])
    async def server(self, ctx):
        embed=discord.Embed(title=f"**Serwer: `{ctx.author.guild.name}`**", description="[dodaj bota](https://discord.com/api/oauth2/authorize?client_id=723210798146781230&permissions=8&scope=bot) | [support serwer](https://discord.gg/ntPMThU)",color=0xfffff)
        embed.add_field(name="**Serwer ID:**", value=f"`{ctx.author.guild.id}`", inline=False)
        embed.add_field(name="**Liczba osób na serwerze:**", value=f"`{len(list(ctx.guild.members))}`", inline=False)
        embed.add_field(name="**Serwer stworzony dnia:**", value="`" + ctx.guild.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC") + "`", inline=False)
        embed.add_field(name="**Liczba ról na serwerze:**", value=f"`{len(ctx.guild.roles)}`", inline=False)
        embed.add_field(name="**Liczba emotek na serwerze:**", value=f"`{len(ctx.guild.emojis)}`", inline=False)
        embed.add_field(name="**Liczba kanałów tekstowych na serwerze:**", value=f"`{len(ctx.guild.text_channels)}`", inline=False)
        embed.add_field(name="**Liczba kanałów głosowych na serwerze:**", value=f"`{len(ctx.guild.voice_channels)}`", inline=False)
        embed.add_field(name="**Region serwera:**", value=f"`{ctx.guild.region}`", inline=False)
        embed.add_field(name="**Własciciel serwera:**", value=f"{ctx.guild.owner.mention}", inline=False)
        embed.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)

    @commands.command(aliases=["dodaj"])
    async def add(self, ctx):
        ok = discord.Embed(
            color=0x85ff99,
            description="> **`Dodaj bota:`** [Klik](https://discord.com/api/oauth2/authorize?client_id=723210798146781230&permissions=8&scope=bot)\n \n> **`Support serwer:`** [Klik](https://discord.gg/Se2bqM4)"
        )
        ok.set_footer(text=f"{ctx.message.author}  •  ({ctx.author.id})", icon_url=ctx.message.author.avatar_url)
        ok.set_author(name=f"Główny Programista: !  HypereK#9999", icon_url="https://cdn.discordapp.com/avatars/498497705388146709/a_1e8a9bef2a1df1e2b73bb0b8d93ebe6a.gif?size=1024")
        ok.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=ok)

def setup(bot):
    bot.add_cog(Info(bot))
    print("zaladowano Info")

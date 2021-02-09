import discord
import os
import datetime
import inspect
import sqlite3
import jishaku
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["jak", "help"])
    async def pomoc(self, ctx):
        n = discord.Embed(
            title="**Nythz Pomoc:**",
            description="Wersja bota: 2.1.1 || W razie problemów [skontaktuj się z nami](https://discord.gg/Se2bqM4).\n\n**Informacyjne:**\n `user-info` `serwer-info` `add` `warny`\n\n**Moderacyjne:**\n`ban` `kick` `warn` `clear-warns` `modlog` `modlog-off`\n\n**Powitanie/Pożegnanie:**\n`pow-kanał` `pow-text` `pow-off` `poż-kanał` `poż-text` `poż-off`\n\n**Fun:**\n`drake` `achievement` `avatar` `dum` `fakt` `hex` `hug` `kiss` `kot` `lis` `meme` `nosacz` `panda` `pat` `pies` `pikachu` `pornhub` `skin` `slap` `supreme` `tickle`\n\n**Profile:**\n`profile-create` `profile` `profile-delete`\n\n**Glevel:**\n`glvl-off` `glvl-on`\n\n**Logi:**\n`logs` `logs-off`\n\n**Administracyjne:**\n`auto-role` `auto-role-off` `automod` `automod-off` `antyraid` `antyraid-off`",
            color=0x91e084
        )
        n.set_thumbnail(url="https://cdn.discordapp.com/icons/726371578811645972/a_164dba0222544c0c794dfbe0b03da9e4.gif?size=1024")
        n.set_footer(text=f"() - Wymagane | [] - Opcjonalne", icon_url=ctx.message.author.avatar_url)
        n.timestamp=datetime.datetime.utcnow()
        await ctx.send(embed=n)

def setup(bot):
    bot.add_cog(Help(bot))
    print("zaladowano Help")

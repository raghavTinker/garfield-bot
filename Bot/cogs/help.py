import discord
from discord.ext import commands
import os
from database import SessionLocal, engine
import models

db = SessionLocal()
try:
    PREFIX = os.environ["PREFIX"]
except:
    PREFIX = "*"

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name="help", aliases=["h"])
    async def help(self, ctx, *args):
        """Give commands list"""
        # check if guild is present
        client = db.query(models.Clients).filter(models.Clients.guild_id == ctx.guild.id).first()
        if not client:
            # embed send
            embed = discord.Embed(
                description="You are not registered, please run `" + PREFIX + "setup` first",
                title="",
                color=discord.Color.red(),
            )
            await ctx.send(embed=embed)
            return
        
        
        prefix = client.prefix
        commands = {f"```{prefix}random```": "Displays a random xkcd comic",
                    f"```{prefix}setup ```": "To update the channel in which bot sends message",
                    f"```{prefix}prefix```": "Change the prefix of the bot"}
        embed = discord.Embed(title="List of commands:", description="These are the commands to use with this bot", color=discord.Color.green())
        count = 1
        for command in commands:
                embed.add_field(name=str(count)+". "+ command, value=commands[command], inline=False)
                count += 1
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
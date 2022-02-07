import discord
from discord.ext import commands , tasks
from database import SessionLocal, engine
import models
import random
db = SessionLocal()

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def random(self, ctx):
        # get all the comics
        comics = db.query(models.Comic).all()
        # get a random comic
        comic = random.choice(comics)
        # get the comic url
        url = comic.url
        # get the comic title
        title = comic.title
        # get the comic date
        date = comic.date
        # create an embed
        embed = discord.Embed(title=title, description=date, color=0x00ff00)
        embed.set_image(url=url)
        # send the embed
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Random(bot))
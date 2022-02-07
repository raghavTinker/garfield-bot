import os
import discord
from discord.ext import commands , tasks
import asyncio
import requests
import random
import datetime
from database import SessionLocal, engine
import models
from functionality.getComic import *

db = SessionLocal()

class Periodic(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.last_sent_comic = None
        task = self.sendComic.start()
    
    @tasks.loop(hours=24)
    async def sendComic(self):
        comic = todayComic()
        # get date for today day/month/year
        #print(comic[2])
        if(comic[1] != self.last_sent_comic):
            # create a comic in the database
            if db.query(models.Comic).filter(models.Comic.url == comic[1]).first() is None:
                comic_db = models.Comic(comic[0], comic[1], comic[2])
                db.add(comic_db)
                db.commit()

                self.last_sent_comic = comic[1]
                embed = discord.Embed(title=comic[0], description=comic[2], color=0x00ff00)
                embed.set_image(url=comic[1])
                clients = db.query(models.Clients).all()
                for client in clients:
                    # get guild from guild id
                    print(client.guild_id)
                    try:
                        guild = await self.bot.fetch_guild(client.guild_id)
                    except:
                        continue
                    # send message to channel id
                    try:
                        # send to channel
                        channel = await self.bot.fetch_channel(client.channel)
                        await channel.send(embed=embed)
                    except:
                        print("Couldn't send to channel")
                        continue
            else:
                print("Already in database")
def setup(bot):
    bot.add_cog(Periodic(bot))

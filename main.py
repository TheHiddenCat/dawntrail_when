import re

import settings

from datetime import datetime

from discord import Intents
from discord.client import Client
from discord.message import Message


intents = Intents.default()
intents.message_content = True

client = Client(intents=intents)
release_date = datetime(2024, 9, 21, 23, 59, 59)
pattern = re.compile("dawntrail\swhen\??")


@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return
    
    if pattern.match(message.content.lower()):
        delta = release_date - datetime.now()
        mention = f"<@{message.author.id}>"

        if delta.seconds > 0:
            days = delta.days
            seconds = delta.seconds
            hours = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60

            response = f"{mention} Approximately {days} days, {hours} hours, {minutes} minutes and {seconds} seconds remaining ⛵"
        else: 
            response = f"{mention} Dawntrail should be released! 🏖️"

        await message.channel.send(response)


client.run(settings.TOKEN)
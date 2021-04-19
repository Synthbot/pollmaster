import discord
from discord import *


async def generate_poll(message: discord.Message):
    if verify(message):
        print("Verified")

        proposal :discord.Message = await message.channel.fetch_message(message.reference.message_id) #Proposal is the message replied to
        print(proposal.content)


def verify(message: discord.Message) -> bool:
    print("Message has a reference:", isinstance(message.reference, MessageReference))
    return message.content.lower() == "seconded" and isinstance(message.reference, MessageReference)


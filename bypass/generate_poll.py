from datetime import datetime, timedelta

import discord
import pytz
from discord import *
from discord.ext.commands import Context

from models.poll import Poll


async def generate_poll(message: discord.Message, bot):
    if verify_second(message):
        print("Verified")

        proposal: discord.Message = await message.channel.fetch_message(message.reference.message_id)  # Proposal is the message replied to
        ctx: Context = await bot.get_context(message)

        # naively make a poll
        poll = Poll(bot, ctx, channel=proposal.channel)
        poll.name = "This is a test poll"
        poll.short = "poll1"
        poll.anonymous = False
        poll.options_reaction = Poll.get_preset_options(2)
        # poll.survey_flags(ctx, force='0')
        poll.multiple_choice = 1
        poll.hide_vote_count = 0
        poll.roles = ['@everyone']  # This lets everyone vote
        poll.weights = 0
        poll.activation = datetime.utcnow()
        poll.duration = datetime.utcnow() + timedelta(hours=1)

        await poll.post_embed(poll.channel)

        # So this naive implementation sorta works. it opens a poll, but beyond that it is broken
        # If you remove a reaction on the poll, the poll instantly closes (probably weird stuff from converting UTC to
        # local time, see poll.is_open() on line 104 of models/poll.py)
        # Spits out an error when you react to the poll: 'NoneType' object has no attribute 'roles'
        #   This issue seems to be with line 825 of poll_controls returning None rather than the member



def verify_second(message: discord.Message) -> bool:
    print("Message has a reference:", isinstance(message.reference, MessageReference))
    return message.content.lower() == "seconded" and isinstance(message.reference, MessageReference) #Probably should rework this with a regex at some point


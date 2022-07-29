
import pytest
import discord.ext.test as test


@pytest.mark.asyncio
async def test_edit(bot):
    guild = bot.guilds[0]
    channel = guild.channels[0]

    mes_o = await channel.send("Test Message")
    mes_e = await mes_o.edit(content="New Message")

    assert mes_o.content == "Test Message"
    assert mes_e.content == "New Message"

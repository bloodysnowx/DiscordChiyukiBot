import discord
import factorio_client
import minecraft_client
import common_client
import os
import random


discord_client = discord.Client()
factorio_client = factorio_client.FactorioClient()
minecraft_client = minecraft_client.MinecraftClient()
common_client = common_client.CommonClient()

async def process_start(client, channel):
    if client.exists == False:
        await channel.send(client.container_name + ' does not exist.')
    elif client.is_running:
        await channel.send(client.container_name + ' is already running.')
    else:    
        client.start()
        await channel.send(client.container_name + ' was started.')

async def process_stop(client, channel):
    if client.exists == False:
        await channel.send(client.container_name + ' does not exist.')
    elif client.is_running == False:
        await channel.send(client.container_name + ' is not running.')
    else:
        client.stop()
        await channel.send(client.container_name + ' was stopped.')

async def process_run(client, channel):
    if client.exists:
        await channel.send(client.container_name + ' already exists.')
    else:
        client.run()
        await channel.send('new ' + client.container_name + ' image was started.')

async def process_update(client, channel):
    if client.exists:
        if client.is_running:
            client.stop()
            await channel.send(client.container_name + ' was stopped.')
        client.remove()
        await channel.send(client.container_name + ' removed.')
    client.update()
    await channel.send('new ' + client.container_name + ' image was pulled.')
    client.run()
    await channel.send('new ' + client.container_name + ' image was started.')

@discord_client.event
async def on_ready():
    print('login successed')

@discord_client.event
async def on_message(message):
    if message.author.bot:
        return

    emojis = message.guild.emojis

    if message.content.startswith('https://www.boomplayer.com/') or message.content.startswith('https://gyazo.com/') or len(message.attachments) > 0:
        await message.add_reaction(random.choice(emojis))
        return

    commands = message.content.split(' ')

    if commands[0] == '/factorio' and len(commands) >= 2:
        if commands[1] == 'start':
            await process_start(factorio_client, message.channel)
        elif commands[1] == 'stop':
            await process_stop(factorio_client, message.channel)
        elif commands[1] == 'update':
            await process_update(factorio_client, message.channel)
        elif commands[1] == 'run':
            await process_run(factorio_client, message.channel)    

    if commands[0] == '/minecraft' and len(commands) >= 2:
        if commands[1] == 'start':
            await process_start(minecraft_client, message.channel)
        elif commands[1] == 'stop':
            await process_stop(minecraft_client, message.channel)
        elif commands[1] == 'update':
            await process_update(minecraft_client, message.channel)
        elif commands[1] == 'run':
            await process_run(minecraft_client, message.channel)

    if commands[0] == '/bot' and len(commands) >= 2:
        if commands[1] == 'host':
            await message.channel.send(common_client.hostname)
        elif commands[1] == 'ip':
            await message.channel.send(common_client.ipaddr)
        else:
            await message.channel.send(
                '/bot host - show server hostname\n' \
                '/bot ip - show server ip address\n' \
                '/factorio start - resume factorio server\n' \
                '/factorio stop - stop factorio server\n' \
                '/factorio update - update factorio server\n' \
                '/factorio run - start factorio server with new image\n' \
                '/minecraft start - resume minecraft server\n' \
                '/minecraft stop - stop minecraft server\n' \
                '/minecraft update - update minecraft server\n' \
                '/minecraft run - start minecraft server with new image\n' \
            )


discord_client.run(os.environ['DISCORD_TOKEN'])
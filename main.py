import discord
import factorio_client
import common_client
import os
import random


discord_client = discord.Client()
factorio_client = factorio_client.FactorioClient()
common_client = common_client.CommonClient()

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
            if factorio_client.exists == False:
                await message.channel.send('factorio does not exist.')
            elif factorio_client.is_running:
                await message.channel.send('factorio is already running.')
            else:    
                factorio_client.start()
                await message.channel.send('factorio was started.')
        elif commands[1] == 'stop':
            if factorio_client.exists == False:
                await message.channel.send('factorio does not exist.')
            elif factorio_client.is_running == False:
                await message.channel.send('factorio is not running.')
            else:
                factorio_client.stop()
                await message.channel.send('factorio was stopped.')
        elif commands[1] == 'update':
            if factorio_client.exists:
                if factorio_client.is_running:
                    factorio_client.stop()
                    await message.channel.send('factorio was stopped.')
                factorio_client.remove()
                await message.channel.send('factorio removed.')
            factorio_client.update()
            await message.channel.send('new factorio image was pulled.')
            factorio_client.run()
            await message.channel.send('new factorio image was started.')
        elif commands[1] == 'run':
            if factorio_client.exists:
                await message.channel.send('factorio already exists.')
            else:
                factorio_client.run()
                await message.channel.send('new factorio image was started.')

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
                '/minecraft start - resume minecraft server(unimplemented feature)\n' \
                '/minecraft stop - stop minecraft server(unimplemented feature)\n' 
            )


discord_client.run(os.environ['DISCORD_TOKEN'])
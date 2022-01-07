from discord.ext import commands
import discord
import asyncio
import logging
import random
import os
logging.basicConfig(level=logging.WARNING)

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

startup_extensions = ["maths", "games", "rrstats"]

bot = commands.AutoShardedBot(command_prefix='?', description=description)

def is_owner():
    async def predicate(ctx):
        return ctx.author.id == 307168824887869440
    return commands.check(predicate)

@bot.event
async def on_ready():
    print('Logged in as {} with ID: {}'.format(bot.user.name, bot.user.id))
    print("Command prefix: {}".format(bot.command_prefix))
    status_list = ["with the API.",
                   "<insert game here>",
                   "with my enormous brain."]
    # Status will only update after a while.
    status_chosen = status_list[random.randint(0, (len(status_list)-1))]
    game = discord.Game(name=status_chosen, type=1)
    print("Status: {}".format(status_chosen))
    await bot.change_presence(status=discord.Status.invisible, game=game)
    await asyncio.sleep(40)
    await bot.change_presence(status=discord.Status.online, game=game)


@bot.command(hidden=True)
@is_owner()
async def load(ctx, extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension("Discord.Extensions."+extension_name)
        bot.active_extensions.append(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("Loaded: {}".format("Discord.Extensions."+extension_name))

@bot.command(hidden=True)
@is_owner()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    bot.unload_extension("Extensions."+extension_name)
    print(bot.active_extensions)
    bot.active_extensions.remove(extension_name)
    await ctx.send("Unloaded: {}.".format("Extensions."+extension_name))

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="RR Stats Bot Info", color=0xff0000)
    embed.add_field(name="Guilds:", value=str(len(bot.guilds)), inline=True)
    embed.add_field(name="Members", value=str(len(bot.users)), inline=True)
    embed.add_field(name="Shards:", value=str(bot.shard_count), inline=True)
    if len(bot.active_extensions) > 0:
        embed.add_field(name="Extensions:", value=str("\n".join(bot.active_extensions)), inline=True)
    embed.add_field(name="Commands:", value=len(bot.commands), inline=True)
    embed.add_field(name="Invite:", value="https://discordapp.com/oauth2/authorize?client_id=374248236220940290&scope=bot&permissions=8", inline=True)
    await ctx.send(embed=embed)


def run(info):
    bot.active_extensions = []
    for extension in startup_extensions:
        try:
            bot.load_extension("Discord.Extensions."+extension)
            print("Loaded: {}".format("Discord.Extensions."+extension))
            bot.active_extensions.append(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    print("Extensions loading finished.")

    if os.path.exists("./Discord/token.txt"):
        with open("./Discord/token.txt", "r") as fp:
            token = fp.read()
    else:
        file = open("./Discord/token.txt", "w")
        logging.DEBUG("No BOT token in 'token.txt'. Will fail startup.")
        file.close()

    try:
        bot.run(str(token))
    except Exception as e:
        print("Error: {} - {}".format(type(e).__name__, str(e)))
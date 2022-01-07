import discord
from discord.ext import commands
import random
import asyncio

class Games():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def c4(self, ctx):
        exit

    @commands.command()
    async def gtn(self, ctx, max: int=100, tries: int=20):
        """Guessing this number."""
        await ctx.send("I am going to decide a number from 1 to {}. \nYour task is to guess it. \nWith each guess I will say whether the number is higher or lower. You have {} tries. Good Luck.".format(max, tries))

        def is_correct(m):
            return m.author == ctx.author and m.content.isdigit()

        answer = random.randint(1, max)
        guesses = 0

        while guesses < tries:
            guesses = guesses + 1
            won = False
            try:
                guess = await self.bot.wait_for('message', check=is_correct, timeout=30.0)
            except asyncio.TimeoutError:
                return await ctx.send('Sorry, you took too long it was {}.'.format(answer))
                break

            if int(guess.content) == answer:
                await ctx.send('You are right!')
                won = True
                break

            elif int(guess.content) < answer:
                await ctx.send('You are too low!')
            elif int(guess.content) > answer:
                await ctx.send('You are too high!')

        if won == True: status = "You Won!"
        else: status = "You Lost!"
        await ctx.send("Game Over. \nGuesses: {}. \nStatus: {}.".format(guesses, status))

def setup(bot):
    bot.add_cog(Games(bot))
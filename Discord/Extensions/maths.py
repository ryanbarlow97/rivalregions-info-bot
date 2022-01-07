import discord
from discord.ext import commands

class Maths():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, no1: int, no2: int):
        await ctx.send('{} + {} = {}'.format(no1, no2, no1+no2))

    @commands.command()
    async def subtract(self, ctx, no1:int, no2:int):
        await ctx.send('{} - {} = {}'.format(no1, no2, no1 - no2))

    @commands.command()
    async def multiply(self, ctx, no1:int, no2:int):
        await ctx.send('{} x {} = {}'.format(no1, no2, no1 * no2))

    @commands.command()
    async def divide(self, ctx, no1: int, no2: int):
        await ctx.send('{} ÷ {} = {}'.format(no1, no2, no1 / no2))


def setup(bot):
    bot.add_cog(Maths(bot))
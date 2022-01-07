import discord
from discord.ext import commands

class RRStats():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def house_cost(self, ctx, level: int):

        def house_cost(level):
            if level <= 10:
                previous_total = (level ** 2 + level) / 2
                cash = 200000000 * previous_total
                gold = previous_total
                ore = 10000000 * previous_total
                oil = 10000000 * previous_total
                diamonds = 10 * previous_total
                return int(cash), int(gold), int(ore), int(oil), int(diamonds)
            if level > 10:
                level = level - 10
                previous_total = (level ** 2 + level) / 2
                cash, gold, ore, oil, diamonds = house_cost(10)
                cash = cash + 600000000 * previous_total
                ore = ore + 40000000 * previous_total
                oil = oil + 40000000 * previous_total
                diamonds = diamonds + 50 * previous_total
                return int(cash), int(gold), int(ore), int(oil), int(diamonds)

        if level < 100 and level > 0:
            cash, gold, ore, oil, diamonds = house_cost(int(level))

        embed = discord.Embed(title="House Cost - Level {}".format(level), color=0xff0000)
        embed.add_field(name="Cash:", value=str(cash)+" $", inline=True)
        embed.add_field(name="Gold", value=str(gold)+" G", inline=True)
        embed.add_field(name="Ore:", value=str(ore)+" Kg", inline=True)
        embed.add_field(name="Oil:", value=str(oil)+" Barr", inline=True)
        embed.add_field(name="Diamonds:", value=str(diamonds)+" Pcs.", inline=True)
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(RRStats(bot))



def damage_formula():
    """(Hospital + 2*Military base + School +
    Sea port (if there is a sea access) + Missile system + Power plant
    + Spaceport + Airport (or Refill station on the Moon))*50000"""
    exit


def factory_cost():
    """Cost formula"""
    exit






import discord
from discord.ext import commands
 
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
 
@bot.event
async def on_ready():
    print('Done! bot is online.')
    await bot.change_presence(status=discord.Status.idle, activity=None)

@bot.command()
async def hello(ctx):
    await ctx.send('안녕하세요!')
@bot.command()
async def bye(ctx):
    await ctx.send('잘가세요!')
@bot.command()
async def 도움말(ctx):
    await ctx.send('hello, bye, 오류, 도움말 명령어가 있어요!')
@bot.command()
async def 오류(ctx):
    await ctx.send('오류가 나거나 명령어가 작동 안할 시 nageune1010@gmail.com에 문의해주세요.')

bot.run('Your Token')

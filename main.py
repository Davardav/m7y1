import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def q(ctx):
    wwwww = 0
    attachments = ctx.message.attachments
    for attachment in attachments:
        file_name = attachment.filename
        file_url = attachment.url
        await attachment.save(f'img/{file_name}')
        await ctx.send("картинка сохранена")
        wwwww = 1
    if wwwww == 0:
        await ctx.send('Картинка не была найдена')
bot.run("ToKEN")
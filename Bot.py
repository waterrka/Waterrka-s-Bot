import disnake
from disnake.ext import commands
from datetime import datetime
import time
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv("API_KEY")
CHANNEL_ID=1401835819714478101

bot = commands.Bot(
    command_prefix="/",
    help_command=None,
    intents=disnake.Intents.all(),
    test_guilds=[1129418341770072265]
)

@bot.event
async def on_ready():
    print(f"{bot.user.name} онлайн!")
    activity = disnake.Activity(type=disnake.ActivityType.watching, name="boosty.to/waterrka")
    await bot.change_presence(activity=activity)
    channel = bot.get_channel(CHANNEL_ID)
    start_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    timestamp = int(time.time())
    embed = disnake.Embed(
        title="Бот онлайн!",
        description=f"Бот запущен <t:{timestamp}:R>",
        color=None
    )
    embed.set_footer(text=f"Время запуска: {start_time}")
    await channel.send(embed=embed)

@bot.command(name="load")
@commands.has_permissions(administrator=True)
async def load(ctx, extension: str):
    extension_name = f".cogs/{extension}"
    if extension_name in bot.extensions:
        await ctx.send(f"⚠️ Модуль `{extension_name}` уже загружен.")
    else:
        try:
            bot.load_extension(extension_name)
            await ctx.send(f'✅ Модуль `{extension_name}` успешно загружен!')
        except Exception as e:
            await ctx.send(f'❌ Ошибка при загрузке модуля `{extension_name}`:\n```{e}```')

@bot.command(name="unload")
@commands.has_permissions(administrator=True)
async def unload(ctx, extension: str):
    extension_name = f".cogs/{extension}"
    if extension_name not in bot.extensions:
        await ctx.send(f"⚠️ Модуль `{extension_name}` уже выгружен.")
    else:
        try:
            bot.unload_extension(extension_name)
            await ctx.send(f'✅ Модуль `{extension_name}` успешно выгружен!')
        except Exception as e:
            await ctx.send(f'❌ Ошибка при выгрузке модуля `{extension_name}`:\n```{e}```')

@bot.command(name="reload")
@commands.has_permissions(administrator=True)
async def reload(ctx, extension: str):
    extension_name = f".cogs/{extension}"
    try:
        bot.reload_extension(extension_name)
        await ctx.send(f'✅ Модуль `{extension_name}` успешно перезагружен!')
    except Exception as e:
        await ctx.send(f'❌ Ошибка при перезагрузке модуля `{extension_name}`:\n```{e}```')

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")
        except Exception as e:
            print(f"Ошибка загрузки {filename}: {e}")

bot.run(API_KEY)
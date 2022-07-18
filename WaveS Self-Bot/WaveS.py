from discord.ext import commands as ifwerezbot
import discord
import aiohttp
import random
import colorama
import os
from colorama import init
init()
from colorama import Fore, Back, Style
import requests
def load():
    window = 'mode 104,19'
    os.system(window)
    print(f"""{Fore.GREEN}{Style.BRIGHT}
          _  _  _                    ______     ______       _    ___       ______             
         (_)(_)(_)                  / _____)   / _____)     | |  / __)     (____  \        _   
          _  _  _ _____ _   _ _____( (____    ( (____  _____| |_| |__ _____ ____)  ) ___ _| |_ 
         | || || (____ | | | | ___ |\____ \    \____ \| ___ | (_   __|_____)  __  ( / _ (_   _)
         | || || / ___ |\ V /| ____|_____) )   _____) ) ____| | | |        | |__)  ) |_| || |_ 
          \_____/\_____| \_/ |_____|______/   (______/|_____)\_)|_|        |______/ \___/  \__)
                                                                                                                                           

        {Fore.CYAN}""")

def gettoken():
    usertoken = input("Введите токен >>>")
    return usertoken
def getprefix():
    prefix = input("Введите префиксс >>> ")
    return prefix

def check_token(authorization):
    try:
        headers = {'Content-Type': 'application/json', 'authorization': authorization}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            token = authorization
            return token
        else:
            print("Неверный токен введите токен ещё раз! (проверки токена не будет)")
            tokenin = input("Введите токен >>> ")
            token = tokenin
            return token
    except UnicodeEncodeError:
        print("Юникод не поддерживается! Введите токен ещё раз (проверки токена не будет!)")
        tokenin = input("Введите токен >>> ")
        token = tokenin
        return token

load()


tokentocheck = gettoken()
prefix = getprefix()
token = check_token(tokentocheck)


dangerous = "`массэмодзи` - Поставить реакцию на последних 20 сообшений\n`спам` - Спамить бля"
emoji = "`пошёлнахуй` - Эмодзи\n`lenny` - Эмодзи\n`что` - Эмодзи\n`медведь` - Эмодзи\n`взволнован` - Эмодзи\n`ак47` - Эмодзи\n`авп` - Эмодзи\n`лмг` - Эмодзи\n`меч` - Эмодзи\n`любовь` - Эмодзи\n`спокойнойночи` - Эмодзи\n`улыбка` - Эмодзи"
server = "`очистить` - Очистить amount сообщений\n`серверинфо` - Информация о сервере"
activity = "`стримить` - Активность\n`играть` - Активность\n`слушать` - Активность\n`смотреть` - Активность\n`стопактивность` - Остановить активность"
fun = "`пенис` - Длина пениса участника"

ifwerez = ifwerezbot.Bot(command_prefix=prefix, self_bot=True)
ifwerez.remove_command("help")

@ifwerez.event
async def on_ready():
	print(f"Селф-Бот Запущен. Напишите {prefix}помощь что-бы получить список команд")
	await ifwerez.change_presence(status=discord.Status.dnd)

@ifwerez.command()
async def бананвжопу(message, member: discord.User):
	await message.channel.send(f"теперь у {member} в жопе банан")


@ifwerez.command()
async def помощь(ctx):
	await ctx.send(f"**```Опасное: ```{dangerous}**\n**```Эмодзи: ```{emoji}**\n**```Сервер: ```{server}**\n**```Активность: ```{activity}**\n**```Веселье: ```{fun}**")

@ifwerez.command()
async def голосование(ctx, *, suggestion):
    await ctx.message.delete()
    msg = await ctx.send(f"Голосование: {suggestion}")
    await msg.add_reaction('\U0001F44D')
    await msg.add_reaction('\U0001F44E')

@ifwerez.command(aliases=['идп', 'аватар'])
async def ава(ctx, *, user: discord.User = None):
    avatar = user.avatar_url
    await ctx.send(f"Аватар {user}")
    await ctx.send(avatar)

@ifwerez.command(aliases=["серинфо"])
async def серверинфо(ctx):
    date_format = "%a, %d %b %Y %I:%M %p"
    try:
        await ctx.send(f"Информация о сервере {ctx.guild.name}:" + "\n" + "Дата создания:" + " - " + f"{ctx.guild.created_at.strftime(date_format)}" + "\n" + "Владелец сервера" + " - " + f"<@{ctx.guild.owner_id}>" + "\n" + "ID Сервера" + " - " + f"{ctx.guild.id}" + "\n" + f"{ctx.guild.member_count} Участников\n{len(ctx.guild.roles)} Ролей\n{len(ctx.guild.text_channels)} Текстовый каналов\n{len(ctx.guild.voice_channels)} Голосовых каналов\n{len(ctx.guild.categories)} Категорий")
    except AttributeError:
        print(f"Ты чё тупой что-бы писать эту команду челику в лс?") 

@ifwerez.command()
async def очистить(ctx, amount: int):
    async for message in ctx.message.channel.history(limit=amount + 1).filter(lambda m: m.author == ifwerez.user).map(lambda m: m):
        try:
            await message.delete()
        except:
            pass

@ifwerez.command()
async def пошёлнахуй(ctx):
    await ctx.message.delete()
    middle = '╭∩╮(･◡･)╭∩╮'
    await ctx.send(middle)

@ifwerez.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@ifwerez.command()
async def что(ctx):
    await ctx.message.delete()
    what = '( ʘ̆ ╭͜ʖ╮ ʘ̆ )'
    await ctx.send(what)

@ifwerez.command()
async def медведь(ctx):
    await ctx.message.delete()
    bear = 'ʕ •ᴥ•ʔ'
    await ctx.send(bear)

@ifwerez.command()
async def взволнован(ctx):
    await ctx.message.delete()
    worried = '(´･ _･｀)'
    await ctx.send(worried)

@ifwerez.command()
async def ак47(ctx):
    await ctx.message.delete()
    ak = '︻╦╤─'
    await ctx.send(ak)


@ifwerez.command()
async def авп(ctx):
    await ctx.message.delete()
    awp = '︻デ═一'
    await ctx.send(awp)

@ifwerez.command()
async def лмг(ctx):
    await ctx.message.delete()
    lmg = '︻╦̵̵͇̿̿̿̿╤──'
    await ctx.send(lmg)

@ifwerez.command()
async def меч(ctx):
    await ctx.message.delete()
    sword = 'ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>'
    await ctx.send(sword)

@ifwerez.command()
async def любовь(ctx):
    await ctx.message.delete()
    love = '(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥'
    await ctx.send(love)

@ifwerez.command()
async def спокойнойночи(ctx):
    await ctx.message.delete()
    night = '✩⋆｡ ˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩'
    await ctx.send(night)

@ifwerez.command()
async def улыбка(ctx):
    await ctx.message.delete()
    smile = '˙ ͜ʟ˙'
    await ctx.send(smile)


@ifwerez.command()
async def стримить(ctx, *, message):
    stream = discord.Streaming(
        name = message,
        url = "https://www.youtube.com/watch?v=j5a0jTc9S10", 
    )
    await ifwerez.change_presence(activity=stream)    

        
@ifwerez.command()
async def играть(ctx, *, message):
    game = discord.Game(
        name=message
    )
    await ifwerez.change_presence(activity=game)
    
    
@ifwerez.command()
async def слушать(ctx, *, message):
    await ifwerez.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))
           
            
@ifwerez.command()
async def смотреть(ctx, *, message):
    await ifwerez.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))


@ifwerez.command()
async def стопактивность(ctx):
    await ifwerez.change_presence(activity=None, status=discord.Status.dnd)



@ifwerez.command(aliases=['хуй', 'член'])
async def пенис(ctx, *, user: discord.User = None):
    if user is None:
        user = ctx.author
    size = random.randint(1, 35)
    dong = ""
    for _i in range(0, size):
        dong += "="
    await ctx.send(f"Размер пипирки ('=' = 1 см) {user}:\n" + f"8{dong}D")

@ifwerez.command()
async def массэмодзи(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)
            
                
@ifwerez.command()
async def спам(ctx, amount:int=None, *, message: str=None):
    await ctx.message.delete()
    for each in range (0, amount):
        await ctx.send(f"{message}")



try:
    ifwerez.run(token, bot=False)
except:
    print("Произошла ошибка при старте селф-бота. Скорей всего вы ввели не вверный токен!")
    print("Нажмите enter что-бы выйти")
    input()
    exit()

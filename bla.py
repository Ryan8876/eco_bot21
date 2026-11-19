import discord
from discord.ext import commands
import webbrowser
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def oi(ctx, count_heh = 5):
    await ctx.send("oi" *count_heh )

@bot.command()
async def google(ctx):
    await ctx.send("abrindo a página do Google")
    await webbrowser.open("https://www.google.com")

@bot.command()
async def roblox(ctx):
    await ctx.send("Abrindo a página do Roblox...")
    await webbrowser.open("https://www.Roblox.com")

@bot.command()
async def minecraft(ctx):
    await ctx.send("Abrindo a página do Mine...")
    await webbrowser.open("https://www.Minecraft.com")

@bot.command()
async def investidor10(ctx):
    await ctx.send("abrindo a página do Investidor...")
    await webbrowser.open("https://www.Investidor10.com")

@bot.command()
async def gmail(ctx):
    await ctx.send("abrindo a página do Gmail...")
    await webbrowser.open("https://www.Gmail.com")

@bot.command()
async def meme(ctx):
    img_rand = random.choice(os.listdir("images"))
    with open(f"Images/{img_rand}", "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def lixo(ctx):
    await ctx.send(f'você esta tento dificultade sem saber onde pode jogar o lixo?,se sim escreva lixonão {bot.user}!')

@bot.command()
async def lixonão(ctx):
    await ctx.send(f'então tá vou te ajudar a cuidar da natureza sem jogar lixo no chão,• Guarde embalagens até achar uma lixeira: leve papéis,bitucas e embalagens na bolsa,mochila ou bolso se não houver lixeira por perto.\n • Tenha uma sacolinha no carro ou na mochila: use-a para juntar resíduos durante deslocamentos e descarte no destino correto depois.\n• Previna entupimentos e poluição: evitar jogar resíduos nas ruas impede que a chuva leve sujeira para bueiros, rios e áreas verdes, reduzindo enchentes e danos aos animais.!')

@bot.command()
async def ajuda(ctx):
    await ctx.send(f'se quer ajuda para cuidar do meio ambiente aqui comandos que pode usar: lixo(serve para você ser ajudado a jogar lixo no lugar certo)\nlixosim(explica passo por passo de como cuidar do meio ambiente!)')

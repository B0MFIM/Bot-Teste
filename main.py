import discord
import logging
from decouple import config
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="!", intents=intents)


# Criando Evento para confirmar se o bot está online
@client.event
async def on_ready():
    print("O BOT ESTA ONLINE PARA USO!")
    print("---------------------------")

# Evento de entrada no servidor
@client.event
async def on_member_join(member):
    channel = client.get_channel(994267922732158986)
    await channel.send(f"Hello {member}! Good luck!")

# Evento de saída no servidor
@client.event
async def on_member_remove(member):
    channel = client.get_channel(994267922732158986)
    await channel.send(f"Goodbye dear {member}! Good luck!")

# Evento de entrada e saida de um canal de voz
@client.event
async def on_voice_state_update(member, before, after):
    channel = client.get_channel(993521203903995916)
    voice = client.get_channel(993521203903995917)
    if before.channel is None and after.channel is not None:
        if after.channel.id == 993521203903995917:
            await channel.send(f"{member} entrou no {voice}!")
    if after.channel is None and before.channel is not None:
        if before.channel.id == 993521203903995917:
            await channel.send(f"{member} saiu do {voice}!")

# Criando Comandos para o bot escrever uma mensagem
@client.command()
async def hello(ctx):
    await ctx.send("Hello Dear!")

@client.command(name="bye")
async def Say_GoodBye(ctx):
    await ctx.send("GoodBye Dear!")


# Importando chave TOKEN
TOKEN = config("TOKEN_SECRET")
# Iniciando o bot
client.run(TOKEN)
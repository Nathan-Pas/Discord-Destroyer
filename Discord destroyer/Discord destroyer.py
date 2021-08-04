
import discord
from discord.ext import commands
from tkinter import *


def launch_bot():
    info = Tk()
    info.title("Discord destroyer")
    info.geometry("500x500")
    info.config(background='#A7A7A7')
    Label(info, text="""le bot va se lancer, veuillez fermez les fenetres,
    des indications seront données dans la console""", font=("Arial", 10), bg="#dee5dc").pack(expand=YES)

    info.mainloop()
    spam = "Nathan = hacker (c'est faux)"
    token = ""  # < token de votre bot
    bot = commands.Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        print("bot pret à spammer")
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






destroyer = Tk()
destroyer.title("Discord destroyer")
destroyer.geometry("720x480")
destroyer.iconbitmap("bitmap.ico")
destroyer.config(background='#dee5dc')

frame = Frame(destroyer, bg='#FFFFFF').pack(expand=YES)


image = PhotoImage(file="start.png").zoom(32).subsample(50)

launcher_button = Button(frame, image=image, bg='#dee5dc', bd=0, relief=SUNKEN, command=launch_bot).pack(expand=YES)

Label(text="veuillez appuyer sur start pour lancer le bot", bg='#dee5dc', font=("Arial", 25)).pack(expand=YES)



destroyer.mainloop()

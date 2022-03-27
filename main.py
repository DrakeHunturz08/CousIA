import random
import time
from discord.ext import commands
from json import load
from pathlib import Path

bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print("[INFO] CousIA is ready...\n")

@bot.event
async def on_message(message):
    content = message.content.lower()
    user = str(message.author)
    channel = message.channel
    user = user[:-5]

    if user == bot.user:
        return
    if message.author.bot: 
        return

    if channel.id == 955184889228054569 or channel.id == 955171243781394473:
        return

    if channel.id == 955199206329569280 or channel.id == 955197223061323796:
        print(user + ": " + str(content))

        if ("hello " in content or "bonjour " in content or "salut " in content or "wesh " in content or "salam " in content or "ciao " in content or "yo " in content) and "cousia " in content:
            await channel.send(f"Salut {user}!")
        
        if "dab" in content and "cousia" in content:
            await channel.send("https://tenor.com/view/dab-dabbing-gif-13418160")
        
        elif ("bête " in content or "moche " in content or "idiot " in content or "laid " in content or "con " in content or "inutile " in content or "sers à rien " in content or "sers a rien" in content or "merde " in content or "nul " in content or "pues " in content) and "cousia " in content:
            await channel.send(insultes(user))

        if ("quit " in content or "dégage " in content or "quitter " in content) and "cousia " in content:
            await channel.send("Je vous quitte, au revoir...")
            exit()
        
        if content ==  ".help":
            await channel.send(helpMsg())

        if ".dice" in content:
            content = list(content.split(" "))
            del content[0]
            await channel.send("Je lance le dé...")
            time.sleep(1)
            await channel.send(f"Le résultat est : {rollingDice(content)}")
        
        if content == ".coinflip":
            await channel.send("Je lance la pièce...")
            time.sleep(1)
            await channel.send(f"Le résultat est : {coinflip()}")
        
        if content == ".clear":
            await channel.purge(5)
        
        if ".calcul" in content:
            content = list(content.split(" "))
            del content[0]
            await channel.send(calcul(content))

def helpMsg():
    return "```\nCommandes Générales :\n\tCommandes :\n\t\t.help - Affiche toutes les commandes valides\n\t\t.dice <number> - Lance un dé\n\t\t.coinflip - Lance une pièce\n\t\t.calcul <calcul> - Fonction de calcul\n\tMessages :\n\t\tSalutations CousIA - Vous pouvez saluer CousIA\n\t\tInsultes CousIA - Vous pouvez insulter CousIA\n```"

def rollingDice(content):
    d = "".join(content)
    return random.randint(1, int(d))

def coinflip():
    coin = ["Pile", "Face"]
    return random.choice(coin)

def calcul(content):
    for i in range(len(content)):
        if content[i] == 'modulo' or content[i] == 'mod':
            content[i] = '%'
        
        if content[i] == 'puissance':
            content[i] = '**'

    cal = "".join(content)
    return eval(str(cal))


def insultes(user):
    current_response = [f"Je ne me permettrai pas d'arriver à votre niveau {user}",
                        f"Tout comme vous {user}",
                        f"Merci bien vous aussi {user}",
                        f"La vérité sort de la bouche des enfants {user}.", 
                        f"Vous n'êtes vraiment pas très sympa, mais le train de vos injures roule sur le rail de mon indifférence, {user}.", 
                        f"Vous habitez en face du cimetière mais dans un avenir proche vous habiterai en face de chez vous {user}.", 
                        "Vous cherchez l'ambiance ou l'ambulance ?",
                        "L'insulte est souvent l'argument final de celui qui ne trouve plus rien à dire.",
                        "A quoi bon insulter quelqu'un ou quelque chose qui ne vit pas, puisqu'il n'en souffre pas ?",
                        f"J'ai moyen de me défendre contre les insultes, pas contre la pitié, {user}.",
                        f"Désolé {user} mais l'insulte est l'arme du faible.",
                        "Les insultes ne salissent que ceux qui les profèrent."]
    return random.choice(current_response)

with Path("Main/config.json").open() as f:
    config = load(f)

token = config["token"]
bot.run(token)

import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def help3(ctx):
    await ctx.send('$hint - Ricevi un consiglio casuale per l\'ecologia!')

@bot.command()
async def hint(ctx):
    consigli = [
        "Spegni le luci quando esci da una stanza.",
        "Chiudi il rubinetto mentre ti lavi i denti.",
        "Usa una borraccia riutilizzabile invece delle bottiglie usa e getta.",
        "Fai la raccolta differenziata correttamente.",
        "Quando puoi, vai a piedi o in bicicletta.",
        "Usa entrambi i lati dei fogli di carta.",
        "Non sprecare cibo: conserva bene gli avanzi.",
        "Scollega i caricabatterie quando non li usi.",
        "Riutilizza gli oggetti invece di buttarli subito.",
        "Pianta fiori o piante adatti agli insetti impollinatori."
    ]

    consiglio = random.choice(consigli)
    await ctx.send(f'🌱 **Consiglio ecologico:** {consiglio}')

bot.run("token")
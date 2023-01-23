#Module Public
import discord #j'importe la librairie discord dans le programme

#Module Perso
from Horodatage import afficherHeureEtAction
import Musique


intents = discord.Intents.default() 
intents.message_content = True #Il traite les messages envoyé dans le serveur
client = discord.Client(intents=intents) #est une instruction de création d'un objet "client" de la bibliothèque Discord

@client.event #Il print dans la console ça
async def Initialisation():   
    print(f'Le bot {client.user} est bien en marche ma geule' )
    print(f'')

@client.event
async def detectionMessage(message):
    if message.author == client.user:
        return

    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        action = "Reaction à $hello"
        afficherHeureEtAction(action)
        return


    if message.content.find("test") != -1 :     #si dans la chaine de caractere il y a test
        await message.channel.send("t'avais un test dans ton message :eyes:")
        action = "Reaction à test"
        afficherHeureEtAction(action)
        return















client.run('MTA2NTM1NjQyNjIzMjQ3NTc0OA.Gsd9O0.XXaFE8rtdI7UR-a2WJao6OL-u9YLYCbvcQAcfo')



"""





def augmente_moi(a):
    return augmente_moi + 2




"""
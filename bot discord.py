import discord
from discord import app_commands
import random

id_do_servidor =

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez

    async def on_ready(self):

        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            await tree.sync(guild = discord.Object(id=id_do_servidor)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'sexta', description='sexta daquelas') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://youtu.be/pCTSdupScwA", ephemeral = False) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'domingo', description='domingo daqueles') #Comando específico para seu servidor
async def slash3(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://youtu.be/a_YER1MoY8o", ephemeral = False) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'sabado', description='sabado daqueles') #Comando específico para seu servidor
async def slash4(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://youtu.be/2wUnC0T1nSc", ephemeral = False) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'dado', description='gira um dado de 6 lados') #Comando específico para seu servidor
async def slash5(interaction: discord.Interaction):
    numero= random.randint(1,6)
    await interaction.response.send_message(f"número {numero}", ephemeral = False) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'segunda', description='segunda daqueles') #Comando específico para seu servidor
async def slash6(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://youtu.be/gk2sbghpahI", ephemeral = False) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'terça', description='terça daquelas') #Comando específico para seu servidor
async def slash7(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://youtu.be/88e90SRhoQA", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'quarta', description='quarta daquelas') #Comando específico para seu servidor
async def slash8(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://youtu.be/EA85YF672Mo", ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'quinta', description='quinta daquelas') #Comando específico para seu servidor
async def slash9(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://youtu.be/nSR07_heXxs", ephemeral = False)

aclient.run('')
import discord
from discord import app_commands
from dotenv import load_dotenv
import os


load_dotenv()
DISCORD_TOKEN = os.getenv("discord_token")

class DiviBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="/",
            intents=intents
        )
        self.tree = app_commands.CommandTree(self)
    
    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"O Bot {self.user} foi ligado com sucesso")


bot = DiviBot() 

@bot.tree.command(name="opa", description="CAARA")
async def opa(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olá {interaction.user.name}")

@bot.tree.command(name="dividendo", description="CAARA")
@app_commands.describe(n1="numero 1", n2="numero 2")
async def dividendo(interaction: discord.Interaction, n1: int, n2: int):
    await interaction.response.send_message({n1+n2}, ephemeral=True) # ephemeral quer dizer que apenas quem fez a interação consegue ver

bot.run(DISCORD_TOKEN)

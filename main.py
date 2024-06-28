
import discord
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    print("Error: DISCORD_TOKEN not found in environment variables")
    exit(1)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return  # Ignore messages from the bot itself
        print(f'Message from {message.author}: {message.content}')
        try:
            await message.channel.send('Hey I am bot')
        except Exception as e:
            print(f'Error sending message: {e}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print(f"Login failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

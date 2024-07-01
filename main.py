
import discord
import os
import  openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')
openai.api_key = os.getenv('OPEN_AI_TOKEN')



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
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=message.content,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            messageSend = response.choices[0].text.strip()
            print(response)
            await message.channel.send(messageSend)

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

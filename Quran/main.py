from typing import Final
import sys

sys.stdout.reconfigure(encoding='utf-8')
from discord import Intents, Client, Message
import os
from dotenv import load_dotenv
from responses import fetch_quran_verse
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

@client.event
async def on_ready() -> None:
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    if message.content.startswith('/quran'):
        query = message.content[len('/quran '):].strip()
        print(f"Extracted query: '{query}'")
        if not query:
            await message.channel.send("Please provide a valid query. Format: /quran <surah>:<ayah>")
            return
        try:
            response_message = fetch_quran_verse(query)
            print(f"Response message: '{response_message}'")
            await message.channel.send(response_message)
        except Exception as e:
            print(f"Error while sending message: {e}")
            await message.channel.send("An error occured while processing the request.")

def main() -> None:
    client.run(token=TOKEN)
if __name__ == '__main__':
    main()
import asyncio
from pyrogram import Client
from config import API_ID, API_HASH

api_id = API_ID
api_hash = API_HASH

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")

asyncio.run(main())
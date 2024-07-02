from pyrogram import Client
from config import API_ID, API_HASH
import asyncio

api_id = API_ID
api_hash = API_HASH

async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
           # Envia uma mensagem para o seu próprio usuário no Telegram
           await app.send_message("me", "Hello from Pyrogram!")

# Executa a função principal
asyncio.run(main())
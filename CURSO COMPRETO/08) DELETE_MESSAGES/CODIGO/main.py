from pyrogram import Client
from config import API_ID, API_HASH
import asyncio

api_id = API_ID
api_hash = API_HASH

async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
           # ID da mensagem que você deseja excluir (substitua com o ID real da mensagem)
           message_id = 123456789

           # Exclui a mensagem
           await app.delete_messages("me", message_ids=message_id)

# Executa a função principal
asyncio.run(main())

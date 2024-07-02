from pyrogram import Client
from config import API_ID, API_HASH
import asyncio

api_id = API_ID
api_hash = API_HASH

async def main():
    async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
        # ID do chat (usuário ou grupo) para onde você deseja enviar a mensagem
        chat_id = "123456789"

        # Enviar ação de "digitando" antes de enviar a mensagem
        await app.send_chat_action(chat_id, "typing")

        # Envie a mensagem real
        await app.send_message(chat_id, "Olá, estou digitando esta mensagem!")

# Executa a função principal
asyncio.run(main())

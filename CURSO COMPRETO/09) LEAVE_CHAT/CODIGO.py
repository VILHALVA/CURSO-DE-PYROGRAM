from pyrogram import Client
import asyncio

async def main():
    # Cria uma instância do cliente Pyrogram
    async with Client("my_account") as app:
        # ID do chat (grupo) que você deseja deixar (substitua com o ID real do chat)
        chat_id = "123456789"

        # Faz o bot sair do chat (grupo)
        await app.leave_chat(chat_id)

# Executa a função principal
asyncio.run(main())

from pyrogram import Client
import asyncio

async def main():
    # Cria uma instância do cliente Pyrogram
    async with Client("my_account") as app:
        # ID do chat (grupo) do qual você deseja desbanir o membro (substitua com o ID real do chat)
        chat_id = "123456789"
        # ID do usuário que você deseja desbanir (substitua com o ID real do usuário)
        user_id = 987654321

        # Desbane o membro do grupo
        await app.unban_chat_member(chat_id, user_id)

# Executa a função principal
asyncio.run(main())

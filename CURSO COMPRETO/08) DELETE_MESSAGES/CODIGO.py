from pyrogram import Client
import asyncio

async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account") as app:
           # ID da mensagem que você deseja excluir (substitua com o ID real da mensagem)
           message_id = 123456789

           # Exclui a mensagem
           await app.delete_messages("me", message_ids=message_id)

# Executa a função principal
asyncio.run(main())
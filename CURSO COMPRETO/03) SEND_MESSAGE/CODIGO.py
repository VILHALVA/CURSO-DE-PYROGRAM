from pyrogram import Client
import asyncio

async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account") as app:
           # Envia uma mensagem para o seu próprio usuário no Telegram
           await app.send_message("me", "Hello from Pyrogram!")

# Executa a função principal
asyncio.run(main())
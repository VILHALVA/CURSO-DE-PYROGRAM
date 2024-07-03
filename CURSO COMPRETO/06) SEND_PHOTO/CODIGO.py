from pyrogram import Client
import asyncio

async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account") as app:
           # Envia uma foto para o seu próprio usuário no Telegram
           await app.send_photo("me", photo="caminho/para/sua/foto.jpg", caption="Minha foto enviada via Pyrogram!")

# Executa a função principal
asyncio.run(main())
from pyrogram import Client
from config import API_ID, API_HASH
import asyncio

api_id = API_ID
api_hash = API_HASH

async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
           # Envia uma mensagem de texto simples
           await app.send_message("me", text="Olá, mundo!")

           # Envia uma foto
           await app.send_photo("me", photo="caminho/para/sua/foto.jpg", caption="Minha foto enviada via Pyrogram!")

           # Envia um documento (arquivo)
           await app.send_document("me", document="caminho/para/seu/documento.pdf", caption="Documento PDF enviado via Pyrogram!")

           # Envia um vídeo
           await app.send_video("me", video="caminho/para/seu/video.mp4", caption="Vídeo enviado via Pyrogram!")

           # Envia uma localização
           await app.send_location("me", latitude=37.7749, longitude=-122.4194, title="Localização de San Francisco", address="San Francisco, CA")

           # Envia um contato
           await app.send_contact("me", phone_number="+1234567890", first_name="John", last_name="Doe")

# Executa a função principal
asyncio.run(main())

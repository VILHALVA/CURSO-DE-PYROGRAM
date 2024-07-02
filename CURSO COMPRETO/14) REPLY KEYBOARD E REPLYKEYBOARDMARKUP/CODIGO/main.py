from pyrogram import Client
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import API_ID, API_HASH
import asyncio

api_id = API_ID
api_hash = API_HASH

async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
           # ID do chat (usuário ou grupo) para onde você deseja enviar a mensagem
           chat_id = "123456789"

           # Define os botões do teclado de resposta
           button1 = KeyboardButton("Opção 1")
           button2 = KeyboardButton("Opção 2")
           button3 = KeyboardButton("Opção 3")

           # Cria o teclado de resposta com uma lista de botões
           reply_markup = ReplyKeyboardMarkup(
               [
                   [button1, button2],
                   [button3]
               ],
               resize_keyboard=True,
               one_time_keyboard=True
           )

           # Envia a mensagem com o teclado de resposta
           await app.send_message(chat_id, "Escolha uma opção:", reply_markup=reply_markup)

# Executa a função principal
asyncio.run(main())

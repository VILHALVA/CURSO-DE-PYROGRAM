from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

async def main():
    # Cria uma instância do cliente Pyrogram
    async with Client("my_account") as app:
        # ID do chat (usuário ou grupo) para onde você deseja enviar a mensagem
        chat_id = "123456789"

        # Define os botões do teclado inline
        button1 = InlineKeyboardButton("Botão 1", callback_data="button1")
        button2 = InlineKeyboardButton("Botão 2", callback_data="button2")
        button3 = InlineKeyboardButton("Botão 3", callback_data="button3")

        # Cria o teclado inline com uma lista de botões
        reply_markup = InlineKeyboardMarkup(
            [
                [button1, button2],
                [button3]
            ]
        )

        # Envia a mensagem com o teclado inline
        await app.send_message(chat_id, "Escolha uma opção:", reply_markup=reply_markup)

# Executa a função principal
asyncio.run(main())

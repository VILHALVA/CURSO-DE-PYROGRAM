from pyrogram import Client, filters
import asyncio

async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account") as app:
           # Define um manipulador para mensagens recebidas
           @app.on_message(filters.me)
           async def echo(client, message):
               # Verifica se a mensagem não foi enviada pelo próprio bot
               if message.from_user.is_self:
                   # Ecoa a mensagem de volta para o remetente
                   await message.reply_text(message.text)

           # Inicia o cliente Pyrogram
           await app.run()

# Executa a função principal
asyncio.run(main())
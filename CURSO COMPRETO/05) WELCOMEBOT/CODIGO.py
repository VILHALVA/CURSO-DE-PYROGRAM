from pyrogram import Client, filters
import asyncio

async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account") as app:
           # Define um manipulador para novos membros entrando no grupo
           @app.on_chat_member(filters.new_chat_members)
           async def welcome(client, message):
               for member in message.new_chat_members:
                   if member.id != client.me.id:  # Verifica se não é o próprio bot
                       # Envia uma mensagem de boas-vindas personalizada
                       await message.reply_text(f"Bem-vindo ao grupo, {member.first_name}!")

           # Inicia o cliente Pyrogram
           await app.run()

# Executa a função principal
asyncio.run(main())
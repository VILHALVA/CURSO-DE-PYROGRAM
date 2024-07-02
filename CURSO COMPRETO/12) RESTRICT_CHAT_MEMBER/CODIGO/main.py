from pyrogram import Client
from pyrogram.types import ChatPermissions
from config import API_ID, API_HASH
import asyncio

api_id = API_ID
api_hash = API_HASH

async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
           # ID do chat (grupo) do qual você deseja restringir o membro (substitua com o ID real do chat)
           chat_id = "123456789"
           # ID do usuário que você deseja restringir (substitua com o ID real do usuário)
           user_id = "987654321"

           # Define as permissões que você deseja restringir para o membro
           permissions = ChatPermissions(
               can_send_messages=False,
               can_send_media_messages=False,
               can_send_stickers=False,
               can_send_animations=False,
               can_send_games=False,
               can_use_inline_bots=False,
               can_invite_users=False,
               can_pin_messages=False
           )

           # Restringe o membro do grupo
           await app.restrict_chat_member(chat_id, user_id, permissions)

# Executa a função principal
asyncio.run(main())

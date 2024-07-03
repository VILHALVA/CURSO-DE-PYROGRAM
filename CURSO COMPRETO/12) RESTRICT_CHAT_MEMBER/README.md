# RESTRICT_CHAT_MEMBER
Para restringir as permissões de um membro em um grupo usando Pyrogram, aqui está como você pode implementar isso:

1. **Importe os Módulos Necessários**:

   Certifique-se de importar os módulos necessários do Pyrogram e as permissões de bate-papo (`ChatPermissions`):

   ```python
   from pyrogram import Client
   from pyrogram.types import ChatPermissions
   import asyncio
   ```

2. **Defina e Execute a Função Principal**:

   Crie uma função assíncrona principal (`async def main()`) para restringir um membro de um grupo:

   ```python
   async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account") as app:
           # ID do chat (grupo) do qual você deseja restringir o membro (substitua com o ID real do chat)
           chat_id = "123456789"
           # ID do usuário que você deseja restringir (substitua com o ID real do usuário)
           user_id = 987654321

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
   ```

3. **Explicação do Código**:

   - **`await app.restrict_chat_member(chat_id, user_id, permissions)`**:
     - `app.restrict_chat_member`: Método para restringir as permissões de um membro em um grupo.
     - `chat_id`: ID do chat (grupo) do qual o membro terá as permissões restringidas. Substitua `"123456789"` pelo ID real do grupo.
     - `user_id`: ID do usuário que você deseja restringir no grupo. Substitua `987654321` pelo ID real do usuário que você deseja restringir.
     - `permissions`: Objeto `ChatPermissions` que define as permissões que você deseja restringir para o membro. No exemplo fornecido, várias permissões estão sendo definidas como `False` para restringir o envio de mensagens, mídia, convites, etc.

4. **Execução**:

   - Ao executar este código, o Pyrogram restringirá as permissões do membro especificado pelo `user_id` no grupo especificado pelo `chat_id` de acordo com as configurações definidas no objeto `ChatPermissions`.

Certifique-se de substituir `chat_id = "123456789"` pelo ID real do grupo e `user_id = 987654321` pelo ID real do usuário que você deseja restringir. Além disso, personalize as permissões no objeto `permissions` conforme necessário para atender aos requisitos específicos do seu caso de uso.
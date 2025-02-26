# UNBAN_CHAT_MEMBER
Para permitir que um membro que foi banido anteriormente volte a participar de um grupo usando Pyrogram, você pode usar o método `unban_chat_member`. Aqui está como você pode implementar isso:

1. **Importe os Módulos Necessários**:

   Certifique-se de importar os módulos necessários do Pyrogram:

   ```python
   from pyrogram import Client
   import asyncio
   ```

2. **Defina e Execute a Função Principal**:

   Crie uma função assíncrona principal (`async def main()`) para desbanir um membro de um grupo:

   ```python
   async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account") as app:
           # ID do chat (grupo) do qual você deseja desbanir o membro (substitua com o ID real do chat)
           chat_id = "123456789"
           # ID do usuário que você deseja desbanir (substitua com o ID real do usuário)
           user_id = 987654321

           # Desbane o membro do grupo
           await app.unban_chat_member(chat_id, user_id)

   # Executa a função principal
   asyncio.run(main())
   ```

3. **Explicação do Código**:

   - **`await app.unban_chat_member(chat_id, user_id)`**:
     - `app.unban_chat_member`: Método para desbanir um membro de um grupo.
     - `chat_id`: ID do chat (grupo) do qual o membro será desbanido. Substitua `"123456789"` pelo ID real do grupo.
     - `user_id`: ID do usuário que você deseja desbanir do grupo. Substitua `987654321` pelo ID real do usuário que você deseja desbanir.

4. **Execução**:

   - Ao executar este código, o Pyrogram permitirá que o membro especificado pelo `user_id` volte a participar do grupo especificado pelo `chat_id`.

Certifique-se de substituir `chat_id = "123456789"` pelo ID real do grupo e `user_id = 987654321` pelo ID real do usuário que você deseja desbanir. Isso garante que o Pyrogram possa realizar a ação corretamente no grupo e no usuário específicos.


# KICK_CHAT_MEMBER
Para remover um membro específico de um grupo usando Pyrogram, você pode usar o método `kick_chat_member`. Aqui está como você pode implementar isso:

1. **Importe os Módulos Necessários**:

   Certifique-se de importar os módulos necessários do Pyrogram e suas credenciais do arquivo de configuração:

   ```python
   from pyrogram import Client
   from config import API_ID, API_HASH
   import asyncio
   ```

2. **Defina e Execute a Função Principal**:

   Crie uma função assíncrona principal (`async def main()`) para remover um membro de um grupo:

   ```python
   async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
           # ID do chat (grupo) que você deseja remover o membro (substitua com o ID real do chat)
           chat_id = "123456789"
           # ID do usuário que você deseja remover do grupo (substitua com o ID real do usuário)
           user_id = "987654321"

           # Remove o membro do grupo
           await app.kick_chat_member(chat_id, user_id)

   # Executa a função principal
   asyncio.run(main())
   ```

3. **Explicação do Código**:

   - **`await app.kick_chat_member(chat_id, user_id)`**:
     - `app.kick_chat_member`: Método para remover um membro de um grupo.
     - `chat_id`: ID do chat (grupo) do qual o membro será removido. Substitua `"123456789"` pelo ID real do grupo.
     - `user_id`: ID do usuário que você deseja remover do grupo. Substitua `"987654321"` pelo ID real do usuário que você deseja remover.

4. **Execução**:

   - Ao executar este código, o Pyrogram removerá o membro especificado pelo `user_id` do grupo especificado pelo `chat_id`.

Certifique-se de substituir `chat_id = "123456789"` pelo ID real do grupo e `user_id = "987654321"` pelo ID real do usuário que você deseja remover. Isso garante que o Pyrogram possa realizar a ação corretamente no grupo e no usuário específicos.
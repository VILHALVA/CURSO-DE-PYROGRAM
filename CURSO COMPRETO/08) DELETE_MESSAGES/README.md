# DELETE_MESSAGES
Para excluir mensagens usando Pyrogram, você pode usar o método `delete_messages` do cliente Pyrogram. Aqui está como você pode fazer isso:

1. **Importe os Módulos Necessários**:

   Certifique-se de importar os módulos necessários do Pyrogram e suas credenciais do arquivo de configuração:

   ```python
   from pyrogram import Client
   from config import API_ID, API_HASH
   import asyncio
   ```

2. **Defina e Execute a Função Principal**:

   Crie uma função assíncrona principal (`async def main()`) para excluir mensagens:

   ```python
   async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
           # ID da mensagem que você deseja excluir (substitua com o ID real da mensagem)
           message_id = 123456789

           # Exclui a mensagem
           await app.delete_messages("me", message_ids=message_id)

   # Executa a função principal
   asyncio.run(main())
   ```

3. **Explicação do Código**:

   - **`await app.delete_messages("me", message_ids=message_id)`**:
     - `app.delete_messages`: Método para excluir uma ou mais mensagens.
     - `"me"`: Destinatário da mensagem (neste caso, você mesmo).
     - `message_ids=message_id`: Lista de IDs de mensagens que você deseja excluir. No exemplo, apenas uma mensagem é excluída, com o ID `message_id`.

4. **Execução**:

   - Ao executar este código, o Pyrogram excluirá a mensagem especificada pelo ID `message_id`.

Certifique-se de substituir `message_id = 123456789` pelo ID real da mensagem que você deseja excluir. Isso garante que o Pyrogram possa localizar e excluir a mensagem corretamente.
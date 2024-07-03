# LEAVE_CHAT
Para fazer o bot deixar um grupo (sair do grupo) usando Pyrogram, você pode usar o método `leave_chat` do cliente Pyrogram. Aqui está como você pode fazer isso:

1. **Importe os Módulos Necessários**:

   Certifique-se de importar os módulos necessários do Pyrogram:

   ```python
   from pyrogram import Client
   import asyncio
   ```

2. **Defina e Execute a Função Principal**:

   Crie uma função assíncrona principal (`async def main()`) para fazer o bot sair de um grupo:

   ```python
   async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account") as app:
           # ID do chat (grupo) que você deseja deixar (substitua com o ID real do chat)
           chat_id = "123456789"

           # Faz o bot sair do chat (grupo)
           await app.leave_chat(chat_id)

   # Executa a função principal
   asyncio.run(main())
   ```

3. **Explicação do Código**:

   - **`await app.leave_chat(chat_id)`**:
     - `app.leave_chat`: Método para fazer o bot sair de um chat (grupo).
     - `chat_id`: ID do chat (grupo) que você deseja deixar. Substitua `"123456789"` pelo ID real do chat que você deseja que o bot saia.

4. **Execução**:

   - Ao executar este código, o bot sairá do chat (grupo) especificado pelo `chat_id`.

Certifique-se de substituir `chat_id = "123456789"` pelo ID real do chat que você deseja que o bot saia. Isso garantirá que o Pyrogram possa localizar e sair corretamente do grupo especificado.


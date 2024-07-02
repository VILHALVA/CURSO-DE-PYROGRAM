# SEND MESSAGE
Para enviar uma mensagem usando Pyrogram, você pode usar o método `send_message` do cliente Pyrogram. Aqui está como você pode fazer isso:

1. **Importe os Módulos Necessários**:
   Certifique-se de importar os módulos necessários do Pyrogram e suas credenciais do arquivo de configuração:

   ```python
   from pyrogram import Client
   from config import API_ID, API_HASH
   import asyncio
   ```

2. **Defina e Execute a Função Principal**:
   Crie uma função assíncrona principal (`async def main()`) para enviar a mensagem:

   ```python
   async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
           # Envia uma mensagem para o seu próprio usuário no Telegram
           await app.send_message("me", "Hello from Pyrogram!")

   # Executa a função principal
   asyncio.run(main())
   ```

3. **Explicação**:
   - **`Client("my_account", api_id=API_ID, api_hash=API_HASH)`**: Cria uma instância do cliente Pyrogram, conectando-se à sua conta usando as credenciais fornecidas.
   - **`await app.send_message("me", "Hello from Pyrogram!")`**: Usa o método `send_message` para enviar uma mensagem para o seu próprio usuário no Telegram, especificando o destinatário (`"me"`) e o conteúdo da mensagem (`"Hello from Pyrogram!"`).

4. **Execução**:
   - Ao executar este código, o Pyrogram solicitará a autorização inicial conforme discutido anteriormente. Depois de autorizar, a mensagem será enviada para sua própria conta no Telegram.

Este é um exemplo básico para enviar uma mensagem usando Pyrogram. Você pode adaptar e expandir esse código para criar bots mais complexos e interativos no Telegram.
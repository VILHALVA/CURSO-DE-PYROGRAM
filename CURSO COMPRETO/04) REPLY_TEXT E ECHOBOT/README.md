# REPLY_TEXT E ECHOBOT
Para criar um bot que responde a mensagens usando `reply_text` e que funcione como um "echobot" (eco de mensagens), você pode seguir este exemplo básico usando Pyrogram:

1. **Importe os Módulos Necessários**:

   Certifique-se de importar os módulos necessários do Pyrogram e suas credenciais do arquivo de configuração:

   ```python
   from pyrogram import Client, filters
   from config import API_ID, API_HASH
   import asyncio
   ```

2. **Defina e Execute a Função Principal**:

   Crie uma função assíncrona principal (`async def main()`) para gerenciar as mensagens recebidas e enviar respostas:

   ```python
   async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
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
   ```

3. **Explicação do Código**:

   - **`@app.on_message(filters.me)`**: Define um decorador para registrar um manipulador de evento que será acionado sempre que o bot receber uma mensagem. `filters.me` garante que apenas as mensagens enviadas pelo próprio bot serão processadas.

   - **`async def echo(client, message):`**: Função assíncrona que recebe dois parâmetros: `client` (o cliente Pyrogram) e `message` (a mensagem recebida).

   - **`if message.from_user.is_self:`**: Verifica se a mensagem foi enviada pelo próprio bot para evitar loops infinitos.

   - **`await message.reply_text(message.text)`**: Usa o método `reply_text` para responder à mensagem recebida, ecoando o texto de volta para o remetente.

4. **Execução**:

   - Ao executar este código, o bot começará a escutar as mensagens enviadas para ele. Quando receber uma mensagem, ele responderá com a mesma mensagem (funcionamento básico de um echobot).

Este exemplo é um ponto de partida simples. Você pode expandir esse bot adicionando lógicas mais complexas, manipulando diferentes tipos de mensagens, incorporando comandos personalizados e muito mais, dependendo dos requisitos do seu projeto.
# WELCOMEBOT
Para criar um bot de boas-vindas usando Pyrogram, você pode seguir um exemplo básico que cumprimenta novos membros quando entram em um grupo. Aqui está um exemplo simples de como você pode implementar isso:

1. **Importe os Módulos Necessários**:

   Certifique-se de importar os módulos necessários do Pyrogram:

   ```python
   from pyrogram import Client, filters
   import asyncio
   ```

2. **Defina e Execute a Função Principal**:

   Crie uma função assíncrona principal (`async def main()`) para gerenciar as mensagens recebidas e enviar respostas:

   ```python
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
   ```

3. **Explicação do Código**:

   - **`@app.on_chat_member(filters.new_chat_members)`**: Define um decorador para registrar um manipulador de evento que será acionado sempre que novos membros entrarem no grupo.

   - **`async def welcome(client, message):`**: Função assíncrona que recebe dois parâmetros: `client` (o cliente Pyrogram) e `message` (a mensagem que contém informações sobre os novos membros).

   - **`for member in message.new_chat_members:`**: Itera sobre todos os novos membros que entraram no grupo.

   - **`if member.id != client.me.id:`**: Verifica se o membro não é o próprio bot para evitar cumprimentar a si mesmo.

   - **`await message.reply_text(f"Bem-vindo ao grupo, {member.first_name}!")`**: Usa o método `reply_text` para enviar uma mensagem de boas-vindas personalizada para cada novo membro que entra no grupo.

4. **Execução**:

   - Ao executar este código, o bot começará a escutar novos membros que entram no grupo e enviará uma mensagem de boas-vindas personalizada para cada um deles.

Este exemplo básico pode ser expandido com lógicas adicionais, como enviar mensagens de boas-vindas para novos membros em grupos específicos, personalizar mensagens com emojis, etc. Adaptando e melhorando conforme necessário, você pode criar um bot de boas-vindas mais sofisticado para atender às necessidades do seu grupo no Telegram.


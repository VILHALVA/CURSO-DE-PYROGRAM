# REPLY KEYBOARD E REPLYKEYBOARDMARKUP
Para criar e enviar um teclado de resposta personalizado usando Pyrogram, aqui está como você pode implementar:

1. **Importe os Módulos Necessários**:

   Certifique-se de importar os módulos necessários do Pyrogram e suas credenciais do arquivo de configuração:

   ```python
   from pyrogram import Client
   from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
   import asyncio
   ```

2. **Defina e Execute a Função Principal**:

   Crie uma função assíncrona principal (`async def main()`) para enviar uma mensagem com um teclado de resposta personalizado:

   ```python
   async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account") as app:
           # ID do chat (usuário ou grupo) para onde você deseja enviar a mensagem
           chat_id = "123456789"

           # Define os botões do teclado de resposta
           button1 = KeyboardButton("Opção 1")
           button2 = KeyboardButton("Opção 2")
           button3 = KeyboardButton("Opção 3")

           # Cria o teclado de resposta com uma lista de botões
           reply_markup = ReplyKeyboardMarkup(
               [
                   [button1, button2],
                   [button3]
               ],
               resize_keyboard=True,
               one_time_keyboard=True
           )

           # Envia a mensagem com o teclado de resposta
           await app.send_message(chat_id, "Escolha uma opção:", reply_markup=reply_markup)

   # Executa a função principal
   asyncio.run(main())
   ```

3. **Explicação do Código**:

   - **`ReplyKeyboardMarkup([...], resize_keyboard=True, one_time_keyboard=True)`**:
     - `ReplyKeyboardMarkup`: Classe para criar um teclado de resposta personalizado.
     - `[...]`: Lista de listas de botões (`KeyboardButton`) que formam as linhas do teclado. Cada lista interna representa uma linha de botões.
     - `resize_keyboard=True`: Opcional. Se definido como `True`, o teclado de resposta será redimensionado automaticamente para caber na largura da tela do dispositivo do usuário.
     - `one_time_keyboard=True`: Opcional. Se definido como `True`, o teclado de resposta será exibido apenas uma vez para o usuário, depois será ocultado automaticamente após o uso.

   - **`await app.send_message(chat_id, "Escolha uma opção:", reply_markup=reply_markup)`**:
     - `app.send_message`: Método para enviar uma mensagem para o chat especificado (`chat_id`).
     - `chat_id`: ID do chat (usuário ou grupo) para onde a mensagem será enviada.
     - `"Escolha uma opção:"`: Texto da mensagem que será enviada.
     - `reply_markup=reply_markup`: Opcional. Parâmetro para enviar o teclado de resposta junto com a mensagem.

4. **Execução**:

   - Ao executar este código, o Pyrogram enviará uma mensagem para o chat especificado com um teclado de resposta personalizado contendo três opções ("Opção 1", "Opção 2" e "Opção 3").

Certifique-se de substituir `chat_id = "123456789"` pelo ID real do chat (usuário ou grupo) para onde você deseja enviar a mensagem com o teclado de resposta. Personalize também os botões (`KeyboardButton`) dentro do `ReplyKeyboardMarkup` conforme necessário para suas opções específicas.
# CALLBACKQUERY
Para lidar com `CallbackQuery` (consultas de callback) usando Pyrogram, você precisa configurar um manipulador de eventos para capturar quando um usuário interage com um botão inline e envia uma `CallbackQuery`. Aqui está como você pode implementar isso:

1. **Importe os Módulos Necessários**:

   Certifique-se de importar os módulos necessários do Pyrogram e suas credenciais do arquivo de configuração:

   ```python
   from pyrogram import Client, filters
   from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
   from config import API_ID, API_HASH
   import asyncio
   ```

2. **Defina e Execute a Função Principal**:

   Crie uma função assíncrona principal (`async def main()`) para configurar um manipulador de eventos para `CallbackQuery`:

   ```python
   async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
           # Define o manipulador para CallbackQuery
           @app.on_callback_query()
           async def callback_handler(client, callback: CallbackQuery):
               # Obtém os dados do callback (callback_data)
               data = callback.data

               # Responde à CallbackQuery (opcional)
               await callback.answer()

               # Realiza a ação com base nos dados do callback
               if data == "button1":
                   await callback.edit_message_text("Você pressionou o Botão 1!")
               elif data == "button2":
                   await callback.edit_message_text("Você pressionou o Botão 2!")
               elif data == "button3":
                   await callback.edit_message_text("Você pressionou o Botão 3!")

           # ID do chat (usuário ou grupo) para onde você deseja enviar a mensagem
           chat_id = "123456789"

           # Define os botões do teclado inline
           button1 = InlineKeyboardButton("Botão 1", callback_data="button1")
           button2 = InlineKeyboardButton("Botão 2", callback_data="button2")
           button3 = InlineKeyboardButton("Botão 3", callback_data="button3")

           # Cria o teclado inline com uma lista de botões
           reply_markup = InlineKeyboardMarkup(
               [
                   [button1, button2],
                   [button3]
               ]
           )

           # Envia a mensagem com o teclado inline
           await app.send_message(chat_id, "Escolha uma opção:", reply_markup=reply_markup)

   # Executa a função principal
   asyncio.run(main())
   ```

3. **Explicação do Código**:

   - **`@app.on_callback_query()`**:
     - Decorador para registrar um manipulador de eventos para `CallbackQuery`. Este manipulador é chamado sempre que um usuário interage com um botão inline.

   - **`async def callback_handler(client, callback: CallbackQuery):`**:
     - Função que lida com `CallbackQuery`. O parâmetro `callback` contém informações sobre a interação do usuário.

   - **`callback.data`**: Atributo que contém os dados enviados quando o botão inline é pressionado.

   - **`await callback.answer()`**: Método opcional para enviar uma resposta à `CallbackQuery`. Pode ser usado para confirmar a interação do usuário.

   - **`await callback.edit_message_text("Mensagem modificada")`**: Método para editar a mensagem original em que o botão foi pressionado. Neste exemplo, a mensagem é modificada para informar qual botão foi pressionado.

4. **Execução**:

   - Ao executar este código, o Pyrogram enviará uma mensagem para o chat especificado com um teclado inline personalizado contendo três botões ("Botão 1", "Botão 2" e "Botão 3"). Quando um usuário pressionar um desses botões, a função `callback_handler` será chamada para processar a interação e responder de acordo.

Certifique-se de substituir `chat_id = "123456789"` pelo ID real do chat (usuário ou grupo) para onde você deseja enviar a mensagem com o teclado inline. Personalize também os botões (`InlineKeyboardButton`) dentro do `InlineKeyboardMarkup` conforme necessário para suas opções específicas.
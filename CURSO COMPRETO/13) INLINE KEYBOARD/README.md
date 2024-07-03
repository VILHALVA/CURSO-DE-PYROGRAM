# INLINE KEYBOARD
Para criar e enviar um teclado inline usando Pyrogram, aqui está como você pode implementar:

1. **Importe os Módulos Necessários**:

   Certifique-se de importar os módulos necessários do Pyrogram e suas credenciais do arquivo de configuração:

   ```python
   from pyrogram import Client
   from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
   import asyncio
   ```

2. **Defina e Execute a Função Principal**:

   Crie uma função assíncrona principal (`async def main()`) para enviar uma mensagem com um teclado inline personalizado:

   ```python
   async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account") as app:
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

   - **`InlineKeyboardMarkup([...])`**:
     - `InlineKeyboardMarkup`: Classe para criar um teclado inline personalizado.
     - `[...]`: Lista de listas de botões (`InlineKeyboardButton`) que formam as linhas do teclado. Cada lista interna representa uma linha de botões.

   - **`InlineKeyboardButton("Texto do Botão", callback_data="dados_de_callback")`**:
     - `InlineKeyboardButton`: Classe para criar um botão inline.
     - `"Texto do Botão"`: Texto visível do botão.
     - `callback_data="dados_de_callback"`: Dados que serão enviados quando o botão for pressionado. Este parâmetro é usado para identificar qual botão foi pressionado.

   - **`await app.send_message(chat_id, "Escolha uma opção:", reply_markup=reply_markup)`**:
     - `app.send_message`: Método para enviar uma mensagem para o chat especificado (`chat_id`).
     - `chat_id`: ID do chat (usuário ou grupo) para onde a mensagem será enviada.
     - `"Escolha uma opção:"`: Texto da mensagem que será enviada.
     - `reply_markup=reply_markup`: Parâmetro para enviar o teclado inline junto com a mensagem.

4. **Execução**:

   - Ao executar este código, o Pyrogram enviará uma mensagem para o chat especificado com um teclado inline personalizado contendo três botões ("Botão 1", "Botão 2" e "Botão 3").

Certifique-se de substituir `chat_id = "123456789"` pelo ID real do chat (usuário ou grupo) para onde você deseja enviar a mensagem com o teclado inline. Personalize também os botões (`InlineKeyboardButton`) dentro do `InlineKeyboardMarkup` conforme necessário para suas opções específicas.
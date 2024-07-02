# INLINE_QUERIES
Para lidar com consultas inline (inline queries) usando Pyrogram, você precisa configurar um manipulador de eventos para capturar quando um usuário faz uma consulta inline. Aqui está como você pode implementar isso:

1. **Importe os Módulos Necessários**:

   Certifique-se de importar os módulos necessários do Pyrogram e suas credenciais do arquivo de configuração:

   ```python
   from pyrogram import Client, filters
   from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
   from config import API_ID, API_HASH
   import asyncio
   ```

2. **Defina e Execute a Função Principal**:

   Crie uma função assíncrona principal (`async def main()`) para configurar um manipulador de eventos para `InlineQuery`:

   ```python
   async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
           # Define o manipulador para InlineQuery
           @app.on_inline_query()
           async def inline_query(client, query: InlineQuery):
               results = []

               # Obtém o texto da consulta
               query_text = query.query.lower()

               # Cria resultados de consulta inline baseados na consulta
               if "hello" in query_text:
                   results.append(
                       InlineQueryResultArticle(
                           title="Saudações",
                           input_message_content=InputTextMessageContent("Olá, como você está?")
                       )
                   )
               if "bye" in query_text:
                   results.append(
                       InlineQueryResultArticle(
                           title="Despedida",
                           input_message_content=InputTextMessageContent("Até logo!")
                       )
                   )

               # Envia os resultados da consulta inline
               await query.answer(results)

   # Executa a função principal
   asyncio.run(main())
   ```

3. **Explicação do Código**:

   - **`@app.on_inline_query()`**:
     - Decorador para registrar um manipulador de eventos para `InlineQuery`. Este manipulador é chamado sempre que um usuário faz uma consulta inline.

   - **`async def inline_query(client, query: InlineQuery):`**:
     - Função que lida com `InlineQuery`. O parâmetro `query` contém informações sobre a consulta inline feita pelo usuário.

   - **`results = []`**: Lista para armazenar os resultados da consulta inline.

   - **Criação de Resultados Inline**:
     - `InlineQueryResultArticle`: Classe para representar um resultado de consulta inline do tipo artigo.
     - `title`: Título do resultado de consulta.
     - `input_message_content`: Conteúdo da mensagem que será enviada quando o usuário selecionar este resultado.

   - **`await query.answer(results)`**:
     - Método para enviar os resultados da consulta inline de volta ao cliente. Isso envia os resultados para o usuário que fez a consulta inline.

4. **Execução**:

   - Ao executar este código, o Pyrogram estará pronto para lidar com consultas inline. Quando um usuário digitar uma consulta inline que contenha "hello" ou "bye", o bot responderá com opções apropriadas.

Certifique-se de personalizar a lógica de criação de resultados de consulta inline (`InlineQueryResultArticle`) conforme necessário para suas necessidades específicas. Isso pode incluir a geração de resultados dinâmicos com base em dados externos ou APIs.
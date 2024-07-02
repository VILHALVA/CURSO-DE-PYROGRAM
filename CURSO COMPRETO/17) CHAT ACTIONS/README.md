# CHAT ACTIONS
Em Pyrogram, para simular ações visuais como "digitando" ou "enviando fotos" em um chat, você pode utilizar os métodos fornecidos pela biblioteca para fornecer uma experiência mais interativa aos usuários. Aqui está como você pode implementar algumas dessas ações:

## Exemplos de Chat Actions com Pyrogram:
1. **Exemplo de Digitando (Typing)**:

   Para indicar que o bot está digitando uma mensagem no chat:

   ```python
   async def send_typing_action(chat_id):
       await app.send_chat_action(chat_id, "typing")
   ```

   - **Explicação**:
     - `app.send_chat_action(chat_id, "typing")`: Este método envia uma ação de "digitando" para o chat especificado (`chat_id`), indicando visualmente para o usuário que o bot está digitando uma mensagem.

2. **Exemplo de Enviando Foto (Uploading Photo)**:

   Para simular o envio de uma foto (ou qualquer mídia) no chat:

   ```python
   async def send_photo_action(chat_id):
       await app.send_chat_action(chat_id, "upload_photo")
   ```

   - **Explicação**:
     - `app.send_chat_action(chat_id, "upload_photo")`: Este método envia uma ação de "enviando foto" para o chat especificado (`chat_id`), proporcionando uma experiência visual ao usuário enquanto o bot está preparando para enviar uma foto.

3. **Exemplo de Enviando Vídeo (Uploading Video)**:

   Para simular o envio de um vídeo (ou qualquer mídia) no chat:

   ```python
   async def send_video_action(chat_id):
       await app.send_chat_action(chat_id, "upload_video")
   ```

   - **Explicação**:
     - `app.send_chat_action(chat_id, "upload_video")`: Este método envia uma ação de "enviando vídeo" para o chat especificado (`chat_id`), indicando que o bot está preparando para enviar um vídeo.

## Como Usar os Exemplos?
Para integrar esses exemplos em seu código Pyrogram, você precisa garantir que está dentro do contexto adequado do cliente Pyrogram (`Client`) e que os métodos de ação de chat são chamados no momento apropriado, geralmente antes de enviar a mensagem real. Aqui está um exemplo mais completo integrando o envio de uma mensagem com ação de "digitando":

```python
from pyrogram import Client
from config import API_ID, API_HASH
import asyncio

async def main():
    async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
        # ID do chat (usuário ou grupo) para onde você deseja enviar a mensagem
        chat_id = "123456789"

        # Enviar ação de "digitando" antes de enviar a mensagem
        await app.send_chat_action(chat_id, "typing")

        # Envie a mensagem real
        await app.send_message(chat_id, "Olá, estou digitando esta mensagem!")

# Executa a função principal
asyncio.run(main())
```

Certifique-se de substituir `chat_id = "123456789"` pelo ID real do chat (usuário ou grupo) para onde você deseja enviar a mensagem com a ação visual. Essas ações ajudam a melhorar a experiência do usuário ao interagir com seu bot, proporcionando feedback visual sobre as atividades em andamento.
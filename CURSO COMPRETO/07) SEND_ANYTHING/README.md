# SEND_ANYTHING 
Para enviar qualquer tipo de conteúdo no Pyrogram, você pode usar o método `send_message` e passar o tipo de conteúdo desejado como parâmetro. Aqui está como você pode enviar diferentes tipos de conteúdos usando Pyrogram:

1. **Importe os Módulos Necessários**:

   Certifique-se de importar os módulos necessários do Pyrogram e suas credenciais do arquivo de configuração:

   ```python
   from pyrogram import Client
   from config import API_ID, API_HASH
   import asyncio
   ```

2. **Defina e Execute a Função Principal**:

   Crie uma função assíncrona principal (`async def main()`) para enviar diferentes tipos de conteúdo:

   ```python
   async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
           # Envia uma mensagem de texto simples
           await app.send_message("me", text="Olá, mundo!")

           # Envia uma foto
           await app.send_photo("me", photo="caminho/para/sua/foto.jpg", caption="Minha foto enviada via Pyrogram!")

           # Envia um documento (arquivo)
           await app.send_document("me", document="caminho/para/seu/documento.pdf", caption="Documento PDF enviado via Pyrogram!")

           # Envia um vídeo
           await app.send_video("me", video="caminho/para/seu/video.mp4", caption="Vídeo enviado via Pyrogram!")

           # Envia uma localização
           await app.send_location("me", latitude=37.7749, longitude=-122.4194, title="Localização de San Francisco", address="San Francisco, CA")

           # Envia um contato
           await app.send_contact("me", phone_number="+1234567890", first_name="John", last_name="Doe")

   # Executa a função principal
   asyncio.run(main())
   ```

3. **Explicação do Código**:

   - **`await app.send_message("me", text="Olá, mundo!")`**: Envia uma mensagem de texto simples para o seu próprio usuário no Telegram.

   - **`await app.send_photo("me", photo="caminho/para/sua/foto.jpg", caption="Minha foto enviada via Pyrogram!")`**: Envia uma foto com legenda para o seu próprio usuário.

   - **`await app.send_document("me", document="caminho/para/seu/documento.pdf", caption="Documento PDF enviado via Pyrogram!")`**: Envia um documento (arquivo) com legenda para o seu próprio usuário.

   - **`await app.send_video("me", video="caminho/para/seu/video.mp4", caption="Vídeo enviado via Pyrogram!")`**: Envia um vídeo com legenda para o seu próprio usuário.

   - **`await app.send_location("me", latitude=37.7749, longitude=-122.4194, title="Localização de San Francisco", address="San Francisco, CA")`**: Envia uma localização geográfica com título e endereço para o seu próprio usuário.

   - **`await app.send_contact("me", phone_number="+1234567890", first_name="John", last_name="Doe")`**: Envia um contato com número de telefone e nome para o seu próprio usuário.

4. **Execução**:

   - Ao executar este código, o Pyrogram enviará cada tipo de conteúdo especificado para o seu próprio usuário no Telegram, conforme definido nos respectivos métodos (`send_message`, `send_photo`, `send_document`, `send_video`, `send_location`, `send_contact`).

Certifique-se de substituir os caminhos de arquivos (`"caminho/para/sua/foto.jpg"`, `"caminho/para/seu/documento.pdf"`, `"caminho/para/seu/video.mp4"`) pelos caminhos reais dos arquivos que você deseja enviar. Isso garantirá que o Pyrogram possa localizar e enviar o conteúdo corretamente.
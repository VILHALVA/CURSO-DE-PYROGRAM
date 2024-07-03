# SEND_PHOTO
Para enviar uma foto usando Pyrogram, você pode usar o método `send_photo` do cliente Pyrogram. Aqui está como você pode fazer isso:

1. **Importe os Módulos Necessários**:

   Certifique-se de importar os módulos necessários do Pyrogram:

   ```python
   from pyrogram import Client
   import asyncio
   ```

2. **Defina e Execute a Função Principal**:

   Crie uma função assíncrona principal (`async def main()`) para enviar uma foto:

   ```python
   async def main():
       # Cria uma instância do cliente Pyrogram
       async with Client("my_account") as app:
           # Envia uma foto para o seu próprio usuário no Telegram
           await app.send_photo("me", photo="caminho/para/sua/foto.jpg", caption="Minha foto enviada via Pyrogram!")

   # Executa a função principal
   asyncio.run(main())
   ```

3. **Explicação do Código**:

   - **`await app.send_photo("me", photo="caminho/para/sua/foto.jpg", caption="Minha foto enviada via Pyrogram!")`**:
     - `app.send_photo`: Método para enviar uma foto.
     - `"me"`: Destinatário da mensagem (nesse caso, você mesmo).
     - `photo="caminho/para/sua/foto.jpg"`: Caminho para a foto que você deseja enviar. Substitua `"caminho/para/sua/foto.jpg"` pelo caminho real da sua foto no sistema de arquivos.
     - `caption="Minha foto enviada via Pyrogram!"`: Legenda opcional para a foto.

4. **Execução**:

   - Ao executar este código, o Pyrogram enviará a foto especificada para o seu próprio usuário no Telegram, com a legenda opcional.

Certifique-se de substituir `"caminho/para/sua/foto.jpg"` pelo caminho real da foto que você deseja enviar. Isso garantirá que o Pyrogram possa localizar e enviar a foto corretamente.


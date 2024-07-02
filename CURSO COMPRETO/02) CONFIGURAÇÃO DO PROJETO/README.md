# CONFIGURAÇÃO DO PROJETO
Nesta etapa, vamos configurar seu projeto para integrar o Pyrogram e prepará-lo para criar seu bot no Telegram. Siga os passos abaixo:

## Passo 1: Obtenção das Credenciais do Telegram
Para interagir com a API do Telegram, você precisa obter as credenciais necessárias (API ID e API Hash). Siga os passos abaixo para obtê-las:

1. **Acesse o site do Telegram**: Vá para [my.telegram.org](https://my.telegram.org) e faça login com seu número de telefone.

2. **Crie uma nova aplicação**: Dentro do site, vá para a seção de desenvolvimento e crie uma nova aplicação. Preencha os campos solicitados, como nome, descrição, etc.

3. **Obtenha suas credenciais**: Após criar a aplicação, você receberá um API ID e um API Hash. Guarde essas informações em um local seguro, pois serão utilizadas em seu projeto.

## Passo 2: Criação do Arquivo de Configuração
1. **Crie um arquivo de configuração**: No diretório do seu projeto, crie um arquivo Python chamado `config.py`.

2. **Adicione suas credenciais**: Dentro do arquivo `config.py`, adicione as credenciais obtidas do passo anterior:
   ```python
   API_ID = "seu_api_id"
   API_HASH = "seu_api_hash"
   ```

   Certifique-se de substituir `"seu_api_id"` e `"seu_api_hash"` pelos valores reais fornecidos pelo Telegram.

## Passo 3: Autorização do Bot no Telegram
Após obter as credenciais (API ID e API Hash) no site do Telegram, o próximo passo é autorizar seu bot para interagir com sua conta. Aqui está como proceder:

### Autorização do Bot
1. **Configure o código inicial**:

   Antes de executar seu bot, é necessário configurar o código inicial com as credenciais obtidas. No arquivo `config.py`, você deve ter algo assim:

   ```python
   API_ID = "seu_api_id"
   API_HASH = "seu_api_hash"
   ```

2. **Execução inicial do bot**:

   Agora, no código Python, você pode usar essas credenciais para iniciar seu bot e autorizá-lo a interagir com sua conta:

   ```python
   import asyncio
   from pyrogram import Client
   from config import API_ID, API_HASH

   async def main():
       async with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
           await app.send_message("me", "Greetings from **Pyrogram**!")

   asyncio.run(main())
   ```

3. **Primeira execução**:

   Ao executar este código pela primeira vez, o Pyrogram abrirá uma janela ou solicitação no terminal para você autorizar o bot:

   - **Solicitação de Autorização**: Quando você executa o bot pela primeira vez, o Pyrogram abrirá uma solicitação de autorização no terminal ou em uma janela separada do navegador, dependendo da sua configuração.

4. **Conclusão da Autorização**:

   - **Clique em "Authorize" (Autorizar)**: Na janela de autorização, clique no botão "Authorize" para conceder permissão ao bot para acessar sua conta do Telegram.
   - **Código de Autorização**: Em seguida, você pode precisar inserir um código de autorização que será enviado para o seu número de telefone associado à sua conta do Telegram, se solicitado.

5. **Bot Autorizado**:

   Depois de concluir esses passos, seu bot estará autorizado e pronto para interagir com sua conta do Telegram. Você pode começar a desenvolver e testar suas funcionalidades usando Pyrogram!

Este processo garante que seu bot tenha permissões adequadas para funcionar corretamente dentro das políticas de segurança e privacidade do Telegram.


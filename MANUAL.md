# MANUAL
## INSTALAÇÃO:
1. **Instale o Python**:
   Certifique-se de ter o Python instalado em seu sistema. Você pode baixar a versão mais recente do Python no [site oficial](https://www.python.org/).

2. **Instale o Pyrogram**:
   Use o pip para instalar a biblioteca Pyrogram. Abra o terminal e execute:
   ```bash
   pip install pyrogram
   ```

3. **Instale o Pyrogram Dependências**:
   Algumas dependências adicionais podem ser necessárias. Instale-as com:
   ```bash
   pip install tgcrypto
   ```

## CONFIGURAÇÃO:
1. **Obtenha um API ID e API Hash**:
   Você precisará de um API ID e API Hash do Telegram para autenticar sua conta. Siga os passos:
   - Vá para [my.telegram.org](https://my.telegram.org).
   - Faça login com seu número de telefone.
   - Crie uma nova aplicação para obter seu API ID e API Hash.

2. **Crie um Arquivo de Configuração**:
   Crie um arquivo chamado `config.py` em seu diretório de projeto e adicione suas credenciais:
   ```python
   API_ID = "sua_api_id"
   API_HASH = "seu_api_hash"
   ```

## CRIANDO O PRIMEIRO BOT:
1. **Configuração do Script do Bot**:
   Crie um arquivo Python chamado `bot.py` e adicione o seguinte código:
   ```python
   from pyrogram import Client, filters

   # Importa as credenciais do arquivo de configuração
   from config import API_ID, API_HASH

   # Cria uma instância do cliente Pyrogram usando seu perfil pessoal
   app = Client("meu_bot", api_id=API_ID, api_hash=API_HASH)

   # Define um manipulador para a mensagem de start
   @app.on_message(filters.command("start"))
   def start(client, message):
       message.reply("Olá! Eu sou um bot criado com Pyrogram.")

   # Inicia o bot
   app.run()
   ```

2. **Executando o Bot**:
   Abra o terminal, navegue até o diretório do seu projeto e execute:
   ```bash
   python bot.py
   ```

3. **Testando o Bot**:
   Abra o Telegram e procure pelo seu bot. Envie a mensagem `/start` e ele deve responder com "Olá! Eu sou um bot criado com Pyrogram."

## CONCLUSÃO:
Você acabou de criar e configurar seu primeiro bot no Telegram usando Pyrogram! A partir daqui, você pode explorar mais funcionalidades da biblioteca para adicionar recursos avançados ao seu bot.
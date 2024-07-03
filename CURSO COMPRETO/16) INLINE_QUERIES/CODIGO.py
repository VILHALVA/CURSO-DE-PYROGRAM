from pyrogram import Client
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
import asyncio

async def main():
    # Cria uma instância do cliente Pyrogram
    async with Client("my_account") as app:
        # Define o manipulador para InlineQuery
        @app.on_inline_query()
        async def inline_query(client, query: InlineQuery):
            results = []

            # Obtém o texto da consulta e converte para minúsculas
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

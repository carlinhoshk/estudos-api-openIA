import os
import openai
openai.api_key = os.getenv("TOKEN_GPT")
arquivos = openai.File.list()

print(arquivos)
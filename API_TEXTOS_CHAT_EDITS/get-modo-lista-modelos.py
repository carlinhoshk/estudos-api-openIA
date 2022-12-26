import os
import openai

openai.api_key = os.getenv("TOKEN_GPT")
lista = openai.Model.list()
print(lista)
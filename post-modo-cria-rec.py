import os
import openai
openai.api_key = os.getenv("TOKEN_GPT")
retorno = openai.Completion.create(
  model="text-davinci-003",
  prompt="Calcule quanto é 3x10 e Fale 'isso é um teste' .",
  max_tokens=22,
  temperature=0
)
texto = retorno["choices"][0]["text"]

texto_sanitizado= texto.replace("\n", "")
print(texto)

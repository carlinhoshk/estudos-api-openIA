import os
import openai
openai.api_key = os.getenv("TOKEN_GPT")
retorno = openai.Edit.create(
  model="text-davinci-edit-001",
  input="What day of the wek is it?",
  instruction="Fix the spelling mistakes"
)
texto = retorno["choices"][0]["text"]

#texto_sanitizado= texto.replace("\n", "")
print(texto)

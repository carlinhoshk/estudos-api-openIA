import os
import openai
openai.api_key = os.getenv("TOKEN_GPT")
retorno = openai.Completion.create(
  model="text-davinci-003",
  prompt=input("Inicie um chat com o modelo text-davinci-003: \n        "),
  max_tokens=22,
  temperature=0
)
texto = retorno["choices"][0]["text"]

texto_sanitizado= texto.replace("\n", "")
print(texto)
with open('API_TEXTOS_CHAT_EDITS/saidas_files/arquivo.txt', 'a') as f:
  f.write(str(texto) + "\n")
exit()

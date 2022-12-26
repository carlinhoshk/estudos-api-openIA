import os
import openai
import urllib.request

openai.api_key = os.getenv("TOKEN_GPT")
retorno = openai.Image.create(
  prompt="Biscoito de chocolate",
  n=2,
  size="1024x1024"
)
print(retorno)
url = retorno["data"][0]["url"]

retorno = urllib.request.urlopen(url)

with open('/home/carlinhoshk/dev/estudos-api-openIA/API_IMAGEM_REMIX/saida-imagem-dados.imagem.jpg', 'wb') as f:
    f.write(retorno.read())
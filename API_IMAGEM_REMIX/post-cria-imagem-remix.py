import os
import openai
import urllib.request

openai.api_key = os.getenv("TOKEN_GPT")
retorno = openai.Image.create(
  prompt="Arvore cortada com grandes raizes",
  n=2,
  size="1024x1024"
)
print(retorno)

# pega o url
url = retorno["data"][0]["url"]

# abre o link do url
imagem_lida = urllib.request.urlopen(url)
# salva a imagem do link
with open('/home/carlinhoshk/dev/estudos-api-openIA/API_IMAGEM_REMIX/saida-imagem-dados/imagem.jpg', 'wb') as f:
    f.write(imagem_lida.read())
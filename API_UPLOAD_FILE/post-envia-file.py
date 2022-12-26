import os
import openai

# envio de um JSON Lines de exemplos de treinamento

openai.api_key = os.getenv("OPENAI_API_KEY")
envia = openai.File.create(
  file=open("mydata.jsonl", "rb"),
  purpose='fine-tune'
)
print(envia)
import os
import openai

# embedding para melhorar modelos e treinamentos 

openai.api_key = os.getenv("TOKEN_GPT")
retorno = openai.Embedding.create(
  model="text-embedding-ada-002",
  input="The food was delicious and the waiter..."
)
print(retorno)
# 23:02 - 25/12/2022 - Programa da documentação para receber info sobre a instancia 
"""Recuperar modelo
PEGUE
https://api.openai.com/v1 /models/{model}

Recupera uma instância de modelo, 
fornecendo informações básicas sobre o modelo, 
como o proprietário e a permissão.

"""

import os
import openai



openai.api_key =  os.getenv("TOKEN_GPT")
arecebimento = openai.Model.retrieve("davinci-search-query")
print(arecebimento)

import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
deleta = openai.File.delete("file-XjGxS3KTG0uNmNOK362iJua3")
print(deleta)
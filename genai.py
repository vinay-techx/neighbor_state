from google import genai
from google.genai import types
import base64

def generate():
  client = genai.Client(
      vertexai=True,
      project="PROJECT_ID",
      location="us-central1",
  )

  response = client.models.generate_content(
      model="gemini-2.0-flash", contents="Explain how AI works in a few words"
  )
  print(response.text)

generate()

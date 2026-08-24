import os
import google
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

def load_prompt():
    with open("prompts/rag_prompt.txt", "r",encoding="utf-8") as f:
        return f.read()
PROMPT_TEMPLATE = load_prompt()
def ask_gemini(question,context):
    prompt = PROMPT_TEMPLATE.format(question=question,context=context)
    response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = prompt
    )
    return response.text
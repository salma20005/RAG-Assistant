# import os
# import google
# from google import genai
# from dotenv import load_dotenv

# load_dotenv()
# client = genai.Client(
#     api_key = os.getenv("GEMINI_API_KEY")
# )

# def load_prompt():
#     with open("prompts/rag_prompt.txt", "r",encoding="utf-8") as f:
#         return f.read()
# PROMPT_TEMPLATE = load_prompt()
# def ask_gemini(question,context):
#     prompt = PROMPT_TEMPLATE.format(question=question,context=context)
#     response = client.models.generate_content(
#         model = 'gemini-3.6-flash',
#         contents = prompt
#     )
#     return response.text



import os
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
def load_llm():
    return ChatGoogleGenerativeAI(api_key=os.getenv("GEMINI_API_KEY"),   model = 'gemini-3.6-flash')
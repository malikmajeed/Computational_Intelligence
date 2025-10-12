from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatOpenAI(
    openai_api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    model="gemini-2.5-flash",
    temperature=0.7
)

def generate_text_with_gemini(prompt: str):
    response = llm.invoke(prompt)
    return response.content

print(generate_text_with_gemini(input("Enter your prompt for Gemini: ")))




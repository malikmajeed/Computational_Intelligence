
# including system and human messages

from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatOpenAI(
    openai_api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    model="gemini-2.5-flash",
    temperature=0.7
)

def generate_text_with_gemini(system_prompt: str, user_prompt: str):
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]
    response = llm.invoke(messages)
    return response.content

system_prompt = "You are a helpful assistant."
user_prompt = input("Enter your prompt for Gemini: ")
print(generate_text_with_gemini(system_prompt, user_prompt))
from dotenv import load_dotenv
from openai import OpenAI
import os #import os module to access environment variables

load_dotenv()  # Load environment variables from .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


#get the base url by searching gemini-openai compatibility api
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     messages=[
#         {"role": "user", 
#          "content": "Write a poem about the sea in the style of Shakespeare."}
#     ]
# )

# print(response.choices[0].message.content)


#Now we will use it in function

def generate_text_with_gemini(prompt:str):
    response = client.chat.completions.create(
        temperature=0.7, #controls randomness/ intellectuality of output
        model="gemini-2.5-flash",
        messages=[
            {"role": "user", 
             "content": prompt}
        ]
    )
    return response.choices[0].message.content



print(generate_text_with_gemini(input("Enter your prompt for Gemini: ")))
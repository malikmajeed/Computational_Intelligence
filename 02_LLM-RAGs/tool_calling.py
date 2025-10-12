from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

tools = [{
    "type":"function",
    "function":{
        "name":"get_weather",
        "description":"Get the weather in a given location",
        "parameters":{
            "type":"object",
            "properties":{
                "location":{
                    "type":"string",
                    "description":"The city and state, e.g. San Francisco, CA"
                },  
            },
            "required":["location"]
        }
    }
}
]

#function to get weather in degree celsius
def get_weather(location: str):
    data = {"Lahore": "32C", "Karachi": "30C", "Islamabad": "28C"}
    return data.get(location, "Location not found")




client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", 
         "content": "Write a poem about the sea in the style of Shakespeare."}
    ],
    tools=tools,
)


message = response.choices[0].message
call_tools = message.tool_calls


if call_tools:
    fn_name = call_tools[0].name
    fn_args = call_tools[0].arguments

    print("Model wants to call:", fn_name, fn_args)

    # step 2: execute function
    result = get_weather(fn_args["location"])
    print("Function result:", result)


    # step 3: send function result back to model
    second_response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            message,
            {"role": "function",
             "name": fn_name,
             "content": result}
        ]
    )
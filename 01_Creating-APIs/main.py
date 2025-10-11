from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

# //creating routes

def student_welcome(name):
    return(f"Hello {name}, welcome to the school!")

@app.get("/")
def any_function_here_but_must():  #one must define a function here else it won't work.
    return student_welcome("Musanif")




# writing function to get input from user



@app.post("/")
#the function as taking city as params
def get_input_from_user(city:str): #the city:str is optional and can be written as city as well. 
    return(f"You've entered {city}")

class Name(BaseModel):
    name: str


@app.post("/data-in-body")
def root(name: Name):

    return {"You entered name": name.name}
    





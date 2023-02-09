# here we are importing all the required modules we need for the ML model
from fastapi import FastAPI
import uvicorn  
from pydantic import BaseModel 
import pickle
from dotenv import load_dotenv
import os

# decoding the Environment Variables 
load_dotenv()

# importing all the environment variables here 
KIDNEY_MODEL = os.environ["KIDNEY"]

# inheriting the model schemas from another python file 
from .model_schemas import kidney

# here we are defining the API structure 
app = FastAPI() # created an object for the FastAPI class 

''' HERE ARE ALL OUR MACHINE LEARNING APIs '''

# this is the kidney machine learning endpoint 
@app.post("/kidney")
async def kidney(data : kidney):
    kidney_model : pickle = pickle.load(open(KIDNEY_MODEL, "rb")) 
    return data 

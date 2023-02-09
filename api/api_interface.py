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
print(type(KIDNEY_MODEL))
# inheriting the model schemas from another python file 
from .model_schemas import kidney
from .model_schemas import heart

# here we are defining the API structure 
app = FastAPI() # created an object for the FastAPI class 

''' HERE ARE ALL OUR MACHINE LEARNING APIs '''

# this is the kidney machine learning endpoint 
@app.post("/kidney")
async def kidney(data : kidney):
    os.chdir(r'C:\Users\admin\Desktop\Technex-2023_AI_Bytes\model_binaries')
    infile = open("kidney.ai",'rb')
    kidney_model = pickle.load(infile)
    d = [[data.bp, data.sg, data.al, data.su, data.rbc, data.pc, data.pcc]]
    prediction = kidney_model.predict(d)[0]
    if prediction == 0: res = "No cancer"
    else: res = "Cancer"
    infile.close()
    return {"Prediction":res}

# this is the heart machine learning endpoint
@app.post("/heart")
async def heart(data: heart ): 
    os.chdir(r'C:\Users\admin\Desktop\Technex-2023_AI_Bytes\model_binaries')
    infile = open("heart.ai", "rb")
    heart_model = pickle.load(infile)
    heart_data = [[data.cp, data.trestbps, data.chol, data.fbs, data.restecg, data.thalach, data.exang]]
    prediction = heart_model.predict(heart_data)[0]
    infile.close()
    if prediction == 0 : res = "You do not have blood cancer"
    else : res = "You have blood cancer"
    return {"Prediction": res}
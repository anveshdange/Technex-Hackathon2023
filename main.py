# improting all the dependencies 
import uvicorn 
import fastapi

# this is the main file of the project
from api.api_interface import app as ML_APP 

if __name__ == "__main__" :
    uvicorn.run("main:ML_APP", port=8000, log_level="info", reload = True )

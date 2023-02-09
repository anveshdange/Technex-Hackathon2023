#importing all the required dependencies 
from pydantic import BaseModel

# here we are defining the input model that we need to get  
class kidney(BaseModel):
    bp: float 
    sg : float
    al : float 
    su : float  
    rbc : float  
    pc :  float  
    pcc : float 

# variable for exporting the data 
# kidney_instance = kidney()  # created an object of the class kidney


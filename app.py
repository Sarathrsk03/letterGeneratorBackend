from fastapi import FastAPI,Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
from datetime import date
from promptToDocx import letterGeneration,createPdf
import os 
from fastapi.staticfiles import StaticFiles
app = FastAPI()


class letterData(BaseModel):
    UUID:int
    date: date
    keywords:list
    receivercity:str
    receivercountry:str
    receiverstate:str 
    recipientAddress: str 
    recipientName: str 
    senderAddress: str 
    senderName: str
    sendercity: str 
    sendercountry: str 
    senderstate: str 
    subject: str
    

app.mount("/letters", StaticFiles(directory="letters", html=True))

@app.post("/create/")
async def letterReceive(create:letterData,request:Request):
    
    data = dict(create)
    UUID = data["UUID"]
    del data["UUID"]
    pr1 = f"{UUID} request received"
    print(pr1)
    letterText = letterGeneration(data)
    pr2 = f"{UUID} response generate"
    print(pr2)
    PDFFileName = createPdf(UUID,letterText)
    pr3 = f"{UUID} pdf generated"
    print(pr3)
    domain = request.base_url
    return str(domain) +"letters/"+str(UUID)+".pdf"

    


   
    



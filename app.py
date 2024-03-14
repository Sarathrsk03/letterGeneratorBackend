

from fastapi import FastAPI,Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
from datetime import date
from promptToDocx import letterGeneration,createPdf
import os 
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ['http://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class letterData(BaseModel):
    uuid:str
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

@app.post("/create")
async def letterReceive(create:letterData,request:Request):
    
    data = dict(create)
    UUID = data["uuid"]
    del data["uuid"]
    pr1 = f"{UUID} request received"
    print(pr1)
    letterText = letterGeneration(data)
    pr2 = f"{UUID} response generate"
    print(pr2)
    PDFFileName = createPdf(UUID,letterText)
    pr3 = f"{UUID} pdf generated"
    print(pr3)
    domain = request.base_url

    #return str(domain) +"letters/"+str(UUID)+".pdf"
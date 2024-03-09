from fastapi import FastAPI, Body
from pydantic import BaseModel,Field
from datetime import date
from promptToDocx import letterGeneration,createPdf


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
    

@app.post("/create/")
async def letterReceive(create:letterData):
    data = dict(create)
    UUID = data["UUID"]
    del data["UUID"]
    letterText = letterGeneration(data)
    PDFFileName = createPdf(UUID,letterText)
    return PDFFileName



    



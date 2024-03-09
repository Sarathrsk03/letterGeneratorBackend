from fastapi import FastAPI, Body
from pydantic import BaseModel,Field
from datetime import date
app = FastAPI()

class letterData(BaseModel):
    date: date
    keywords:list
    receivercity:str
    receivercountry:str
    receiverstate:str 
    receipientAddress: str 
    recipientName: str 
    senderAddress: str 
    senderName: str
    sendercity: str 
    sendercountry: str 
    senderstate: str 
    subject: str
    type: str

@app.post("/create/")
async def letterReceive(create:letterData):
    return create



import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key= os.getenv("GEMINI_API"))
fr = open("test.txt","w")
fr1 = open("prompt.txt","r")

def letterGeneration(preStructuredPromptFile:str,userData:dict):

    

    # Set up the model
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])

    

    prompt = preStructuredPromptFile + str(userData) +"Verify if you have followed all the rules mentioned before generating the response "



    convo.send_message(prompt)
    fr.write(convo.last.text)
    print(convo.last.text)


userData = {"date":"2024-02-24","keywords":["FrontEnd developer","CTC:15 lakhs"],"receivercity":"Chennai","receivercountry":"India","receiverstates":"Tamilnadu","recipientAddress": "Number 18,Liberty Apartments,door number 22, Second Floor Sekar Road","recipientName": "SARATH",
"senderAddress": "18/24 Mayflower Apartments , A4, Third Floor \nNageshwara Road\nNungambakkam","senderName": "Veer", "sendercity": "chennai", "sendercountry": "India","senderstat": "tamilnadu","subject": "Job Offer","type1": "MR"}


str1 = fr1.read()
letterGeneration(str1,userData)





    


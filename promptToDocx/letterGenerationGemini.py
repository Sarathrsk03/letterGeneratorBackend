import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key= os.getenv("GEMINI_API"))


def letterGeneration(data:dict):

    

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

    fileNames = {"ApplicationForATMCard":"/promptToDocx/preStructuredPrompts/atmCard.txt",
                "medicalLeave":"/promptToDocx/preStructuredPrompts/ApplicationForMedicalLeaveToHOD.txt",
                "jobOffer":"/promptToDocx/preStructuredPrompts/jobOffer.txt",
                "ApplicationForReCAT-ReFAT":"/promptToDocx/preStructuredPrompts/recat_refat.txt"}
    
    typeOfLetter = data.get("subject")
    if "\u2060" in typeOfLetter:
        typeOfLetter = typeOfLetter[1:] 
    
    fileLocation=os.getcwd()+fileNames[typeOfLetter]
    preStructuredPromptFile = (open(fileLocation,"r")).read()

    prompt = preStructuredPromptFile + str(data) +"Verify if you have followed all the rules mentioned before generating the response."
    #print(prompt)


    convo.send_message(prompt)
    return convo.last.text






    


# Models and Types
from typing import List
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI, HTTPException

# ---------------------------------------------------------------

# Load Helper Functions
import helper

# Set up the Server
app = FastAPI()


# Define the base models
class SinglishQuote(BaseModel):
    msg: str

class SinglishQuotes(BaseModel):
    quotes: List[SinglishQuote]

class EnglishQuote(BaseModel):
    singlish_message: str
    english_meaning: str
    mood: str
    sentiment: float

class EnglishQuotes(BaseModel):
    quotes: List[EnglishQuote]


@app.get("/")
async def get_root():
    return {"version": "0.0.1"}


@app.post("/singlish/explain")
async def explain_singlish(singlish_quote: SinglishQuote):
    # Rephrase a Singlish message into English.
    try:
        prompt = f"""
        I will provide a message that is in Singlish, and I want to rephrase it in English.
        Return a JSON string in the following format:

        {{
            "english_meaning": "Xxxx",
            "mood": "Yyyy",
            "sentiment": z
        }}

        The key 'english_meaning' contains the rephrased English message in sentence case;
        the key 'mood' contains the mood of the message in sentence case;
        the key 'sentiment' contains a sentiment score between the range of 
        -1 to 1 inclusive with -1 being a negative sentiment and 1 being positive.

        Do not enclose the output in quotes.

        The message is: '{singlish_quote.msg}'
        """
        english_meaning = helper.explain_singlish(prompt, max_tokens = 2000, 
                                                  llm_model = "gpt-3.5-turbo-instruct")

        return english_meaning
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/singlish/explain_list")
async def explain_singlish_list(singlish_quotes: SinglishQuotes):
    # Rephrases a list of Singlish quotes.
    try:
    # Create ab empty list to store the converted quotes.
    #english_quotes = EnglishQuotes(quotes=[])
    #for quote in singlish_quotes.quotes:
        prompt = f"""
        I will provide a list of messages that are in Singlish, and I want to rephrase each message in English.
        Return the output as a list of JSON using the following template:

        {{
            "quotes": [
                {{
                    "singlish_message": "Wxxx",
                    "english_meaning": "Xxxx",
                    "mood": "Yyyy",
                    "sentiment": z
                }},
                {{
                    "singlish_message": "Wxxx",
                    "english_meaning": "Xxxx",
                    "mood": "Yyyy",
                    "sentiment": z
                }}
            ]
        }}
        
        The key 'singlish_message' contains the original Singlish message;
        the key 'english_meaning' contains the rephrased English message in sentence case;
        the key 'mood' contains the mood of the message in sentence case;
        the key 'sentiment' contains a sentiment score between the range of 
        -1 to 1 inclusive with -1 being a most negative sentiment and 1 being most positive.

        Do not enclose the output in quotes.

        The message is: '{singlish_quotes}'
        """
        english_meaning = helper.explain_singlish(prompt, max_tokens = 2000, 
                                                  llm_model = "gpt-3.5-turbo-instruct")
        english_quotes = EnglishQuotes(**english_meaning)

        return english_quotes
    except Exception as e:
        # Handle exceptions
        raise HTTPException(status_code=500, detail=str(e))
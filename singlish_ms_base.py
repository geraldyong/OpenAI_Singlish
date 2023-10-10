# Models and Types

# FastAPI
from fastapi import FastAPI, HTTPException

# ---------------------------------------------------------------

# Load Helper Functions
import helper

# Set up the Server
app = FastAPI()

@app.get("/")
async def get_root():
    return {"version": "0.0.1"}

@app.post("/singlish/explain")
async def explain_singlish(msg: str):
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

        The message is: '{msg}'
        """
        english_meaning = helper.explain_singlish(prompt, max_tokens = 2000, llm_model = "gpt-3.5-turbo-instruct")

        return english_meaning
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

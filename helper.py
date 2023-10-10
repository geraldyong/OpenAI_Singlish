import os
import openai
import re

# ---------------------------------------------------------------

# Helper functions to post-process returned results
def strip_pretext(msg: str) -> str:
    # Find the position of '{'
    pos = msg.find('{')

    # If '{' is found in the string
    if pos != -1:
        # Slice the string from the position of '{' to the end
        result = msg[pos:]
    else:
        # If '{' is not found in the string
        result = msg

    return result

def escape_single_quotes(s: str) -> str:
    # Replace single quotes that are not preceded by a backslash with escaped single quotes
    return re.sub(r"(?<!\\)'", r"\'", s)

def remove_extra_spaces(s: str) -> str:
    # Remove extra spaces
    return re.sub(r"\s+", r" ", s)

def check_ending_brace(s: str) -> str:
    # Check that there is an ending brace
    return s if s.endswith('}') else s + '}'


# OpenAI 
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.organization = os.getenv('OPENAI_ORGANIZATION_ID')

def explain_singlish(prompt, max_tokens, llm_model = "gpt-3.5-turbo-instruct"):
    # Takes a prompt that contains a Singlish message and explain what it means.
    response = openai.Completion.create(
        engine = llm_model,
        prompt=prompt,
        max_tokens = max_tokens
    )

    return eval(check_ending_brace(remove_extra_spaces(strip_pretext(response.choices[0].text.strip()))))

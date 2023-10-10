# OpenAI_Singlish

This repository contains code to create a microservice that takes in Singlish messages and rephrases it in English.

## Prerequisites

* You will need to have an OpenAI API account, with available usage tokens.
* You will also need an API Key, which you can create from https://platform.openai.com/account/api-keys
* Python 3.11 with libraries FastAPI, Pydantic (see requirements.txt)

## Steps to Run Microservice

1. Install the required libraries.
   ```
   pip install -r requirements.txt
   ```
2. Export your OpenAI keys as environment variables.
   ```
   export OPENAI_API_KEY=xxxx
   export OPENAI_API_KEY=yyyy
   ``` 
3. Start up the microservice.
   ```
   uvicorn singlish_ms:app --reload
   ```
4. Load up the browser to point to the link that was listed.
5. Access the `/docs` endpoint.


## Steps to Package As Docker Image

1. Build the docker image.
   ```
   docker build -t singlish:latest .
   ```
2. Bring up the docker serivce.
   ```
   docker compose up -d
   ```
3. Check that the container is up.
   ```
   docker ps -a | grep singlish
   ```

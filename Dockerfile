FROM python:3.11-slim

WORKDIR /app

COPY singlish_ms.py /app
COPY helper.py /app
COPY requirements.txt /app

RUN pip install -r requirements.txt \
    pip install "uvicorn[standard]"

EXPOSE 8000

CMD ["uvicorn", "singlishi_ms:app", "--host", "0.0.0.0", "--reload"]

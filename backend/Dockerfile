FROM python:3.10

WORKDIR /app

COPY ./src src
COPY ./heart-attack-prediction heart-attack-prediction
COPY ./services services
COPY ./requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

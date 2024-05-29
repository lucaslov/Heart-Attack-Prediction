FROM python:3.9

WORKDIR /app

COPY ./src src/fastapi
COPY ./heart-attack-prediction src/heart-attack-prediction
COPY ./services src/services
COPY ./requirements.txt .
COPY ./model.py /src
COPY ./main.py /src
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
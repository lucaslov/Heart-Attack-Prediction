FROM python:3.8
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src .

CMD ["streamlit", "run", "main.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
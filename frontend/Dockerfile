FROM python:3.10
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src .

ENV STREAMLIT_SERVER_RUN_ON_SAVE true
ENV STREAMLIT_SERVER_HEADLESS true

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

FROM python:3.8

WORKDIR /src

COPY ./src /src

RUN pip install streamlit

CMD ["streamlit", "run", "main.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
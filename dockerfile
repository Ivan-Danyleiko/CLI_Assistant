FROM python:3.10-slim

ENV APP_HOME / app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]


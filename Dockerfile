FROM python:3.12.4

RUN apt-get update && \
    apt-get install -y postgresql-client

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app app
COPY run.py .

EXPOSE 5000

CMD [ "python", "run.py"]
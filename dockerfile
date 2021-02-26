FROM python:3.9-slim as production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

COPY requirements/prod.txt ./requirements/prod.txt
RUN pip install -r ./requirements/prod.txt

COPY manage.py ./manage.py
COPY machinelearning ./machinelearning

EXPOSE 8000

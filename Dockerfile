FROM python:3.11.8-slim-bookworm

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN python -m pip install --upgrade pip

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

# COPY . /backend
COPY . .

ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 8000 --reload

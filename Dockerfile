FROM python:3.11.8-slim-bookworm

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN python -m pip install --upgrade pip

RUN pip install uv

COPY ./pyproject.toml pyproject.toml

COPY . .

EXPOSE 8000

ENTRYPOINT ["python", "-m", "uv", "run", "main.py"]

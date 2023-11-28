FROM python:3.10-slim-bookworm

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY docker/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "-m", "app.app"]

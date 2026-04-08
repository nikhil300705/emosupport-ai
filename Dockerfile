FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY inference.py ./inference.py

CMD ["python3", "-u", "inference.py"]
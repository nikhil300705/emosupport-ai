FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY inference.py /app/inference.py

CMD ["python3", "-u", "/app/inference.py"]
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=5000
ENV FLASK_DEBUG=1

CMD ["sh", "-c", "gunicorn -w 1 -b 0.0.0.0:$PORT app:app"]

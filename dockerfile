FROM python:3.12-slim

WORKDIR /app

RUN echo "deb http://deb.debian.org/debian bookworm main" > /etc/apt/sources.list && \
    apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
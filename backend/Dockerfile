FROM python:3.11-alpine

WORKDIR /app

# Instalar dependencias para PostGIS en Alpine
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    geos-dev \
    proj-dev \
    gdal-dev \
    postgresql-dev \
    curl

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

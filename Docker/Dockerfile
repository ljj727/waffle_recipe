FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    libgl1-mesa-glx \
    libglib2.0-0 \
    lsb-release \
    apt-transport-https \
    ca-certificates


WORKDIR /app
COPY .. .
RUN pip install -r requirements.txt

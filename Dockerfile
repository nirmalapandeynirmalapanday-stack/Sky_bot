FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    ffmpeg \
    pulseaudio \
    pulseaudio-utils \
    alsa-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash", "start.sh"]

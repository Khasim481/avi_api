FROM python:3.9-slim-buster

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000 5001 5002

COPY . .

# CMD [ "python", "./open_sky.py" ]
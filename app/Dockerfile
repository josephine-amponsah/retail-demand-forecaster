FROM python:3.9.13

LABEL maintainer "Josephine Amponsah, josephine.amponsah98@gmail.com"

# set working directory in container
WORKDIR C:\Users\HP\Downloads\mybooks\project\retail-optimization\app

# Copy and install packages
COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy app folder to app folder in container
COPY /app /usr/src/app/

# Changing to non-root user
RUN useradd -m appUser
USER appUser

# Run locally on port 8050
CMD waitress-serve --host 127.0.0.1 hello:app

On Sat, Dec 3, 2022 at 7:03 PM Samuel Boafo <sefa.boafo@gmail.com >wrote:
FROM python:3.8.6-slim-buster

LABEL maintainer "Robin Opdam, robinopdam@hotmail.com"

# set working directory in container
WORKDIR /usr/src/app

# Copy and install packages
COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy app folder to app folder in container
COPY /app /usr/src/app/

# Changing to non-root user
RUN useradd -m appUser
USER appUser

# Run locally on port 8050
CMD gunicorn --bind 0.0.0.0:8050 app:serverFROM python:3.8.6-slim-buster

LABEL maintainer "Robin Opdam, robinopdam@hotmail.com"

# set working directory in container
WORKDIR /usr/src/app

# Copy and install packages
COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy app folder to app folder in container
COPY /app /usr/src/app/

# Changing to non-root user
RUN useradd -m appUser
USER appUser

# Run locally on port 8050
CMD gunicorn --bind 0.0.0.0:8050 app:server

On Sat, Dec 3, 2022 at 7:03 PM Samuel Boafo <sefa.boafo@gmail.com >wrote:
FROM python:3.8.6-slim-buster

LABEL maintainer "Robin Opdam, robinopdam@hotmail.com"

# set working directory in container
WORKDIR /usr/src/app

# Copy and install packages
COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy app folder to app folder in container
COPY /app /usr/src/app/

# Changing to non-root user
RUN useradd -m appUser
USER appUser

# Run locally on port 8050
CMD gunicorn --bind 0.0.0.0:8050 app:server

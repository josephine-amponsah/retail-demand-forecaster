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
CMD waitress-serve --host 127.0.0.1 --port 8080 myapp:server

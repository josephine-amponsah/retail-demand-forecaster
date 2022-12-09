FROM python:3.9.13

LABEL maintainer "Josephine Amponsah, josephine.amponsah98@gmail.com"

# ENV APP_HOME /app

# set working directory in container
WORKDIR /usr/src/app
# Copy and install packages
COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt

# Copy app folder to app folder in container
COPY --chown=app:app . ./

# Changing to non-root user
RUN useradd -m appUser
USER appUser

# Run locally on port 8050
CMD waitress-serve --host 127.0.0.1 --port 8080 app:server

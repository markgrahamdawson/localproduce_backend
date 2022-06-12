# Pull base image
FROM --platform=linux/amd64 python:3.10.4-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTOHNDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Set work directory
RUN mkdir /code
RUN mkdir /code/static
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .
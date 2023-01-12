# syntax=docker/dockerfile:1

# Deriving the minima base image
FROM python:3.9-alpine

COPY . /app
WORKDIR /app
COPY ./ressources/integration_test_data.csv ../ressources/integration_test_data.csv
RUN pip install -r ./src/requirements.txt


# Command to run the tests
CMD [ "python3", "./src/app.py"]
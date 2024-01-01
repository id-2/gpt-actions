#!/usr/bin/env python3

# Get the base image
FROM python:3.11-slim as base
ADD . /src
WORKDIR /src

# Make the script executable
RUN chmod +x /src/validate.py

# Install dependencies
RUN pip install pyyaml
RUN pip install yamllint

# Create a new stage for setting up the environment
FROM base as final
WORKDIR /src
ENV PYTHONPATH=/src
CMD [ "python", "/src/validate.py" ]
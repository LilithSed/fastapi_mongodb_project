# Pull the python image
FROM python:3.12.5-slim-bookworm

# The environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Disable PIP caching
ENV PIP_NO_CACHE_DIR=1

# Set working directory
WORKDIR /usr/src

# Create temporary directory and set permissions
RUN mkdir -p ./temp_media && \
    chmod 777 ./temp_media

# Copy requirements file
COPY ops/docker/requirements.txt ./

ENV LOCAL_PATH="/usr/src/setup"
RUN echo "export PYTHONPATH=${PYTHONPATH}:${LOCAL_PATH}" >> ~/.bashrc

# Update sources
RUN apt update --allow-releaseinfo-change && \
    apt install nano -y && \
    apt clean

RUN apt-get update && apt-get install -y \
    ffmpeg \
    && apt-get clean


RUN apt-get install build-essential python3-dev -y

# Copy and install dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy contents to container
COPY . .

# Elevatus permissions for the run file
RUN chmod +x ./ops/scripts/run.sh

# Expose port 8000
EXPOSE 8000

CMD ./ops/scripts/run.sh app

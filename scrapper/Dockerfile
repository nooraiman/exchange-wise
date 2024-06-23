# Use Python slim-buster image as a parent image
FROM python:3.12-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Firefox ESR and Geckodriver
RUN apt-get update && apt-get install -y firefox-esr wget
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz
RUN tar -xvzf geckodriver-v0.34.0-linux64.tar.gz
RUN chmod +x geckodriver
RUN mv geckodriver /usr/local/bin/

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Run wise.py when the container launches
CMD ["python3", "wise.py"]
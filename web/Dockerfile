# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install Flask
RUN pip install flask

RUN mkdir -p /app/templates

# Copy the Flask app to the Docker image
COPY main.py /app/
COPY vendor /app/static/vendor
COPY templates/ /app/templates/

# Set the FLASK_APP environment variable
ENV FLASK_APP=/app/main.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5909"]
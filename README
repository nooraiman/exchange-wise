# Currency Converter

This repository contains tools for currency conversion: a Python script to scrape rates from Wise and save them to `wise.json`, and a Flask web app for conversions. Designed for Docker and Docker Compose, it streamlines deployment and ensures uniformity across environments.

## Overview

The suite consists of two main components:

1. **Currency Converter Scraper**: A Python script (`wise.py`) that uses Selenium to scrape currency conversion rates from the Wise website for various currency pairs.

2. **Currency Converter Web App**: A Flask web application (`main.py`) that provides a simple interface for converting currencies. It accepts query parameters for the amount and currency pair and displays the converted amount on a web page.

## Prerequisites
- Docker
- Docker Compose

## Setup


### Docker and Docker Compose Setup

- Ensure Docker and Docker Compose are installed on your system.
- Use the provided `Dockerfile` and `docker-compose.yml` to build and run the services.

### Modifying Docker Compose Volume Paths
To match your directory structure for data volumes, modify the volumes paths in the docker-compose.yml file. For example, if your data directory is /path/to/your/data, update the volumes as follows:
```
services:
  scrape:
    volumes:
      - /path/to/your/data:/data
  web:
    volumes:
      - /path/to/your/data/wise.json:/app/static/wise.json
```

## Usage

### Running with Docker Compose

To start the application using Docker Compose, run:

```bash
docker-compose up --build
```

Access the application at http://127.0.0.1:5909/ and use query parameters like `?amount=100&currency=USDMYR` to perform conversions. 

Example: http://127.0.0.1:5909/?amount=10&currency=USDMYR


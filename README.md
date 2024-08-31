# San Francisco Food Truck Finder

## Overview
This project provides a way to find nearby food trucks in San Francisco based on a given latitude and longitude. It includes both a command-line interface (CLI) and a web API.

## Features
- **CLI Tool**: Find the nearest food trucks directly from your terminal.
- **Web API**: A RESTful API that returns nearby food trucks in JSON format.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the CLI tool: `python cli.py <latitude> <longitude> --num-trucks <number_of_trucks>`
3. Start the web server: `python app.py`
4. Access the API: `http://127.0.0.1:5000/api/foodtrucks?latitude=<lat>&longitude=<long>&num_trucks=<number_of_trucks>`

## Learning Goals
I typically work on web APIs, but I chose to explore CLI development for this project to broaden my skill set.
# Weather API Project

A simple Django web project that fetches and displays weather information for cities using a 3rd party API (Visual Crossing).

https://roadmap.sh/projects/weather-api-wrapper-service


## Features

- Fetch weather data from a third-party API
- Use environment variables to store API keys securely
- Caching with Redis for better performance (optional)
- Rate limiting to prevent abuse
- Show today's and tomorrow's weather information
- Simple form to input city name



## Requirements

- Python 3.x
- Django
- Django REST Framework
- requests
- python-dotenv
- django-ratelimit
- Redis (for caching)
- Docker (optional, for running Redis)



## Notes
Get a free API key from Visual Crossing if you don't have one.
The .env file is included in .gitignore to avoid committing sensitive data.
Caching and rate limiting improve the performance and security of the application.


## Installation and Setup

1. Clone the repository:

3. pip install -r requirements.txt

3.Create a .env file and add your environment variables:
API_KEY=your_visual_crossing_api_key
REDIS_URL=redis://localhost:6379/0
Run Redis 

4.Start the Django development server:
python manage.py runserver
Open your browser and go to http://localhost:8000/, then enter a city name.

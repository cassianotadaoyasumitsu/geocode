### Flask Geocoding API

## Overview

- This Flask application provides a simple interface to interact with the Google Geocoding API. It includes features for health checking and geocoding addresses. The application uses Flask Caching with Redis to cache the responses, optimizing performance for repeated requests.


## Features

- **Health Check Endpoint**: A basic endpoint to check if the application is running.
- **Geocoding Endpoint**: An endpoint to geocode addresses using the Google Geocoding API, with caching implemented to improve response times for repeated queries.


## Requirements

- Python 3.x
- Flask
- Flask-Caching
- Redis
- Requests


## Installation

1. Clone the repository:
2. Install the required packages:
3. Ensure Redis is installed and running on your machine.


## Configuration

Set the following environment variables for the application:
- `REDIS_HOST`: Hostname for the Redis server.
- `REDIS_PORT`: Port number for the Redis server.
- `CACHE_TTL`: Time-to-live for cache, in seconds.
- `GOOGLE_MAPS_API_GEOCODE_ENDPOINT`: (Optional) Override the default Google Geocoding API endpoint.


## Running the Application

1. Start the Flask application:
    ```
   docker-compose up -d
   ```
2. The application will be available at `http://127.0.0.1:5000`.


### Endpoints

#### Health Check

- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns 'OK' if the application is running.


#### Geocode

- **URL**: `/geocode/json`
- **Method**: `GET`
- **Parameters**:
- `address` (required): The address to geocode.
- `key` (required): Your Google API key.
- **Description**: Returns the geocoded results from the Google Geocoding API. Responses are cached to improve performance.


#### Swagger UI

- **URL**: `/apidocs`


## Error Handling

Errors are returned as JSON with a description of the issue.


## License

This software and its source code are proprietary to Cassiano Tadao Yasumitsu. It may not be used, modified, distributed, or reproduced in any way without express permission. For more information on obtaining a license, please contact.



---


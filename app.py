import os
import requests

from flask import Flask, request, jsonify
from flask_caching import Cache
from flasgger import Swagger, swag_from
from logging import getLogger

from utils.log_filter import GeocodeLogFilter

app = Flask(__name__)
swagger = Swagger(app)

cache = Cache(
    app,
    config={
        "CACHE_TYPE": "RedisCache",
        "CACHE_REDIS_HOST": os.environ.get("REDIS_HOST"),
        "CACHE_REDIS_PORT": os.environ.get("REDIS_PORT"),
        "CACHE_DEFAULT_TIMEOUT": os.environ.get("CACHE_TTL"),
    },
)


getLogger("werkzeug").addFilter(GeocodeLogFilter())


@app.route("/")
@swag_from("swagger/health_check.yml")
def health_check():
    return jsonify({"status": "OK"})


@app.route("/geocode/json", methods=["GET"])
@cache.cached(query_string=True)
@swag_from("swagger/geocode.yml")
def geocode():
    """
        This function caching google maps api responses.
        location example: http://127.0.0.1:5000/geocode/json?address=Eiffel+Tower,+Paris,+France&key=91be9212e0ae86c852de3d78084013c4
    """
    address = request.args.get("address")
    if not address:
        return jsonify({"error": "'address' is required in the query parameters."}), 400

    key = request.args.get("key")
    if not key:
        return jsonify({"error": "'key' is required in the query parameters."}), 400

    resp = requests.get(
        os.environ.get(
            "GOOGLE_MAPS_API_GEOCODE_ENDPOINT",
            "https://maps.googleapis.com/maps/api/geocode/json",
        ),
        {"address": address, "key": key},
    )

    try:
        # Raise an HTTPError for bad responses (4xx or 5xx)
        resp.raise_for_status()
    except Exception as err:
        return (
            jsonify({"error": f"Failed to retrieve geocode data. {err}"}),
            resp.status_code,
        )

    # Return the JSON response from the Google Geocoding API
    return jsonify(resp.json())


if __name__ == "__main__":
    app.run()

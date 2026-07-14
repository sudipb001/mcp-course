"""
api.py

Pure business logic for the REST API MCP Server.

Uses the free JSONPlaceholder service (https://jsonplaceholder.typicode.com)
for demonstration purposes. No API key is required. Later you can
swap this for your own business API — see api_key_example() below
for how credentials should be handled.
"""

import os

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# Example of protecting a real API key: never hard-code it.
# Store it in an environment variable and load it at runtime.
API_KEY = os.getenv("API_KEY")


def get_posts():
    try:
        response = requests.get(f"{BASE_URL}/posts", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        return f"API request failed: {error}"


def get_post(post_id: int):
    try:
        response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        return f"API request failed: {error}"

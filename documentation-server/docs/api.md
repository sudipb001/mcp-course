# Calling REST APIs from MCP

Many practical MCP servers act as a bridge between an AI model and
an external REST API — weather services, GitHub, payment gateways,
or your own company's internal services.

## Basic GET Request

```python
import requests

def get_posts():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        timeout=10
    )
    response.raise_for_status()
    return response.json()
```

## Key Practices

- **Always set a timeout.** Without one, a hung server can make
  your MCP tool wait indefinitely.
- **Always call `raise_for_status()`** (or otherwise check the
  status code) so that HTTP errors surface as exceptions rather
  than silently returning bad data.
- **Catch `requests.RequestException`** to handle network failures
  gracefully instead of crashing the server.
- **Never hard-code API keys.** Load them from environment
  variables with `os.getenv("API_KEY")`.

## Example Error Handling

```python
import requests

def get_posts():
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts",
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        return f"API request failed: {error}"
```

## Why This Matters for AI Clients

REST APIs typically return structured JSON, which AI models can
summarize, transform, or reason about far more reliably than
loosely formatted text. Keeping the JSON structure intact all the
way through your MCP tool gives the AI model the best possible
input to work with.

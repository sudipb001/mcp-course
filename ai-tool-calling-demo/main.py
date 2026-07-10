import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from weather import get_weather

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Returns the current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        },
    }
]

messages = [{"role": "user", "content": "What is the weather in Kolkata?"}]

response = client.chat.completions.create(
    model="gpt-4.1", messages=messages, tools=tools
)

message = response.choices[0].message

if message.tool_calls:

    tool_call = message.tool_calls[0]

    arguments = json.loads(tool_call.function.arguments)

    result = get_weather(arguments["city"])

    messages.append(message)

    messages.append(
        {"role": "tool", "tool_call_id": tool_call.id, "content": json.dumps(result)}
    )

    final_response = client.chat.completions.create(model="gpt-4.1", messages=messages)

    print(final_response.choices[0].message.content)

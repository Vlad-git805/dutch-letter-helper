# OpenAI SDK

## What is OpenAI SDK?

Official Python library for communicating with OpenAI API.

Instead of manually sending HTTP requests, SDK handles:

- Authentication
- HTTPS requests
- JSON serialization
- Response parsing

Example:

```python
client = OpenAI(api_key=...)

response = client.responses.create(...)
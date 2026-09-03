import httpx, json

api_key = "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"
model = "openai/gpt-oss-20b"
base_url = "https://api.groq.com/openai/v1"

client = httpx.Client(base_url=base_url, timeout=30)

system = (
    "You are a shopping agent. Respond ONLY with a single JSON object, no prose or markdown. "
    "Example:\n"
    '{"action": "TOOL_CALL", "tool_name": "search_products", "arguments": {"query": "shoes"}}'
)

messages = [
    {"role": "system", "content": system},
    {"role": "user", "content": "Hi, I'm looking for a Mouse under 2000 rupees"}
]

r = client.post(
    "/chat/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"model": model, "messages": messages, "max_tokens": 500},
)
print(r.status_code)
print(json.dumps(r.json(), indent=2))

import ollama

print("Connecting...")

client = ollama.Client(host="http://127.0.0.1:11434")

print("Sending request...")

response = client.chat(
    model="llama3.2:1b",
    messages=[
        {"role": "user", "content": "Say hello."}
    ]
)

print(response["message"]["content"])
import ollama

class BaseAgent:
    def __init__(self):
        self.model = "llama3.2:1b"

    def ask(self, prompt: str):
        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"]
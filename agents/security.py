from agents.base_agent import BaseAgent

class SecurityAgent(BaseAgent):

    def analyze(self, diff: str) -> str:
        prompt = f"""
You are a cybersecurity expert.

Analyze the following git diff for:

- exposed secrets
- API keys
- unsafe code
- injection vulnerabilities
- missing exception handling
- authentication flaws

Return structured bullet points.

CODE DIFF:
{diff}
"""
        return self.ask(prompt)
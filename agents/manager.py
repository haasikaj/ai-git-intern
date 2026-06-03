from agents.base_agent import BaseAgent

class ManagerAgent(BaseAgent):

    def decide(self, diff: str) -> str:
        prompt = f"""
You are an AI engineering manager.

Decide how to analyze this git diff.

Return:
- which agents are needed (architect, security)
- priority level (low/medium/high)
- focus areas

CODE DIFF:
{diff}
"""
        return self.ask(prompt)
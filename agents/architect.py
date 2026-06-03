from agents.base_agent import BaseAgent

class ArchitectAgent(BaseAgent):

    def analyze(self, diff: str) -> str:
        prompt = f"""
You are a senior software architect.

Analyze the following git diff and identify:

- design issues
- architecture problems
- maintainability risks
- scalability concerns

Return structured bullet points.

CODE DIFF:
{diff}
"""
        return self.ask(prompt)
from agents.base_agent import BaseAgent

class WriterAgent(BaseAgent):

    def summarize(self, architect_review: str, security_review: str) -> str:

        prompt = f"""
You are a technical writer.

Your job is to convert AI analysis into a clean GitHub markdown report.

FORMAT:

# AI Code Review Report

## Architecture Issues
{architect_review}

## Security Issues
{security_review}

## Summary
Write a short, clear summary of all risks and improvements.

Make it clean, structured, and professional.
"""

        return self.ask(prompt)
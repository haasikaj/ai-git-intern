import asyncio
import os

from dotenv import load_dotenv
load_dotenv()

from core.git_parser import get_repo_diff

from agents.architect import ArchitectAgent
from agents.security import SecurityAgent
from agents.writer import WriterAgent


diff = get_repo_diff()

architect = ArchitectAgent()
security = SecurityAgent()
writer = WriterAgent()


async def run_agents():

    print("Running Architect + Security in parallel...")

    loop = asyncio.get_event_loop()

    architect_task = loop.run_in_executor(
        None,
        architect.analyze,
        diff
    )

    security_task = loop.run_in_executor(
        None,
        security.analyze,
        diff
    )

    architect_review, security_review = await asyncio.gather(
        architect_task,
        security_task
    )

    print("Generating final report...")

    final_report = writer.summarize(
        architect_review,
        security_review
    )

    os.makedirs("outputs", exist_ok=True)

    with open("outputs/review.md", "w", encoding="utf-8") as f:
        f.write(final_report)

    print("\n Report saved to outputs/review.md")


if __name__ == "__main__":
    asyncio.run(run_agents())
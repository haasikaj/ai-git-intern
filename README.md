# AI Git Intern — Multi-Agent Code Review System

AI Git Intern is a local multi-agent system that automatically reviews Git changes using Ollama (local LLMs).

It simulates a real engineering team with specialized AI agents:

- Architect Agent → analyzes code structure and design
- Security Agent → detects vulnerabilities and risks
- Writer Agent → generates clean Markdown reports

---

## How it works

1. Reads Git diff from local repository
2. Sends diff to multiple AI agents
3. Each agent performs a specialized review
4. Writer agent combines results into a final report
5. Saves output to `outputs/review.md`

---

## Tech Stack

- Python
- Ollama (Llama 3.2 1B)
- GitPython
- Async Python (for parallel agents)

---

## Output Example

The system generates:

-----------------------------------------------------------------
# AI Code Review Report

## Architecture Issues

This analysis highlights several issues with the current architecture of the AI code:

*   **Maintainability Risks**: The repetitive `run_agents()` function can be refactored into a more modular design. Additionally, there are no tests in place to verify the correctness of individual components or functions.
*   **Scalability Concerns**: The script does not provide information about how it will handle increased load or improve efficiency when scaled horizontally (adding more instances of agents).
*   **Security Issues**: There is an exposure of secrets through API keys, environment variables, and potentially sensitive data. However, proper handling and rotation of these variables are necessary to ensure security.

## Security Issues

The following structured bullet points analyze the exposed secrets:

*   **Exposed Secrets**: No exposed secrets were found.
*   **API Keys**: None of the API keys used in the code have been hardcoded or exposed publicly.
*   **Unsafe Code**: The binary comparison (`==`) is present but not considered a security risk.

## Summary

This analysis suggests that several improvements are necessary to enhance the maintainability, scalability, and security of the AI code:

*   Refactor the repetitive `run_agents()` function into separate components with clear responsibilities.
*   Implement more robust error handling mechanisms in place for API call failures.
*   Explore alternative concurrency models or parallelization techniques to improve efficiency.
*   Ensure proper handling of authentication failures when using environment variables or OAuth token-based authentication.

The overall structure and content are clean, professional, and easy to understand.
----------------------------------------------------------------


Example includes:
- architecture issues
- security vulnerabilities
- final summary report

---

## How to Run

```bash
python main.py

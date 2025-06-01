# agents/developer.py
import os
from .base_agent import BaseAgent
from google.generativeai import GenerativeModel

class DeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(role="developer")
        self.model = GenerativeModel("gemini-2.0-flash")

    def handle_task(self, task: str) -> str:
        prompt = f"""
You are an expert software developer proficient in Html,CSS,Python, JavaScript, Java, and C++.

Given the following task, please provide:

- Clean, production-ready code with comments, OR
- A clear technical explanation if the task is conceptual.

Task:
{task}

If the task does not specify a programming language, please provide the solution in Python by default.

Respond ONLY with the code or explanation—do not add extra commentary.
"""
        response = self.model.generate_content(prompt)
        return response.text.strip()

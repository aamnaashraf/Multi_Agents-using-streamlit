# agents/email_writer.py
import os
from .base_agent import BaseAgent
from google.generativeai import GenerativeModel

class EmailWriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(role="email_writer")  # Call base class constructor
        self.model = GenerativeModel("gemini-2.0-flash")

    def handle_task(self, task: str) -> str:
        prompt = f"""
You are an expert email writer.

Your job is to draft professional, polite, and effective emails based on the user's request.

Task:
{task}

Write the full email:
"""
        response = self.model.generate_content(prompt)
        return response.text.strip()



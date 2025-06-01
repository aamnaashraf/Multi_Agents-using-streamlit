# agents/marketing.py
import os
from .base_agent import BaseAgent
from google.generativeai import GenerativeModel

class MarketingAgent(BaseAgent):
    def __init__(self):
        super().__init__(role="marketing")  # Call base constructor
        self.model = GenerativeModel("gemini-2.0-flash")

    def handle_task(self, task: str) -> str:
        prompt = f"""
You are a digital marketing expert.

Help with marketing strategies, content, social media posts, or ad ideas based on the task.

Task:
{task}

Marketing content or plan:
"""
        response = self.model.generate_content(prompt)
        return response.text.strip()


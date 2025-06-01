# agents/mobile_dev.py
import os
from .base_agent import BaseAgent
from google.generativeai import GenerativeModel

class MobileAppDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(role="mobile_app_developer")  # Call base constructor
        self.model = GenerativeModel("gemini-2.0-flash")

    def handle_task(self, task: str) -> str:
        prompt = f"""
You are an expert mobile app developer (iOS & Android).

Help with design ideas, app features, architecture, or mobile code.

Task:
{task}

Response:
"""
        response = self.model.generate_content(prompt)
        return response.text.strip()


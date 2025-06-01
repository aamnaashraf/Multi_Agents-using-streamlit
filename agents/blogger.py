# agents/blogger.py
import os
from .base_agent import BaseAgent
from google.generativeai import GenerativeModel

class BloggerAgent(BaseAgent):
    def __init__(self):
        super().__init__(role="blogger")  # Base class constructor call
        self.model = GenerativeModel("gemini-2.0-flash")

    def handle_task(self, task: str) -> str:
        prompt = f"""
You are a creative and engaging blog writer.

Write a blog post based on the user's topic or idea. Include an intro, main body, and a short conclusion.

Task:
{task}

Blog post:
"""
        response = self.model.generate_content(prompt)
        return response.text.strip()

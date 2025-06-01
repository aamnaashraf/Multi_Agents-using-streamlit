# agents/base_agent.py
from abc import ABC, abstractmethod
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class BaseAgent(ABC):
    def __init__(self, role):
        self.role = role
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    @abstractmethod
    def handle_task(self, task: str) -> str:
        pass

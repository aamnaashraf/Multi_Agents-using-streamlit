# agents/manager.py
from .email_writer import EmailWriterAgent
from .blogger import BloggerAgent
from .developer import DeveloperAgent
from .marketing import MarketingAgent
from .mobile import MobileAppDeveloperAgent

class ManagerAgent:
    def __init__(self):
        self.agents = {
            "email": EmailWriterAgent(),
            "blogger": BloggerAgent(),
            "developer": DeveloperAgent(),
            "marketing": MarketingAgent(),
            "mobile_app_developer": MobileAppDeveloperAgent()
        }

    def handle_task(self, task: str) -> str:
        task_lower = task.lower()

        # Simple general question handling keywords
        general_keywords = ["hello", "hi", "how are you", "what is your name", "thanks", "thank you"]
        if any(keyword in task_lower for keyword in general_keywords):
            return "Hello! How can I assist you today?"

        # Routing to specific agents based on keywords
        if any(word in task_lower for word in ["email", "write email", "send email", "email content"]):
            agent = self.agents.get("email")
        elif any(word in task_lower for word in ["blog", "write blog", "blog post"]):
            agent = self.agents.get("blogger")
        elif any(word in task_lower for word in ["code", "landing page" "program", "developer", "software", "script" , "HTML" , "CSS", "javascript"]):
            agent = self.agents.get("developer")
        elif any(word in task_lower for word in ["marketing", "advertisement", "ad", "social media", "SEO"]):
            agent = self.agents.get("marketing")
        elif any(word in task_lower for word in ["mobile", "app", "ios", "android"]):
            agent = self.agents.get("mobile_app_developer")
        else:
            return "Sorry, we don't have an agent to handle this task."

        if agent:
            return agent.handle_task(task)
        else:
            return "Sorry, we don't have an agent to handle this task."



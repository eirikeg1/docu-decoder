from typing import List
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
from src.api_integrations.interfaces.llm_generic_interface import LLMGenericInterface


class OpenAIInterface(LLMGenericInterface):
    
    client = None
        
    def __init__(self):
        self.setup()
        
    def setup(self, environment: bool = False):
        if not environment:
            dotenv_path = find_dotenv()
            load_dotenv(dotenv_path)
        
        self.client = OpenAI()
            
            
    
    def sys_message(self, message: str):
        return {"role": "system", "content": message}
    
    def user_message(self, message: str):
        return {"role": "user", "content": message}
    
    prompts = {
        "expert tutor": "You are an expert tutor. Give an extensive and descriptive answer using relevant technical terms and examples.",
        "profile_picture": "Create an avatar of a happy robot tutor in the course {course_name}. Make the robot be the highlight, with a background displaying a simple pattern",
    }
        
      
    def generic_request(self, query: str, params: dict = None, history_key: str = None) -> str | List[str]:
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.prompts["expert tutor"]},
                {"role": "user", "content": query}
            ]
        )
        
        return completion.choices[0].text
        
        
        
        
        

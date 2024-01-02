import os
from src.api_integrations.supabase import create_client, Client
from src.api_integrations.interfaces.database_interface import DataBaseInterface

class SupabaseInterface(DataBaseInterface):
    
    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")

        self.supabase: Client = create_client(url, key)
        
    def add_document(self, document: dict) -> bool:
        pass
    
    def add_paragraph(self, paragraph: dict):
        pass
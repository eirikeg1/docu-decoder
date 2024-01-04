import os
from src.api_integrations.supabase import create_client, Client
from src.api_integrations.interfaces.database_interface import DataBaseInterface
from collections import defaultdict

class SupabaseInterface(DataBaseInterface):
    
    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")

        self.supabase: Client = create_client(url, key)
        
    def add_document(self, document: dict) -> bool:
        """Adds a single document to the database.

        Args:
            document (dict): contains the document metadata and dictionaries containing the paragraphs, keywords, topics, images, and sources

        Returns:
            bool: True if the document was added successfully, False otherwise
        """
        id = document.get("id")
        title = document.get("title")
        author = document.get("author")
        description = document.get("description")
        embedding_model = document.get("embedding_model")
        summary_model = document.get("summary_model")
        hash_value = document.get("hash_value")
        
        document_data = {"id": id, "title": title, "description": description, "hash_value": hash_value}
        
        if author:
            document_data["author"] = author
        if embedding_model:
            document_data["embedding_model"] = embedding_model
        if summary_model:
            document_data["summary_model"] = summary_model
        
        paragraphs = document.get("paragraphs")
        keywords = document.get("keywords")
        topics = document.get("topics")
        images = document.get("images")
        sources = document.get("sources")
        
        
        # POST data
        data, count = self.supabase.table('document').insert(document_data).execute()
    
    def add_paragraph(self, paragraph: dict):
        pass
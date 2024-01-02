import os
from supabase import create_client, Client

class SupabaseInterface:
    
    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")

        supabase: Client = create_client(url, key)
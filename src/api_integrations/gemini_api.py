

from src.api_integrations.interfaces.llm_generic_interface import LLMGenericInterface


class GeminiAPI(LLMGenericInterface):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def get_account_balance(self):
        pass
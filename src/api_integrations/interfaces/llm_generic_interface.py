from abc import abstractmethod


class LLMGenericInterface:
    
    @abstractmethod
    def __init__(self, api_key = None):
        pass
    
    @abstractmethod
    def generic_request(self, query: str, params: dict = None) -> str:
        pass
    
    # @abstractmethod
    def handle_error(self, error: Exception) -> str:
        raise NotImplementedError("Handle error method not implemented")
    
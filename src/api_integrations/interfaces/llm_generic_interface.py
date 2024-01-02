from abc import abstractmethod


class LLMGenericInterface:
    
    @abstractmethod
    def generic_request(self, query: str, params: dict = None, history_key: str = None) -> str:
        pass
    
    @abstractmethod
    def setup(self, environment: bool = False):
        pass
    
    # @abstractmethod
    def handle_error(self, error: Exception) -> str:
        # To add in the future
        raise NotImplementedError("Handle error method not implemented")
    
    @abstractmethod
    def summerize_paragraph(self, text: str) -> str:
        pass
    
from abc import abstractmethod

class DatabaseInterface:
    
    @abstractmethod
    def add_entry(self, entry: dict, key: str = None):
        pass
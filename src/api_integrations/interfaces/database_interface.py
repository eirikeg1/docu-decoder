from abc import abstractmethod

class DatabaseInterface:
    
    @abstractmethod
    def add_document(self, document: dict) -> bool:
        """Adds a single document to the database

        Args:
            document (dict): {id: str?, title: str, paragraphs: List[str]?, course_id: str, author_name: str?}
            
        Returns:
            bool: True if the document was added successfully, False otherwise
        """
        pass
    
    @abstractmethod
    def add_paragraph(self, paragraph: dict):
        pass
    
    
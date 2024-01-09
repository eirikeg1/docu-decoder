from typing import Iterator, List
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTPage
from collections import Counter

# Does not ask LLM to summarize short paragraphs to save resources
MIN_PARAGRAPH_LENGTH = 200

def read_file(file_name: str) -> Iterator[LTPage]:
    """Takes a filepath, extracts the pages with `pdfminer` and returns an iterator over the pages

    Args:
        file_name (str): relative path from where the function is called

    Returns:
        Iterator[LTPage]: Iterator over the pages of the document in PDFMiner's LTPage format
    """
    file = extract_pages(file_name)
    return file
    
    
def get_paragraphs(file: Iterator[LTPage]) -> List[dict]:
    """Takes a file iterator and returns a list of paragraphs

    Args:
        file (Iterator[LTPage]): Takes a document as returned by `read_file`

    Returns:
        List[dict]: Returns list of dicts with keys: id, page, paragraph
    """
    paragraphs = []
    page_num = 0
    paragraph_id = 0
    
    for page_layout in file:
        page_num += 1
        
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                paragraphs.append({
                    'id': paragraph_id,
                    'page': page_num,
                    'paragraph': element.get_text()
                })
                paragraph_id += 1
                
    return paragraphs

def get_terms(file: Iterator[LTPage]) -> List[dict]:
    pass

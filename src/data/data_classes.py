from dataclasses import dataclass, astuple

@dataclass
class Paragraph:
    number: int
    page: int
    paragraph: str

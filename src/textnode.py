from enum import  Enum

class TextType(Enum):
    TEXT = "text" # for plain text
    BOLD = "bold" # for **bold text**
    ITALIC = "italic" # for _italic text_
    CODE = "code"  # for `code text`
    LINK = "link" # for [anchor text](url)
    IMAGE = "image"  # for ![alt text](url)



class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode(text: {self.text}, text_type: {self.text_type.value}, url: {self.url})"




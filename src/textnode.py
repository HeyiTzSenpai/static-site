from enum import  Enum
from src.leafnode import LeafNode


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

    @staticmethod
    def text_node_to_html_node(text_node):
        if text_node.text_type not in TextType.__members__.values():
            raise ValueError(f"invalid text type: {text_node.text_type}")
        text = text_node.text
        text_type = text_node.text_type
        url = text_node.url
        if text_type == TextType.TEXT:
            return LeafNode(None, text)
        elif text_type == TextType.BOLD:
            return LeafNode("b", text)
        elif text_type == TextType.ITALIC:
            return LeafNode("i", text)
        elif text_type == TextType.CODE:
            return LeafNode("code", text)
        elif text_type == TextType.LINK:
            return LeafNode("a", text,  {"href": url})
        elif text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src": url, "alt": text})





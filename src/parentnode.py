from src.htmlnode import  HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag = tag, children = children, props = props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All Parent nodes must have a tag.")
        if self.children is None or len(self.children) == 0:
            raise ValueError("All Parent nodes must have children.")

        #render recursively all child HTML strings
        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        props_str = self.props_to_html()
        if props_str:
            return f"<{self.tag} {props_str}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}>{children_html}</{self.tag}>"










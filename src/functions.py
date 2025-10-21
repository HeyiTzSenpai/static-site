import re
from src.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_list = node.text.split(delimiter)

        if len(split_list) % 2 == 0:
            raise ValueError("Invalid Markdown syntax")

        for i in range(0, len(split_list)):
            if split_list[i] == "":
                continue
            if i % 2 == 0:
                normal_text = split_list[i]
                new_nodes.append(TextNode(normal_text, TextType.TEXT))
            else:
                special_text = split_list[i]
                new_nodes.append(TextNode(special_text, text_type))

    return new_nodes


def extract_markdown_images(text: str):
    # Matches ![alt text](url)
    return re.findall(r"!\[([^\]]+)]\(([^)]+)\)", text)



def extract_markdown_links(text: str):
    # Matches [text](url) that are NOT preceded by !
    return re.findall(r"(?<!!)\[([^\]]+)]\(([^)]+)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        # Only text nodes are split — leave others intact
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        image_markdown = extract_markdown_images(text)

        # No images in this node → just keep it
        if len(image_markdown) == 0:
            new_nodes.append(node)
            continue

        # Otherwise, process each image found
        remaining_text = text
        for alt, url in image_markdown:
            image_markdown_str = f"![{alt}]({url})"
            parts = remaining_text.split(image_markdown_str, 1)
            before = parts[0]

            # Add the text that appears before the image
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            # Add the actual image node
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            # Continue with what’s left after this image
            remaining_text = parts[1] if len(parts) > 1 else ""

        # Add anything that remains at the end
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    pattern = r"(?<!\!)\[([^\[\]]+)\]\(([^\(\)]+)\)"

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = list(re.finditer(pattern, text))
        if not matches:
            new_nodes.append(node)
            continue

        last_index = 0
        for match in matches:
            start, end = match.span()
            alt, url = match.groups()

            # text before this link
            before = text[last_index:start]
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            # the link node itself
            new_nodes.append(TextNode(alt, TextType.LINK, url))
            last_index = end

        # any trailing text after the last link
        after = text[last_index:]
        if after:
            new_nodes.append(TextNode(after, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    # Start with one big TEXT node
    nodes = [TextNode(text, TextType.TEXT)]

    # Inline code: `code`
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    # Bold: **text**
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    # Italic: _text_
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    # Images: ![alt](url)
    nodes = split_nodes_image(nodes)
    # Links: [text](url)
    nodes = split_nodes_link(nodes)

    return nodes







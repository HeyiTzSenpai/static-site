import unittest
from src.functions import split_nodes_delimiter, extract_markdown_links, extract_markdown_images, text_to_textnodes
from src.textnode import TextNode, TextType


class TestFunctions(unittest.TestCase):

    def test_split_nodes_delimiter_code_single_instance(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

        # 🔹 Test for double-delimiter (like bold text with **)

    def test_split_nodes_delimiter_double_instance(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

        # 🔹 Test for triple-delimiter (like markdown-style ```code block```)

    def test_split_nodes_delimiter_triple_instance(self):
        node = TextNode("This is text with a ```code block``` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "```", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com)"
        )
        self.assertListEqual(
            [("link", "https://www.google.com")],
            matches
        )

    def test_extract_markdown_links_mixed(self):
        text = (
            "Here is a [link](https://example.com) "
            "and an ![image](https://i.imgur.com/image.png)"
        )
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [("link", "https://example.com")],
            matches
        )

        # 🔹 Test simple plain text (no Markdown formatting)
        def test_plain_text(self):
            text = "This is just plain text."
            expected = [TextNode("This is just plain text.", TextType.TEXT)]
            self.assertListEqual(text_to_textnodes(text), expected)

        # 🔹 Test complex Markdown example with all features
        def test_full_markdown_text(self):
            text = (
                "This is **bold** _italic_ and `code` "
                "with ![image alt](https://example.com/image.png) "
                "and a [link](https://boot.dev)"
            )
            expected = [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" with ", TextType.TEXT),
                TextNode("image alt", TextType.IMAGE, "https://example.com/image.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
            self.assertListEqual(text_to_textnodes(text), expected)

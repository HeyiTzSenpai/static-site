import unittest

from src.htmlnode import  HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple(self):
        node = HTMLNode("p", "Hello World", None, {"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        expected = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(result, expected)

    def test_props_to_html_single(self):
        node = HTMLNode("p", None, None, {"src": "image.png"})
        result = node.props_to_html()
        expected = 'src="image.png"'
        self.assertEqual(result, expected)

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Hello")
        result = node.props_to_html()
        expected = ""
        self.assertEqual(result, expected)
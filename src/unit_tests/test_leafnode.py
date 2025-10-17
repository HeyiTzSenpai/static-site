import unittest
from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_no_props(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_props(self):
        """Should include HTML attributes when props are provided"""
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_no_tag_returns_value(self):
        """Should return just the text if tag is None"""
        node = LeafNode(None, "Just text.")
        self.assertEqual(node.to_html(), "Just text.")

    def test_to_html_raises_if_value_missing(self):
        """Should raise ValueError if value is None"""
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()



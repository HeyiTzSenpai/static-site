import unittest

from textnode import  TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq2(self):
        node = TextNode("this is a text node", TextType.IMAGE)
        node2 = TextNode("this is a text node", TextType.IMAGE)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
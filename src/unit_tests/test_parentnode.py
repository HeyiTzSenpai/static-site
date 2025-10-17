import unittest

from src.parentnode import ParentNode
from src.leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_htlm_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node =ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_no_children(self):
        parent_node = ParentNode("b", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()


    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node] )
        with self.assertRaises(ValueError):
            parent_node.to_html()





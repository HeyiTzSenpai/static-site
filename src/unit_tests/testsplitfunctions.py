import unittest
from src.htmlnode import HTMLNode
from src.textnode import TextNode, TextType
from src.functions import split_nodes_image, split_nodes_link


class TestSplitFunctions(unittest.TestCase):
    # 🔹 Single test with multiple images
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) "
            "and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    # 🔹 Image at the beginning
    def test_split_images_starts_with_image(self):
        node = TextNode(
            "![first](https://img1.png) and then some text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("first", TextType.IMAGE, "https://img1.png"),
                TextNode(" and then some text", TextType.TEXT),
            ],
            new_nodes,
        )

    # 🔹 Image at the end
    def test_split_images_ends_with_image(self):
        node = TextNode(
            "Here is one ![only](https://img1.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Here is one ", TextType.TEXT),
                TextNode("only", TextType.IMAGE, "https://img1.png"),
            ],
            new_nodes,
        )

    # 🔹 Multiple links in one string
    def test_split_links(self):
        node = TextNode(
            "This is text with a [boot dev](https://www.boot.dev) "
            "and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )

    # 🔹 Link at beginning and end of text
    def test_split_links_beginning_and_end(self):
        node = TextNode(
            "[start link](https://start.com) middle [end link](https://end.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("start link", TextType.LINK, "https://start.com"),
                TextNode(" middle ", TextType.TEXT),
                TextNode("end link", TextType.LINK, "https://end.com"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
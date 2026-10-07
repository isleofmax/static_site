
import unittest

from utilities import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_code_nodes(self):
        node = node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
            ]
        )

    def test_bold_nodes(self):
        node = node = TextNode("This is text with a *bold block*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertListEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            ]
        )

    def test_italic_nodes(self):
        node = node = TextNode("_Italic block_ here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(new_nodes, [
            TextNode("Italic block", TextType.ITALIC),
            TextNode(" here", TextType.TEXT)
            ]
        )


class ExtractImagesLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_images(
                "This is text with an [link](https://www.google.it)"
        )
        self.assertListEqual([("link", "https://www.google.it")], matches)

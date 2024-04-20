import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p")
        node2 = HTMLNode("p")
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("a", "Click me!", None, {"href": "https://www.google.com", "target": "_blank"})
        s = node.props_to_html()
        self.assertEqual(s, ' href="https://www.google.com" target="_blank" ')

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        output = node.to_html()
        sample = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(output, sample)
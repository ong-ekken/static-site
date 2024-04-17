import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p")
        node2 = HTMLNode("p")
        self.assertEqual(node, node2)
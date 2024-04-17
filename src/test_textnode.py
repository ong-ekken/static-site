import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_type_unequal(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)

    def test_text_unequal(self):
        node = TextNode("This is a text ndoe", None)
        node2 = TextNode(123, None)
        self.assertNotEqual(node, node2)

if __name__=="__main__":
    unittest.main()

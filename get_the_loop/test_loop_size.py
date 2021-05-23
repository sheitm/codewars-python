from unittest import TestCase

from solution import Node
from solution import loop_size

class TestLoop_size(TestCase):
    def test_loop_size_small(self):
        node1 = Node()
        node2 = Node()
        node3 = Node()
        node4 = Node()
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2
        size = loop_size(node1)
        self.assertEqual(3, size, f"Expected loop size 3, got {size}.")

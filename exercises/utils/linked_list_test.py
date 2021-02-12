import unittest
import hypothesis.strategies as st
from hypothesis import given
from linked_list import make_linked_list, linked_list_to_list


class Test(unittest.TestCase):
    def test_1(self):
        values = [3, 9, 20]
        head = make_linked_list(values)
        linked_list_values = linked_list_to_list(head)
        self.assertEqual(head.val, 3)
        self.assertEqual(head.next.val, 9)
        self.assertEqual(head.next.next.val, 20)
        self.assertEqual(head.next.next.next, None)
        self.assertEqual(values, linked_list_values)

    def test_2(self):
        values = [3]
        head = make_linked_list(values)
        linked_list_values = linked_list_to_list(head)
        self.assertEqual(head.val, 3)
        self.assertEqual(head.next, None)
        self.assertEqual(values, linked_list_values)

    @given(st.lists(st.integers()))
    def test_random(self, values):
        head = make_linked_list(values)
        linked_list_values = linked_list_to_list(head)
        self.assertEqual(values, linked_list_values)


if __name__ == "__main__":
    unittest.main()

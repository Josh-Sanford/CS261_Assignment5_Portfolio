import unittest

from a5_include import DynamicArray
from min_heap import MinHeap


class MyTestCase(unittest.TestCase):
    def test_add_ex1(self):
        h = MinHeap()
        print(h, h.is_empty())
        for value in range(300, 200, -15):
            h.add(value)
            print(h)

    def test_add_ex2(self):
        h = MinHeap(['fish', 'bird'])
        print(h)
        for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
            h.add(value)
            print(h)

    def test_get_min_ex1(self):
        h = MinHeap(['fish', 'bird'])
        print(h)
        print(h.get_min(), h.get_min())

    def test_remove_min_ex1(self):
        h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
        while not h.is_empty():
            print(h, end=' ')
            print(h.remove_min())

    def test_build_heap_ex1(self):
        da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
        h = MinHeap(['zebra', 'apple'])
        print(h)
        h.build_heap(da)
        print(h)
        da.set_at_index(0, 500)
        print(da)
        print(h)


if __name__ == '__main__':
    unittest.main()

# Course: CS261 - Data Structures
# Assignment: 5 Part 2
# Student: Josh Sanford
# Description: This file implements a min heap data structure


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new object to the min heap, following min heap properties.
        """
        self.heap.append(node)
        index = self.heap.length() - 1
        parent_index = (index - 1) // 2
        while self.heap.get_at_index(parent_index) > self.heap.get_at_index(index) and index > 0:
            self.heap.swap(parent_index, index)
            index = parent_index
            parent_index = (index - 1) // 2

    def get_min(self) -> object:
        """
        Returns the node with the minimum key without removing it from the heap. Raises exception if heap is empty.
        """
        if self.is_empty():
            raise MinHeapException
        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Returns the minimum node and removes it from the heap.
        """
        if self.is_empty():
            raise MinHeapException
        if self.heap.length() == 1:
            return self.heap.pop()
        min_key = self.get_min()
        self.heap.set_at_index(0, self.heap.pop())
        left_child_index = (2 * 0) + 1
        right_child_index = (2 * 0) + 2
        replacement_index = 0
        while not self.is_empty():
            replacement = self.heap.get_at_index(replacement_index)
            if left_child_index < self.heap.length():
                left_child = self.heap.get_at_index(left_child_index)
            else:
                left_child = None
            if right_child_index < self.heap.length():
                right_child = self.heap.get_at_index(right_child_index)
            else:
                right_child = None
            if left_child is None and right_child is None:
                break
            # find minimum child and percolate if needed
            # if only left child
            if left_child is not None and right_child is None:
                if replacement > left_child:
                    self.heap.swap(replacement_index, left_child_index)
                break
            # if left child is minimum child
            elif left_child < right_child:
                if replacement > left_child:
                    self.heap.swap(replacement_index, left_child_index)
                    replacement_index = left_child_index
                    left_child_index = (2 * replacement_index) + 1
                    right_child_index = (2 * replacement_index) + 2
            # if right child is minimum child
            elif left_child > right_child:
                if replacement > right_child:
                    self.heap.swap(replacement_index, right_child_index)
                    replacement_index = right_child_index
                    left_child_index = (2 * replacement_index) + 1
                    right_child_index = (2 * replacement_index) + 2
        return min_key

    def build_heap(self, da: DynamicArray) -> None:
        """
        Builds a heap from the given DynamicArray object, replacing the current heap.
        """
        # copy the contents of the new array to the heap's array
        for i in range(da.length()):
            if i >= self.heap.length():
                self.heap.append(da.get_at_index(i))
            else:
                self.heap.set_at_index(i, da.get_at_index(i))

        n = self.heap.length()  # total number of nodes
        index = (n // 2) - 1    # first non-leaf element
        while index >= 0:
            left_child_index = (2 * index) + 1
            right_child_index = (2 * index) + 2
            cur = self.heap.get_at_index(index)
            if left_child_index < self.heap.length():
                left_child = self.heap.get_at_index(left_child_index)
            else:
                left_child = None
            if right_child_index < self.heap.length():
                right_child = self.heap.get_at_index(right_child_index)
            else:
                right_child = None
            # percolate non-leaf element down its subtree
            if left_child < right_child:  # if left child is minimum child
                if cur > left_child:
                    self.heap.swap(index, left_child_index)
                index -= 1
            elif right_child < left_child:  # if right child is minimum child
                if cur > right_child:
                    self.heap.swap(index, right_child_index)
                index -= 1


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)

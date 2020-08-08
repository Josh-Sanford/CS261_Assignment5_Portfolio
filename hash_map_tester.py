import unittest
from hash_map import HashMap, hash_function_1, hash_function_2


class MyTestCase(unittest.TestCase):
    def test_get_keys(self):
        hash_map = HashMap(10, hash_function_1)
        print(hash_map)
        print(hash_map.contains_key(5))


if __name__ == '__main__':
    unittest.main()

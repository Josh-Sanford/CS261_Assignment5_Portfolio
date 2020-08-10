import unittest
from hash_map import HashMap, hash_function_1, hash_function_2


class MyTestCase(unittest.TestCase):
    def test_put_and_contains_key(self):
        hash_map = HashMap(100, hash_function_1)
        hash_map.put("a", 1)
        print(hash_map)
        print(hash_map.contains_key("a"))
        self.assertTrue(hash_map.contains_key("a"))

    def test_put_ex1(self):
        m = HashMap(50, hash_function_1)
        for i in range(150):
            m.put('str' + str(i), i * 100)
            if i % 25 == 24:
                print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


if __name__ == '__main__':
    unittest.main()

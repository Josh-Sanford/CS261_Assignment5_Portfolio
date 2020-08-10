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

    def test_get_keys(self):
        hash_map = HashMap(3, hash_function_1)
        hash_map.put("key 1", "1")
        hash_map.put("key 2", "2")
        hash_map.put("key 3", "3")
        hash_map.put("key 4", "4")
        print(hash_map.get_keys())

    def test_get_keys_ex1(self):
        m = HashMap(10, hash_function_2)
        for i in range(100, 200, 10):
            m.put(str(i), str(i * 10))
        print(m.get_keys())

        m.resize_table(1)
        print(m.get_keys())

        m.put('200', '2000')
        m.remove('100')
        m.resize_table(2)
        print(m.get_keys())


if __name__ == '__main__':
    unittest.main()

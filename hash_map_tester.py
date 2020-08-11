import unittest
from hash_map import HashMap, hash_function_1, hash_function_2


class MyTestCase(unittest.TestCase):
    def test_clear(self):
        hash_map = HashMap(5, hash_function_1)
        hash_map.put("key 1", "1")
        hash_map.put("key 2", "2")
        hash_map.put("key 3", "3")
        print("size:", hash_map.size, "capacity:", hash_map.capacity)
        print(hash_map)
        hash_map.clear()
        print("size:", hash_map.size, "capacity:", hash_map.capacity)
        print(hash_map)

    def test_clear_ex1(self):
        m = HashMap(100, hash_function_1)
        print(m.size, m.capacity)
        m.put('key1', 10)
        m.put('key2', 20)
        m.put('key1', 30)
        print(m.size, m.capacity)
        m.clear()
        print(m.size, m.capacity)

    def test_clear_ex2(self):
        m = HashMap(50, hash_function_1)
        print(m.size, m.capacity)
        m.put('key1', 10)
        print(m.size, m.capacity)
        m.put('key2', 20)
        print(m.size, m.capacity)
        m.resize_table(100)
        print(m.size, m.capacity)
        m.clear()
        print(m.size, m.capacity)

    def test_get(self):
        hash_map = HashMap(10, hash_function_2)
        for i in range(1, 31):
            hash_map.put('key' + str(i), i)
        print(hash_map)
        value = hash_map.get("key25")
        print("value =", value)
        self.assertEqual(value, 25)
        value = hash_map.get("key18")
        print("value =", value)
        self.assertEqual(value, 18)
        value = hash_map.get("key2")
        print("value =", value)
        self.assertEqual(value, 2)
        value = hash_map.get("key9")
        print("value =", value)
        self.assertEqual(value, 9)
        value = hash_map.get("key50")
        print("value =", value)
        self.assertEqual(value, None)

    def test_get_ex1(self):
        m = HashMap(30, hash_function_1)
        print(m.get('key'))
        m.put('key1', 10)
        print(m.get('key1'))

    def test_get_ex2(self):
        m = HashMap(150, hash_function_2)
        for i in range(200, 300, 7):
            m.put(str(i), i * 10)
        print(m.size, m.capacity)
        for i in range(200, 300, 21):
            print(i, m.get(str(i)), m.get(str(i)) == i * 10)
            print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    def test_remove(self):
        hash_map = HashMap(10, hash_function_2)
        for i in range(1, 31):
            hash_map.put('key' + str(i), i)
        print("size:", hash_map.size, "capacity:", hash_map.capacity)
        print(hash_map)
        self.assertTrue(hash_map.contains_key('key4'))
        hash_map.remove('key4')
        print("size:", hash_map.size, "capacity:", hash_map.capacity)
        print(hash_map)
        self.assertFalse(hash_map.contains_key('key4'))

    def test_remove_ex1(self):
        m = HashMap(50, hash_function_1)
        print(m.get('key1'))
        m.put('key1', 10)
        print(m.get('key1'))
        m.remove('key1')
        print(m.get('key1'))
        m.remove('key4')

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

    def test_put_ex2(self):
        m = HashMap(40, hash_function_2)
        for i in range(50):
            m.put('str' + str(i // 3), i * 100)
            if i % 10 == 9:
                print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    def test_contains_key_ex1(self):
        m = HashMap(50, hash_function_1)
        print(m.contains_key('key1'))
        m.put('key1', 10)
        m.put('key2', 20)
        m.put('key3', 30)
        print(m.contains_key('key1'))
        print(m.contains_key('key4'))
        print(m.contains_key('key2'))
        print(m.contains_key('key3'))
        m.remove('key3')
        print(m.contains_key('key3'))

    def test_contains_key_ex2(self):
        m = HashMap(75, hash_function_2)
        keys = [i for i in range(1, 1000, 20)]
        for key in keys: m.put(str(key), key * 42)
        print(m.size, m.capacity)
        result = True
        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(result)

    def test_empty_buckets_ex1(self):
        m = HashMap(100, hash_function_1)
        print(m.empty_buckets(), m.size, m.capacity)
        m.put('key1', 10)
        print(m.empty_buckets(), m.size, m.capacity)
        m.put('key2', 20)
        print(m.empty_buckets(), m.size, m.capacity)
        m.put('key1', 30)
        print(m.empty_buckets(), m.size, m.capacity)
        m.put('key4', 40)
        print(m.empty_buckets(), m.size, m.capacity)

    def test_empty_buckets_ex2(self):
        m = HashMap(50, hash_function_1)
        for i in range(150):
            m.put('key' + str(i), i * 100)
            if i % 30 == 0:
                print(m.empty_buckets(), m.size, m.capacity)

    def test_table_load(self):
        hash_map = HashMap(10, hash_function_2)
        for i in range(1, 31):
            hash_map.put('key' + str(i), i)
        print(hash_map)
        print(hash_map.table_load())
        self.assertTrue(3.0, hash_map.table_load())

    def test_table_load_ex1(self):
        m = HashMap(100, hash_function_1)
        self.assertEqual(m.table_load(), 0.0)
        m.put('key1', 10)
        self.assertEqual(m.table_load(), 0.01)
        m.put('key2', 20)
        self.assertEqual(m.table_load(), 0.02)
        m.put('key1', 30)
        self.assertEqual(m.table_load(), 0.02)

    def test_table_load_ex2(self):
        m = HashMap(50, hash_function_1)
        for i in range(50):
            m.put('key' + str(i), i * 100)
            if i % 10 == 0:
                print(m.table_load(), m.size, m.capacity)

    def test_resize_table(self):
        hash_map = HashMap(10, hash_function_2)
        for i in range(1, 31):
            hash_map.put('key' + str(i), i)
        print("size:", hash_map.size, "capacity:", hash_map.capacity)
        print(hash_map)
        hash_map.resize_table(20)
        print("size:", hash_map.size, "capacity:", hash_map.capacity)
        print(hash_map)
        hash_map.resize_table(5)
        print("size:", hash_map.size, "capacity:", hash_map.capacity)
        print(hash_map)

    def test_resize_table_ex1(self):
        m = HashMap(20, hash_function_1)
        m.put('key1', 10)
        print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
        m.resize_table(30)
        print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))

    def test_resize_table_ex2(self):
        m = HashMap(75, hash_function_2)
        keys = [i for i in range(1, 1000, 13)]
        for key in keys:
            m.put(str(key), key * 42)
        print(m.size, m.capacity)

        for capacity in range(111, 1000, 117):
            m.resize_table(capacity)
            m.put('some key', 'some value')
            result = m.contains_key('some key')
            m.remove('some key')
            for key in keys:
                result &= m.contains_key(str(key))
                result &= not m.contains_key(str(key + 1))
            print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))

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

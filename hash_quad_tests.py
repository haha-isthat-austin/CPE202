import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        print('horner hash result: ', ht.horner_hash(('cat')))
        print('test 1e hash table: ', ht.hash_table)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_horny_hasher(self):
        ht = HashTable(5)
        ht.insert('a', 0)
        print('test 02 post a insert: ', ht.hash_table)
        print('horner hash of a: ', ht.horner_hash('a'))
        ht.insert('f', 0)
        print('horner hash of f: ', ht.horner_hash('f'))
        print('test 02 post f insert: ', ht.hash_table)
        self.assertEqual(ht.get_index('f'), 3)

    def test_02(self):
        ht = HashTable(5)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 2)
        print('test 02 post a insert: ', ht.hash_table)
        ht.insert("f", 0)
        self.assertEqual(ht.get_index("f"), 3)
        ht.insert("k", 0) #causes rehash
        self.assertEqual(ht.get_index("a"), 9)
        self.assertEqual(ht.get_index("f"), 3)
        self.assertEqual(ht.get_index("k"), 8)
        print(ht.hash_table)

if __name__ == '__main__':
   unittest.main()

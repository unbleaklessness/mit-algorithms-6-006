import unittest
from random import shuffle
from insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        xs = list(range(100))
        expected = sorted(xs)
        for _ in range(100):
            shuffle(xs)
            xs_sorted = insertion_sort(xs)
            self.assertEqual(xs_sorted, expected)

if __name__ == '__main__':
    unittest.main()
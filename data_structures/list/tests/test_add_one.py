import unittest
from data_structures.list.src.list import add_one


class AddOneTests(unittest.TestCase):
    def test_empty_list(self):
        """ Test empty list to return empty list as result """
        input_arr = []

        result = add_one(input_arr)

        self.assertEqual([], result)

    def test_0(self):
        arr = ['0']
        result = add_one(arr)

        self.assertEqual(['1'], result)

    def test_1(self):
        arr = ['1']

        result = add_one(arr)

        self.assertEqual(['2'], result)

    def test_999(self):
        arr = ['9', '9', '9']

        result = add_one(arr)

        self.assertEqual(['1','0','0','0'], result)


if __name__ == '__main__':
    unittest.main()

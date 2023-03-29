class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)

import unittest

class TestIntegerList(unittest.TestCase):

    def test_add_operation(self):
        my_obj = IntegerList(1, 2, 3)
        self.assertEqual(my_obj.add(4), [1, 2, 3, 4])

    def test_add_operation_fail(self):
        my_obj = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as error:
            my_obj.add('a')
        self.assertEqual(str(error.exception), "Element is not Integer")

    def test_remove_index(self):
        my_obj = IntegerList(2, 3, 4)
        result = my_obj.remove_index(1)
        self.assertEqual(result, 3)

    def test_remove_index_fail(self):
        my_obj = IntegerList(2, 3, 4)
        with self.assertRaises(IndexError) as error:
            result = my_obj.remove_index(5)
        self.assertEqual(str(error.exception), "Index is out of range")

    def test_init(self):
        my_obj = IntegerList(2, 'a', 4)
        self.assertEqual(my_obj._IntegerList__data, [2, 4])

    def test_get_data(self):
        my_obj = IntegerList(2, 'a', 4)
        self.assertEqual(my_obj.get_data(), [2, 4])

    def test_get(self):
        my_obj = IntegerList(2, 'a', 4)
        self.assertEqual(my_obj.get(0), 2)

    def test_get_fail(self):
        my_obj = IntegerList(2, 3, 4)
        with self.assertRaises(IndexError) as error:
            my_obj.get(5)
        self.assertEqual(str(error.exception), "Index is out of range")

    def test_insert(self):
        my_obj = IntegerList(2, 3, 4)
        my_obj.insert(1, 9)
        self.assertEqual(my_obj.get_data(), [2, 9, 3, 4])

    def test_fail_index(self):
        my_obj = IntegerList(2, 3, 4)
        with self.assertRaises(IndexError) as error:
            my_obj.insert(5, 6)
        self.assertEqual(str(error.exception), "Index is out of range")

    def test_fail_value(self):
        my_obj = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as error:
            my_obj.insert(1, 'a')
        self.assertEqual(str(error.exception), "Element is not Integer")

    def test_biggest(self):
        my_obj = IntegerList(1, 2, 3)
        self.assertEqual(my_obj.get_biggest(), 3)

    def test_get_index(self):
        my_obj = IntegerList(1, 2, 3)
        self.assertEqual(my_obj.get_index(2), 1)


if __name__ == '__name__':
    unittest.main()
from project.toy_store import ToyStore
import unittest


class TestTheStor(unittest.TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_constructor_initialization(self):
        self.assertIsNone(self.toy_store.toy_shelf["A"])
        self.assertIsNone(self.toy_store.toy_shelf["B"])
        self.assertIsNone(self.toy_store.toy_shelf["C"])
        self.assertIsNone(self.toy_store.toy_shelf["D"])
        self.assertIsNone(self.toy_store.toy_shelf["E"])
        self.assertIsNone(self.toy_store.toy_shelf["F"])
        self.assertIsNone(self.toy_store.toy_shelf["G"])
        self.assertEqual(len(self.toy_store.toy_shelf), 7)

    def test_add_toy_success(self):
        self.assertEqual(self.toy_store.add_toy("A", "truck"), "Toy:truck placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf["A"], "truck")

    def test_add_toy_wrong_shelf(self):
        with self.assertRaises(Exception) as exp:
            self.toy_store.add_toy("j", "truck")
        self.assertEqual(str(exp.exception), "Shelf doesn't exist!")

    def test_add_same_toy_twice(self):
        self.toy_store.add_toy("A", "truck")
        with self.assertRaises(Exception) as exp:
            self.toy_store.add_toy("A", "truck")
        self.assertEqual(str(exp.exception), "Toy is already in shelf!")

    def test_add_toy_on_taken_shelf(self):
        self.toy_store.add_toy("A", "truck")
        with self.assertRaises(Exception) as exp:
            self.toy_store.add_toy("A", "car")
        self.assertEqual(str(exp.exception), "Shelf is already taken!")

    def test_remove_toy_success(self):
        self.toy_store.add_toy("A", "truck")
        self.assertEqual(self.toy_store.remove_toy("A", "truck"), "Remove toy:truck successfully!")
        self.assertIsNone(self.toy_store.toy_shelf["A"])

    def test_remove_toy_unexisting_shelf(self):
        with self.assertRaises(Exception) as exp:
            self.toy_store.remove_toy("j", "truck")
        self.assertEqual(str(exp.exception), "Shelf doesn't exist!")

    def test_remove_wrong_toy(self):
        with self.assertRaises(Exception) as exp:
            self.toy_store.remove_toy("A", "car")
        self.assertEqual(str(exp.exception), "Toy in that shelf doesn't exists!")


if __name__ == "__name__":
    unittest.main()
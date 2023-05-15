from project.bookstore import Bookstore
import unittest

class TestTheApp(unittest.TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(15)
        self.books = {
            "mine": 10,
            "yours": 3
        }

    def test_constructor(self):
        self.assertEqual(self.bookstore.books_limit, 15)
        self.assertEqual(self.bookstore.total_sold_books, 0)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})

    def test_zero_book_limit(self):
        with self.assertRaises(ValueError) as err:
            self.bookstore.books_limit = 0

        self.assertEqual(str(err.exception), "Books limit of 0 is not valid")

    def test_len_count(self):
        self.bookstore.availability_in_store_by_book_titles = self.books
        self.assertEqual(len(self.bookstore), 13)

    def test_receive_book_not_enough_space(self):
        self.bookstore.availability_in_store_by_book_titles = self.books
        with self.assertRaises(Exception) as err:
            self.bookstore.receive_book("his", 3)

        self.assertEqual(str(err.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_new_book_success(self):
        self.assertEqual(self.bookstore.receive_book("his", 2), "2 copies of his are available in the bookstore.")
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"his": 2})

    def test_receive_existing_book_success(self):
        self.bookstore.availability_in_store_by_book_titles = self.books
        self.assertEqual(self.bookstore.receive_book("mine", 2), "12 copies of mine are available in the bookstore.")

    def test_sell_nonexisting_book(self):
        with self.assertRaises(Exception) as err:
            self.bookstore.sell_book("mine", 2)

        self.assertEqual(str(err.exception), "Book mine doesn't exist!")

    def test_sell_existing_not_enough(self):
        self.bookstore.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as err:
            self.bookstore.sell_book("mine", 11)

        self.assertEqual(str(err.exception), "mine has not enough copies to sell. Left: 10")

    def test_sell_success(self):
        self.bookstore.availability_in_store_by_book_titles = {"mine": 1, "yours": 5}
        self.assertEqual(self.bookstore.sell_book("yours", 2), "Sold 2 copies of yours")
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"mine": 1, "yours": 3})
        self.assertEqual(self.bookstore.total_sold_books, 2)

    def test_str_represent(self):
        self.bookstore.availability_in_store_by_book_titles = {"mine": 1, "yours": 5}
        self.assertEqual(self.bookstore.__str__(), "Total sold books: 0\nCurrent availability: 6\n - mine: 1 copies\n - yours: 5 copies")



if __name__ == "__name__":
    unittest.main()
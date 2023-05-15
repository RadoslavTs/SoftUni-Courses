from project.movie import Movie
import unittest

class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        self.movie = Movie('halo', 2000, 9)

    def test_constructor(self):
        self.assertEqual(self.movie.name, 'halo')
        self.assertEqual(self.movie.year, 2000)
        self.assertEqual(self.movie.rating, 9.0)
        self.assertEqual(self.movie.actors, [])

    def test_getter_movie(self):
        with self.assertRaises(ValueError) as err:
            self.movie.name = ''
        self.assertEqual(str(err.exception), "Name cannot be an empty string!")

    def test_getter_year(self):
        with self.assertRaises(ValueError) as err:
            self.movie.year = 1886
        self.assertEqual(str(err.exception), "Year is not valid!")

    def test_add_existing_actor(self):
        self.movie.actors.append('Rado')
        self.assertEqual(self.movie.add_actor('Rado'), "Rado is already added in the list of actors!")
        self.assertEqual(self.movie.actors, ["Rado"])

    def test_add_new_actor(self):
        self.movie.add_actor("Rado")
        self.assertEqual(self.movie.actors, ["Rado"])

    def test_greater_than(self):
        other_movie = Movie('hola', 2002, 8.5)
        self.assertEqual(self.movie > other_movie, '"halo" is better than "hola"')

    def test_not_greater(self):
        other_movie = Movie('hola', 2002, 9.5)
        self.assertEqual(self.movie > other_movie, '"hola" is better than "halo"')

    def test_repr_method(self):
        self.movie.add_actor("Rado")
        self.movie.add_actor("Emo")

        self.assertEqual(self.movie.__repr__(), f"Name: halo\n"
                                                f"Year of Release: 2000\n"
                                                f"Rating: 9.00\n"
                                                f"Cast: Rado, Emo")


if __name__ == '__name__':
    unittest.main()
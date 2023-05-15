from project.tennis_player import TennisPlayer
import unittest


class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer('Rado', 33, 100)

    def test_constructor(self):
        self.assertEqual(self.player.name, 'Rado')
        self.assertEqual(self.player.age, 33)
        self.assertEqual(self.player.points, 100)
        self.assertEqual(self.player.wins, [])

    def test_name_value_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = 'R'
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")

    def test_name_value_raise_border(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = 'Ra'
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")

    def test_age_value_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.player.age = 17
        self.assertEqual(str(ex.exception), "Players must be at least 18 years of age!")

    def test_add_new_win(self):
        self.assertIsNone(self.player.add_new_win('Bulgaria'))
        self.assertEqual(self.player.wins[0], 'Bulgaria')
        self.assertEqual(len(self.player.wins), 1)

    def test_add_existing_win(self):
        self.player.add_new_win('Bulgaria')
        self.assertEqual(self.player.add_new_win('Bulgaria'), "Bulgaria has been already added to the list of wins!")
        self.assertEqual(self.player.wins[0], "Bulgaria")
        self.assertEqual(len(self.player.wins), 1)

    def test_less_than(self):
        player_two = TennisPlayer('Niki', 25, 200)
        self.assertEqual(self.player < player_two, 'Niki is a top seeded player and he/she is better than Rado')

    def test_less_than_opposite(self):
        player_two = TennisPlayer('Niki', 25, 50)
        self.assertEqual(self.player < player_two, 'Rado is a better player than Niki')

    def test_less_than_equal(self):
        player_two = TennisPlayer('Niki', 25, 100)
        self.assertEqual(self.player < player_two, 'Rado is a better player than Niki')

    def test_string_represent(self):
        self.player.add_new_win('Bulgaria')
        self.player.add_new_win('Serbia')
        answer = "Tennis Player: Rado\nAge: 33\nPoints: 100.0\nTournaments won: Bulgaria, Serbia"
        self.assertEqual(self.player.__str__(), answer)

    def test_string_represent_empty_wins(self):
        answer = "Tennis Player: Rado\nAge: 33\nPoints: 100.0\nTournaments won: "
        self.assertEqual(self.player.__str__(), answer)


if __name__ == "__name__":
    unittest.main()
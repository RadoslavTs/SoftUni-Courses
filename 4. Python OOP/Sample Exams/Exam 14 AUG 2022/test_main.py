from project.horse_race_app import HorseRaceApp
import unittest

from project.horse_specification.appaloosa import Appaloosa


class TestMyApp(unittest.TestCase):
    def setUp(self) -> None:
        self.my_horse = Appaloosa("Rocket", 119)

    def test_constructor(self):
        with self.assertRaises(ValueError) as err:
            self.my_horse.train()

        self.assertEqual(str(err.exception), "Horse speed is too high!")







if __name__ == "__name__":
    unittest.main()



# print(horseRaceApp.add_jockey("Peter", 19))
# print(horseRaceApp.add_jockey("Mariya", 21))
# print(horseRaceApp.create_horse_race("Summer"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
# print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))

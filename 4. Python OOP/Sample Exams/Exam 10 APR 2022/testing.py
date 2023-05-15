from project.controller import Controller
from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
import unittest

class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = Controller()

    def test_constructor(self):
        self.assertEqual(self.controller.supplies, [])
        self.assertEqual(self.controller.players, [])

    def test_create_player_bad_name(self):
        with self.assertRaises(ValueError) as err:
            player = Player('', 20)
        self.assertEqual(str(err.exception), "Name not valid!")

    def test_create_player_same_name(self):
        player = Player('Rado', 20)
        with self.assertRaises(Exception ) as err:
            player_two = Player('Rado', 20)
        self.assertEqual(str(err.exception), "Name Rado is already used!")

    def test_create_player_bad_age(self):
        with self.assertRaises(ValueError) as err:
            player = Player('Rado', 11)
        self.assertEqual(str(err.exception), "The player cannot be under 12 years old!")

    def test_create_player_bad_stamina(self):
        with self.assertRaises(ValueError) as err:
            player_one = Player('Rado', 12, -1)
        self.assertEqual(str(err.exception), "Stamina not valid!")

        with self.assertRaises(ValueError) as err:
            player_two = Player('Rado', 12, 101)
        self.assertEqual(str(err.exception), "Stamina not valid!")

    def test_need_sustain(self):
        player_one = Player('Rado', 12, 90)
        player_two = Player('Emo', 12, 100)
        self.assertTrue(player_one.need_sustenance)
        self.assertFalse(player_two.need_sustenance)

    def test_str_represent_player(self):
        player_one = Player('Rado', 12, 90)
        self.assertEqual(player_one.__str__(), "Player: Rado, 12, 90, True")

    def test_create_supply_empty_name(self):
        with self.assertRaises(ValueError) as err:
            my_drink = Drink("")
        self.assertEqual(str(err.exception), "Name cannot be an empty string.")
        with self.assertRaises(ValueError) as err:
            my_drink = Food("")
        self.assertEqual(str(err.exception), "Name cannot be an empty string.")

    def test_create_supply_negative_energy(self):
        with self.assertRaises(ValueError) as err:
            my_drink = Drink("rad", -5)
        self.assertEqual(str(err.exception), "Energy cannot be less than zero.")
        with self.assertRaises(ValueError) as err:
            my_drink = Food("rad", -1)
        self.assertEqual(str(err.exception), "Energy cannot be less than zero.")

    def test_supply_constructor(self):
        my_drink = Drink("rad")
        my_food = Food("rad")
        self.assertEqual(my_drink.energy, 15)
        self.assertEqual(my_food.energy, 25)

    def test_supply_constructor_with_energy(self):
        my_drink = Drink("rad", 50)
        my_food = Food("rad", 120)
        self.assertEqual(my_drink.energy, 50)
        self.assertEqual(my_food.energy, 120)

    def test_details_supply(self):
        my_drink = Drink("rad", 50)
        my_food = Food("rad", 120)
        self.assertEqual(my_drink.details(), "Drink: rad, 50")
        self.assertEqual(my_food.details(), "Food: rad, 120")

    def test_add_players_success(self):
        player_one = Player('Rado', 12, 90)
        player_two = Player('Emo', 12, 100)
        self.assertEqual(self.controller.add_player(player_one, player_two), "Successfully added: Rado, Emo")

    def test_add_players_same(self):
        player_one = Player('Rado', 12, 90)
        player_two = Player('Niki', 12, 100)
        self.assertEqual(self.controller.add_player(player_one, player_one, player_two), "Successfully added: Rado, Niki")

    def test_sustain_result(self):
        apple = Food("apple", 22)
        cheese = Food("cheese")
        juice = Drink("orange juice")
        water = Drink("water")
        player_one = Player('Rado', 12, 90)
        self.controller.add_player(player_one)
        self.controller.add_supply(apple, cheese, juice, water)
        self.assertEqual(self.controller.sustain('Rado', 'Food'), "Rado sustained successfully with cheese.")
        supplies = []
        for supply in self.controller.supplies:
            supplies.append(supply.name)
        self.assertEqual(supplies, ['apple', 'orange juice', 'water'])
        self.assertEqual(player_one.stamina, 100)

    def test_sustain_no_need(self):
        apple = Food("apple", 22)
        cheese = Food("cheese")
        juice = Drink("orange juice")
        water = Drink("water")
        player_one = Player('Rado', 12, 100)
        self.controller.add_player(player_one)
        self.controller.add_supply(apple, cheese, juice, water)
        self.assertEqual(self.controller.sustain('Rado', 'Food'), "Rado have enough stamina.")
        supplies = []
        for supply in self.controller.supplies:
            supplies.append(supply.name)
        self.assertEqual(supplies, ['apple', 'cheese', 'orange juice', 'water'])
        self.assertEqual(player_one.stamina, 100)

    def test_sustain_no_drink(self):
        apple = Food("apple", 22)
        cheese = Food("cheese")
        player_one = Player('Rado', 12, 90)
        self.controller.add_player(player_one)
        self.controller.add_supply(apple, cheese)
        self.assertEqual(self.controller.sustain('Rado', 'Drink'), "There are no drink supplies left!")

    def test_sustain_no_food(self):
        juice = Drink("orange juice")
        water = Drink("water")
        player_one = Player('Rado', 12, 90)
        self.controller.add_player(player_one)
        self.controller.add_supply(juice, water)
        self.assertEqual(self.controller.sustain('Rado', 'Food'), "There are no food supplies left!")

    def test_duel(self):
        first_player = Player('Peter', 15)
        second_player = Player('Lilly', 12, 80)
        self.controller.add_player(first_player, second_player)
        self.assertEqual(self.controller.duel("Peter", "Lilly"), "Winner: Peter")
        self.assertEqual(first_player.stamina, 60)
        self.assertEqual(second_player.stamina, 50)

    def test_duel_no_stamina(self):
        first_player = Player('Peter', 15, 0)
        second_player = Player('Lilly', 12, 94)
        self.controller.add_player(first_player, second_player)
        self.assertEqual(self.controller.duel("Peter", "Lilly"), "Player Peter does not have enough stamina.")

    def test_duel_to_zero(self):
        first_player = Player('Peter', 15, 100)
        second_player = Player('Lilly', 12, 20)
        self.controller.add_player(first_player, second_player)
        self.assertEqual(self.controller.duel("Peter", "Lilly"), "Winner: Peter")
        self.assertEqual(second_player.stamina, 0)
        self.assertEqual(first_player.stamina, 90)

    def test_next_day(self):
        first_player = Player('Peter', 20, 100)
        second_player = Player('Lilly', 30, 20)
        self.controller.add_player(first_player, second_player)
        self.controller.next_day()
        self.assertEqual(first_player.stamina, 60)
        self.assertEqual(second_player.stamina, 0)

    def test_next_day_with_sustain(self):
        first_player = Player('Peter', 30, 100)
        second_player = Player('Lilly', 30, 20)
        juice = Drink("orange juice")
        water = Drink("water")
        apple = Food("apple", 22)
        cheese = Food("cheese")

        self.controller.add_player(first_player, second_player)
        self.controller.add_supply(juice, water, apple, cheese)
        self.controller.next_day()
        self.assertEqual(first_player.stamina, 80)
        self.assertEqual(second_player.stamina, 37)

    def test_str(self):
        first_player = Player('Peter', 30, 100)
        second_player = Player('Lilly', 30, 20)
        juice = Drink("orange juice")
        water = Drink("water")
        apple = Food("apple", 22)
        cheese = Food("cheese")
        self.controller.add_player(first_player, second_player)
        self.controller.add_supply(juice, apple)
        result = f"Player: Peter, 30, 100, False\nPlayer: Lilly, 30, 20, True\nDrink: orange juice, 15\nFood: apple, 22"
        self.assertEqual(str(self.controller), result)


if __name__ == "__name__":
    unittest.main()
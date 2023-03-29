from project.hero import Hero

import unittest

class TestTheHero(unittest.TestCase):
    def setUp(self) -> None:
        self.my_hero = Hero('Rado', 10, 90.2, 150.7)

    def test_constructor(self):
        self.assertEqual(self.my_hero.username, 'Rado')
        self.assertEqual(self.my_hero.level, 10)
        self.assertEqual(self.my_hero.health, 90.2)
        self.assertEqual(self.my_hero.damage, 150.7)

    def test_battle_self(self):
        enemy_hero = Hero('Rado', 20, 91.2, 151.7)
        with self.assertRaises(Exception) as error:
            self.my_hero.battle(enemy_hero)
        self.assertEqual(str(error.exception), "You cannot fight yourself")

    def test_battle_low_hp(self):
        enemy_hero = Hero('Miro', 20, 91.2, 151.7)
        self.my_hero.health = 0
        with self.assertRaises(ValueError) as error:
            self.my_hero.battle(enemy_hero)
        self.assertEqual(str(error.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_negative_hp(self):
        enemy_hero = Hero('Miro', 20, 91.2, 151.7)
        self.my_hero.health = -5
        with self.assertRaises(ValueError) as error:
            self.my_hero.battle(enemy_hero)
        self.assertEqual(str(error.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_enemy_low_hp(self):
        enemy_hero = Hero('Miro', 20, 0, 151.7)
        with self.assertRaises(ValueError) as error:
            self.my_hero.battle(enemy_hero)
        self.assertEqual(str(error.exception), f"You cannot fight Miro. He needs to rest")

    def test_battle_enemy_negative_hp(self):
        enemy_hero = Hero('Miro', 20, -5, 151.7)
        with self.assertRaises(ValueError) as error:
            self.my_hero.battle(enemy_hero)
        self.assertEqual(str(error.exception), f"You cannot fight Miro. He needs to rest")

    def test_battle_enemy_draw(self):
        enemy_hero = Hero('Miro', 20, 50, 151.7)
        self.assertEqual(self.my_hero.battle(enemy_hero), 'Draw')

    def test_battle_win(self):
        enemy_hero = Hero('Miro', 1, 50, 10)
        self.assertEqual(self.my_hero.battle(enemy_hero), "You win")
        self.assertLess(enemy_hero.health, 1)
        self.assertEqual(self.my_hero.level, 11)
        self.assertEqual(self.my_hero.health, 85.2)
        self.assertEqual(self.my_hero.damage, 155.7)

    def test_battle_lose(self):
        self.my_hero.level = 1
        enemy_hero = Hero('Miro', 20, 5000, 10)
        self.assertEqual(self.my_hero.battle(enemy_hero), "You lose")
        self.assertEqual(enemy_hero.level, 21)
        self.assertEqual(enemy_hero.health, 4854.3)
        self.assertEqual(enemy_hero.damage, 15)

    def test_string_representation(self):
        result = f"Hero Rado: 10 lvl\nHealth: 90.2\nDamage: 150.7\n"
        self.assertEqual(self.my_hero.__str__(), result)

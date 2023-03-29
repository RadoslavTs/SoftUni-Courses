from project.mammal import Mammal
import unittest


class MammalTest(unittest.TestCase):

    def test_constructor(self):
        cow = Mammal('Lola', 'Herbivore', 'Moo')
        self.assertEqual(cow.name, 'Lola')
        self.assertEqual(cow.type, 'Herbivore')
        self.assertEqual(cow.sound, 'Moo')
        self.assertEqual(cow._Mammal__kingdom, 'animals')

    def test_make_sound(self):
        cow = Mammal('Lola', 'Herbivore', 'Moo')
        result = cow.make_sound()
        self.assertEqual(result, 'Lola makes Moo')

    def test_get_kindgdom(self):
        cow = Mammal('Lola', 'Herbivore', 'Moo')
        self.assertEqual(cow.get_kingdom(), 'animals')

    def test_info(self):
        cow = Mammal('Lola', 'Herbivore', 'Moo')
        self.assertEqual(cow.info(), 'Lola is of type Herbivore')
from project.plantation import Plantation
import unittest

class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        self.farm = Plantation(5)
        self.plants = {'rado': ['sliva', 'cheresha'], "miro": ['diula', 'bor', 'chinar']}

    def test_constructor(self):
        self.assertEqual(self.farm.size, 5)
        self.assertEqual(self.farm.plants, {})
        self.assertEqual(self.farm.workers, [])

    def test_negative_size_initially(self):
        with self.assertRaises(ValueError) as err:
            self.farm.size = -5

        self.assertEqual(str(err.exception), "Size must be positive number!")

    def test_hire_success(self):
        self.assertEqual(self.farm.hire_worker('Rado'), "Rado successfully hired.")

    def test_hire_same_worker_twice(self):
        self.farm.hire_worker('Rado')
        with self.assertRaises(ValueError) as err:
            self.farm.hire_worker('Rado')
        self.assertEqual(str(err.exception), "Worker already hired!")

    def test_count_plants(self):
        self.farm.plants = self.plants
        self.assertEqual(len(self.farm), 5)

    def test_count_plants_zero(self):
        self.assertEqual(len(self.farm), 0)

    def test_planting_wrong_worker(self):
        with self.assertRaises(ValueError) as err:
            self.farm.planting('Rado', 'Sliva')
        self.assertEqual(str(err.exception), "Worker with name Rado is not hired!")

    def test_too_much_plants(self):
        self.farm.plants = self.plants
        self.farm.hire_worker('Rado')
        with self.assertRaises(ValueError) as err:
            self.farm.planting('Rado', 'Sliva')

        self.assertEqual(str(err.exception), "The plantation is full!")

    def test_planting_success_second_plant(self):
        self.farm.size = 10
        self.farm.plants = self.plants
        self.farm.hire_worker('rado')
        self.assertEqual(self.farm.planting('rado', 'Sliva'), "rado planted Sliva.")
        self.assertEqual(self.farm.plants, {'rado': ['sliva', 'cheresha', 'Sliva'], "miro": ['diula', 'bor', 'chinar']})

    def test_planting_success_first_plant(self):
        self.farm.size = 10
        self.farm.hire_worker('rado')
        self.assertEqual(self.farm.planting('rado', 'Sliva'), "rado planted it's first Sliva.")
        self.assertEqual(self.farm.plants, {'rado': ['Sliva']})

    def test_string_represent(self):
        self.farm.hire_worker('Rado')
        self.farm.planting('Rado', 'Sliva')
        self.assertEqual(self.farm.__str__(), 'Plantation size: 5\nRado\nRado planted: Sliva')

    def test_repr_represent(self):
        self.farm.hire_worker('Rado')
        self.farm.planting('Rado', 'Sliva')
        self.assertEqual(self.farm.__repr__(), 'Size: 5\nWorkers: Rado')


if __name__ == "__name__":
    unittest.main()
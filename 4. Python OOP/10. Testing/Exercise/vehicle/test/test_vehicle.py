from project.vehicle import Vehicle
import unittest


class TestVehicle(unittest.TestCase):

    def setUp(self) -> None:
        self.my_car = Vehicle(40, 100)

    def test_constructor(self):
        self.assertEqual(self.my_car.fuel, 40)
        self.assertEqual(self.my_car.capacity, 40)
        self.assertEqual(self.my_car.horse_power, 100)
        self.assertEqual(self.my_car.fuel_consumption, 1.25)

    def test_drive(self):
        self.my_car.drive(10)
        self.assertEqual(self.my_car.fuel, 27.5)

    def test_drive_fail(self):
        with self.assertRaises(Exception) as error:
            self.my_car.drive(100)
        self.assertEqual(str(error.exception), "Not enough fuel")

    def test_refuel(self):
        self.my_car.fuel = 0
        self.my_car.refuel(10)
        self.assertEqual(self.my_car.fuel, 10)

    def test_refuel_fail(self):
        with self.assertRaises(Exception) as error:
            self.my_car.refuel(100)
        self.assertEqual(str(error.exception), "Too much fuel")

    def test_string_representation(self):
        result = "The vehicle has 100 horse power with 40 fuel left and 1.25 fuel consumption"
        self.assertEqual(self.my_car.__str__(), result)
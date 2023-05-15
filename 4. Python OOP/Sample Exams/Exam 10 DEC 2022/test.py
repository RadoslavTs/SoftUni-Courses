import unittest

from project.christmas_pastry_shop_app import ChristmasPastryShopApp
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class TestTheApp(unittest.TestCase):
    def setUp(self) -> None:
        self.shop = ChristmasPastryShopApp()

    def test_add_delicacy_success(self):
        self.assertEqual(self.shop.add_delicacy("Gingerbread", "Gingy", 5.20), 'Added delicacy Gingy - Gingerbread to the pastry shop.')
        self.assertEqual(self.shop.add_delicacy("Stolen", "Stoly", 5.20), 'Added delicacy Stoly - Stolen to the pastry shop.')

    def test_add_delicacy_same_name(self):
        self.shop.add_delicacy("Gingerbread", "Gingy", 5.20)
        with self.assertRaises(Exception) as exp:
            self.shop.add_delicacy("Gingerbread", "Gingy", 5.20)
        self.assertEqual(str(exp.exception), "Gingy already exists!")

    def test_add_wrong_type_delicacy(self):
        with self.assertRaises(Exception) as exp:
            self.shop.add_delicacy("Rado", "Gertrud", 5)
        self.assertEqual(str(exp.exception), "Rado is not on our delicacy menu!")

    def test_add_booth_success(self):
        self.assertEqual(self.shop.add_booth("Open Booth", 1, 30), "Added booth number 1 in the pastry shop.")
        self.assertEqual(self.shop.add_booth("Private Booth", 2, 30), "Added booth number 2 in the pastry shop.")

    def test_add_booth_same__number(self):
        self.shop.add_booth("Open Booth", 1, 30)
        with self.assertRaises(Exception) as exp:
            self.shop.add_booth("Open Booth", 1, 30)
        self.assertEqual(str(exp.exception), "Booth number 1 already exists!")

    def test_add_wrong_booth_type(self):
        with self.assertRaises(Exception) as exp:
            self.shop.add_booth("wrong Booth", 1, 30)
        self.assertEqual(str(exp.exception), "wrong Booth is not a valid booth!")

    def test_reserve_booth_success(self):
        self.shop.add_booth("Open Booth", 1, 5)
        self.shop.add_booth("Private Booth", 5, 30)
        self.assertEqual(self.shop.reserve_booth(10), "Booth 5 has been reserved for 10 people.")
        self.assertEqual(self.shop.reserve_booth(5), "Booth 1 has been reserved for 5 people.")

    def test_reserve_booth_fail(self):
        self.shop.add_booth("Open Booth", 1, 5)
        self.shop.add_booth("Private Booth", 5, 30)
        with self.assertRaises(Exception) as exp:
            self.shop.reserve_booth(50)
        self.assertEqual(str(exp.exception), "No available booth for 50 people!")

    def test_order_delicacy_sucess(self):
        self.shop.add_booth("Open Booth", 1, 5)
        self.shop.add_delicacy("Gingerbread", "Gingy", 5.20)
        self.assertEqual(self.shop.order_delicacy(1, "Gingy"), "Booth 1 ordered Gingy.")

    def test_order_delicacy_wrong_booth(self):
        self.shop.add_booth("Open Booth", 1, 5)
        self.shop.add_delicacy("Gingerbread", "Gingy", 5.20)
        with self.assertRaises(Exception) as exp:
            self.shop.order_delicacy(3, "Gingy")
        self.assertEqual(str(exp.exception), "Could not find booth 3!")

    def test_order_wrong_delicacy(self):
        self.shop.add_booth("Open Booth", 1, 5)
        self.shop.add_delicacy("Gingerbread", "Gingy", 5.20)
        with self.assertRaises(Exception) as exp:
            self.shop.order_delicacy(1, "Rado")
        self.assertEqual(str(exp.exception), "No Rado in the pastry shop!")

    def test_leave_booth_success(self):
        self.shop.add_booth("Open Booth", 1, 30)
        self.shop.reserve_booth(10)
        self.assertEqual(self.shop.leave_booth(1), "Booth 1:\nBill: 25.00lv.")
        self.shop.reserve_booth(10)
        self.assertEqual(self.shop.booths[0].price_for_reservation, 25)
        self.shop.add_delicacy("Gingerbread", "Gingy", 5.20)
        self.shop.order_delicacy(1, "Gingy")
        self.assertEqual(self.shop.leave_booth(1), "Booth 1:\nBill: 30.20lv.")
        self.assertFalse(self.shop.booths[0].is_reserved)
        self.assertEqual(self.shop.booths[0].delicacy_orders, [])
        self.assertEqual(self.shop.booths[0].price_for_reservation, 0)

    def test_get_income(self):
        self.assertEqual(self.shop.get_income(), "Income: 0.00lv.")
        self.shop.add_booth("Open Booth", 1, 30)
        self.shop.reserve_booth(10)
        self.shop.add_delicacy("Gingerbread", "Gingy", 5.20)
        self.shop.order_delicacy(1, "Gingy")
        self.shop.leave_booth(1)
        self.assertEqual(self.shop.get_income(), "Income: 30.20lv.")

    def test_add_delicacy_wrong_name(self):
        with self.assertRaises(ValueError) as err:
            Gingerbread('', 10)
        self.assertEqual(str(err.exception), "Name cannot be null or whitespace!")

    def test_add_delicacy_wrong_price(self):
        with self.assertRaises(ValueError) as err:
            Gingerbread('Rado', -50)
        self.assertEqual(str(err.exception), "Price cannot be less or equal to zero!")

    def test_delicacy_details(self):
        delicacy = Gingerbread('Rado', 50)
        self.assertEqual(delicacy.details(), "Gingerbread Rado: 200g - 50.00lv.")
        delicacy_two = Stolen('Rado_two', 50)
        self.assertEqual(delicacy_two.details(), "Stolen Rado_two: 250g - 50.00lv.")
# print(shop.delicacies[0].details())
# print(shop.add_booth("Open Booth", 1, 30))
# print(shop.add_booth("Private Booth", 10, 5))
# print(shop.reserve_booth(30))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.reserve_booth(5))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.get_income())
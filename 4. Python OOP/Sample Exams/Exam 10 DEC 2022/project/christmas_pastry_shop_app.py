from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in [d.name for d in self.delicacies]:
            raise Exception(f"{name} already exists!")

        if type_delicacy == 'Gingerbread':
            delicacy = Gingerbread(name, price)
        elif type_delicacy == 'Stolen':
            delicacy = Stolen(name, price)

        else:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        existing = False
        for booth in self.booths:
            if booth.booth_number == booth_number:
                existing = True
                break
        if existing:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ["Open Booth", "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")

        if type_booth == "Open Booth":
            self.booths.append(OpenBooth(booth_number, capacity))
        else:
            self.booths.append(PrivateBooth(booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            current_booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            current_delicacy = next(filter(lambda x: x.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        current_booth.add_order(current_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        current_booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))

        bill_price = sum(x.price for x in current_booth.delicacy_orders) + current_booth.price_for_reservation
        current_booth.leave_booth()
        self.income += bill_price

        return f"Booth {booth_number}:\n" \
               f"Bill: {bill_price:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

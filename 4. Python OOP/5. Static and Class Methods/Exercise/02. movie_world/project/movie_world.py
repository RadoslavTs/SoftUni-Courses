from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        try:
            customer = next(filter(lambda x: x.id == customer_id, self.customers))
            dvd = next(filter(lambda x: x.id == dvd_id, self.dvds))
        except StopIteration:
            pass

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        for customerz in self.customers:
            for rented in customerz.rented_dvds:
                if rented == dvd:
                    return f"DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        try:
            customer = next(filter(lambda x: x.id == customer_id, self.customers))
            dvd = next(filter(lambda x: x.id == dvd_id, self.dvds))
        except StopIteration:
            pass

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += f'{customer}\n'

        for dvd in self.dvds:
            result += f"{dvd}\n"

        return result

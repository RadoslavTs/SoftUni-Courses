from typing import List, Dict

from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []
        self.paid_bills = 0

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception(f"The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        result = []
        for item in self.menu:
            result.append(item.details())

        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        ordered_meals = []
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        try:
            current_client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            self.register_client(client_phone_number)
            current_client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))

        for meal, quantity in meal_names_and_quantities.items():
            try:
                current_meal = next(filter(lambda x: x.name == meal, self.menu))
            except StopIteration:
                raise Exception(f"{meal} is not on the menu!")

            if current_meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {current_meal.__class__.__name__}: {meal}!")

            if current_meal.name not in current_client.ordered_meals:
                current_client.ordered_meals[current_meal.name] = 0

            current_client.ordered_meals[current_meal.name] += quantity
            current_meal.quantity -= quantity
            current_client.shopping_cart.append(current_meal)
            current_client.bill += current_meal.price * quantity

        for meal in current_client.shopping_cart:
            ordered_meals.append(meal.name)

        return f"Client {client_phone_number} successfully ordered {', '.join(ordered_meals)} for {current_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        current_client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))
        if not current_client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in self.menu:
            for meal_own in current_client.ordered_meals:
                if meal_own == meal.name:
                    meal.quantity += current_client.ordered_meals[meal_own]

        current_client.ordered_meals = {}

        current_client.shopping_cart.clear()
        current_client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        current_client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))
        if not current_client.shopping_cart:
            raise Exception("There are no ordered meals!")
        current_client.shopping_cart.clear()
        paid_bill = current_client.bill

        self.paid_bills += 1
        current_client.bill = 0

        return f"Receipt #{self.paid_bills} with total amount of {paid_bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
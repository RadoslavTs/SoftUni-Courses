from typing import List

from project.animal import Animal
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []
        self.remaining_worker_capacity = workers_capacity
        self.remaining_animal_capacity = animal_capacity

    def add_animal(self, animal: Animal, price: float) -> str:
        if self.__budget >= price and self.remaining_animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.remaining_animal_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price and self.remaining_animal_capacity > 0:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.remaining_worker_capacity > 0:
            self.workers.append(worker)
            self.remaining_worker_capacity -= 1
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda x: x.name == worker_name, self.workers))
            self.workers.remove(worker)
            self.remaining_worker_capacity += 1
            return f"{worker_name} fired successfully"
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        amount_needed = 0
        for worker in self.workers:
            amount_needed += worker.salary
        if amount_needed <= self.__budget:
            self.__budget -= amount_needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        amount_needed = 0
        for animal in self.animals:
            amount_needed += animal.money_for_care
        if amount_needed < self.__budget:
            self.__budget -= amount_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda x: x.__class__.__name__ == "Lion", self.animals))
        cheetas = list(filter(lambda x: x.__class__.__name__ == "Cheetah", self.animals))
        tigers = list(filter(lambda x: x.__class__.__name__ == "Tiger", self.animals))

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:",
        ]
        result.extend(lions)

        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)

        result.append(f"----- {len(cheetas)} Cheetahs:")
        result.extend(cheetas)

        return '\n'.join(str(x) for x in result)

    def workers_status(self):
        info = {"Keeper": [], "Caretaker": [], "Vet": []}
        [info[w.__class__.__name__].append(str(w)) for w in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:",
            *info["Keeper"],
            f"----- {len(info['Caretaker'])} Caretakers:",
            *info["Caretaker"],
            f"----- {len(info['Vet'])} Vets:",
            *info["Vet"],
        ]

        return '\n'.join(result)

    def return_workers(self):
        print(f'{self.workers}, {self.__workers_capacity}')

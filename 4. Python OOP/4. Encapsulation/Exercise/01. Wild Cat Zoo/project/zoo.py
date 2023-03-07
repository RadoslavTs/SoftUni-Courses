from project.animal import Animal
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []
        self.remaining_worker_capacity = workers_capacity
        self.remaining_animal_capacity = animal_capacity

    def add_animal(self, animal, price):
        if self.__budget >= price and self.remaining_animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.remaining_animal_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price and self.remaining_animal_capacity > 0:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
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
        lions = []
        cheetas = []
        tigers = []

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                cheetas.append(animal)
            else:
                tigers.append(animal)
        lions_string = f"----- {len(lions)} Lions:\n"
        tigers_string = f"----- {len(tigers)} Tigers:\n"
        cheetas_string = f"----- {len(cheetas)} Cheetahs:\n"
        for lion in lions:
            lions_string += f'{lion}\n'
        for tiger in tigers:
            tigers_string += f'{tiger}\n'
        for cheetah in cheetas:
            cheetas_string += f"{cheetah}\n"

        return f"You have {len(self.animals)} animals\n" + f"{lions_string}" + f"{tigers_string}" + f"{cheetas_string[:-1]}"

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            else:
                vets.append(worker)
        keepers_string = f"----- {len(keepers)} Keepers:\n"
        caretakers_string = f"----- {len(caretakers)} Caretakers:\n"
        vets_string = f"----- {len(vets)} Vets:\n"
        for keeper in keepers:
            keepers_string += f'{keeper}\n'
        for caretaker in caretakers:
            caretakers_string += f'{caretaker}\n'
        for vet in vets:
            vets_string += f"{vet}\n"

        return f"You have {len(self.workers)} workers\n" + f"{keepers_string}" + f"{caretakers_string}" + f"{vets_string[:-1]}"

    def return_workers(self):
        print(f'{self.workers}, {self.__workers_capacity}')

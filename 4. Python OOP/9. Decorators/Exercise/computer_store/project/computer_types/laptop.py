from project.computer_types.computer import Computer


class Laptop(Computer):

    def available_processors(self):
        return {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }

    def max_ram(self):
        return 64

    def type(self):
        return 'laptop'

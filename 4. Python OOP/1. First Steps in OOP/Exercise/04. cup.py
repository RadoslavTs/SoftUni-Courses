class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, quant):
        if self.quantity + quant <= self.size:
            self.quantity += quant

    def status(self):
        remaining = self.size - self.quantity
        return remaining


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())

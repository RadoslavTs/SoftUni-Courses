from project.beverage.cold_beverage import HotBeverage


class Tea(HotBeverage):
    def __init__(self, name, price):
        super().__init__(name, price, 0)


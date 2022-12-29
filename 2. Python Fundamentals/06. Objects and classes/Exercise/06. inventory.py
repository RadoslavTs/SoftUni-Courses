class Inventory:
    items = []

    def __init__(self, __capacity: int):
        self.capacity = __capacity
        self.capacity_left = self.capacity

    def add_item(self, item: str):
        capacity_left = self.capacity
        if self.capacity_left > 0:
            Inventory.items.append(item)
            self.capacity_left -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        return_list = ", ".join(Inventory.items)
        return f"Items: {return_list}.\nCapacity left: {self.capacity_left}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)


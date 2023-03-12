class Equipment:
    ID: int = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.ID

    @staticmethod
    def get_next_id():
        Equipment.ID += 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

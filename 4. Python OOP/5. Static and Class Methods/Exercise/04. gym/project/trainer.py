class Trainer:
    ID: int = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.ID

    @staticmethod
    def get_next_id():
        Trainer.ID += 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
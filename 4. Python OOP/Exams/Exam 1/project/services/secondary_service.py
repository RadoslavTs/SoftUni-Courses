from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPA = 15

    def __init__(self, name: str):
        super().__init__(name, self.CAPA)

    def details(self):
        if self.robots:
            return f"{self.name} Secondary Service:\nRobots: {' '.join([x.name for x in self.robots])}"
        else:
            return f"{self.name} Secondary Service:\nRobots: none"

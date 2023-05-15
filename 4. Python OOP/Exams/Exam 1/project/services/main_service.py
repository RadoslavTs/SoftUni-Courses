from project.services.base_service import BaseService


class MainService(BaseService):
    CAPA = 30

    def __init__(self, name: str):
        super().__init__(name, self.CAPA)

    def details(self):
        if self.robots:
            return f"{self.name} Main Service:\nRobots: {' '.join([x.name for x in self.robots])}"
        else:
            return f"{self.name} Main Service:\nRobots: none"

from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140

    def train(self):
        self.speed = self.MAX_SPEED if self.speed + 3 > self.MAX_SPEED else self.speed + 3


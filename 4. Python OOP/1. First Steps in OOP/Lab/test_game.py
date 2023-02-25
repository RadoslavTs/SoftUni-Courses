import random


class Game:
    def __init__(self, max_attempts=3):
        self.number = random.randint(1, 10)
        self.max_attempts = max_attempts
        self.won = False
        self.attempts = 0

    def guess(self, num):
        self.attempts += 1

        if num == self.number:
            self.won = True
            print("You won!")
        elif num < self.number and self.attempts < self.max_attempts:
            print("Higher! Try Again")
        elif num > self.number and self.attempts < self.max_attempts:
            print("Lower! Try Again")

        if not self.won and self.attempts == self.max_attempts:
            print(f"You lost, the number was: {self.number}")


game = Game()
while not game.won and game.attempts < game.max_attempts:
    number = int(input("Guess a number: "))
    game.guess(number)

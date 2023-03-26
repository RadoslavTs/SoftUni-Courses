from typing import List

from project.band_members.musician import Musician


class Band:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Musician] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        value_set = set(list(value))
        if not value or (len(value_set) == 1 and value_set.pop() == ' '):
            raise ValueError("Musician name cannot be empty!")
        self.__name = value

    def add_member(self, musician):
        self.members.append(musician)

    def remove_member(self, musician):
        self.members.remove(musician)

    def __str__(self):
        return f"{self.__name} with {len(self.members)} members."

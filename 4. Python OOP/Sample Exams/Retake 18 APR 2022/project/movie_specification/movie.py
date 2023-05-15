from abc import ABC, abstractmethod

from project.user import User


class Movie(ABC):
    MIN_AGE = 0

    def __init__(self, title: str, year: int, owner: User, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes: int = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value.strip() == '':
            raise ValueError("The title cannot be empty string!")
        
        self.__title = value
        
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")
        
        self.__year = value
    
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")

        self.__owner = value

    @abstractmethod
    def details(self):
        pass

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.MIN_AGE and self.__class__.__name__ == "Fantasy":
            raise ValueError("Fantasy movies must be restricted for audience under 6 years!")
        elif value < self.MIN_AGE and self.__class__.__name__ == "Action":
            raise ValueError("Action movies must be restricted for audience under 12 years!")
        elif value < self.MIN_AGE and self.__class__.__name__ == "Thriller":
            raise ValueError("Thriller movies must be restricted for audience under 16 years!")

        self.__age_restriction = value

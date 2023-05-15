from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        valid_horse_types = ["Appaloosa", "Thoroughbred"]
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in valid_horse_types:
            if horse_type == "Appaloosa":
                new_horse = Appaloosa(horse_name, horse_speed)
            else:
                new_horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        current_horse = None
        try:
            current_jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys))
        except:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        for i in range(len(self.horses)-1, -1, -1):
            horse = self.horses[i]
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                current_horse = self.horses[i]
                break

        if not current_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if current_jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        current_horse.is_taken = True
        current_jockey.horse = current_horse
        return f"Jockey {jockey_name} will ride the horse {current_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        try:
            current_horse_race = next(filter(lambda x: x.race_type == race_type, self.horse_races))
        except:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            current_jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys))
        except:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not current_jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        for jockey in current_horse_race.jockeys:
            if jockey.name == jockey_name:
                return f"Jockey {jockey_name} has been already added to the {race_type} race."

        current_horse_race.jockeys.append(current_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        winner_speed = 0
        winner_jockey = None

        try:
            current_horse_race = next(filter(lambda x: x.race_type == race_type, self.horse_races))
        except:
            raise Exception(f"Race {race_type} could not be found!")

        if len(current_horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        for jockey in current_horse_race.jockeys:
            if jockey.horse.speed > winner_speed:
                winner_jockey = jockey
                winner_speed = jockey.horse.speed

        return f"The winner of the {race_type} race, with a speed" \
               f" of {winner_jockey.horse.speed}km/h is {winner_jockey.name}! " \
               f"Winner's horse: {winner_jockey.horse.name}."








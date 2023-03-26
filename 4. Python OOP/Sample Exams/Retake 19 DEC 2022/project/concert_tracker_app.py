from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ['Guitarist', 'Drummer', 'Singer']:
            raise ValueError("Invalid musician type!")
        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")
        if musician_type == 'Guitarist':
            self.musicians.append(Guitarist(name, age))
        elif musician_type == 'Drummer':
            self.musicians.append(Drummer(name, age))
        else:
            self.musicians.append(Singer(name, age))

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception("{band_name} band is already created!")
        else:
            self.bands.append(Band(name))

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")
        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician_found = False
        band_found = False
        current_band = ''
        current_musician = ''
        for musician in self.musicians:
            if musician.name == musician_name:
                musician_found = True
                current_musician = musician
                break
        for band in self.bands:
            if band.name == band_name:
                band_found = True
                current_band = band
        if not musician_found:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band_found:
            raise Exception(f"{band_name} isn't a band!")

        current_band.members.append(current_musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        musician_found = False
        band_found = False
        current_band = ''
        current_musician = ''
        for band in self.bands:
            if band.name == band_name:
                band_found = True
                current_band = band
                break

        if not band_found:
            raise Exception(f"{band_name} isn't a band!")

        for musician in current_band.members:
            if musician.name == musician_name:
                current_musician = musician
                musician_found = True
                break

        if not musician_found:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        current_band.members.remove(current_musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        current_band = next(filter(lambda x: x.name == band_name, self.bands))
        concert = next(filter(lambda x: x.place == concert_place, self.concerts))
        singers = 0
        drummers = 0
        guitarists = 0
        needed_skills_available = True
        rock_required_skills = {
            'Drummer': ['play the drums with drumsticks'],
            'Singer': ['sing high pitch notes'],
            'Guitarist': ['play rock']
        }
        metal_required_skills = {
            'Drummer': 'play the drums with drumsticks',
            'Singer': 'sing low pitch notes',
            'Guitarist': 'play metal'
        }
        jazz_required_skills = {
            'Drummer': ['play the drums with drum brushes'],
            'Singer': ['sing high pitch notes', 'sing low pitch notes'],
            'Guitarist': ['play jazz']
        }
        current_skills = {'Drummer': [], 'Singer': [], 'Guitarist': []}

        for musician in current_band.members:
            if musician.__class__.__name__ == "Drummer":
                drummers += 1
                for skill in musician.skills:
                    current_skills['Drummer'].append(skill)
            elif musician.__class__.__name__ == "Singer":
                singers += 1
                for skill in musician.skills:
                    current_skills['Singer'].append(skill)
            elif musician.__class__.__name__ == "Guitarist":
                guitarists += 1
                for skill in musician.skills:
                    current_skills['Guitarist'].append(skill)

        if singers < 1 or drummers < 1 or guitarists < 1:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == 'Metal':
            for k, v in metal_required_skills.items():
                for skill in v:
                    if skill not in current_skills[k]:
                        needed_skills_available = False
                        break
        elif concert.genre == 'Rock':
            for k, v in rock_required_skills.items():
                for skill in v:
                    if skill not in current_skills[k]:
                        needed_skills_available = False
                        break
        else:
            for k, v in jazz_required_skills.items():
                for skill in v:
                    if skill not in current_skills[k]:
                        needed_skills_available = False
                        break

        if not needed_skills_available:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."


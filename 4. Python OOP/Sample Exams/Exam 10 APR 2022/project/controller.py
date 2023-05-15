from collections import deque

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        added = []
        for player in args:
            if player not in self.players:
                added.append(player.name)
                self.players.append(player)
        return f"Successfully added: {', '.join(added)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        current_player = None
        valid_sustenances = ['Food', 'Drink']
        supply_index = None
        for i in range(len(self.supplies)-1, -1, -1):
            if self.supplies[i].__class__.__name__ == sustenance_type:
                supply_index = i
                break
        try:
            current_player = next(filter(lambda x: x.name == player_name, self.players))
        except StopIteration:
            pass

        if current_player:
            if current_player.stamina == 100:
                return f"{player_name} have enough stamina."

        if supply_index is not None and current_player and sustenance_type in valid_sustenances:
            available_energy = self.supplies[supply_index].energy
            player_stamina = current_player.stamina
            resulting_energy = available_energy + player_stamina

            if resulting_energy > 100:
                current_player.stamina = 100
            else:
                current_player.stamina = resulting_energy
            supply_name = self.supplies[supply_index].name
            del self.supplies[supply_index]
            return f"{player_name} sustained successfully with {supply_name}."

        if not supply_index:
            if sustenance_type == 'Drink':
                return f"There are no drink supplies left!"
            if sustenance_type == 'Food':
                return f"There are no food supplies left!"

    def duel(self, first_player_name: str, second_player_name: str):
        player_one = next(filter(lambda x: x.name == first_player_name, self.players))
        player_two = next(filter(lambda x: x.name == second_player_name, self.players))

        if player_one.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        if player_two.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        if player_one.stamina < player_two.stamina:
            first_attacker = player_one
            second_attacker = player_two
        else:
            first_attacker = player_two
            second_attacker = player_one

        second_attacker_stamina = second_attacker.stamina - (first_attacker.stamina / 2)
        if second_attacker_stamina <= 0:
            second_attacker.stamina = 0
            if second_attacker.name == player_one.name:
                player_one.stamina = 0
            else:
                player_two.stamina = 0
            return f"Winner: {first_attacker.name}"
        else:
            second_attacker.stamina = second_attacker_stamina
            if second_attacker.name == player_one.name:
                player_one.stamina = second_attacker_stamina
            else:
                player_two.stamina = second_attacker_stamina

        first_attacker_stamina = first_attacker.stamina - (second_attacker_stamina / 2)
        if first_attacker_stamina <= 0:
            first_attacker.stamina = 0
            if first_attacker.name == player_one.name:
                player_one.stamina = 0
            else:
                player_two.stamina = 0
            return f"Winner: {second_attacker.name}"
        else:
            first_attacker.stamina = first_attacker_stamina
            if first_attacker.name == player_one.name:
                player_one.stamina = first_attacker_stamina
            else:
                player_two.stamina = first_attacker_stamina

        if player_one.stamina > player_two.stamina:
            return f"Winner: {player_one.name}"
        else:
            return f"Winner: {player_two.name}"

    def next_day(self):
        for player in self.players:
            current_stamina = player.stamina - (player.age * 2)
            if current_stamina <= 0:
                player.stamina = 0
            else:
                player.stamina = current_stamina
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        players = []
        supplies = []
        for player in self.players:
            players.append(f'Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}')
        players_string = '\n'.join(players)
        for supply in self.supplies:
            supplies.append(f"{supply.__class__.__name__}: {supply.name}, {supply.energy}")
        supplies_string = '\n'.join(supplies)
        return f"{players_string}\n{supplies_string}"


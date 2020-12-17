#!/bin/python3
""" Docstring """


import random


class Encounter():
    """ Docstring """

    def __init__(self, party, npc_group):
        self.party = party
        self.npc_group = npc_group
        self.battle_order = []

    def calculate_battle_order(self):
        continue

    def set_player_initiative_roll(self, roll, player):
        modifier = self.party.party_players[player.name].initiative_modifier
        self.party.party_players[player.name].initiative = roll + modifier
        self.battle_order.append(self.party.party_players[player.name])

    def generate_npc_initiatives(self):
        for key in self.npc_group.group_composition:
            roll = random.randrange(1, 20)
            self.npc_group.group_compsotion[key].initiative = roll
            self.battle_order.append(self.npc_group.group_compsotion[key])

    def sort_battle_order(self):
        self.battle_order.sort(key=lambda x: x.initiative, reverse=False)


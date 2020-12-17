#!/bin/python3
""" Docstring """

class Party():
    """ Docstring """
    def __init__(self, p_id=None, p_name = None):
        self.party_id = p_id
        self.party_name = p_name
        self.party_players = {}

    def add_party_member(self, name, level, initiative_modifier):
        player = new PlayerCharacter(name, level, initiative_modifier)
        self.party_players.update(player.name, player)

    def remove_party_member(self, name):
        del self.party_players[name]

    def update_party_member(self, name, level, initiative_modifier):
        player = new PlayerCharacter(name, level, initiative_modifier)
        self.party_players[name] = player

    def save_party(self):
        """ should return a party id from the db """
        continue

    def retrieve_party(self, party_id):
        """ should populate the party form the db """
        continue

    def clear_party(self):
        self.party_players = {}

    
class PlayerCharacter():
    """ Docstring """
    def __init__(self, name, level, initiative_modifier):
        self.player_name = name
        self.player_level = level
        self.player_initiative_modifier = initiative_modifier
        self.player_initiative = initiative


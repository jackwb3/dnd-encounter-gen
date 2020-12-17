#!/bin/python3
""" Docstring """

class NPCGroup():
    """ Docstring """
    def __init__(self, p_id=None, p_name = None):
        self.group_id = p_id
        self.group_name = p_name
        self.group_composition = {}

    def add_group_member(self, name, level, initiative_modifier):
        player = new NonPlayerCharacter(name, level, initiative_modifier)
        self.group_composition.update(player.name, player)

    def remove_group_member(self, name):
        del self.group_composition[name]

    def update_group_member(self, name, level, initiative_modifier):
        player = new PlayerCharacter(name, level, initiative_modifier)
        self.group_composition[name] = player

    def save_group(self):
        """ should return a group id from the db """
        continue

    def retrieve_group(self, group):
        """ should populate the group form the db """
        continue

    def clear_group(self):
        self.group_composition = {}

    
class NonPlayerCharacter():
    """ Docstring """
    def __init__(self, name, level, initiative_modifier):
        self.npc_name = name
        self.npc_level = level
        self.npc_initiative_modifier = initiative_modifier


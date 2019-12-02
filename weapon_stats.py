"""
ACIT-2515 Assignment 2
Class Name: TestWeaponManager
Created by: Jun
Version: 1.0
Create Date: 2019-11-13
Description: a class generates necessary data
Last Modified:

"""


class WeaponStats:
    """ a class generates necessary data """

    def __init__(self, total_inuse_weapon, total_retired_weapons, total_firearm_num, total_sword_num):
        # Initialize the data values
        self._total_retired_weapons = total_retired_weapons
        self._total_firearm_num = total_firearm_num
        self._total_sword_num = total_sword_num
        self._total_weapon_inuse = total_inuse_weapon

    def get_total_retired_weapons(self):
        # Return the number of all retired weapons
        return self._total_retired_weapons

    def get_total_firearm_num(self):
        # Return the total number of all firearm
        return self._total_firearm_num

    def get_total_sword_num(self):
        # Return the total number of all swords
        return self._total_sword_num

    def get_total_weapon_inuse(self):
        # return the number of all weapons are inuse
        return self._total_weapon_inuse

    def to_dict(self):
        # return the dictionary of the stats
        dict = {
            'total_retired_weapons': self._total_retired_weapons,
            'total_firearm_num': self._total_firearm_num,
            'total_sword_num': self._total_sword_num,
            'total_weapon_inuse': self._total_weapon_inuse
        }
        return dict

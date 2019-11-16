"""
ACIT-2515 Assignment 2
Class Name: Firearm
Created by: Jun
Version: 1.1
Create Date: 2019-10-14
Description: A child class of Abstract Weapon
Last Modified:
- [2019-10-14 :Jun] add validators for the parameters
"""

from abstract_weapon import AbstractWeapon


class Firearm(AbstractWeapon):
    """ Firearm Class - Maintains the details of a firearm """

    BULLETS_NUM_LABEL = "Firearm bullets_num"
    RANGE_LABEL = "Firearm range"
    IS_OVERHEAT_LABEL = "Firearm is_overheat"

    # Statistics on a firearm entity
    def __init__(self, name, materials, is_cold_weapon, is_inuse, bullets_num, range):
        # Initialize parent class
        super().__init__(name, materials, is_cold_weapon, is_inuse)
        # Initialize the data values
        AbstractWeapon._validate_int_input(Firearm.BULLETS_NUM_LABEL, bullets_num)
        self._bullets_num = bullets_num
        AbstractWeapon._validate_int_input(Firearm.RANGE_LABEL, range)
        self._range = range
        self._is_overheat = False

    def set_bullets_num(self, bullets_num):
        # setter for firearm bullets number
        AbstractWeapon._validate_int_input(Firearm.BULLETS_NUM_LABEL, bullets_num)
        self._bullets_num = bullets_num

    def get_bullets_num(self):
        # return bullet numbers - int
        return self._bullets_num

    def get_range(self):
        # return range - int
        return self._range

    def get_overheat(self):
        # return overheat status - boolean
        return self._is_overheat

    def set_overheat(self, is_overheat):
        # setter for firearm overheat status
        AbstractWeapon._validate_boolean_input(Firearm.IS_OVERHEAT_LABEL, is_overheat)
        self._is_overheat = is_overheat

    def get_type(self):
        # return type of the weapon
        return "Firearm"

    def get_usage_status(self):
        # If the bullet number greater than 0, this firearm is in use
        if self._bullets_num > 0:
            self.set_is_inuse(True)
        else:
            self.set_is_inuse(False)
        return self.get_is_inuse()

    def to_dict(self):
        # convert the sword object into python dictionary
        dict = {
            'id': self._id,
            'name': self._name,
            'materials': self._materials,
            'is_cold_weapon': self._is_cold_weapon,
            'is_inuse': self._is_inuse,
            'bullets_num': self._bullets_num,
            'range': self._range,
            'is_overheat': self._is_overheat,
            'type': self.get_type()
        }
        return dict


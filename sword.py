"""
ACIT-2515 Assignment 2
Class Name: Sword
Created by: Jun
Version: 1.0
Create Date: 2019-10-15
Description: A child class of Abstract Weapon
Last Modified:
"""

from abstract_weapon import AbstractWeapon


class Sword(AbstractWeapon):
    """ Sword Class - Maintains the details of a sword """

    SHARP_LABEL = "Sword sharp"
    LENGTH_LABEL = "Sword length"
    IS_DOUBLE_EDGED_LABEL = "Sword is_double_edged"

    # Statistics on a sword entity
    def __init__(self, name, materials, is_cold_weapon, is_inuse, sharp, length, is_double_edged):
        # Initialize parent class
        super().__init__(name, materials, is_cold_weapon, is_inuse)
        # Initialize the data values
        Sword._validate_float_input(Sword.SHARP_LABEL, sharp)
        self._sharp = sharp
        Sword._validate_float_input(Sword.LENGTH_LABEL, length)
        self._length = length
        AbstractWeapon._validate_boolean_input(Sword.IS_DOUBLE_EDGED_LABEL, is_double_edged)
        self._is_double_edged = is_double_edged

    def get_sharp(self):
        # return sharp of the sword - float
        return self._sharp

    def get_double_edged(self):
        # return if the sword is double edged
        return self._is_double_edged

    def get_length(self):
        # return the length of the sword
        return self._length

    def get_type(self):
        # return type of the sword
        return "Sword"

    def get_usage_status(self):
        # If the bullet number greater than 0, this sword is in use
        if self._sharp > 0.8:
            self.set_is_inuse(False)
        else:
            self.set_is_inuse(True)
        return self.get_is_inuse()

    def to_dict(self):
        # convert the sword object into python dictionary
        dict = {
            'id' : self._id,
            'name': self._name,
            'materials': self._materials,
            'is_cold_weapon': self._is_cold_weapon,
            'is_inuse': self._is_inuse,
            'sharp': self._sharp,
            'length': self._length,
            'is_double_edged': self._is_double_edged,
            'type': self.get_type()
        }
        return dict

    @staticmethod
    def _validate_float_input(display_name, float_obj):
        # check if input is a boolean
        if float_obj is None:
            raise ValueError(display_name + " cannot be undefined.")
        if not isinstance(float_obj, float):
            raise ValueError(display_name + " should be a float value.")

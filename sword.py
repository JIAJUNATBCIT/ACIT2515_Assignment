"""
ACIT-2515 Assignment 4
Class Name: Sword
Created by: Jun
Version: 2.0
Create Date: 2019-10-15
Description: A child class of Abstract Weapon
Last Modified:
- [2019-10-14 :Jun] add validators for the parameters
- [2019-12-01 :Jun] re-write the whole class to make it as a SQLAlchemy declarative
"""

from abstract_weapon import AbstractWeapon
from sqlalchemy import Column, String, Integer, Float, DateTime


class Sword(AbstractWeapon):
    """ Sword Class - Maintains the details of a sword """

    SHARP_LABEL = "Sword sharp"
    LENGTH_LABEL = "Sword length"
    IS_DOUBLE_EDGED_LABEL = "Sword is_double_edged"

    WEAPON_TYPE = "Sword"
    sharp = Column(Float)
    length = Column(Float)
    is_double_edged = Column(Integer)

    # Statistics on a sword entity
    def __init__(self, name, materials, is_cold_weapon, is_inuse, manufacture_date, sharp, length, is_double_edged):
        # Initialize parent class
        super().__init__(name, materials, is_cold_weapon, is_inuse, manufacture_date, Sword.WEAPON_TYPE)
        # Initialize the data values
        AbstractWeapon._validate_float_input(Sword.SHARP_LABEL, sharp)
        self.sharp = sharp
        AbstractWeapon._validate_float_input(Sword.LENGTH_LABEL, length)
        self.length = length
        AbstractWeapon._validate_boolean_input(Sword.IS_DOUBLE_EDGED_LABEL, is_double_edged)
        self.is_double_edged = is_double_edged

    def get_sharp(self):
        # return sharp of the sword - float
        return self.sharp

    def get_double_edged(self):
        # return if the sword is double edged
        return self.is_double_edged

    def get_length(self):
        # return the length of the sword
        return self.length

    def get_type(self):
        # return type of the sword
        return self.WEAPON_TYPE

    def get_usage_status(self):
        if self.is_inuse:
            status = "[" + str(self.id) + "]" + self.name + " is a(n) " + self.type + " manufactured at " + \
                     self.manufacture_date.strftime("%Y-%m-%d") + " and still in use"
        else:
            status = "[" + str(self.id) + "]" + self.name + " is a(n) " + self.type + " was manufactured at " + \
                     self.manufacture_date.strftime("%Y-%m-%d") + " and retired at " + self.retired_date.strftime("%Y-%m-%d") if self.retired_date else None
        return status

    def to_dict(self):
        # convert the sword object into python dictionary
        dict = {
            'id' : self.id,
            'name': self.name,
            'materials': self.materials,
            'is_cold_weapon': self.is_cold_weapon,
            'is_inuse': self.is_inuse,
            'manufacture_date': self.manufacture_date.strftime("%Y-%m-%d"),
            'retired_date': self.retired_date.strftime("%Y-%m-%d") if self.retired_date else None,
            'sharp': self.sharp,
            'length': self.length,
            'is_double_edged': self.is_double_edged,
            'type': self.get_type()
        }
        return dict

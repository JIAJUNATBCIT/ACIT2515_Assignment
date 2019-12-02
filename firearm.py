"""
ACIT-2515 Assignment 4
Class Name: Firearm
Created by: Jun
Version: 2.0
Create Date: 2019-10-14
Description: A child class of Abstract Weapon
Last Modified:
- [2019-10-14 :Jun] add validators for the parameters
- [2019-12-01 :Jun] re-write the whole class to make it as a SQLAlchemy declarative
"""

from abstract_weapon import AbstractWeapon
from sqlalchemy import Column, String, Integer, Float, DateTime


class Firearm(AbstractWeapon):
    """ Firearm Class - Maintains the details of a firearm """

    BULLETS_NUM_LABEL = "Firearm bullets_num"
    RANGE_LABEL = "Firearm range"
    IS_OVERHEAT_LABEL = "Firearm is_overheat"

    WEAPON_TYPE = "Firearm"
    bullets_num = Column(Integer)
    range = Column(Float)
    is_overheat = Column(Integer)

    # Statistics on a firearm entity
    def __init__(self, name, materials, is_cold_weapon, is_inuse, manufacture_date, bullets_num, range):
        # Initialize parent class
        super().__init__(name, materials, is_cold_weapon, is_inuse, manufacture_date, Firearm.WEAPON_TYPE)
        # Initialize the data values
        AbstractWeapon._validate_int_input(Firearm.BULLETS_NUM_LABEL, bullets_num)
        self.bullets_num = bullets_num
        AbstractWeapon._validate_float_input(Firearm.RANGE_LABEL, range)
        self.range = range
        self.is_overheat = AbstractWeapon.BOOLEAN_FALSE

    def get_type(self):
        # return type of the weapon
        return self.WEAPON_TYPE

    def get_usage_status(self):
        if self.is_inuse:
            status = "[" + str(self.id) + "]" + self.name + " is a(n) " + self.type + " manufactured at " +\
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
            'bullets_num': self.bullets_num,
            'range': self.range,
            'is_overheat': self.is_overheat,
            'type': self.get_type()
        }
        return dict

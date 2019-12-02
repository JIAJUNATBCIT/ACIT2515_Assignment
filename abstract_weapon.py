"""
ACIT-2515 Assignment 4
Class Name: AbstractWeapon
Created by: Jun
Version: 2.0
Create Date: 2019-10-04
Description: A parent class to generate different weapon objects
Last Modified:
- [2019-10-14 :Jun] add validators for the parameters and get ready for unit test
- [2019-10-14 :Jun] delete setter for id to avoid duplicate id
- [2019-12-01 :Jun] re-write the whole class to make it as a SQLAlchemy declarative
"""

from sqlalchemy import Column, String, Integer, Float, DateTime
from base import Base
import datetime


class AbstractWeapon(Base):
    """ Abstract Weapon entity - Parent class of the weapons """

    NAME_LABEL = "Weapon name"
    MATERIALS_LABEL = "Weapon materials"
    IS_COLD_WEAPON_LABEL = "Weapon is_cold_weapon"
    IS_INUSE_LABEL = "Weapon is_inuse"
    MANUFACTURE_DATE_LABEL = "Weapon manufacture date"
    RETIRED_DATE_LABEL = "Weapon retired date"
    TYPE_LABEL = "Weapon type"

    # declare parameters

    BOOLEAN_TRUE = 1
    BOOLEAN_FALSE = 0

    __tablename__ = "weapons"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    materials = Column(String(100))
    is_cold_weapon = Column(Integer)
    is_inuse = Column(Integer)
    manufacture_date = Column(DateTime)
    retired_date = Column(DateTime)
    type = Column(String(20))

    def __init__(self, name, materials, is_cold_weapon, is_inuse, manufacture_date, type):
        # Create an instance of weapon

        # set the name of the weapon
        AbstractWeapon._validate_string_input(AbstractWeapon.NAME_LABEL, name)
        self.name = name

        # set the materials of the weapon
        AbstractWeapon._validate_string_input(AbstractWeapon.MATERIALS_LABEL, materials)
        self.materials = materials

        # set weather weapon is cold weapon
        AbstractWeapon._validate_boolean_input(AbstractWeapon.IS_COLD_WEAPON_LABEL, is_cold_weapon)
        self.is_cold_weapon = is_cold_weapon

        # set if weapon is in use
        AbstractWeapon._validate_boolean_input(AbstractWeapon.IS_COLD_WEAPON_LABEL, is_inuse)
        self.is_inuse = is_inuse

        # set weapon's manufacture date
        AbstractWeapon._validate_datetime(AbstractWeapon.MANUFACTURE_DATE_LABEL, manufacture_date)
        self.manufacture_date = manufacture_date

        AbstractWeapon._validate_string_input(AbstractWeapon.TYPE_LABEL, type)
        self.type = type

        # set weapon's retired date
        self.retired_date = None

    def set_retired(self, retired_date):
        AbstractWeapon._validate_datetime(AbstractWeapon.MANUFACTURE_DATE_LABEL, retired_date)
        if self.manufacture_date > retired_date:
            raise ValueError(self.RETIRED_DATE_LABEL + " could not before manufacture date")
        self.is_inuse = self.BOOLEAN_FALSE
        self.retired_date = retired_date

    def get_type(self):
        # Abstract method for get_type
        raise NotImplementedError("get_type method must be implemented")

    def get_usage_status(self):
        # Abstract method for usage status
        raise NotImplementedError("get_usage_status must be implemented")

    def to_dict(self):
        # Abstract method for convert the object into dictionary
        raise NotImplementedError("to_dict must be implemented")

    @staticmethod
    def _validate_int_input(display_name, int_obj):
        # check if input is a boolean
        if int_obj is None:
            raise ValueError(display_name + " cannot be undefined.")
        if not isinstance(int_obj, int):
            raise ValueError(display_name + " should be an int value.")

    @staticmethod
    def _validate_string_input(display_name, str_obj):
        # check if input is a string
        if str_obj is None:
            raise ValueError(display_name + " cannot be undefined.")
        if not isinstance(str_obj, str):
            raise ValueError(display_name + " should be a string value.")
        if str_obj == "":
            raise ValueError(display_name + " cannot be empty.")

    @staticmethod
    def _validate_boolean_input(display_name, bool_obj):
        # check if input is a boolean
        if bool_obj is None:
            raise ValueError(display_name + " cannot be undefined.")
        if bool_obj == "":
            raise ValueError(display_name + " cannot be empty.")
        if not isinstance(bool_obj, bool):
            raise ValueError(display_name + " should be a boolean value.")

    @staticmethod
    def _validate_datetime(display_name, date_obj):
        """Validates a datetime"""
        if date_obj is None or type(date_obj) != datetime.datetime or date_obj == "":
            raise ValueError("%s is not a valid date/time." % display_name)

    @staticmethod
    def _validate_float_input(display_name, float_obj):
        # check if input is a boolean
        if float_obj is None:
            raise ValueError(display_name + " cannot be undefined.")
        if not isinstance(float_obj, float):
            raise ValueError(display_name + " should be a float value.")

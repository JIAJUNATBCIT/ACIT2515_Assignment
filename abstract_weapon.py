"""
ACIT-2515 Assignment 2
Class Name: AbstractWeapon
Created by: Jun
Version: 1.1
Create Date: 2019-10-14
Description: A parent class to generate different weapon objects
Last Modified:
- [2019-10-14 :Jun] add validators for the parameters and get ready for unit test
- [2019-10-14 :Jun] delete setter for id to avoid duplicate id
"""


class AbstractWeapon:
    """ Abstract Weapon entity - Parent class of the weapons """

    NAME_LABEL = "Weapon name"
    MATERIALS_LABEL = "Weapon materials"
    IS_COLD_WEAPON_LABEL = "Weapon is_cold_weapon"
    IS_INUSE_LABEL = "Weapon is_inuse"
    INIT_ID = 0

    def __init__(self, name, materials, is_cold_weapon, is_inuse):
        # Initialize the data values
        self._id = AbstractWeapon.INIT_ID
        AbstractWeapon._validate_string_input(AbstractWeapon.NAME_LABEL, name)
        self._name = name
        AbstractWeapon._validate_string_input(AbstractWeapon.MATERIALS_LABEL, materials)
        self._materials = materials
        AbstractWeapon._validate_boolean_input(AbstractWeapon.IS_COLD_WEAPON_LABEL, is_cold_weapon)
        self._is_cold_weapon = is_cold_weapon
        AbstractWeapon._validate_boolean_input(AbstractWeapon.IS_INUSE_LABEL, is_inuse)
        self._is_inuse = is_inuse

    def get_id(self):
        # Return the weapon id
        return self._id

    def set_id(self, id):
        # Setter for weapon id
        AbstractWeapon._validate_int_input(AbstractWeapon.NAME_LABEL, id)
        self._id = id

    def get_name(self):
        # Return the weapon name
        return self._name

    def set_name(self, name):
        # setter for the weapon name
        # name should not be none
        AbstractWeapon._validate_string_input(AbstractWeapon.NAME_LABEL, name)
        self._name = name

    def get_materials(self):
        # Return the weapon materials
        return self._materials

    def set_materials(self, materials):
        # setter for the weapon materials
        # materials should not be none
        AbstractWeapon._validate_string_input(AbstractWeapon.MATERIALS_LABEL, materials)
        self._materials = materials

    def get_is_cold_weapon(self):
        # return boolean whether weapon a cold weapon
        return self._is_cold_weapon

    def set_is_cold_weapon(self, is_cold_weapon):
        # setter for if the weapon a cold weapon
        # is_cold_weapon should not be none
        AbstractWeapon._validate_boolean_input(AbstractWeapon.IS_COLD_WEAPON_LABEL, is_cold_weapon)
        self._is_cold_weapon = is_cold_weapon

    def get_is_inuse(self):
        # return boolean whether weapon is in use
        return self._is_inuse

    def set_is_inuse(self, is_inuse):
        # setter for if the weapon is in use
        # inuse should not be none
        AbstractWeapon._validate_boolean_input(AbstractWeapon.IS_INUSE_LABEL, is_inuse)
        self._is_inuse = is_inuse

    def get_type(self):
        # Abstract method for get_type
        raise NotImplementedError("Get_type method must be implemented")

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

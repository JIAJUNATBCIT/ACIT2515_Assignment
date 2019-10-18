"""
ACIT-2515 Assignment 2
Class Name: Weapon_Manager
Created by: Jun
Version: 1.0
Create Date: 2019-10-16
Description: Maintain weapon entities - CRUD
Last Modified:
"""

import copy
from abstract_weapon import AbstractWeapon


class Weapon_Manager:
    """ A class to maintain weapon entities - CRUD """

    ID_LABLE = "id"
    TYPE_LABEL = "type"

    def __init__(self):
        # Initialize the data values
        self._weapons = []
        self._next_available_id = 0  # '0' by default

    def get(self, id):
        # get the weapon by its id
        AbstractWeapon._validate_int_input(Weapon_Manager.ID_LABLE, id)
        if len(self._weapons) > 0:
            for weapon in self._weapons:
                if weapon.get_id() == id:
                    return weapon
        # return None if weapon is not in the list or the list is empty
        return None

    def add(self, weapon):
        # Add a weapon into the list
        if weapon is None:
            raise ValueError("Add failed - weapon is undefined.")
        # set the next_available_id as the new entity id
        weapon_dul = copy.deepcopy(weapon)
        weapon_dul.set_id(self._next_available_id)
        self._weapons.append(weapon_dul)
        self._next_available_id += 1
        # Return the next_available id
        return self._next_available_id

    def get_all(self):
        # Get all entities in the list
        return self._weapons

    def get_all_by_type(self, type):
        # get all entities by the input type
        AbstractWeapon._validate_string_input(self.TYPE_LABEL, type)
        weapons_by_type = []
        if len(self._weapons) > 0:
            for weapon in self._weapons:
                if weapon.get_type() == type:
                    weapons_by_type.append(weapon)
        return weapons_by_type

    def update(self, update_weapon):
        # update the item in the list
        update_flag = False
        if len(self._weapons) > 0:
            # could not update by an undefined item
            if update_weapon is None:
                raise ValueError("Update failed - weapon is undefined.")
            for i in range(0, len(self._weapons)):
                if self._weapons[i].get_id() == update_weapon.get_id():
                    # item is found, overwrite it
                    self._weapons[i] = update_weapon
                    update_flag = True
                    break
            if not update_flag:
                raise ValueError("Update failed - no such weapon")

    def delete(self, id):
        # delete an item from the list
        delete_flag = False
        if len(self._weapons) > 0:
            # could not delete by an invalid id
            AbstractWeapon._validate_int_input(Weapon_Manager.ID_LABLE, id)
            for i in range(0, len(self._weapons)):
                if self._weapons[i].get_id() == id:
                    del self._weapons[i]
                    delete_flag = True
                    break
            if not delete_flag:
                raise Exception("Delete failed - no such weapon")

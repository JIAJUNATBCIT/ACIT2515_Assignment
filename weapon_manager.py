"""
ACIT-2515 Assignment 3
Class Name: Weapon_Manager
Created by: Jun
Version: 1.3
Create Date: 2019-10-16
Description: Maintain weapon entities - CRUD
Last Modified:
- [2019-10-14 :Jun] add get_weapons_stats to generate a report of the weapon status
- [2019-11-13 :Jun] add filepath and read,write method to save the json data
- [2019-11-15 :Jun] add _sync_next_id method to return the next available id base on our inventory
"""

import os
import copy
import json
from abstract_weapon import AbstractWeapon
from weapon_stats import WeaponStats
from sword import Sword
from firearm import Firearm


class WeaponManager:
    """ A class to maintain weapon entities - CRUD """

    ID_LABLE = "id"
    TYPE_LABEL = "type"
    FILE_PATH_LABEL = "filepath"

    def __init__(self, filepath):
        # Initialize the data values
        self._weapons = []
        self._next_available_id = 0  # '0' by default
        AbstractWeapon._validate_string_input(self.FILE_PATH_LABEL, filepath)
        self._filepath = filepath # keep the weapon's jason data
        self._read_entities_from_file()

    def get(self, id):
        # get all entities from the file
        self._read_entities_from_file()
        # get the weapon by its id
        AbstractWeapon._validate_int_input(WeaponManager.ID_LABLE, id)
        if len(self._weapons) > 0:
            for weapon in self._weapons:
                if weapon.get_id() == id:
                    return weapon
        # return None if weapon is not in the list or the list is empty
        return None

    def add(self, weapon):
        # get all entities from the file
        self._read_entities_from_file()
        # Add a weapon into the list
        if weapon is None:
            raise ValueError("Add failed - weapon is undefined.")
        # get the next available id
        self._next_available_id = self._sync_next_id()
        # set the next_available_id as the new entity id
        weapon_dul = copy.deepcopy(weapon)
        weapon_dul.set_id(self._next_available_id)
        self._weapons.append(weapon_dul)
        self._write_entities_from_file() # write the list into file
        # Return the next_available id
        return self._next_available_id

    def get_all(self):
        # Get all entities from the file
        self._read_entities_from_file()
        return self._weapons

    def get_all_by_type(self, type):
        # get all entities by the input type
        AbstractWeapon._validate_string_input(self.TYPE_LABEL, type)
        weapons_by_type = []
        get_flag = False
        if len(self._weapons) > 0:
            for weapon in self._weapons:
                if weapon.get_type() == type:
                    weapons_by_type.append(weapon)
                    get_flag = True
            if not get_flag:
                raise ValueError("Get failed - no such weapon/type")
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
            self._write_entities_from_file() # write the list into file
            if not update_flag:
                raise ValueError("Update failed - no such weapon")

    def delete(self, id):
        # get all entities from the file
        self._read_entities_from_file()
        # delete an item from the list
        delete_flag = False
        if len(self._weapons) > 0:
            # could not delete by an invalid id
            AbstractWeapon._validate_int_input(WeaponManager.ID_LABLE, id)
            for i in range(0, len(self._weapons)):
                if self._weapons[i].get_id() == id:
                    del self._weapons[i]
                    delete_flag = True
                    break
        self._write_entities_from_file()  # write the list into file
        if not delete_flag:
            raise ValueError("Delete failed - no such weapon")

    def get_weapons_stats(self):
        # Return the weapon status
        total_weapon_num = len(self._weapons)
        total_firearm_num = len(self.get_all_by_type("Firearm"))
        total_sword_num = len(self.get_all_by_type("Sword"))
        inuse_weapons = []
        for weapon in self._weapons:
            if weapon.get_is_inuse:
                inuse_weapons.append(weapon)
        total_weapon_inuse = len(inuse_weapons)
        return WeaponStats(total_weapon_num, total_firearm_num, total_sword_num, total_weapon_inuse)

    def _read_entities_from_file(self):
        # Read json entities from file
        if os.path.exists(self._filepath):
            temp_weapons = []
            with open(self._filepath, 'r') as file:
                if file is not None:
                    data = json.load(file)
                    for entity in data:
                        if entity["type"] == "Sword":
                            weapon = Sword(
                                        entity["name"],
                                        entity["materials"],
                                        entity["is_cold_weapon"],
                                        entity["is_inuse"],
                                        entity["sharp"],
                                        entity["length"],
                                        entity["is_double_edged"]
                                     )
                        else:
                            weapon = Firearm(
                                        entity["name"],
                                        entity["materials"],
                                        entity["is_cold_weapon"],
                                        entity["is_inuse"],
                                        entity["bullets_num"],
                                        entity["range"]
                                     )
                        weapon.set_id(entity["id"])
                        temp_weapons.append(weapon)
                    self._weapons = temp_weapons

    def _write_entities_from_file(self):
        temp_list = []
        if self._weapons is not None and len(self._weapons) >= 0:
            for weapon in self._weapons:
                temp_list.append(weapon.to_dict())
            with open(self._filepath, 'w') as file:
                json.dump(temp_list, file)

    def _sync_next_id(self):
        """
        - Assignment 3:
        Since now we store our data in database(right now is in a file), which means our system might be shutdown
        any time and all data in memory will be refreshed. However, we do not store the next available id in database,
        it will lead to a problem of duplicated id. eg:
        - We add the first entity into our system which id is 0
        - We reboot our system
        - We add another entity into our system, since memory already refreshed, id will again, start from 0
        - We get 2 entities with the same id (id=0)
        In order to avoid above situation, every time before we add an entity, we need to load all item from our
        database and find the next available id.
        * This method helps to find the next available id.
        :return: next available id
        """
        # create a temporary list to store ids
        _ids = []
        if self._weapons is not None and len(self._weapons) > 0:
            for weapon in self._weapons:
                _ids.append(int(weapon.get_id()))
            return max(_ids) + 1
        else: # no item in the list, next available id will be 1
            return 1

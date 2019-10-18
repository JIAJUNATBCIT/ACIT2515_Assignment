"""
ACIT-2515 Assignment 2
Class Name: TestWeaponManager
Created by: Jun
Version: 1.2
Create Date: 2019-10-16
Description: test cases for class Weapon Manager
Last Modified:
- [2019-10-16: Jun] put all validators in the Abstract class
- [2019-10-18: Jun] Add tearDown method
"""

import unittest
from firearm import Firearm
from sword import Sword
from weapon_manager import Weapon_Manager


class TestWeaponManager(unittest.TestCase):
    """ Unit Tests for the Weapon_Manager Class """

    # create different type of weapon objects
    def setUp(self) -> None:
        self.test_firearm_1 = Firearm("Armsel Striker", "iron", False, True, 50, 50)
        self.test_firearm_2 = Firearm("Beretta A303", "iron", False, False, 0, 100)
        self.test_sword_1 = Sword("Skull Cleaver", "iron", True, True, 0.91, 3.1, False)
        self.test_sword_2 = Sword("Dawn Splitter", "wood", False, False, 0.82, 2.7, True)
        self.test_sword_3 = Sword("Grimfrost", "wood", False, False, 0.82, 2.7, True)
        self.test_weapon_manager = Weapon_Manager()

    def tearDown(self) -> None:
        self.test_firearm_1 = None
        self.test_firearm_2 = None
        self.test_sword_1 = None
        self.test_sword_2 = None
        self.test_sword_3 = None
        self.test_weapon_manager = Weapon_Manager()

    def test_weapon_manager(self):
        """ 001 - Test the constructor """
        self.assertIsNotNone(self.test_weapon_manager)

    def test_add(self):
        """ 002 - Test the add method """

        # 002A - add an undefined item into the list
        self.assertRaisesRegex(Exception, "Add failed - weapon is undefined.", self.test_weapon_manager.add, None)

        # 002B - add an valid item into the list
        self.assertEqual(len(self.test_weapon_manager.get_all()), 0)
        self.test_weapon_manager.add(self.test_firearm_1)
        self.assertEqual(len(self.test_weapon_manager.get_all()), 1)
        self.test_weapon_manager.add(self.test_sword_1)
        self.assertEqual(len(self.test_weapon_manager.get_all()), 2)

        # 002C - add a duplicate item into the list - success, but both items' ids will be different
        self.test_weapon_manager.add(self.test_sword_1)
        self.assertEqual(len(self.test_weapon_manager.get_all()), 3)
        self.assertNotEqual(self.test_weapon_manager._weapons[1].get_id(), self.test_weapon_manager._weapons[2].get_id())

        # 002D - 3 items already in the list, add the fourth item, should return next available id - 4
        self.assertEqual(self.test_weapon_manager.add(self.test_sword_3), 4)

    def test_get_all(self):
        """ 003 - Test the get_all method """

        # 003A - add 3 items into the list, this method should return a list with 3 elements
        self.test_weapon_manager.add(self.test_firearm_1)
        self.test_weapon_manager.add(self.test_sword_1)
        self.test_weapon_manager.add(self.test_sword_2)
        self.assertEqual(len(self.test_weapon_manager.get_all()), 3)

    def test_get_all_by_type(self):
        """ 004 - Test the get_all_by_type method """

        # 004A - Must reject an undefined Weapon type
        self.assertRaisesRegex(ValueError, "type cannot be undefined.", self.test_weapon_manager.get_all_by_type, None)

        # 004B - Must reject an empty Weapon type
        self.assertRaisesRegex(ValueError, "type cannot be empty.", self.test_weapon_manager.get_all_by_type, "")

        # 004C - Must reject a non-string Weapon type
        self.assertRaisesRegex(ValueError, "type should be a string value.", self.test_weapon_manager.get_all_by_type, 99)

        # 004D - Add 2 swords and 1 firearm into the list and get all
        # items with the type 'Sword', method should return 2
        self.test_weapon_manager.add(self.test_firearm_1)
        self.test_weapon_manager.add(self.test_sword_1)
        self.test_weapon_manager.add(self.test_sword_2)
        self.assertEqual(len(self.test_weapon_manager.get_all_by_type("Sword")), 2)

    def test_update(self):
        """ 005 - Test the update method """

        # 005A - Must reject an undefined item
        self.test_weapon_manager.add(self.test_firearm_1)
        self.assertRaisesRegex(ValueError, "Update failed - weapon is undefined.", self.test_weapon_manager.update, None)

        # 005B - Update an item that not exist, should raise an exception
        self.test_weapon_manager.add(self.test_firearm_2)
        self.test_sword_1.set_id(999)
        self.assertRaisesRegex(ValueError, "Update failed - no such weapon", self.test_weapon_manager.update,
                               self.test_sword_1)

        # 005C - Update an item
        self.test_weapon_manager.add(self.test_sword_2) # id of sword_2 has been set to 2
        self.test_sword_3.set_id(2) # set sword_3's id to 2
        self.test_weapon_manager.update(self.test_sword_3) # sword_2 will be overwritten by sword_3 as both have the
        # same id
        self.assertEqual(self.test_weapon_manager.get(2).get_name(), "Grimfrost") # item with id 2 should be
        # overwritten by sword_3 now

    def test_delete(self):
        """ 006 - Test the delete method """

        # 006A - Must reject an invalid id
        self.test_weapon_manager.add(self.test_firearm_1)
        self.assertRaisesRegex(ValueError, "id cannot be undefined.", self.test_weapon_manager.delete, None)
        self.assertRaisesRegex(ValueError, "id should be an int value.", self.test_weapon_manager.delete, "1")

        # 006B - Delete an item that not exist
        self.test_weapon_manager.add(self.test_firearm_2)
        self.test_weapon_manager.add(self.test_sword_1)
        self.test_weapon_manager.add(self.test_sword_2)
        # there are 4 items in the list and id range from 0 ~ 3, delete a none-exist item with by id equals 4
        self.assertRaisesRegex(Exception, "Delete failed - no such weapon", self.test_weapon_manager.delete, 4)

        # 006C - Delete an item(id=1) - should have 3 items left
        self.test_weapon_manager.delete(1)
        self.assertEqual(len(self.test_weapon_manager.get_all()), 3)

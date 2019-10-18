"""
ACIT-2515 Assignment 2
Class Name: TestFirearm
Created by: Jun
Version: 1.1
Create Date: 2019-10-15
Description: test cases for class Firearm
Last Modified:
- [2019-10-15 :Jun] add test case for the get_type method
"""

import unittest
from firearm import Firearm


class TestFirearm(unittest.TestCase):
    """ Unit Tests for the Firearm Class """

    # create the firearm objects
    def setUp(self) -> None:
        self.test_firearm_1 = Firearm("Armsel Striker", "iron", False, True, 50, 50)
        self.test_firearm_2 = Firearm("Beretta A303", "iron", False, False, 0, 100)

    def test_firearm(self):
        """ 001 Test the constructor """
        self.assertIsNotNone(self.test_firearm_1)
        self.assertIsNotNone(self.test_firearm_2)

    def test_firearm_invalid_parameters(self):
        """ 002 - Invalid Construction Parameters """

        # 002A - Must reject an undefined Weapon name
        self.assertRaisesRegex(ValueError, "Weapon name cannot be undefined.", Firearm, None, "iron",
                               False, True, 50, 50)

        # 002B - Must reject an empty Weapon name
        self.assertRaisesRegex(ValueError, "Weapon name cannot be empty.", Firearm, "", "iron",
                               False, True, 50, 50)

        # 002C - Must reject a non-string Weapon name
        self.assertRaisesRegex(ValueError, "Weapon name should be a string value.", Firearm, 99, "iron",
                               False, True, 50, 50)

        # 002D - Must reject an undefined Weapon materials
        self.assertRaisesRegex(ValueError, "Weapon materials cannot be undefined.", Firearm,
                               "Armsel Striker", None, False, True, 50, 50)

        # 002E - Must reject an empty Weapon materials
        self.assertRaisesRegex(ValueError, "Weapon materials cannot be empty.", Firearm, "Armsel Striker",
                               "",
                               False, True, 50, 50)

        # 002F - Must reject a non-string Weapon materials
        self.assertRaisesRegex(ValueError, "Weapon materials should be a string value.", Firearm,
                               "Armsel Striker", 99, False, True, 50, 50)

        # 002G - Must reject an undefined Weapon is_cold_weapon
        self.assertRaisesRegex(ValueError, "Weapon is_cold_weapon cannot be undefined.", Firearm,
                               "Armsel Striker", "iron", None, True, 50, 50)

        # 002H - Must reject a non-boolean Weapon is_cold_weapon
        self.assertRaisesRegex(ValueError, "Weapon is_cold_weapon should be a boolean value.", Firearm,
                               "Armsel Striker", "iron", "False", True, 50, 50)

        # 002I - Must reject an undefined Weapon is_inuse
        self.assertRaisesRegex(ValueError, "Weapon is_inuse cannot be undefined.", Firearm,
                               "Armsel Striker", "iron", False, None, 50, 50)

        # 002J - Must reject a non-boolean Weapon is_inuse
        self.assertRaisesRegex(ValueError, "Weapon is_inuse should be a boolean value.", Firearm,
                               "Armsel Striker", "iron", False, "True", 50, 50)

        # 002K - Must reject an undefined Firearm bullets_num
        self.assertRaisesRegex(ValueError, "Firearm bullets_num cannot be undefined.", Firearm,
                               "Armsel Striker", "iron", False, True, None, 50)

        # 002L - Must reject a non-integer Firearm bullets_num
        self.assertRaisesRegex(ValueError, "Firearm bullets_num should be an int value.", Firearm,
                               "Armsel Striker", "iron", False, True, "50", 50)

        # 002M - Must reject an undefined Firearm range
        self.assertRaisesRegex(ValueError, "Firearm range cannot be undefined.", Firearm,
                               "Armsel Striker", "iron", False, True, 50, None)

        # 002N - Must reject a non-integer Firearm range
        self.assertRaisesRegex(ValueError, "Firearm range should be an int value.", Firearm,
                               "Armsel Striker", "iron", False, True, 50, "50")

    def test_get_bullets_num(self):
        """ 003 - Test the get_bullets_num method """

        # 003A - should show up 0 if firearm is out of bullets
        self.assertEqual(self.test_firearm_2.get_bullets_num(), 0)

        # 003B - should show up 50 if firearm has 50 bullets left
        self.assertEqual(self.test_firearm_1.get_bullets_num(), 50)

    def test_set_bullets_num(self):
        """ 004 - Test the set_bullets_num method """

        # 004A - Must reject an undefined Firearm bullets_num
        self.assertRaisesRegex(ValueError, "Firearm bullets_num cannot be undefined.",
                               self.test_firearm_1.set_bullets_num, None)

        # 004B - Must reject a non-integer Firearm bullets_num
        self.assertRaisesRegex(ValueError, "Firearm bullets_num should be an int value",
                               self.test_firearm_1.set_bullets_num, "50")

        # 004C - Set bullets_num to 100
        self.test_firearm_1.set_bullets_num(100)
        self.assertEqual(self.test_firearm_1.get_bullets_num(), 100)

    def test_get_range(self):
        """ 005 - Test the get_range method """

        # 005A - should show up 50 if firearm's range is 50
        self.assertEqual(self.test_firearm_1.get_range(), 50)

    def test_get_overheat(self):
        """ 006 - Test the get_overheat method """

        # False - should show up False since firearm's overheat is set to false by default
        self.assertFalse(self.test_firearm_1.get_overheat())

    def test_set_overheat(self):
        """ 007 - Test the set_overheat method """

        # 007A - Must reject an undefined Weapon is_overheat
        self.assertRaisesRegex(ValueError, "Firearm is_overheat cannot be undefined.", self.test_firearm_1.set_overheat, None)

        # 007B - Must reject a non-boolean Weapon is_overheat
        self.assertRaisesRegex(ValueError, "Firearm is_overheat should be a boolean value.", self.test_firearm_1.set_overheat, "True")

        # 007C - Set Weapon is_overheat to True
        self.test_firearm_1.set_overheat(True)
        self.assertTrue(self.test_firearm_1.get_overheat())

    def test_get_type(self):
        """ 008 - Test the get_type method """

        # 008A - Should return 'Firearm' string
        self.assertEqual(self.test_firearm_1.get_type(), "Firearm")


if __name__ == '__main__':
    unittest.main()

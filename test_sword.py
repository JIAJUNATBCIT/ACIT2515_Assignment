"""
ACIT-2515 Assignment 2
Class Name: TestSword
Created by: Jun
Version: 1.3
Create Date: 2019-10-15
Description: test cases for class Sword
Last Modified:
- [2019-10-15 :Jun] add test case for the get_type method
- [2019-10-18: Jun] Add tearDown method
- [2019-11-15: Jun] Add test case for the to_dict method
"""

import unittest
from sword import Sword


class TestSword(unittest.TestCase):
    """ Unit Tests for the Sword Class """

    # create the sword objects
    def setUp(self) -> None:
        self.test_sword_1 = Sword("Skull Cleaver", "iron", True, True, 0.91, 3.1, False)
        self.test_sword_2 = Sword("Dawn Splitter", "wood", False, False, 0.82, 2.7, True)

    def tearDown(self) -> None:
        self.test_sword_1 = None
        self.test_sword_2 = None

    def test_sword(self):
        """ 001 - Test the constructor """
        self.assertIsNotNone(self.test_sword_1)
        self.assertIsNotNone(self.test_sword_2)

    def test_sword_invalid_parameters(self):
        """ 002 - Invalid Construction Parameters """

        # 002A - Must reject an undefined Weapon name
        self.assertRaisesRegex(ValueError, "Weapon name cannot be undefined.", Sword, None, "iron",
                               False, True, 0.82, 2.7, True)

        # 002B - Must reject an empty Weapon name
        self.assertRaisesRegex(ValueError, "Weapon name cannot be empty.", Sword, "", "iron",
                               False, True, 0.82, 2.7, True)

        # 002C - Must reject a non-string Weapon name
        self.assertRaisesRegex(ValueError, "Weapon name should be a string value.", Sword, 99, "iron",
                               False, True, 0.82, 2.7, True)

        # 002D - Must reject an undefined Weapon materials
        self.assertRaisesRegex(ValueError, "Weapon materials cannot be undefined.", Sword,
                               "Skull Cleaver", None, False, True, 0.82, 2.7, True)

        # 002E - Must reject an empty Weapon materials
        self.assertRaisesRegex(ValueError, "Weapon materials cannot be empty.", Sword, "Skull Cleaver",
                               "", False, True, 0.82, 2.7, True)

        # 002F - Must reject a non-string Weapon materials
        self.assertRaisesRegex(ValueError, "Weapon materials should be a string value.", Sword,
                               "Armsel Striker", 99, False, True, 0.82, 2.7, True)

        # 002G - Must reject an undefined Weapon is_cold_weapon
        self.assertRaisesRegex(ValueError, "Weapon is_cold_weapon cannot be undefined.", Sword,
                               "Skull Cleaver", "iron", None, True, 0.82, 2.7, True)

        # 002H - Must reject a non-boolean Weapon is_cold_weapon
        self.assertRaisesRegex(ValueError, "Weapon is_cold_weapon should be a boolean value.", Sword,
                               "Skull Cleaver", "iron", "False", True, 0.82, 2.7, True)

        # 002I - Must reject an undefined Weapon is_inuse
        self.assertRaisesRegex(ValueError, "Weapon is_inuse cannot be undefined.", Sword,
                               "Skull Cleaver", "iron", False, None, 0.82, 2.7, True)

        # 002J - Must reject a non-boolean Weapon is_inuse
        self.assertRaisesRegex(ValueError, "Weapon is_inuse should be a boolean value.", Sword,
                               "Skull Cleaver", "iron", False, "True", 0.82, 2.7, True)

        # 002K - Must reject an undefined Sword sharp
        self.assertRaisesRegex(ValueError, "Sword sharp cannot be undefined.", Sword,
                               "Skull Cleaver", "iron", False, True, None, 2.7, True)

        # 002L - Must reject a non-float Sword sharp
        self.assertRaisesRegex(ValueError, "Sword sharp should be a float value.", Sword,
                               "Skull Cleaver", "iron", False, True, "0.82", 2.7, True)

        # 002M - Must reject an undefined Sword length
        self.assertRaisesRegex(ValueError, "Sword length cannot be undefined.", Sword,
                               "Skull Cleaver", "iron", False, True, 0.82, None, True)

        # 002N - Must reject a non-float Sword length
        self.assertRaisesRegex(ValueError, "Sword length should be a float value.", Sword,
                               "Skull Cleaver", "iron", False, True, 0.82, "2.7", True)

        # 002O - Must reject a undefined Sword is_double_edged
        self.assertRaisesRegex(ValueError, "Sword is_double_edged cannot be undefined.", Sword,
                               "Skull Cleaver", "iron", False, True, 0.82, 2.7, None)

        # 002P - Must reject a non-boolean Sword is_double_edged
        self.assertRaisesRegex(ValueError, "Sword is_double_edged should be a boolean value.", Sword,
                               "Skull Cleaver", "iron", False, True, 0.82, 2.7, "True")

    def test_get_sharp(self):
        """ 003 - Test the get_sharp method """

        # should show up 0.91 if the sword's sharp is 0.91
        self.assertEqual(self.test_sword_1.get_sharp(), 0.91)

    def test_get_double_edged(self):
        """ 004 - Test the get_double_edged method """

        # False - should show up false since sword_1's is a single edged sword
        self.assertFalse(self.test_sword_1.get_double_edged())

    def test_get_length(self):
        """ 005 - Test the get_length method """

        # should show up 3.1 if the sword's length is 3.1
        self.assertEqual(self.test_sword_1.get_length(), 3.1)

    def test_get_type(self):
        """ 006 - Test the get_type method """

        # 006A - Should return 'Sword' string
        self.assertEqual(self.test_sword_1.get_type(), "Sword")

    def test_to_dict(self):
        """ 007 - Test the to_dict method """

        test_sword = {
            "id": 0,
            "name": "Skull Cleaver",
            "materials": "iron",
            "is_cold_weapon": True,
            "is_inuse": True,
            "sharp": 0.91,
            "length": 3.1,
            "is_double_edged": False,
            "type": "Sword"
        }

        # 007A - should return a dictionary same as the test_sword
        self.assertEqual(self.test_sword_1.to_dict(), test_sword)


if __name__ == '__main__':
    unittest.main()

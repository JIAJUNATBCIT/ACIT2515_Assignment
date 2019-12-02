"""
ACIT-2515 Assignment 4
Class Name: Weapon_Manager
Created by: Jun
Version: 2.0
Create Date: 2019-10-16
Description: Maintain weapon entities - CRUD
Last Modified:
- [2019-10-14 :Jun] add get_weapons_stats to generate a report of the weapon status
- [2019-11-13 :Jun] add filepath and read,write method to save the json data
- [2019-11-15 :Jun] add _sync_next_id method to return the next available id base on our inventory
- [2019-12-01 :Jun] re-write the whole class to make it as a SQLAlchemy declarative
"""

from abstract_weapon import AbstractWeapon
from weapon_stats import WeaponStats
from sword import Sword
from firearm import Firearm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class WeaponManager:
    """ A class to maintain weapon entities - CRUD """

    def __init__(self, db_filename):
        # Initialize the database
        if db_filename is None or db_filename == "":
            raise ValueError("DB Name cannot be undefined")
        if not isinstance(db_filename, str):
            raise ValueError("DB Name should be a string value")
        engine = create_engine("sqlite:///" + db_filename)
        self._db_session = sessionmaker(bind=engine, expire_on_commit=False)

    def get(self, id):
        # get the weapon by its id
        session = self._db_session()
        weapon = session.query(Firearm).filter(
            Firearm.id == id, Firearm.type == Firearm.WEAPON_TYPE).first()

        if weapon is None:
            weapon = session.query(Sword).filter(Sword.id == id, Sword.type == Sword.WEAPON_TYPE).first()

        session.close()
        return weapon

    def add(self, weapon):
        # Add a weapon into the list
        if weapon is None or not isinstance(weapon, AbstractWeapon):
            raise ValueError("Add failed - weapon is undefined.")

        # Verify no duplicated Id
        if self.get(weapon.id):
            raise ValueError("Id already exists.")

        session = self._db_session()
        session.add(weapon)
        session.commit()
        session.close()

    def get_all(self):
        # Get all entities from database
        session = self._db_session()
        all_weapons = []
        swords = self.get_all_by_type("Sword")
        firearms = self.get_all_by_type("Firearm")
        all_weapons.extend(swords)
        all_weapons.extend(firearms)
        session.close()
        return all_weapons

    def get_all_by_type(self, type):
        # get all entities by the input type
        AbstractWeapon._validate_string_input(AbstractWeapon.TYPE_LABEL, type)
        session = self._db_session()
        if Firearm.WEAPON_TYPE == type:
            weapons = session.query(Firearm).filter(Firearm.type == type).all()
        else:
            weapons = session.query(Sword).filter(Sword.type == type).all()
        session.close()
        return weapons

    def update(self, update_weapon):
        # update the item in the database
        session = self._db_session()
        if update_weapon is None:
            raise ValueError("Update failed - weapon is undefined.")
        if not self.get(update_weapon.id):
            raise ValueError("Update failed - no such weapon")
        if update_weapon.get_type() == "Sword":
            sword = session.query(Sword).filter(Sword.id == update_weapon.id)
            sword.update({
                Sword.name : update_weapon.name,
                Sword.materials: update_weapon.materials,
                Sword.is_cold_weapon: update_weapon.is_cold_weapon,
                Sword.is_inuse: update_weapon.is_inuse,
                Sword.manufacture_date: update_weapon.manufacture_date,
                Sword.retired_date: update_weapon.retired_date,
                Sword.sharp: update_weapon.sharp,
                Sword.length: update_weapon.length,
                Sword.is_double_edged: update_weapon.is_double_edged
            })
        else:
            firearm = session.query(Firearm).filter(Firearm.id == update_weapon.id)
            firearm.update({
                Firearm.name : update_weapon.name,
                Firearm.materials: update_weapon.materials,
                Firearm.is_cold_weapon: update_weapon.is_cold_weapon,
                Firearm.is_inuse: update_weapon.is_inuse,
                Firearm.manufacture_date: update_weapon.manufacture_date,
                Firearm.retired_date: update_weapon.retired_date,
                Firearm.bullets_num: update_weapon.bullets_num,
                Firearm.range: update_weapon.range,
                Firearm.is_overheat: update_weapon.is_overheat
            })
        session.flush()
        session.commit()
        session.close()

    def delete(self, id):
        # Delete an entity from database
        if id is None or not isinstance(id, int):
            raise ValueError("Invalid id.")

        session = self._db_session()

        weapon = session.query(AbstractWeapon).filter(
            AbstractWeapon.id == id).first()

        if weapon is None:
            session.close()
            raise ValueError("Delete failed - no such weapon")

        session.delete(weapon)
        session.commit()
        session.close()

    def get_weapons_stats(self):
        # Return the weapon status
        weapons = self.get_all()
        inuse_weapons = []
        retired_weapons = []
        for weapon in weapons:
            if weapon.is_inuse:
                inuse_weapons.append(weapon)
            if weapon.retired_date is not None:
                retired_weapons.append(weapon)
        total_weapon_inuse = len(inuse_weapons)
        total_retired_weapons_num = len(retired_weapons)
        total_firearm_num = len(self.get_all_by_type("Firearm"))
        total_sword_num = len(self.get_all_by_type("Sword"))
        return WeaponStats(total_weapon_inuse, total_retired_weapons_num, total_firearm_num, total_sword_num)

    def get_weapons_reports(self, type):
        # Return the usage report for each in use weapons
        if type is None or not isinstance(type, str) or type not in(Firearm.WEAPON_TYPE, Sword.WEAPON_TYPE):
            raise ValueError("Invalid weapon type.")
        # return the report for each weapons
        weapons = self.get_all_by_type(type)
        weapons_desc = []
        for weapon in weapons:
            weapons_desc.append(weapon.get_usage_status())
        return weapons_desc

    def set_retire(self, id, retire_date):
        # Update a weapon to 'retired' status
        AbstractWeapon._validate_int_input("Weapon id",id)
        AbstractWeapon._validate_datetime("Retire Date", retire_date)
        session = self._db_session()
        weapon = session.query(Firearm).filter(
            Firearm.id == id, Firearm.type == Firearm.WEAPON_TYPE).first()
        if weapon is None:
            weapon = session.query(Sword).filter(Sword.id == id, Sword.type == Sword.WEAPON_TYPE).first()
        weapon.set_retired(retire_date)
        session.commit()
        session.close()



import tkinter as tk
from tkinter import messagebox
import requests
import re


class AddFirearmPopup(tk.Frame):
    """ Popup Frame to Add a Firearm """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=3)

        tk.Label(self, text="Name:").grid(row=2, column=1)
        self._name = tk.Entry(self)
        self._name.grid(row=2, column=2)
        tk.Label(self, text="Materials:").grid(row=3, column=1)
        self._materials = tk.Entry(self)
        self._materials.grid(row=3, column=2)
        tk.Label(self, text="Cold Weapon:").grid(row=4, column=1)
        self._is_cold_weapon = tk.BooleanVar()
        radio1 = tk.Radiobutton(self, text="Yes", value=True, variable=self._is_cold_weapon)
        radio1.grid(row=4, column=2)
        radio2 = tk.Radiobutton(self, text="No", value=False, variable=self._is_cold_weapon)
        radio2.grid(row=4, column=3)
        tk.Label(self, text="Inuse:").grid(row=5, column=1)
        self._is_inuse = tk.BooleanVar()
        radio3 = tk.Radiobutton(self, text="Yes", value=True, variable=self._is_inuse)
        radio3.grid(row=5, column=2)
        radio4 = tk.Radiobutton(self, text="No", value=False, variable=self._is_inuse)
        radio4.grid(row=5, column=3)
        tk.Label(self, text="Manufacture Date:").grid(row=6, column=1)
        self._manufacture_date = tk.Entry(self)
        self._manufacture_date.grid(row=6, column=2)
        tk.Label(self, text="Bullets Num:").grid(row=7, column=1)
        self._bullets_num = tk.Entry(self)
        self._bullets_num.grid(row=7, column=2)
        tk.Label(self, text="Range:").grid(row=8, column=1)
        self._range = tk.Entry(self)
        self._range.grid(row=8, column=2)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=9, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=9, column=2)

    def _submit_cb(self):
        """ Submit Add Firearm """

        # Validate the non-string data values
        if re.match("^\d{4}-\d{2}-\d{2}$", self._manufacture_date.get()) is None:
            messagebox.showerror("Error", "Manufacture Date must have format yyyy-mm-dd")
            return

        if re.match("^\d+$", self._bullets_num.get()) is None:
            messagebox.showerror("Error", "Bullets Number must be a valid integer")
            return

        if re.match("^\s*(?=.*[1-9])\d*(?:\.\d{1,2})?\s*$", self._range.get()) is None:
            messagebox.showerror("Error", "Range must be a valid float")
            return

        # Create the dictionary for the JSON request body
        data = {}
        data['name'] = self._name.get()
        data['materials'] = self._materials.get()
        data['is_cold_weapon'] = self._is_cold_weapon.get()
        data['is_inuse'] = self._is_inuse.get()
        data['manufacture_date'] = self._manufacture_date.get()
        data['bullets_num'] = self._bullets_num.get()
        data['range'] = self._range.get()
        data['type'] = "Firearm"

        self._add_firearm(data)

    def _add_firearm(self, data):
        """ Adds a firearm to the backend grid """
        headers = {"content-type": "application/json"}
        response = requests.post("http://127.0.0.1:5000/weaponwarehouse/weapons", json=data, headers=headers)

        if response.status_code == 200:
            self._close_cb()
        else:
            messagebox.showerror("Error", "Cannot add tablet because: " + response.text)
            self.focus_get()

import tkinter as tk
from tkinter import messagebox
import requests
import re


class UpdateSwordPopup(tk.Frame):
    """ Popup Frame to Add a Sword """

    def __init__(self, parent, id, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=3)

        tk.Label(self, text="Name:").grid(row=3, column=1)
        self._name = tk.Entry(self)
        self._name.grid(row=3, column=2)
        tk.Label(self, text="Materials:").grid(row=4, column=1)
        self._materials = tk.Entry(self)
        self._materials.grid(row=4, column=2)
        tk.Label(self, text="Cold Weapon:").grid(row=5, column=1)
        self._is_cold_weapon = tk.BooleanVar()
        radio1 = tk.Radiobutton(self, text="Yes", value=True, variable=self._is_cold_weapon)
        radio1.grid(row=5, column=2)
        radio2 = tk.Radiobutton(self, text="No", value=False, variable=self._is_cold_weapon)
        radio2.grid(row=5, column=3)
        tk.Label(self, text="Inuse:").grid(row=6, column=1)
        self._is_inuse = tk.BooleanVar()
        radio3 = tk.Radiobutton(self, text="Yes", value=True, variable=self._is_inuse)
        radio3.grid(row=6, column=2)
        radio4 = tk.Radiobutton(self, text="No", value=False, variable=self._is_inuse)
        radio4.grid(row=6, column=3)
        tk.Label(self, text="Manufacture Date:").grid(row=7, column=1)
        self._manufacture_date = tk.Entry(self)
        self._manufacture_date.grid(row=7, column=2)
        tk.Label(self, text="Sharp:").grid(row=8, column=1)
        self._sharp = tk.Entry(self)
        self._sharp.grid(row=8, column=2)
        tk.Label(self, text="Length:").grid(row=9, column=1)
        self._length = tk.Entry(self)
        self._length.grid(row=9, column=2)
        tk.Label(self, text="Double Edged:").grid(row=10, column=1)
        self._is_double_edged = tk.BooleanVar()
        radio5 = tk.Radiobutton(self, text="Yes", value=True, variable=self._is_double_edged)
        radio5.grid(row=10, column=2)
        radio6 = tk.Radiobutton(self, text="No", value=False, variable=self._is_double_edged)
        radio6.grid(row=10, column=3)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=11, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=11, column=2)

    def _submit_cb(self):
        """ Submit the Add sword """

        # Validate the non-string data values
        if re.match("^\d{4}-\d{2}-\d{2}$", self._manufacture_date.get()) is None:
            messagebox.showerror("Error", "Received date must have format yyyy-mm-dd")
            return

        if re.match("^\s*(?=.*[1-9])\d*(?:\.\d{1,2})?\s*$", self._sharp.get()) is None:
            messagebox.showerror("Error", "Range must be a valid float")
            return

        if re.match("^\s*(?=.*[1-9])\d*(?:\.\d{1,2})?\s*$", self._length.get()) is None:
            messagebox.showerror("Error", "Range must be a valid float")
            return

        # Create the dictionary for the JSON request body
        data = {}
        data['name'] = self._name.get()
        data['materials'] = self._materials.get()
        data['is_cold_weapon'] = self._is_cold_weapon.get()
        data['is_inuse'] = int(self._is_inuse.get())
        data['manufacture_date'] = self._manufacture_date.get()
        data['sharp'] = self._sharp.get()
        data['length'] = self._length.get()
        data['is_double_edged'] = self._is_double_edged.get()
        data['type'] = "Sword"

        self._add_sword(data)

    # Implement your code here
    def _add_sword(self, data):
        """ Adds a phone to the backend grid """
        headers = {"content-type": "application/json"}
        response = requests.post("http://127.0.0.1:5000/repairshop/devices", json=data, headers=headers)

        if response.status_code == 200:
            self._close_cb()
        else:
            messagebox.showerror("Error", "Cannot add tablet because: " + response.text)
            self.focus_get()

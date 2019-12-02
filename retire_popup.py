import tkinter as tk
from tkinter import messagebox
import requests


class RetirePopup(tk.Frame):
    """ Popup Frame to Complete a Repair """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="Id:").grid(row=1, column=1)
        self._id = tk.Entry(self)
        self._id.grid(row=1, column=2)
        tk.Label(self, text="Retire Date:").grid(row=2, column=1)
        self._retired_date = tk.Entry(self)
        self._retired_date.grid(row=2, column=2)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=7, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=7, column=2)

    def _submit_cb(self):
        """ Submit retire weapon """

        data = {}
        data['id'] = int(self._id.get())
        data['retired_date'] = self._retired_date.get()
        self._retire_weapon(data)

    def _retire_weapon(self, data):
        headers = {"content-type": "application/json"}
        response = requests.put("http://127.0.0.1:5000/weaponwarehouse/weapons/retire", json=data, headers=headers)

        if response.status_code != 200:
            messagebox.showerror("Error", "Cannot set retired because: " + response.text)
            self.focus_get()
        else:
            self._close_cb()

import tkinter as tk
import requests
from add_sword_popup import AddSwordPopup
from add_firearm_popup import AddFirearmPopup
from update_sword_popup import UpdateSwordPopup
from update_firearm_popup import UpdateFirearmPopup
from retire_popup import RetirePopup
from tkinter import messagebox


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="Weapon Inventory").grid(row=1, column=1, columnspan=5)
        tk.Label(self, text="Weapon Type: ").grid(row=2, column=1)
        self._weapon_type = tk.BooleanVar()
        radio1 = tk.Radiobutton(self, text="Firearm", value=True, variable=self._weapon_type, command=self._update_weapons_list)
        radio1.grid(row=2, column=2, columnspan=2)
        radio2 = tk.Radiobutton(self, text="Sword", value=False, variable=self._weapon_type, command=self._update_weapons_list)
        radio2.grid(row=2, column=4, columnspan=2)
        self._weapons_listbox = tk.Listbox(self, selectmode='multiple', exportselection=0, width=120, height=30)
        self._weapons_listbox.grid(row=3, column=1, columnspan=5)

        self._update_stats()

        tk.Button(self, text="Add Sword", command=self._add_sword).grid(row=5, column=1)
        tk.Button(self, text="Add Firearm", command=self._add_firearm).grid(row=5, column=2)
        tk.Button(self, text="Set Retire", command=self._weapon_retire).grid(row=5, column=3)
        tk.Button(self, text="Delete Weapon", command=self._remove_device).grid(row=5, column=4)
        tk.Button(self, text="Update", command=self._update_weapon).grid(row=5, column=5)
        tk.Button(self, text="Quit", command=self._quit_callback).grid(row=6, column=1, columnspan=5)

        self._update_weapons_list()

    def _add_sword(self):
        """ Add sword Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddSwordPopup(self._popup_win, self._close_win_cb)

    def _remove_device(self):
        """ Remove device Popup """
        selections = self._weapons_listbox.curselection()
        for i in selections:
            desc = self._weapons_listbox.get(i)
            _id = self._get_id_from_desc(desc)
            response = requests.delete("http://127.0.0.1:5000/weaponwarehouse/weapons/" + _id)
            if response.status_code != 200:
                messagebox.showerror("Error", "Could not delete weapon, Id: " + _id)
                break
        self._update_weapons_list()

    def _close_win_cb(self):
        """ Close Popup """
        self._popup_win.destroy()
        self._update_weapons_list()

    def _add_firearm(self):
        """ Add Tablet Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddFirearmPopup(self._popup_win, self._close_win_cb)

    def _weapon_retire(self):
        """ set retire status to selected weapon """
        self._popup_win = tk.Toplevel()
        self._popup = RetirePopup(self._popup_win, self._close_win_cb)

    def _quit_callback(self):
        """ Quit """
        self.quit()

    def _update_weapons_list(self):
        """ Update the List of Weapons """
        response_swords = requests.get("http://127.0.0.1:5000/weaponwarehouse/weapons/reports/Sword")
        response_firearms = requests.get("http://127.0.0.1:5000/weaponwarehouse/weapons/reports/Firearm")

        if response_swords.status_code != 200:
            messagebox.showwarning("Warning", "Could not retrieve the swords.")
            return

        if response_firearms.status_code != 200:
            messagebox.showwarning("Warning", "Could not retrieve the firearms.")
            return

        weapon_descs = []
        self._weapons_listbox.delete(0, tk.END)
        sword_descs = response_swords.json()
        firearm_descs = response_firearms.json()
        if self._weapon_type.get():
            weapon_descs.extend(firearm_descs)
        else:
            weapon_descs.extend(sword_descs)
        if weapon_descs is not None and len(weapon_descs) > 0:
            for weapon_desc in weapon_descs:
                self._weapons_listbox.insert(tk.END, weapon_desc)
        self._update_stats()

    def _update_stats(self):
        response_stats = requests.get("http://127.0.0.1:5000/weaponwarehouse/weapons/stats")
        if response_stats.status_code != 200:
            messagebox.showwarning("Warning", "Could not retrieve stats.")
            return
        stats = response_stats.json()
        self._total_inuse_weapon = stats['total_weapon_inuse']
        self._total_firearm_num = stats['total_firearm_num']
        self._total_sword_num = stats['total_sword_num']
        self._total_retired_weapons = stats['total_retired_weapons']
        tk.Label(self, text="In Use: " + str(self._total_inuse_weapon)).grid(row=4, column=1)
        tk.Label(self, text="Firearm: " + str(self._total_firearm_num)).grid(row=4, column=2)
        tk.Label(self, text="Sword: " + str(self._total_sword_num)).grid(row=4, column=3)
        tk.Label(self, text="Retired: " + str(self._total_retired_weapons)).grid(row=4, column=4)

    def _update_weapon(self):
        """ Update weapon Popup """
        selection = self._weapons_listbox.curselection()
        if len(selection) > 1:
            messagebox.showwarning("Warning", "You should update weapon ONE at a time")
        desc = self._weapons_listbox.get(selection)
        _id = self._get_id_from_desc(desc)
        self._popup_win = tk.Toplevel()
        if self._weapon_type.get():
            self._popup = UpdateFirearmPopup(self._popup_win, _id, self._close_win_cb)
        else:
            self._popup = UpdateSwordPopup(self._popup_win, _id, self._close_win_cb)


    def _get_id_from_desc(self, desc):
        index_of_rightblace = desc.find("]")
        return desc[1:index_of_rightblace]

if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()

import tkinter
from tkinter import ttk, messagebox
from tkinter.ttk import Progressbar

from keygen.crypto_coin_factory import CoinFactory


class KeygenWidget:

    def __init__(self, root):
        self.currencies = CoinFactory.get_available_currencies()

        combo_frame = tkinter.Frame(root, pady=15)
        tkinter.Label(combo_frame, text="Select currency").pack()
        # Adding combobox drop down list
        self.crypto_chosen = ttk.Combobox(combo_frame, width=27, values=self.currencies)
        # self.crypto_chosen.bind("<<ComboboxSelected>>", self.on_currency_checkbox_selected)
        self.crypto_chosen.current(0)
        self.crypto_chosen.pack()
        combo_frame.pack()

        count_frame = tkinter.Frame(root, pady=15)
        tkinter.Label(count_frame, text="Select count").pack()
        default_count = tkinter.StringVar()
        default_count.set(10)
        self.count_spin = tkinter.Spinbox(count_frame, from_=1, to=1000, textvariable=default_count)
        self.count_spin.pack()
        count_frame.pack()

        self.lasers = ["A", "B", "C"]
        laser_frame = tkinter.Frame(root, pady=15)
        tkinter.Label(laser_frame, text="Select laser").pack()
        # Adding combobox drop down list
        self.laser_chosen = ttk.Combobox(laser_frame, width=27, values=self.lasers)
        # self.crypto_chosen.bind("<<ComboboxSelected>>", self.on_currency_checkbox_selected)
        self.laser_chosen.current(0)
        self.laser_chosen.pack()
        laser_frame.pack()

        btn_frame = tkinter.Frame(root, pady=15)
        generate_btn = tkinter.Button(btn_frame, text="Generate", width=20, height=3)
        generate_btn.config(command=self.on_generate_clicked)
        generate_btn.pack()
        btn_frame.pack()

        # Progress bar widget
        progress_frame = tkinter.Frame(root)
        progress = Progressbar(progress_frame, orient=tkinter.HORIZONTAL, length=100, mode='indeterminate')
        progress['value'] = 100
        progress.pack()
        progress_frame.pack()

    def on_generate_clicked(self):
        crypto_chosen = self.crypto_chosen.get()
        chosen_laser = self.laser_chosen.get()
        count = self.count_spin.get()
        print("Generate...")
        print("Crypto chosen: " + crypto_chosen)
        print("Laser chosen: " + chosen_laser)
        print("Count: " + count)
#         https://pythonspot.com/tk-message-box/
        messagebox.showinfo("Generate success", "Crypto successfully generated!")

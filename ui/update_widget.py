import tkinter
from tkinter import messagebox
from tkinter.ttk import Progressbar

from controller.update_controller import UpdateController


class UpdateWidget:
    def __init__(self, root):
        last_coin_frame = tkinter.Frame(root, pady=15)
        tkinter.Label(last_coin_frame, text="Enter the last good coin id").pack()
        self.last_coin_entry = tkinter.Entry(last_coin_frame)
        self.last_coin_entry.pack()
        last_coin_frame.pack()

        btn_frame = tkinter.Frame(root, pady=15)
        update_btn = tkinter.Button(btn_frame, text="Update", width=20, height=2)
        update_btn.config(command=self.on_update_clicked)
        update_btn.pack()
        btn_frame.pack()

        # Progress bar widget
        progress_frame = tkinter.Frame(root)
        self.progress = Progressbar(progress_frame, orient=tkinter.HORIZONTAL, length=100, mode='indeterminate')
        self.progress.pack()
        progress_frame.pack()

        self.update_controller = UpdateController(self, root)

    def on_update_clicked(self):
        last_good_coin = self.last_coin_entry.get()
        print("Update clicked: " + last_good_coin)
        self.progress['value'] = 100
        self.update_controller.update(last_good_coin)

    def show_success(self):
        self.progress['value'] = 0
        messagebox.showinfo("Generate success", "Crypto successfully generated!")
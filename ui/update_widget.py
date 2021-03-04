import tkinter
from tkinter import messagebox
from tkinter.ttk import Progressbar


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
        progress = Progressbar(progress_frame, orient=tkinter.HORIZONTAL, length=100, mode='indeterminate')
        progress['value'] = 100
        progress.pack()
        progress_frame.pack()

    def on_update_clicked(self):
        print("Update clicked: " + self.last_coin_entry.get())
        messagebox.showinfo("Update success", "Crypto successfully updated!")
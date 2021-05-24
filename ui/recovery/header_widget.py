from tkinter import ttk

import tkinter


class HeaderWidget:
    def __init__(self, frame, currencies=None, on_currency_selected=None, on_refreshed=None, on_saved=None):
        self.frame = frame
        self.currencies = currencies
        self.on_currency_selected = on_currency_selected
        self.on_refreshed = on_refreshed
        self.on_saved = on_saved

        self.crypto_chosen = None
        self.count_label = None

        self.init_ui()

    def init_ui(self):

        combo_frame = tkinter.Frame(self.frame)
        tkinter.Label(combo_frame, text="Currency").pack()
        # Adding combobox drop down list
        self.crypto_chosen = ttk.Combobox(combo_frame, width=27, values=self.currencies)
        self.crypto_chosen.bind("<<ComboboxSelected>>", self.on_currency_checkbox_selected)
        self.crypto_chosen.current(0)
        self.crypto_chosen.pack()

        self.count_label = tkinter.Label(combo_frame, text="0 Scanned coins")
        self.count_label.pack()

        combo_frame.pack(side=tkinter.LEFT)

        refresh_btn = tkinter.Button(self.frame, text="Refresh", font=('Arial', 12, 'bold'), width=15, height=5)
        refresh_btn.config(command=self.on_refresh_btn_clicked)
        refresh_btn.pack(side=tkinter.LEFT, padx=(0, 10), pady=(16, 0))

        save_btn = tkinter.Button(self.frame, text="Save", font=('Arial', 12, 'bold'), width=15, height=5)
        save_btn.config(command=self.on_save_btn_clicked)
        save_btn.pack(side=tkinter.LEFT, padx=(0, 10), pady=(16, 0))

    def set_scanned_count(self, count):
        self.count_label.config(text="{} Scanned coins".format(count))

    def on_currency_checkbox_selected(self, event):
        selected_currency = self.crypto_chosen.get()
        if self.on_currency_selected is not None:
            self.on_currency_selected(selected_currency)

    def on_refresh_btn_clicked(self):
        if self.on_refreshed is not None:
            self.on_refreshed()

    def on_save_btn_clicked(self):
        if self.on_saved is not None:
            self.on_saved()

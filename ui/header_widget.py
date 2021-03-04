from tkinter import ttk

import tkinter


class HeaderWidget:
    def __init__(self, frame, currencies=None, on_currency_selected=None, on_refreshed=None):
        self.frame = frame
        self.currencies = currencies
        self.on_currency_selected = on_currency_selected
        self.on_refreshed = on_refreshed
        self.init_ui()

    def init_ui(self):
        refresh_btn = tkinter.Button(self.frame, text="Refresh",font=('Arial', 8, 'bold'), width=10, height=2)
        refresh_btn.config(command=self.on_refresh_btn_clicked)
        refresh_btn.pack(side=tkinter.LEFT, padx=(0, 10), pady=(16, 0))

        combo_frame = tkinter.Frame(self.frame)
        tkinter.Label(combo_frame, text="Currency").pack()
        # Adding combobox drop down list
        self.crypto_chosen = ttk.Combobox(combo_frame, width=27, values=self.currencies)
        self.crypto_chosen.bind("<<ComboboxSelected>>", self.on_currency_checkbox_selected)
        self.crypto_chosen.current(0)
        self.crypto_chosen.pack()
        combo_frame.pack(side=tkinter.LEFT)

    def on_currency_checkbox_selected(self, event):
        selected_currency = self.crypto_chosen.get()
        if self.on_currency_selected is not None:
            self.on_currency_selected(selected_currency)

    def on_refresh_btn_clicked(self):
        if self.on_refreshed is not None:
            self.on_refreshed()

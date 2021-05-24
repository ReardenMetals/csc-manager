import tkinter
from PIL import Image, ImageTk

from app_tools.coin_img_util import CoinImageUtil


class CoinWidget:

    def __init__(self, frame, frame_width, frame_height):
        self.frame = frame
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.private_key = 'none'
        self.snip = 'none'
        self.address = 'none'
        self.currency = 'BTC'

        self.currency_photo_label = None
        self.action_title_label = None
        self.child_frame = None

        self.frame.pack_propagate(0)

        self.top_frame = tkinter.Frame(self.frame, width=frame_width, height=50, borderwidth=2)
        self.fill_top()
        self.top_frame.pack(pady=(0, 2))

        self.bottom_frame = tkinter.Frame(self.frame, width=frame_width, bg="WHITE", borderwidth=2)
        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.pack(fill=tkinter.BOTH, expand=True)

    def fill_top(self):
        self.top_frame.pack_propagate(0)

        image_path = CoinImageUtil.get_coin_image_by_currency(self.currency)
        image = Image.open(image_path)
        image = image.resize((40, 40), Image.ANTIALIAS)
        photo_image = ImageTk.PhotoImage(image)

        self.currency_photo_label = tkinter.Label(self.top_frame, image=photo_image)
        self.currency_photo_label.photo = photo_image
        self.currency_photo_label.pack(side=tkinter.LEFT)

        title_frame = tkinter.Frame(self.top_frame, borderwidth=2)
        self.action_title_label = tkinter.Label(title_frame, text="", font=('Helvetica', 18, 'bold'))
        self.action_title_label.pack(fill=tkinter.BOTH)
        title_frame.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True, padx=(0, 40))

    def clean_frame(self):
        if self.child_frame is not None:
            self.child_frame.destroy()
            self.child_frame = None

    def show_none(self):
        self.clean_frame()

    def show_correct(self):
        self.clean_frame()
        correct_frame = tkinter.Frame(self.bottom_frame)
        correct_frame.grid(row=0, column=0, sticky="")
        correct_image = ImageTk.PhotoImage(Image.open(CoinImageUtil.get_path('resources', 'img', 'correct.png')))
        correct_label = tkinter.Label(correct_frame, image=correct_image, bg="WHITE")
        correct_label.photo = correct_image
        correct_label.pack()
        correct_frame.place()
        self.child_frame = correct_frame

    def show_incorrect(self):
        self.clean_frame()
        incorrect_frame = tkinter.Frame(self.bottom_frame)
        incorrect_frame.grid(row=0, column=0, sticky="")
        incorrect_image = ImageTk.PhotoImage(Image.open(CoinImageUtil.get_path('resources', 'img', 'incorrect.png')))
        incorrect_label = tkinter.Label(incorrect_frame, image=incorrect_image, bg="WHITE")
        incorrect_label.photo = incorrect_image
        incorrect_label.pack()
        incorrect_frame.place()
        self.child_frame = incorrect_frame

    def show_coin_details(self):
        self.clean_frame()
        parent_frame = tkinter.Frame(self.bottom_frame)
        parent_frame.grid(row=0, column=0, sticky="nsew")
        tkinter.Label(parent_frame, text="PRIVATE KEY(WIF)", font=('Times', 14, 'bold'), fg="white", bg='darkgreen',
                      bd=7).pack()
        tkinter.Label(parent_frame, text=self.private_key, font=('Times', 14), fg="black", bd=7, wraplength=500).pack()
        tkinter.Label(parent_frame, text="SNIP", font=('Times', 14), fg="white", bg='darkgreen', bd=7).pack()
        tkinter.Label(parent_frame, text=self.snip, font=('Times', 14), fg="black", bd=7).pack()
        tkinter.Label(parent_frame, text="ADDRESS", font=('Times', 14), fg="white", bg='darkgreen', bd=7).pack()
        tkinter.Label(parent_frame, text=self.address, font=('Times', 14), fg="black", borderwidth=1, bd=7,
                      wraplength=500).pack()
        parent_frame.place()
        self.child_frame = parent_frame

    def show_coin_details_info(self, private_key, snip, address):
        self.private_key = private_key
        self.snip = snip
        self.address = address
        self.show_coin_details()

    def set_currency(self, currency):
        self.currency = currency

        image_path = CoinImageUtil.get_coin_image_by_currency(self.currency)
        image = Image.open(image_path)
        image = image.resize((40, 40), Image.ANTIALIAS)
        photo_image = ImageTk.PhotoImage(image)

        self.currency_photo_label.configure(image=photo_image)
        self.currency_photo_label.photo = photo_image

    def set_action_title(self, title):
        self.action_title_label.configure(text=title)

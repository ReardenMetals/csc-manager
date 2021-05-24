import tkinter
from tkinter import ttk

from ui.coin_checker_widget import CoinCheckerWidget
from ui.dispatcher_tab import DispatcherTab
from ui.keygen_widget import KeygenWidget
from ui.log_widget import LogWidget
from ui.manager_notebook import ManagerNotebook
from ui.recovery_widget import RecoveryWidget
from ui.update_widget import UpdateWidget


class MainWidget:

    def __init__(self, frame):
        self.frame = frame

        self.tabControl = ManagerNotebook(frame)

        self.coin_checker_frame = DispatcherTab(self.tabControl)
        self.coin_checker_widget = CoinCheckerWidget(self.coin_checker_frame)
        self.coin_checker_frame.pack()

        self.keygen_frame = DispatcherTab(self.tabControl)
        self.keygen_widget = KeygenWidget(self.keygen_frame)
        self.keygen_frame.pack()

        self.update_frame = DispatcherTab(self.tabControl)
        self.update_widget = UpdateWidget(self.update_frame)
        self.update_frame.pack()

        self.recovery_frame = DispatcherTab(self.tabControl)
        self.recovery_widget = RecoveryWidget(self.recovery_frame)
        self.recovery_frame.pack()

        self.tabControl.add(self.coin_checker_frame, text='Coin Checker')
        self.tabControl.add(self.keygen_frame, text='KeyGen')
        self.tabControl.add(self.update_frame, text='Update')
        self.tabControl.add(self.recovery_frame, text='Recovery')

        self.tabControl.pack()

        # Log frame
        bottom_frame_width = 650
        log_frame = tkinter.Frame(self.frame, height=300, width=bottom_frame_width, borderwidth=3, bg='GRAY')

        self.log_widget = LogWidget(log_frame, frame_width=bottom_frame_width)
        log_frame.pack(fill=tkinter.BOTH, expand=True)

    def add_log(self, text):
        self.log_widget.add_log(text)

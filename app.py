
from app_tools.logger import StdoutRedirector
from scan_states.context import Context
from ui.main_widget import MainWidget
import sys


class App(Context):

    def __init__(self, window_title, window):
        super().__init__()
        self.window = window
        self.window.title(window_title)
        self.main_widget = MainWidget(self.window)
        sys.stdout = StdoutRedirector(self)

    def log(self, log):
        self.window.after(10, lambda: self.main_widget.add_log(log))

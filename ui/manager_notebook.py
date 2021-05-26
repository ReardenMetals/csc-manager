from tkinter import ttk


class ManagerNotebook(ttk.Notebook):

    def __init__(self, master):
        ttk.Notebook.__init__(self, master)
        self.bind("<<NotebookTabChanged>>", self.on_tab_change)
        self.visit_str = 'viewed'
        self.leave_str = 'left'
        self.prev_id = [None]  # mutable list

    def on_tab_change(self, event):
        current_id = [event.widget.index("current")]
        if self.prev_id[0] is not None:
            event.widget.winfo_children()[self.prev_id[0]].on_visible_out(self, self.prev_id[0], self.leave_str)
        event.widget.winfo_children()[current_id[0]].on_visible_in(self, current_id[0], self.visit_str)
        self.prev_id[0] = current_id[0]
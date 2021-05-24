import tkinter


class DispatcherTab(tkinter.Frame):

    def __init__(self, parent, in_callback=None, out_callback=None):
        self.parent = parent
        self.in_callback = in_callback
        self.out_callback = out_callback
        tkinter.Frame.__init__(self, parent)

    def on_visible_in(self, parent, id, str):
        if self.in_callback is not None:
            self.in_callback()
        # print('%s is %s' % (parent.tab(id, 'text'), str))

    def on_visible_out(self, parent, id, str):
        if self.out_callback is not None:
            self.out_callback()
        # print('%s is %s' % (parent.tab(id, 'text'), str))

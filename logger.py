class Logger:

    def __init__(self, appender=None):
        self.appender = appender

    def set_appender(self, appender):
        self.appender = appender

    def log(self, *args):
        print(*args)
        if self.appender is not None:
            self.appender.log(args)


logger = Logger()

import asynctkinter as at

from logic.update import update


class UpdateController:
    def __init__(self, root, window):
        self.root = root
        self.window = window

    def update(self, last_good_coin):
        self.start_async(self.update_async(last_good_coin))

    async def update_async(self, last_good_coin):
        await self.run_in_thread(lambda: update(last_good_coin))
        print("self.root.show_success()")
        self.root.show_success()

    def start_async(self, task):
        at.start(task)

    def run_in_thread(self, func):
        return at.run_in_thread(func, after=self.window.after)



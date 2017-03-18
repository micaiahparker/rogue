from .state import State


class Menu(State):
    def __init__(self, parent, x, y, width, height):
        super().__init__(parent, x, y, width, height)
        self.cursor = 0
        self.options = []

    def draw(self):
        for i, option in enumerate(self.options):
            self.window.draw_str(0, i, str(option))

    def key_UP(self, event):
        if self.options:
            self.cursor = (self.cursor - 1) % len(self.options)

    def key_DOWN(self, event):
        if self.options:
            self.cursor = (self.cursor + 1) % len(self.options)

    def key_ENTER(self, event):
        if self.options:
            self.options[self.cursor](self, event)

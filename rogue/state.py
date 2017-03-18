from tdl.event import App
from tdl import Window, init


class BaseState(App):
    def __init__(self, width, height, title):
        self.window = init(width, height, title)

    def update(self, dt):
        self.clear()
        if self.parent:
            self.parent.draw()
        self.draw()
        tdl.flush()

    def clear(self):
        self.window.clear()

    def draw(self):
        pass

    def key_ESCAPE(self, event):
        self.suspend()

class State(BaseState):
    def __init__(self, parent, x, y, width, height):
        self.parent = parent
        self.window = Window(self.parent.window, x, y, width, height)

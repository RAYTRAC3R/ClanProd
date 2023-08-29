from clan import *

class Screens(object):
    game_screen = screen
    game_x = W
    game_y = H
    all_screens = {}
    last_screen = ''

    def __init__(self, name=None):
        self.name = name
        if name is not None:
            self.all_screens[name] = self
            game.all_screens[name] = self

    def on_use(self):
        pass

    def screen_switches(self):
        pass
    
class MapScreen(Screens):
    def on_use(self):
        screen.blit()
import ppb
import random

class Placeholder(ppb.Sprite):
    def on_update(self, update_event, signal):
        self.position = ppb.Vector(random.random(), random.random())
    def on_button_pressed(self, update_event, signal):
        pass
    def on_key_pressed(self, update_event, signal):
        pass

def setup(scene):
    p1 = Placeholder()
    scene.add(p1)

ppb.run(setup=setup)

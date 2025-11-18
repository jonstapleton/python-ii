import ppb
import math

class Player(ppb.Sprite):
    def on_update(self, update_event, signal):
        self.position += ppb.Vector(0.1, 0)

def setup(scene):
    obj1 = Player()
    obj1.position = ppb.Vector(0,1)
    obj = Player()
    scene.add(obj)
    scene.add(obj1)

ppb.run(setup=setup)

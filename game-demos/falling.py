import ppb

gravity = ppb.Vector(0,- 1)

class Sprite(ppb.Sprite):
    position = ppb.Vector(0,0)
    velocity = ppb.Vector(0,-0.25)
    def on_update(self, event, signal):
        self.position = self.position + self.velocity * event.time_delta
        self.velocity = self.velocity + gravity*event.time_delta

def setup(scene):
    scene.add(Sprite())

ppb.run(setup=setup)

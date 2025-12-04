import ppb

red = ppb.Image((255,0,0))
green = ppb.Image((0, 255, 0))
class Sprite(ppb.Sprite):
    position = ppb.Vector(0,0)
    velocity = ppb.Vector(0,-1.25)
    def on_update(self, event, signal):
        self.position = self.position + self.velocity * event.time_delta
        self.image = green
        for s in event.scene.get(kind=Sprite):
            self_below_s = self.top <= s.bottom
            self_above_s = self.bottom >= s.top
            if not self == s and not (self_below_s or self_above_s):
                self.image = red
                s.image = red

def setup(scene):
    scene.add(Sprite())
    scene.add(Sprite(position=ppb.Vector(0,-3), velocity = ppb.Vector(0,0)))

ppb.run(setup=setup)

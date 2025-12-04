import ppb

class Box(ppb.Sprite):
    id = None
    position = ppb.Vector(0,0)
    def on_button_pressed(self, event, signal):
        mouse = event.position
        if mouse.x > self.position.x-self.width/2 and mouse.x < self.position.x + self.width/2:
            print(f"Got button press at id {self.id}")

def setup(scene):
    for i in range(3):
        box = Box(position=ppb.Vector(i*2-3/2,0), id=i)
        scene.add(box)
        scene.toggle = True

ppb.run(setup=setup)

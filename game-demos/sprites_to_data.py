import ppb

boxes = [False, False, False]

class Box(ppb.Sprite):
    id = None
    position = ppb.Vector(0,0)
    red = ppb.Image((255,0,0))
    green = ppb.Image((0, 255, 0))
    on = False
    def on_button_pressed(self, event, signal):
        mouse = event.position
        if mouse.x > self.position.x-self.width/2 and mouse.x < self.position.x + self.width/2:
            print(f"Got button press at id {self.id}")
            boxes[self.id] = not boxes[self.id]
            if boxes[self.id]:
                self.image = self.red
                self.on = True
            else:
                self.image = self.green
                self.on = False

def setup(scene):
    for i in range(3):
        box = Box(position=ppb.Vector(i*2-3/2,0), id=i)
        scene.add(box)
    scene.on_update = scene_update

ppb.run(setup=setup)

import ppb

class X(ppb.Sprite):
    layer = 0
    image = ppb.Rectangle(255,0,0)

class Board(ppb.Sprite):
    layer = 1
    width = 8
    height = 8
    def on_button_pressed(self, event, signal):
        x = X()
        self.add(x)
        
def setup(scene):
    b = Board()
    x = X()
    scene.add(b)
    scene.add(x)
ppb.run(setup=setup)

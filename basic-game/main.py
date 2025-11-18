import ppb

class Player(ppb.Sprite):
    image = ppb.Image("spaceship.png")
    sound = ppb.Sound("swosh-01.flac")
    size = 2
    def on_button_pressed(self, event, signal):
        signal(ppb.events.PlaySound(self.sound))

class Button(ppb.RectangleSprite):
    image = ppb.Rectangle(255,0,0, (4,1))
    width = 4
    height = 1
    layer = 0

class Label(ppb.Sprite):
    image = ppb.Text('default', font=ppb.Font('Poppins-Light.ttf', size=12))
    layer = 1
    def __init__(self, message):
        self.image = ppb.Text(message, font=ppb.Font('Poppins-Light.ttf', size=12))
    
def setup(scene):
    scene.background_color = (255,255,255)
    # obj = Button()
    # label= Label("good!")
    # label2 = Label("hello!")
    # label2.position = ppb.Vector(0, 1)
    pl = Player()
    scene.add(pl)
    # scene.add(label)
    # scene.add(label2)
    # scene.add(obj)
    
ppb.run(setup=setup)

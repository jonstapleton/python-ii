import ppb

class Button(ppb.RectangleSprite):
    def on_button_pressed(self, event, signal):
        if event.position 
        print("Got call to move to next scene!")

def setup(scene):
    scene.add(button)

ppb.run(setup=setup)

import ppb
import random

class Row(ppb.RectangleSprite):
    image = ppb.Rectangle(255,0,0, (4,1))
    width = 4
    height = 1
    
    # respond to keyboard events
    def on_key_pressed(self, update_event, signal):
        print(update_event)
    def on_button_pressed(self, update_event, signal):
        pass
    def on_mouse_motion(self, update_event, signal):
        pass

def setup(scene):
    r = Row()
    r.width = 3
    r.height = 2
    scene.add(r)

ppb.run(setup=setup)

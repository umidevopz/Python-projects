from ursina import * 
from ursina.shaders import lit_with_shadows_shader
app = Ursina()


# game window costumize

window.title = 'My Game'                # The window title
window.borderless = False                # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = True     # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True 

# textures

damn_text = load_texture('/home/umidevop/Downloads/img2.png')
dmn_text = load_texture('/home/umidevop/Downloads/download.jpeg')
damn = Entity(
    model = 'cube',
    color = color.red,
    scale = (2),
    collider = 'box',
    position = (0),
    texture = damn_text
)


dmn = Entity(
    model = 'cube',
    color = color.blue,
    scale = (2,2),
    collider = 'box',
    position = (1),
    texture = 'brick',
    y=1,
    x=3, 
    shader=lit_with_shadows_shader
)
def update():
    damn.x += held_keys['right arrow'] * time.dt * 7
    damn.x -= held_keys['left arrow'] * time.dt * 7
    damn.y += held_keys['up arrow'] * time.dt * 7
    damn.y -= held_keys['down arrow'] * time.dt * 7
    dmn.x += held_keys['right arrow'] * time.dt * 10
    dmn.x -= held_keys['left arrow'] * time.dt * 10
    dmn.y += held_keys['up arrow'] * time.dt * 10
    dmn.y -= held_keys['down arrow'] * time.dt * 10

app.run()
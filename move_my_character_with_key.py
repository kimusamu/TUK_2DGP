from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
grass = load_image('TUK_GROUND.png')
character = load_image('drill4_sprite.png')


def handle_events():
    global running

    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here


running = True
x = 800 // 2
frame = 0

# fill here


close_canvas()


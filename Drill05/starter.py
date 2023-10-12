import random

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def rand_hand_xy():
    global hand_x, hand_y
    hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

def move_char():
    global frame
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if(hand_x > before_x):
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
    hand.draw(hand_x, hand_y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)

def make_xy():
    global x, y, hand_x, hand_y
    for i in range(0, 100 + 1, 10):
        t = i / 100
        x = (1 - t) * x + t * hand_x
        y = (1 - t) * y + t * hand_y
        move_char()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hand_x = 0
hand_y = 0
before_x = TUK_WIDTH // 2
hide_cursor()

rand_hand_xy()
make_xy()

while running:
    if x == hand_x and y == hand_y:
        before_x = hand_x
        rand_hand_xy()
        make_xy()
    handle_events()

close_canvas()





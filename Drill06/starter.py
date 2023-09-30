from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
follow_hand = load_image('hand_arrow.png')

def save_hand_xy():
    global hand_x, hand_y, list_x, list_y
    list_x.append(hand_x)
    list_y.append(hand_y)

def handle_events():
    global running
    global x, y, hand_x, hand_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            hand_x, hand_y = event.x, TUK_HEIGHT - 1 - event.y
            save_hand_xy()

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hand_x = 0
hand_y = 0
hide_cursor()

list_x = []
list_y = []

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(x, y)

    for i in range (len(list_x)):
        follow_hand.draw(list_x[i], list_y[i])

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()
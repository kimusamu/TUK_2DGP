from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y, mx, my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            list_x.append(event.x)
            list_y.append(TUK_HEIGHT - 1 - event.y)

def draw_first():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

def draw_last():
    update_canvas()
    delay(0.01)

def draw_char_hand():
    global frame, list_x
    character.clip_draw(frame * 100, 0, 100, 100, x, y, 100, 100)
    frame = (frame + 1) % 8
    hand.draw(mx, my)
    if len(list_x) > 0:
        for i in range(len(list_x)):
            hand.draw(list_x[i], list_y[i])

def character_move():
    global list_x, list_y, go_x, go_y, x, y

    if len(list_x) > 0:
        for i in range(1, 100 + 1, 1):
            draw_first()
            handle_events()
            t = i / 100
            x = (1 - t) * go_x + t * list_x[0]
            y = (1 - t) * go_y + t * list_y[0]
            draw_char_hand()
            draw_last()

        if (x == list_x[0] and y == list_y[0]):
            del list_x[0], list_y[0]
            go_x, go_y = x, y

    else:
        draw_first()
        draw_char_hand()
        draw_last()

running = True

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
mx, my = TUK_WIDTH // 2, TUK_HEIGHT // 2
go_x, go_y = TUK_WIDTH // 2, TUK_HEIGHT // 2

frame = 0

hide_cursor()

list_x = []
list_y = []

while running:
    handle_events()
    character_move()

close_canvas()

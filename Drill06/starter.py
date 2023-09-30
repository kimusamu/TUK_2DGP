from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y, hand_x, hand_y, mx, my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            list_x.append(event.x)
            list_y.append(TUK_HEIGHT - 1 - event.y)

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
mx, my = TUK_WIDTH // 2, TUK_HEIGHT // 2
go_x, go_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hand_x = 0
hand_y = 0

hide_cursor()

list_x = []
list_y = []

while running:
    handle_events()

    if len(list_x) > 0:
        for i in range(1, 100 + 1, 1):
            clear_canvas()
            TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
            handle_events()
            t = i / 100
            x = (1 - t) * go_x + t * list_x[0]
            y = (1 - t) * go_y + t * list_y[0]
            character.clip_draw(frame * 100, 0, 100, 100, x, y, 100, 100)
            frame = (frame + 1) % 8
            hand.draw(mx, my)
            for i in range(len(list_x)):
                hand.draw(list_x[i], list_y[i])
            update_canvas()
            delay(0.01)

        if (x == list_x[0] and y == list_y[0]):
            del list_x[0], list_y[0]
            go_x, go_y = x, y

    else:
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.draw(mx, my)
        character.clip_draw(frame * 100, 0, 100, 100, x, y, 100, 100)
        frame = (frame + 1) % 8
        update_canvas()
        delay(0.01)

close_canvas()

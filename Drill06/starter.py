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

def character_move():
    global list_x, list_y, char_x, char_y
    if len(list_x) > 0:
        for i in range(0, 100 + 1, 1):
            t = i / 100
            char_x = (1 - t) * char_x + t * list_x[0]
            char_y = (1 - t) * char_y + t * list_y[0]
            draw_char()

        if(char_x == list_x[0] and char_y == list_y[0]):
            del list_x[0], list_y[0]

def draw_char():
    global frame
    character.clip_draw(frame * 100, 0, 100, 100, char_x, char_y, 100, 100)
    frame = (frame + 1) % 8

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hand_x = 0
hand_y = 0
char_x = TUK_WIDTH // 2
char_y = TUK_HEIGHT // 2
hide_cursor()

list_x = []
list_y = []

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(x, y)

    for i in range (len(list_x)):
        follow_hand.draw(list_x[i], list_y[i])

    character_move()
    draw_char()

    update_canvas()
    handle_events()

close_canvas()

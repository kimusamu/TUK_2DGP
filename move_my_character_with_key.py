from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('drill4_sprite.png')

def handle_events():
    global running, dir_x, dir_y, idle_or_run, frame_y, right_left

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            idle_or_run = True
            if event.key == SDLK_RIGHT:
                right_left = True
                frame_y = 200
                dir_x += 1

            elif event.key == SDLK_LEFT:
                right_left = False
                frame_y = 200
                dir_x -= 1

            elif event.key == SDLK_UP:
                frame_y = 0
                dir_y += 1

            elif event.key == SDLK_DOWN:
                frame_y = 300
                dir_y -= 1

            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            idle_or_run = False
            if event.key == SDLK_RIGHT:
                dir_x -= 1

            elif event.key == SDLK_LEFT:
                dir_x += 1

            elif event.key == SDLK_UP:
                dir_y -= 1

            elif event.key == SDLK_DOWN:
                dir_y += 1

def idle_or_run_character():
    if (idle_or_run == False):
        if (right_left == True):
            character.clip_draw(idle_frame * idle_frame_size + idle_frame_size_x, frame_y, idle_size_x, idle_size_y, x, y)

        elif (right_left == False):
            character.clip_composite_draw(idle_frame * idle_frame_size + idle_frame_size_x, frame_y, idle_size_x, idle_size_y, 0, 'h', x, y, idle_size_x, idle_size_y)

    elif (idle_or_run == True):
        if (right_left == True):
            character.clip_draw(run_frame * run_frame_size - run_frame_size_x, frame_y, run_size_x, run_size_y, x, y)

        elif (right_left == False):
            character.clip_composite_draw(run_frame * run_frame_size - run_frame_size_x, frame_y, run_size_x, run_size_y, 0, 'h', x, y, run_size_x, run_size_y)

running = True
idle_or_run = False
right_left = True

x = 800 // 2
y = 90
dir_x = 0
dir_y = 0

idle_frame = 0
run_frame = 3
frame_y = 300

idle_frame_size = 73
idle_frame_size_x = 34
idle_size_x = 80
idle_size_y = 90

run_frame_size = 100
run_frame_size_x = 8
run_size_x = 96
run_size_y = 100

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    idle_or_run_character()

    if (idle_or_run == False):
        idle_frame = (idle_frame + 1) % 3

    elif (idle_or_run == True):
        run_frame = (run_frame + 1) % 8
        if (run_frame > 6):
            run_frame = 3

    update_canvas()
    handle_events()

    x += dir_x * 30
    if(x > 1250):
        x = 1250
    elif(x < 0):
        x = 0

    y += dir_y * 30
    if(y > 1000):
        y = 1000
    elif(y < 0):
        y = 0

    delay(0.1)

close_canvas()


from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('drill4_sprite.png')

def handle_events():
    global running, dir_x, dir_y, idle_or_run

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            idle_or_run = True
            if event.key == SDLK_RIGHT:
                dir_x += 1

            elif event.key == SDLK_LEFT:
                dir_x -= 1

            elif event.key == SDLK_UP:
                dir_y += 1

            elif event.key == SDLK_DOWN:
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


running = True
idle_or_run = False

x = 800 // 2
y = 90
dir_x = 0
dir_y = 0

idle_frame = 0
run_frame = 3

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

    if(idle_or_run == False):
        character.clip_draw(idle_frame * idle_frame_size + idle_frame_size_x, 0, idle_size_x, idle_size_y, x, y)
        idle_frame = (idle_frame + 1) % 3

    elif(idle_or_run == True):
        character.clip_draw(run_frame * run_frame_size - run_frame_size_x, 0, run_size_x, run_size_y, x, y)
        run_frame = (run_frame + 1) % 8

        if(run_frame > 6):
            run_frame = 3

    update_canvas()
    handle_events()



    x += dir_x * 30
    y += dir_y * 30

    delay(0.1)

close_canvas()


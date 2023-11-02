from pico2d import *
import game_framework

import game_world
from bird import Bird
from grass import Grass
from boy import Boy

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global grass
    global boy
    global birds1
    global birds2
    global birds3
    global birds4
    global birds5
    global birds6
    global birds7
    global birds8
    global birds9
    global birds10

    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)


    birds1 = Bird()
    game_world.add_object(birds1, 1)

    birds2 = Bird()
    game_world.add_object(birds2, 1)

    birds3 = Bird()
    game_world.add_object(birds3, 1)

    birds4 = Bird()
    game_world.add_object(birds4, 1)

    birds5 = Bird()
    game_world.add_object(birds5, 1)

    birds6 = Bird()
    game_world.add_object(birds6, 1)

    birds7 = Bird()
    game_world.add_object(birds7, 1)

    birds8 = Bird()
    game_world.add_object(birds8, 1)

    birds9 = Bird()
    game_world.add_object(birds9, 1)

    birds10 = Bird()
    game_world.add_object(birds10, 1)



def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # delay(0.1)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass


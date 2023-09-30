from pico2d import *
import math

open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')

def square_move():
    x = 400
    y = 90
    
    while(x < 780):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)

    while(y < 560):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.01)

    while(x > 20):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.01)

    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.01)

    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)

def circle_move():
    x = 400
    y = 90

    angle = 180
    r = 200
    rx = 400
    ry = 300

    while(angle != 178):
        if(angle == 360):
            angle = 0

        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = r * math.sin(angle / 360 * 2 * math.pi) + rx
        y = r * math.cos(angle / 360 * 2 * math.pi) + ry
        angle = angle + 2
        delay(0.01)

while(True):
    square_move()
    circle_move()

close_canvas()

from pico2d import load_image
import random

import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill here
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x = random.randint(100, 700)
        self.y = 300
        self.frame = 0
        self.action = 2
        self.face_dir = 1
        self.dir = 0

    def draw(self):
        if(self.face_dir == -1):
            self.image.clip_composite_draw(int(self.frame) * 183, self.action * 100, 183, 90, 0, '', int(self.x), self.y, 50, 50)

        else:
            self.image.clip_composite_draw(int(self.frame) * 183, self.action * 100, 183, 90, 0, 'v', int(self.x), self.y, 50, 50)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        if(self.frame > 4):
            self.action -= 1

        if(self.action < 0):
            self.action = 2

        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        if self.x <= 1600:
            self.face_dir = -1

        elif self.x >= 0:
            self.face_dir = 1
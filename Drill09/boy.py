# 이것은 각 상태들을 객체로 구현한 것임.
import math

from pico2d import load_image, get_time
from sdl2 import SDLK_SPACE, SDL_KEYDOWN, SDL_KEYUP, SDLK_RIGHT, SDLK_LEFT, SDLK_a


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT

def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT

def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def auto_run(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

class Sleep:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        print('고개 숙이기')

    @staticmethod
    def exit(boy, e):
        print('고개 들기')
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        print('드르렁')

    @staticmethod
    def draw(boy):
        if boy.action == 2:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100,
                                          -math.pi / 2, '', boy.x + 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100,
                                          math.pi / 2, '', boy.x - 25, boy.y - 25, 100, 100)



class Idle:

    @staticmethod
    def enter(boy, e):
        if boy.action == 0:
            boy.action = 2
        elif boy.action == 1:
            boy.action = 3
        boy.dir = 0
        boy.frame = 0
        boy.wait_time = get_time() # pico2d import 필요
        print('고개 들기')

    @staticmethod
    def exit(boy, e):
        print('고개 숙이기')
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        if get_time() - boy.wait_time > 2:
            boy.state_machine.handle_event(('TIME_OUT', 0))
        print('공부 하기')

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)


class Run:

    @staticmethod
    def enter(boy, e):
        if right_down(e) or left_up(e): #오른쪽으로 RUN
            boy.dir, boy.action = 1, 1
            print('오른쪽 간다')
        elif left_down(e) or right_up(e): #왼쪽으로 RUN
            boy.dir, boy.action = -1, 0
            print('왼쪽 간다')

    @staticmethod
    def exit(boy ,e):
        print('가만히 있거나 잘거다')
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.x += boy.dir * 5
        print('이동한다')

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y)


class AutoRun:


    @staticmethod
    def enter(boy, e):
        if boy.action == 2:
            boy.dir, boy.action = -1, 0

        elif boy.action == 3:
            boy.dir, boy.action = 1, 1

        boy.wait_time_idle = get_time()
        print('자동으로 움직여야지')

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

        boy.x += boy.dir * 20
        print('자동으로 움직이는중')

        if boy.x >= 800:
            boy.dir, boy.action = -1, 0

        elif boy.x <= 0:
            boy.dir, boy.action = 1, 1

        if get_time() - boy.wait_time_idle > 5:
            boy.state_machine.handle_event(('TIME_OUT', 0))
            print('서야겠다')

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100, boy.x, boy.y + 30, 200, 200)


class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Idle
        self.table = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep,
                   auto_run: AutoRun},
            AutoRun: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Idle},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle},
            Sleep: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, space_down: Idle,
                    auto_run: AutoRun},
        }

    def start(self):
        self.cur_state.enter(self.boy, ('START', 0))

    def update(self):
        self.cur_state.do(self.boy)

    def handle_event(self, e): #state event handling
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True #성공적으로 이벤트 변환
        return False #이벤트를 성공하지 못함

    def draw(self):
        self.cur_state.draw(self.boy)


class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.action = 3
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event): #state event handling
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()

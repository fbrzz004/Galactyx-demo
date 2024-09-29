from abc import ABC, abstractmethod
from random import randint, uniform

from pygame.draw import circle


class Jet(ABC):
    def __init__(self, screen_instance,
                 x_positions,
                 y_init,
                 image_rect, velocity_x: list,
                 jet_active:list,
                 velocity_y=0,
                 amount=10):

        # set the screen instance
        self.__screen = screen_instance
        self._screen_rect = screen_instance.get_rect()

        # set the image rect for to get the exact position of jets
        self._image_rect = image_rect
        self._initial_radio = 4
        self._amount = amount

        # set the statics x, y initial position
        self._y_init = y_init
        self._x_jet_lambda_current = x_positions
        self._x_jet_lambda_past = self._x_jet_lambda_current(self._image_rect)

        # jet state
        self._jet_active = jet_active

        # set the list with all list (x, y, radio) that represent
        # each circle of jet's flame
        self.__init_list_unit()

        # set the velocity for each
        self._velocity_x = velocity_x
        self._velocity_y = velocity_y

        # lambda random function
        self.__color = lambda : (randint(100, 255),
                                 randint(0, 255),
                                 randint(0, 255))

    def __init_list_unit(self):
        self._list_unit_jet = []
        for x_init in self._x_jet_lambda_current(self._image_rect):
            line_flame = []
            for _ in range(int(self._amount / len(self._x_jet_lambda_current(self._image_rect)))):
                line_flame.append([x_init, self._y_init, self._initial_radio])
            self._list_unit_jet.append(line_flame)

    def _draw(self):
        for index, vx in enumerate(self._velocity_x):
            if self._jet_active[index]:
                for unit_jet in self._list_unit_jet[index]:
                    circle(self.__screen, self.__color(),
                           (uniform(unit_jet[0] - 10,unit_jet[0] + 10), unit_jet[1]),
                           uniform(unit_jet[2] - 4, unit_jet[2]))

    def _move(self):
        for index, vx in enumerate(self._velocity_x):
            if self._jet_active[index]:
                for unit_jet in self._list_unit_jet[index]:
                    unit_jet[0] += int(self._x_jet_lambda_current(self._image_rect)[index] - self._x_jet_lambda_past[index])
                    unit_jet[0] += uniform(vx - 2, vx + 2)
                    unit_jet[1] += uniform(self._velocity_y - 4, self._velocity_y + 4)
                self._x_jet_lambda_past[index] = self._x_jet_lambda_current(self._image_rect)[index]

    def _check_x_position(self, y_stop):
        for x_index, x_init in enumerate(self._x_jet_lambda_current(self._image_rect)):
            if self._jet_active[x_index]:
                for unit_jet in self._list_unit_jet[x_index]:
                    if unit_jet[1] > y_stop():
                        unit_jet[0] = x_init
                        unit_jet[1] = self._y_init
                        unit_jet[2] = self._initial_radio

    @abstractmethod
    def run(self):
        pass


class MainJet(Jet):
    def __init__(self, screen_instance, image_rect, amount=30):

        # set x position
        self._gen_three_x_pos = lambda imager : [
            imager.x + imager.width / 2,
            imager.x + imager.width / 2 - 15,
            imager.x + imager.width / 2 + 15
        ]

        self.__y_init = image_rect.y + image_rect.height

        Jet.__init__(self, screen_instance=screen_instance,
                     x_positions=self._gen_three_x_pos,
                     y_init=self.__y_init,
                     image_rect=image_rect, velocity_y=4, velocity_x=[0, 1, -1], amount=amount,
                     jet_active=[1, 1, 1])

        self.__y_stop = lambda : uniform(self._y_init + 100 - 140, self._y_init + 100 + 240)

    def run(self):
        self._move()
        self._check_x_position(self.__y_stop)
        self._draw()

class DirectionalJet(Jet):
    def __init__(self, screen_instance, image_rect, amount=10):

        self.__gen_three_x_pos = lambda imager : [imager.x + imager.width / 2 - 60,
                                                  imager.x + imager.width / 2 + 60]

        self.__y_init = image_rect.y + image_rect.height - 35

        Jet.__init__(self, screen_instance=screen_instance,
                     x_positions=self.__gen_three_x_pos,
                     y_init=self.__y_init,
                     image_rect=image_rect,
                     velocity_y=4, velocity_x=[-5, 5], amount=amount,
                     jet_active=[0, 0])

        self.__y_stop = lambda : uniform(self._y_init + 60 - 140, self._y_init + 60 + 240)

    def run(self):
        self._move()
        self._check_x_position(self.__y_stop)
        self._draw()

    def on_left(self):
        self._jet_active[0] = 1

    def on_right(self):
        self._jet_active[1] = 1

    def off_left(self):
        self._jet_active[0] = 0

    def off_right(self):
        self._jet_active[1] = 0







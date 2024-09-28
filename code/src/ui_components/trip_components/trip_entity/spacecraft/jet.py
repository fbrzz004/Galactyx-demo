from abc import ABC, abstractmethod
from random import randint, uniform

from pygame.draw import circle


class Jet(ABC):
    def __init__(self, screen_instance,
                 x_positions,
                 image_rect, velocity_x=0,
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
        self._y_init = self._image_rect.y + self._image_rect.height
        self._x_jet = list(x_positions(self._image_rect))

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
        for x_init in self._x_jet:
            for _ in range(int(self._amount / len(self._x_jet))):
                self._list_unit_jet.append([x_init, self._y_init, self._initial_radio])

    def _init_post_unit(self):
        for x_index, x_init in enumerate(self._x_jet):
            for unit_jet in self._list_unit_jet[int(x_index * len(self._x_jet) / len(self._x_jet)):
                                                 int((x_index + 1) * len(self._x_jet) / len(self._x_jet))]:
                unit_jet[0] = self._x_jet[x_index]
                unit_jet[1] = self._y_init
                unit_jet[2] = self._initial_radio

    @abstractmethod
    def _move(self):
        pass

    def _draw(self):
        for unit_jet in self._list_unit_jet:
            circle(self.__screen, self.__color(),
                   (uniform(unit_jet[0] - 10,unit_jet[0] + 10), unit_jet[1]),
                   uniform(unit_jet[2] - 4, unit_jet[2]))

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def _check_x_position(self):
        pass


class MainJet(Jet):
    def __init__(self, screen_instance, image_rect, amount=30):

        # set x position
        self._gen_three_x_pos = lambda imager : [
            imager.x + imager.width / 2,
            imager.x + imager.width / 2 - 15,
            imager.x + imager.width / 2 + 15
        ]

        Jet.__init__(self, screen_instance=screen_instance,
                     x_positions=self._gen_three_x_pos,
                     image_rect=image_rect, velocity_y=4, amount=amount)

        self.__y_stop = self._y_init + 100

    def _check_x_position(self):
        for jet_unit in self._list_unit_jet:
            if jet_unit[1] > uniform(self.__y_stop - 140, self.__y_stop + 240):
                jet_unit[0] = self._gen_three_x_pos(self._image_rect)[randint(0, 2)]
                jet_unit[1] = self._y_init
                jet_unit[2] = self._initial_radio

    def _move(self):
        for unit_jet in self._list_unit_jet:
            unit_jet[0] = self._gen_three_x_pos(self._image_rect)[randint(0, 2)]
            unit_jet[1] += uniform(self._velocity_y - 10, self._velocity_y + 10)

    def run(self):
        self._move()
        self._check_x_position()
        self._draw()





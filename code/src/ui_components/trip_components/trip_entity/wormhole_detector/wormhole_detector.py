from .card import Card
from pygame import K_j, KSCAN_J


class WormHoleDetector:
    def __init__(self, screen_instance, get_energy_spacecraft):
        self.__screen = screen_instance
        self.__get_energy_spacecraft = get_energy_spacecraft()

        self.__is_running = False

        self.__min_for_running = .7
        self.__max_for_running = .71

        self.__card = Card(
            screen_instance=screen_instance,
            letter='J',
            state='Jump',
            activator=[K_j, KSCAN_J],
            get_factor=self.get_factor,
            max_factor=self.__max_for_running
        )

    def get_factor(self):
        l, l_max = self.__get_energy_spacecraft()
        return l / l_max

    def run(self):
        if self.__is_running:
            if self.get_factor() > self.__max_for_running:
                self.__card.run()
        else:
            if self.get_factor() < self.__min_for_running:
                self.__is_running = True

    def handler(self, event):
        state = None

        if self.__is_running and self.get_factor() > self.__max_for_running:
            state = self.__card.handler(event)

        return state
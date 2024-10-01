from src.ui_components.trip_components.trip_background.wormhole_background import WormholeBackground


class JumpTrip:
    def __init__(self, screen_instance):

        self.__wormhole_background = WormholeBackground(
            screen_instance=screen_instance
        )

    def draw(self):
        self.__wormhole_background.draw()

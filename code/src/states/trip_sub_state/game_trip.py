from src.ui_components.trip_components.trip_background.star_background import StarBackground
from src.ui_components.trip_components.trip_entity.enemy import Enemy
from src.ui_components.trip_components.trip_entity.group_asteroid import GroupAsteroid
from src.ui_components.trip_components.trip_entity.dyson_sphere import DysonSphere
from src.ui_components.trip_components.trip_entity.spacecraft import Spacecraft


class GameTrip:
    def __init__(self, screen_instance):

        # background
        self.__star_background = StarBackground(
            screen_instance=screen_instance
        )

        self.__dyson_sphere = DysonSphere(
            screen_instance=screen_instance
        )

        self.__group_asteroid = GroupAsteroid(
            screen_instance=screen_instance,
            amount_asteroids=3
        )

        self.__enemy = Enemy(
            screen_instance=screen_instance
        )

        self.__player_spacecraft = Spacecraft(
            screen_instance=screen_instance
        )

    def draw(self):
        # draw background star
        self.__star_background.draw()

        # draw the dyson sphere auto moving
        self.__dyson_sphere.run()

        # draw the asteroid
        self.__group_asteroid.run()

        # draw the enemy
        self.__enemy.run()

        # draw the spacecraft
        self.__player_spacecraft.run()

    def handle_events(self, event):
        self.__player_spacecraft.handler(event)

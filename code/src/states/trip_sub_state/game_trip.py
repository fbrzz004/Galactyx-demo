from src.ui_components.trip_components.trip_background.star_background import StarBackground
from src.ui_components.trip_components.trip_entity.enemy import Enemy
from src.ui_components.trip_components.trip_entity.group_asteroid import GroupAsteroid
from src.ui_components.trip_components.trip_entity.dyson_sphere import DysonSphere
from src.ui_components.trip_components.trip_entity.spacecraft.spacecraft import Spacecraft

from ...ui_components.trip_components.trip_entity.spacecraft.bullet.manager_bullet import ManagerBullet


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

        # this obj manage the bullet spacecraft's weapon
        self.__manager_bullet = ManagerBullet()

    def __verify_collision_bullet_with_other_objet(self):
        self.__manager_bullet.is_collision(self.__group_asteroid.get_rect_callable_collision())

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

        # run the manager of bullet
        self.__manager_bullet.run()

    def handle_events(self, event):
        self.__player_spacecraft.handler(event, manager_bullet=self.__manager_bullet)
        self.__verify_collision_bullet_with_other_objet()


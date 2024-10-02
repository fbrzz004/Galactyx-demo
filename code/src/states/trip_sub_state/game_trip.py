from src.ui_components.trip_components.trip_background.star_background import StarBackground
from src.ui_components.trip_components.trip_entity.enemy import Enemy
from src.ui_components.trip_components.trip_entity.group_asteroid import GroupAsteroid
from src.ui_components.trip_components.trip_entity.dyson_sphere import DysonSphere
from src.ui_components.trip_components.trip_entity.spacecraft.spacecraft import Spacecraft

from ...ui_components.trip_components.trip_entity.spacecraft.bullet.manager_bullet import ManagerBullet
from ...ui_components.trip_components.trip_entity.spacecraft.spacecraft_collision_manager import \
    SpacecraftCollisionManager
from ...ui_components.trip_components.trip_hud.energy_hud import EnergyHud


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
            amount_asteroids=30
        )

        self.__enemy = Enemy(
            screen_instance=screen_instance
        )

        self.__player_spacecraft = Spacecraft(
            screen_instance=screen_instance,
            get_energy = self.__dyson_sphere.into_energy
        )

        # this obj manage the bullet spacecraft's weapon
        self.__manager_bullet = ManagerBullet()

        # this obj manage the spacecraft collision
        self.__manager_spacecraft_collision = SpacecraftCollisionManager(
            spacecraft_rect=self.__player_spacecraft.get_rect(),
            get_energy=self.__dyson_sphere.into_energy
        )

        # hud implementation
        self.__energy_weapon_hud = EnergyHud(screen_instance=screen_instance,
                                             get_current_level=self.__player_spacecraft.get_energy_weapon,
                                             left=10, bottom=screen_instance.get_rect().height - 10,
                                             title="Energy Weapon")

        # hud implementation
        self.__energy_life = EnergyHud(screen_instance=screen_instance,
                                       get_current_level=self.__manager_spacecraft_collision.get_live,
                                       right=screen_instance.get_rect().width - 10, bottom=screen_instance.get_rect().height - 10,
                                       title="Energy Life")

    def __verify_collision_bullet_with_other_objet(self):
        self.__manager_bullet.is_collision(self.__group_asteroid.get_rect_callable_collision())

    def __verify_collision_spacecraft_to_asteroids(self):
        self.__manager_spacecraft_collision.is_collision(self.__group_asteroid.get_rect_callable_collision())

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

        # run the spacecraft-collision
        self.__manager_spacecraft_collision.run()

        # hud section
        # hud energy weapon
        self.__energy_weapon_hud.run()
        # hud energy life
        self.__energy_life.run()

        self.__verify_collision_bullet_with_other_objet()
        self.__verify_collision_spacecraft_to_asteroids()

    def handle_events(self, event):
        self.__player_spacecraft.handler(event, manager_bullet=self.__manager_bullet)


        state = None

        if not self.__manager_spacecraft_collision.is_live():
            state = 'game_over'

        return state



from src.ui_components.trip_components.trip_background.star_background import StarBackground
from ...ui_components.trip_components.trip_entity.enemy.enemy import Enemy
from src.ui_components.trip_components.trip_entity.group_asteroid import GroupAsteroid
from src.ui_components.trip_components.trip_entity.dyson_sphere import DysonSphere
from src.ui_components.trip_components.trip_entity.spacecraft.spacecraft import Spacecraft

from ...ui_components.trip_components.trip_entity.spacecraft.bullet.manager_bullet import ManagerBullet
from ...ui_components.trip_components.trip_entity.spacecraft.spacecraft_collision_manager import \
    SpacecraftCollisionManager
from ...ui_components.trip_components.trip_entity.wormhole_detector.wormhole_detector import WormHoleDetector
from ...ui_components.trip_components.trip_hud.energy_hud import EnergyHud


class GameTrip:
    def __init__(self, screen_instance, get_level_jump):

        # background
        self.__star_background = StarBackground(
            screen_instance=screen_instance,
            get_level_jump=get_level_jump
        )

        self.__dyson_sphere = DysonSphere(
            screen_instance=screen_instance
        )

        self.__group_asteroid = GroupAsteroid(
            screen_instance=screen_instance,
            amount_asteroids=6
        )

        self.__player_spacecraft = Spacecraft(
            screen_instance=screen_instance,
            get_energy = self.__dyson_sphere.into_energy
        )

        # this obj manage the spacecraft collision
        self.__manager_spacecraft_collision = SpacecraftCollisionManager(
            spacecraft_rect=self.__player_spacecraft.get_rect(),
            get_energy=self.__dyson_sphere.into_energy
        )

        self.__enemy = Enemy(
            screen_instance=screen_instance,
            rect_player=self.__player_spacecraft.get_rect(),
            kill_player=self.__manager_spacecraft_collision.minus_live_shoot
        )

        # this obj manage the bullet spacecraft's weapon
        self.__manager_bullet = ManagerBullet(screen_width=screen_instance.get_rect().width)

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

        # detector to jump
        self.__jump_detector = WormHoleDetector(
            screen_instance=screen_instance,
            get_energy_spacecraft=self.__manager_spacecraft_collision.get_live
        )

        self.__next_sub_state = None

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
        self.__enemy.shooting_by_player(bullets=self.__manager_bullet.get_bullets())

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

        # detector to jump
        self.__jump_detector.run()

    def handle_events(self, event):
        self.__player_spacecraft.handler(event, manager_bullet=self.__manager_bullet)

        if self.__jump_detector.handler(event) and not self.__next_sub_state:
            self.__next_sub_state = 'Jump'

    def return_next_sub_state(self):
        if not self.__manager_spacecraft_collision.is_live():
            self.__next_sub_state = 'game_over'

        return self.__next_sub_state


from ..spacecraft.bullet.manager_bullet import ManagerBullet
from ..spacecraft.bullet.bullet import Bullet


class WeaponEnemy:
    def __init__(self, screen_instance,
                 enemy_rect):
        self.__screen = screen_instance
        self.__enemy_rect = enemy_rect

        self.__x_muzzle = lambda spa_r : [
            spa_r.x + spa_r.width / 2 - 10,
            spa_r.x + spa_r.width / 2 + 10,
        ]

        self.__velocity_y = 20

        self.__counter_latency = 30

    def shoot(self, manager_bullet: ManagerBullet):
        if self.__counter_latency == 0:
            manager_bullet.add_bullet(
                Bullet(screen_instance=self.__screen,
                       x_muzzle=self.__x_muzzle(self.__enemy_rect),
                       y_muzzle=self.__enemy_rect.y + self.__enemy_rect.height,
                       velocity_y=self.__velocity_y)
            )
            self.__counter_latency = 30
        else:
            self.__counter_latency -= 1




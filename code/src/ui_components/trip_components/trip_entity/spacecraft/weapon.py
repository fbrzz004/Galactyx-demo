from .bullet.manager_bullet import ManagerBullet
from .bullet.bullet import Bullet


class Weapon:
    def __init__(self, screen_instance,
                 spacecraft_rect):
        self.__screen = screen_instance
        self.__spacecraft_rect = spacecraft_rect

        self.__amount_energy = 100

        self.__x_muzzle = lambda spa_r : [
            spa_r.x + spa_r.width / 2 - 25,
            spa_r.x + spa_r.width / 2 + 20,
        ]

    def shoot(self, manager_bullet: ManagerBullet, energy):
        if self.__amount_energy > 0:
            manager_bullet.add_bullet(
                Bullet(screen_instance=self.__screen,
                       x_muzzle=self.__x_muzzle(self.__spacecraft_rect),
                       y_muzzle=self.__spacecraft_rect.y + 30,
                       energy=energy)
            )
            self.__amount_energy -= energy



from .bullet.manager_bullet import ManagerBullet
from .bullet.bullet import Bullet


class Weapon:
    def __init__(self, screen_instance,
                 spacecraft_rect,
                 get_energy):
        self.__screen = screen_instance
        self.__spacecraft_rect = spacecraft_rect

        self.__amount_energy = 200
        self.__max_energy = 200

        self.__x_muzzle = lambda spa_r : [
            spa_r.x + spa_r.width / 2 - 25,
            spa_r.x + spa_r.width / 2 + 20,
        ]

        self.__get_energy=get_energy

    def shoot(self, manager_bullet: ManagerBullet, energy):
        if self.__amount_energy > 0:
            manager_bullet.add_bullet(
                Bullet(screen_instance=self.__screen,
                       x_muzzle=self.__x_muzzle(self.__spacecraft_rect),
                       y_muzzle=self.__spacecraft_rect.y - 170)
            )
            self.__amount_energy -= energy

    def auto_get_energy(self):
        if self.__amount_energy < self.__max_energy and self.__get_energy(self.__spacecraft_rect):
            self.__amount_energy += 1

    def get_energy(self):
        return self.__amount_energy, self.__max_energy



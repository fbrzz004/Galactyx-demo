from functools import singledispatch
from .bullet import Bullet
from pygame import Rect

class ManagerBullet:
    def __init__(self):
        self.__bullets = []

    def add_bullet(self, bullet: Bullet):
        self.__bullets.append(bullet)

    @singledispatch
    def is_collision(self, rect_of_collision, set_collision_rect):
        for bullet in self.__bullets:
            for rect_b in bullet.get_rects().copy():
                if rect_b.colliderect(rect_of_collision):
                    bullet.get_rects().remove(rect_b)
                    set_collision_rect()
                    break
                if rect_b.y + rect_b.height < 0:
                    bullet.get_rects().remove(rect_b)

    @is_collision.register(list)
    def is_collision(self, list_rect_of_collisions):
        for rect_of_collision, set_collision_rect in list_rect_of_collisions:
            for bullet in self.__bullets:
                for rect_b in bullet.get_rects().copy():
                    if rect_b.colliderect(rect_of_collision):
                        bullet.get_rects().remove(rect_b)
                        set_collision_rect()
                        break
                    if rect_b.y + rect_b.height < 0:
                        bullet.get_rects().remove(rect_b)

    def run(self):
        for bullet in self.__bullets:
            bullet.run()
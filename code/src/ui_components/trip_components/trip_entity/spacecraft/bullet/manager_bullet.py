from functools import singledispatch
from .bullet import Bullet
from pygame import Rect

class ManagerBullet:
    def __init__(self):
        self.__bullets = []

    def add_bullet(self, bullet: Bullet):
        self.__bullets.append(bullet)

    @singledispatch
    def is_collision(self, rect_of_collision: Rect, set_collision_rect: callable):
        for bullet in self.__bullets:
            for rect_b in bullet.rects:
                if rect_b.colliderect(rect_of_collision):
                    bullet.rects.remove(rect_b)
                    set_collision_rect()
                if rect_b.y + rect_b.height < 0:
                    bullet.rects.remove(rect_b)

    @is_collision.register
    def _(self, rect_of_collisions: list):
        for bullet in self.__bullets:
            for rect_b in bullet.rects:
                for rect_of_collision, set_collision_rect in rect_of_collisions:
                    if rect_b.colliderect(rect_of_collision):
                        bullet.rects.remove(rect_b)
                        set_collision_rect()
                    if rect_b.y + rect_b.height < 0:
                        bullet.rects.remove(rect_b)

    def run(self):
        for bullet in self.__bullets:
            bullet.run()
from functools import singledispatch

class SpacecraftCollisionManager:
    def __init__(self, spacecraft_rect, get_energy):

        self.__live = 100
        self.__spacecraft_rect = spacecraft_rect
        self.__calculate_damage = lambda w, h: w * h * 0.0004

        self.__get_energy=get_energy

    @singledispatch
    def is_collision(self, list_rect_of_collisions):
        for rect_of_collision, set_collision_rect in list_rect_of_collisions:
            if self.__spacecraft_rect.colliderect(rect_of_collision):
                self.__live -= self.__calculate_damage(rect_of_collision.width,
                                                       rect_of_collision.height)
                set_collision_rect()

    def get_live(self):
        if self.__live < 0: self.__live = 0
        return self.__live

    def is_live(self):
        return True if self.__live > 0 else False

    def run(self):
        if self.__get_energy(self.__spacecraft_rect) and self.__live < 100:
            self.__live += 0.01
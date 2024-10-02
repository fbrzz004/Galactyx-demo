from .bullet import Bullet

class ManagerBullet:
    def __init__(self, screen_width):
        self.__bullets = []
        self.__screen_width = screen_width
        self.__f = 0

    def add_bullet(self, bullet: Bullet):
        self.__bullets.append(bullet)

    def get_bullets(self):
        return self.__bullets

    def is_collision_only_one(self, rect_of_collision, set_collision_rect):
        for bullet in self.__bullets:
            for rect_b in bullet.get_rects().copy():
                if rect_b.colliderect(rect_of_collision):
                    bullet.get_rects().remove(rect_b)
                    set_collision_rect()

    def is_collision(self, list_rect_of_collisions):
        for rect_of_collision, set_collision_rect in list_rect_of_collisions:
            for bullet in self.__bullets:
                for rect_b in bullet.get_rects().copy():
                    if rect_b.colliderect(rect_of_collision):
                        bullet.get_rects().remove(rect_b)
                        set_collision_rect()


    def __clear_bullets(self):
        for bullet in self.__bullets.copy():
            if bullet.get_rects():
                for rect_b in bullet.get_rects():
                    if not (0 < rect_b.y + rect_b.height < self.__screen_width):
                        self.__bullets.remove(bullet)
                        break
            else:
                self.__bullets.remove(bullet)


    def run(self):
        for bullet in self.__bullets:
            bullet.run()

        self.__clear_bullets()

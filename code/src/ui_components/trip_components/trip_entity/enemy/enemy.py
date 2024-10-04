from random import uniform

from pygame.image import load as load_image
from pygame.transform import rotate, scale

from src.ui_components.trip_components.trip_entity.enemy.weapon_enemy import WeaponEnemy
from src.ui_components.trip_components.trip_entity.spacecraft.bullet.manager_bullet import ManagerBullet
from pygame.draw import rect
from pygame import Rect

from pathlib import Path


class Enemy:
    def __init__(self, screen_instance, rect_player, kill_player: callable):
        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()

        self.__image = rotate(surface=load_image(Path('assets/images/enemy/enemy.png')),
                              angle=180)

        self.__standard_scale_factor = 1/6
        self.__image = scale(surface=self.__image, size=(self.__image.get_width() * self.__standard_scale_factor,
                                                         self.__image.get_height() * self.__standard_scale_factor))

        self.__image_rect = self.__image.get_rect()
        self.__image_rect_y = 10
        self.__image_rect.y = -self.__image_rect.height - 10
        self.__image_rect.x = uniform(self.__screen_rect.width * 1/4, self.__screen_rect.width * 3/4)

        self.__rect_player = rect_player
        self.__kill_player = kill_player

        # weapon
        self.__weapon = WeaponEnemy(
            screen_instance=screen_instance,
            enemy_rect=self.__image_rect
        )

        self.__manager_bullet = ManagerBullet(screen_width=self.__screen_rect.height)

        self.__lives = 0
        self.__max_lives = 100

        self.__count_time_hidden = uniform(100, 1000)

        # hud by energy
        self.__max_width = 100
        self.__rect_energy = Rect(self.__image_rect.x + (self.__image_rect.width - self.__max_width) / 2, (self.__image_rect_y + self.__image_rect.height) / 3, self.__max_width, 20)
        self.__rect_energy_outline = self.__rect_energy.copy()

        # auto behavior x velocity
        self.__min_x_velocity = 1
        self.__max_x_velocity = 4

    def __start_enemy(self):
        if self.__image_rect.y < 10:
            self.__image_rect.y += 1.4
        else:
            self.__image_rect.y = 10

    def __check_collision_bullet_with_player(self):
        self.__manager_bullet.is_collision_only_one(self.__rect_player, self.__kill_player)

    def __auto_behavior(self):
        factor = (self.__rect_player.x - self.__image_rect.x) / abs(self.__rect_player.x - self.__image_rect.x) if (self.__rect_player.x - self.__image_rect.x) else 0
        self.__image_rect.x += uniform(self.__min_x_velocity, self.__max_x_velocity) * factor
        self.__update_x_rect_energy()

    def __auto_shoot(self):
        if (self.__rect_player.x <= self.__image_rect.x <= self.__rect_player.x + self.__rect_player.width or
            self.__image_rect.x <= self.__rect_player.x <= self.__image_rect.x + self.__image_rect.width):
            self.__weapon.shoot(self.__manager_bullet)


    def shooting_by_player(self, bullets: list):
        if self.__image_rect.y == self.__image_rect_y:
            for bullet in bullets:
                for r in bullet.get_rects().copy():
                    if r.colliderect(self.__image_rect):
                        self.__lives -= 5
                        self.__update_width_rect_energy()
                        bullet.get_rects().remove(r)

    def __manage_behavior_hidden(self):
        if self.__lives == 0:
            self.__count_time_hidden -= 0.5
            if self.__count_time_hidden < 0:
                self.__lives = self.__max_lives
                self.__update_width_rect_energy()
                self.__count_time_hidden = uniform(100, 1000)
            else:
                self.__image_rect.y = -self.__image_rect.height - 10

    def __update_width_rect_energy(self):
        self.__rect_energy.width = self.__max_width * (self.__lives / self.__max_lives)

    def __update_x_rect_energy(self):
        self.__rect_energy.x = self.__image_rect.x + (self.__image_rect.width - self.__max_width) / 2
        self.__rect_energy_outline.x = self.__rect_energy.x

    def __show_live_hud(self):
        rect(surface=self.__screen,
             color=self.__set_color_energy(),
             rect=self.__rect_energy,
             border_radius=5)
        rect(surface=self.__screen,
             color="white",
             rect=self.__rect_energy_outline,
             border_radius=5,
             width=1)

    def __set_color_energy(self):
        level = self.__rect_energy.width
        if level > 75:
            return 144, 238, 144
        elif level > 50:
            return 255, 223, 0
        elif level > 25:
            return 255, 140, 0
        elif level > 0:
            return 200, 0, 0

    def run(self):
        self.__manage_behavior_hidden()

        if self.__lives > 0:
            self.__start_enemy()
            self.__auto_behavior()
            self.__screen.blit(self.__image, (self.__image_rect.x, self.__image_rect.y))
            self.__manager_bullet.run()
            if self.__image_rect.y == self.__image_rect_y:
                self.__auto_shoot()
                self.__show_live_hud()
            self.__check_collision_bullet_with_player()
        else:
            self.__lives = 0
            self.__update_width_rect_energy()
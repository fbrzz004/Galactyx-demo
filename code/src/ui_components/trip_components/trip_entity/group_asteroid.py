from src.ui_components.trip_components.trip_entity.asteroid import Asteroid

class GroupAsteroid:
    def __init__(self, screen_instance, amount_asteroids = 6):
        self.__asteroids_object = [
            Asteroid(screen_instance) for _ in range(amount_asteroids)
        ]

    def __run_asteroids(self):
        for asteroid in self.__asteroids_object:
            asteroid.run()

    def get_rect_callable_collision(self):
        rect_callable = []

        for asteroid in self.__asteroids_object:
            rect_callable.append([asteroid.get_rect(), asteroid.destroyed])

        return rect_callable

    def run(self):
        self.__run_asteroids()
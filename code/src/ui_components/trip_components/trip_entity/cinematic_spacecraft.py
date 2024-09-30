# cinematic_spacecraft.py
from pygame.image import load as load_image
from pygame.transform import scale, rotate

class CinematicSpacecraft:
    def __init__(self, screen_instance):

        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()

        # scale image
        self.__standard_size_factor = 1/7
        self.__original_image = load_image("assets/images/player/player_spaceship.png").convert_alpha()

        # rotate image
        self.__rotated_image = rotate(self.__original_image, -55)
         
        self.__scaled_image = scale(
            self.__rotated_image,
            (
                int(self.__rotated_image.get_rect().width * self.__standard_size_factor),
                int(self.__rotated_image.get_rect().height * self.__standard_size_factor)
            )
        )
        self.__image = self.__scaled_image
        self.__image_rect = self.__image.get_rect()


        self.__position_x = 0  # Start at x = 0
        self.__position_y = self.__screen_rect.height - self.__image_rect.height - 180 

        # velocity
        self.__velocity_x = 8.0 
        self.__velocity_y = -3.0 

        # scale
        self.__scale_increment = 0.04 
        self.__current_scale = 1.0 
    def update(self):
        # update position 
        self.__position_x += self.__velocity_x
        self.__position_y += self.__velocity_y

        # update image rect
        self.__image_rect.x = int(self.__position_x)
        self.__image_rect.y = int(self.__position_y)


        # scale image
        self.__current_scale += self.__scale_increment * 0.01  # Ajusta el factor de escala según sea necesario
        new_width = int(self.__scaled_image.get_rect().width * self.__current_scale)
        new_height = int(self.__scaled_image.get_rect().height * self.__current_scale)
        self.__image = scale(self.__scaled_image, (new_width, new_height))
        self.__image_rect = self.__image.get_rect()
        self.__image_rect.x = int(self.__position_x)
        self.__image_rect.y = int(self.__position_y)


    def __reset_position(self):
        self.__position_x = 0
        self.__position_y = self.__screen_rect.height - self.__image_rect.height
        self.__current_scale = 1.0
        self.__image = self.__scaled_image
        self.__image_rect = self.__image.get_rect()

    def draw(self):
        self.__screen.blit(self.__image, self.__image_rect)

    def run(self):
        self.update()
        self.draw()

    def get_position(self):
        return (self.__image_rect.x, self.__image_rect.y)

    def get_rect(self):
        return self.__image_rect

    def get_image(self):
        return self.__image

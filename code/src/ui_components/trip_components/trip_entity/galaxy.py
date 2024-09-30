# galaxy.py
from pygame.image import load as load_image
from pygame.transform import scale, rotate

class Galaxy:
    def __init__(self, screen_instance):
        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()

        # Load the original galaxy image
        self.__original_image = load_image("assets/images/galaxies/galaxy-andromeda.png").convert_alpha()

        # Initial size configuration
        self.__initial_size = (300, 300)  # Initial size
        self.__max_size = (600, 600)      # Maximum size
        self.__current_size = self.__initial_size

        # Scale the image to the initial size
        self.__image = scale(self.__original_image, self.__current_size)
        self.__image_rect = self.__image.get_rect()

        # Initial position in the top-right corner
        self.__image_rect.topright = (self.__screen_rect.width, 0)

        # Velocity and scale configuration
        self.__velocity_x = 0.5    # Velocity of left movement (pixels/frame)
        self.__scale_increment = 1.4  # Scale increment for each frame

    def __update_position(self):
        """Move the galaxy to the left."""
        self.__image_rect.x -= self.__velocity_x

    def __update_scale(self):
        """Increase the size of the galaxy to simulate approach."""
        new_width = self.__current_size[0] + self.__scale_increment
        new_height = self.__current_size[1] + self.__scale_increment

        # Check that the size does not exceed the maximum
        if new_width <= self.__max_size[0] and new_height <= self.__max_size[1]:
            self.__current_size = (new_width, new_height)
            self.__image = scale(self.__original_image, (int(new_width), int(new_height)))
            self.__image_rect = self.__image.get_rect()
            self.__image_rect.topright = (self.__screen_rect.width, self.__image_rect.y)

    def __reset_galaxy(self):
        """Reset the galaxy once it has moved completely off the screen."""
        self.__current_size = self.__initial_size
        self.__image = scale(self.__original_image, self.__initial_size)
        self.__image_rect = self.__image.get_rect()
        self.__image_rect.topright = (self.__screen_rect.width, 0)

    def update(self):
        """Update the position and scale of the galaxy."""
        self.__update_position()
        self.__update_scale()

        # Reset the galaxy if it has moved completely off the screen
        if self.__image_rect.right < 0 or self.__image_rect.y > self.__screen_rect.height:
            self.__reset_galaxy()

    def get_rect(self):
        """Return the galaxy rectangle."""
        return self.__image_rect

    def get_image(self):
        """Return the galaxy image."""
        return self.__image
    
    def run(self):
        """Update and draw the galaxy on the screen."""
        self.update()
        self.__screen.blit(self.__image, self.__image_rect)



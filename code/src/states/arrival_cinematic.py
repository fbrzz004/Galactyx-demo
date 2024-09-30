from src.states.abstract_state import AbstractState
from src.ui_components.button.text_button import TextButton
from src.ui_components.trip_components.trip_entity.galaxy import Galaxy
from src.ui_components.trip_components.trip_entity.cinematic_spacecraft import CinematicSpacecraft

class ArrivalCinematic(AbstractState):
    def __init__(self, screen_instance):
        AbstractState.__init__(self, screen_instance=screen_instance,
                               path_image_background="assets\\images\\ui\\background\\background_image_arrival.png")

        self.galaxy = Galaxy(screen_instance)
        self.cinematic_spacecraft = CinematicSpacecraft(screen_instance)

        self.__button_to_end = TextButton(
            position=(self._screen_rect.width - 20 - 100,
                      self._screen_rect.height - 20 - 30),
            dimension=(100, 30),
            label='To End',
            backgrounds_button_color_default='White',
            backgrounds_button_color_on_top_of='Gray',
            label_button_color='Black'
        )

    def draw(self):
        if self._image_background:
            self._screen.blit(self._image_background, (0, 0))
        else:
            self._screen.fill(self._background)
        self.galaxy.run()
        self.cinematic_spacecraft.run()
        self.check_collision()
        self.__button_to_end.draw(self._screen)

    def get_position(self):
        return (self.__image_rect.x, self.__image_rect.y)

    def check_collision(self):
        spacecraft_pos = self.cinematic_spacecraft.get_position()
        spacecraft_rect = self.cinematic_spacecraft.get_rect()
        galaxy_rect = self.galaxy.get_rect()

        proximity_threshold = 50  # Pixels

        spacecraft_center = (
            spacecraft_rect.centerx,
            spacecraft_rect.centery
        )

        galaxy_center = galaxy_rect.center

        distance = ((spacecraft_center[0] - galaxy_center[0]) ** 2 + (spacecraft_center[1] - galaxy_center[1]) ** 2) ** 0.5

        if distance < proximity_threshold:
            self._exit = True
            self.machine_observer.ui_class = 'end'

    
    def handle_events(self, event, machine_observer):
        if self.__button_to_end.handle_event():
            machine_observer.ui_class = 'end'
            self._exit = True

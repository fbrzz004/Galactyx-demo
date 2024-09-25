from tkinter.ttk import Treeview

from src.states.abstract_state import AbstractState
from src.ui_components.button.text_button import TextButton
from src.ui_components.narrative_display.narrative_display import NarrativeDisplay
from src.narratives.intro_narratives import intro_narrative

class OriginCinematic(AbstractState):
    def __init__(self, screen_instance):
        AbstractState.__init__(self, screen_instance=screen_instance,
                               path_image_background="..\\assets\\images\\ui\\background\\background_image_origin_cinematic.png")

        self.__display_narrative = NarrativeDisplay(screen_instance=screen_instance,
                                                    narrative=intro_narrative,
                                                    type_writer_effect=True)

        self.__button_continue = TextButton(
            position=(self._screen_rect.width - 20 - 100,
                      self._screen_rect.height - 20 - 30),
            dimension=(100, 30),
            label='Continue',
            backgrounds_button_color_default='White',
            backgrounds_button_color_on_top_of='Gray',
            label_button_color='Black'
        )

    def draw(self):
        self.__display_narrative.run()

        if self.__display_narrative.is_end():
            self.__button_continue.draw(self._screen)


    def handle_events(self, event, machine_observer):
        label_button_pressed = self.__button_continue.handle_event()

        if label_button_pressed == 'Continue':
            machine_observer.ui_class = 'map_levels'
            self._exit = True


import pygame
import time
from src.states.abstract_state import AbstractState
from src.ui_components.button.text_button import TextButton
from src.ui_components.narrative_display.narrative_display import NarrativeDisplay
from src.narratives.intro_narratives import intro_narrative

class OriginCinematic(AbstractState):
    def __init__(self, screen_instance):
        AbstractState.__init__(self, screen_instance=screen_instance)

        # Cargar las imágenes de las diferentes escenas
        self.__images = [
            pygame.image.load("assets\\images\\ui\\background\\background_image_trip.png"),  # En el espacio: Buscando al planeta.
            pygame.image.load("assets\\images\\planet\\starts03.png"),          # Se muestra el planeta (lo que antes era)
            pygame.image.load("assets\\images\\planet\\planet_destructive.png"),# Se muestra la actualidad del planeta (destruido)
            pygame.image.load("assets\\images\\planet\\nave.png"),        # Naves alrededor del planeta destruyendo. Naves nodrizas
            pygame.image.load("assets\\images\\planet\\chain_character.png"), # Se enfoca en el personaje principal para tener una misión.
            pygame.image.load("assets\\images\\planet\\naveship.png"),      # Se muestra el interior de la nave del personaje principal.
            pygame.image.load("assets\\images\\planet\\end.png")      # Finaliza cuando la nave del personaje va rumbo a buscar planeta.
        ]

        # Configuración de las narrativas para cada imagen
        self.__narratives = [
            NarrativeDisplay(screen_instance=screen_instance, narrative=intro_narrative[0], type_writer_effect=True, background_color='black'),
            NarrativeDisplay(screen_instance=screen_instance, narrative=intro_narrative[1], type_writer_effect=True, background_color='black'),
            NarrativeDisplay(screen_instance=screen_instance, narrative=intro_narrative[2], type_writer_effect=True, background_color='black'),
            NarrativeDisplay(screen_instance=screen_instance, narrative=intro_narrative[3], type_writer_effect=True, background_color='black'),
            NarrativeDisplay(screen_instance=screen_instance, narrative=intro_narrative[4], type_writer_effect=True, background_color='black'),
            NarrativeDisplay(screen_instance=screen_instance, narrative=intro_narrative[5], type_writer_effect=True, background_color='black')
        ]

        self.__button_continue = TextButton(
            position=(self._screen_rect.width - 20 - 100, self._screen_rect.height - 20 - 30),
            dimension=(100, 30),
            label='Continue',
            backgrounds_button_color_default='White',
            backgrounds_button_color_on_top_of='Gray',
            label_button_color='Black'
        )

        self.__current_image_index = 0  # Índice de la imagen actual
        self.__zooming = True  # Empezamos con el zoom en la primera imagen
        self.__zoom_factor = 1.0  # Zoom inicial
        self.__zoom_speed = 0.001  # Velocidad de zoom
        self.__zoom_duration = 2  # Duración del zoom en segundos
        self.__start_time = time.time()  # Tiempo de inicio del zoom
        self.__narrative_started = False  # Para controlar cuándo empieza la narrativa

    def draw(self):
        # Obtener la imagen actual
        current_image = self.__images[self.__current_image_index]

        # Aplicar efecto de zoom si es necesario
        if self.__zooming:
            # Calcular cuánto tiempo ha pasado
            elapsed_time = time.time() - self.__start_time
            if elapsed_time < self.__zoom_duration:
                # Aumentar el factor de zoom con el tiempo
                self.__zoom_factor += self.__zoom_speed
                zoomed_image = pygame.transform.scale(
                    current_image,
                    (int(self._screen_rect.width * self.__zoom_factor),
                     int(self._screen_rect.height * self.__zoom_factor))
                )
                # Centramos la imagen al hacer zoom
                zoom_rect = zoomed_image.get_rect(center=self._screen_rect.center)
                self._screen.blit(zoomed_image, zoom_rect)
            else:
                # Terminar el zoom después de la duración y mostrar la imagen a tamaño completo
                self.__zooming = False
                self._screen.blit(pygame.transform.scale(current_image, (self._screen_rect.width, self._screen_rect.height)), (0, 0))
                self.__narrative_started = True  # Activar la narrativa
        else:
            # Mostrar la imagen actual a tamaño completo si no hay zoom
            self._screen.blit(pygame.transform.scale(current_image, (self._screen_rect.width, self._screen_rect.height)), (0, 0))

            # Mostrar la narrativa asociada a la imagen actual si está activada
            if self.__narrative_started:
                self.__narratives[self.__current_image_index].run()

                # Si la narrativa ha terminado, permitir el cambio de imagen con el botón
                if self.__narratives[self.__current_image_index].is_end():
                    self.__button_continue.draw(self._screen)

    def handle_events(self, event, machine_observer):
        # Solo permitimos interacción si la narrativa ha terminado
        if self.__narratives[self.__current_image_index].is_end():
            label_button_pressed = self.__button_continue.handle_event()

            # Al presionar el botón "Continue", avanzamos a la siguiente imagen/narrativa
            if label_button_pressed == 'Continue':
                if self.__current_image_index < len(self.__images) - 1:
                    self.__current_image_index += 1  # Pasamos a la siguiente imagen
                    self.__zooming = True  # Reiniciamos el zoom para la nueva imagen
                    self.__zoom_factor = 1.0  # Reset del zoom
                    self.__start_time = time.time()  # Reiniciar el tiempo de inicio
                    self.__narrative_started = False  # Reiniciar el estado de narrativa
                else:
                    # Si estamos en la última imagen, finalizar el estado
                    machine_observer.ui_class = 'map_levels'
                    self._exit = True

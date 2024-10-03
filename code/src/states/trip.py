from src.states.abstract_state import AbstractState
from src.states.trip_sub_state.game_over_trip import GameOverTrip
from src.states.trip_sub_state.game_trip import GameTrip
from src.states.trip_sub_state.jump_cinematic import JumpTrip
from src.ui_components.trip_components.trip_hud.map_hud import MapHud


class Trip(AbstractState):
    def __init__(self, screen_instance):
        AbstractState.__init__(self, screen_instance=screen_instance)

        self.__screen = screen_instance

        # time_line
        self.__map_hud = MapHud(
            screen_instance=screen_instance
        )

        self.__map_hud.activate()

        # sub_state game trip
        self.__game_trip_sub_state = GameTrip(screen_instance, self.__map_hud.get_level_jump)


    def draw(self):
        self.__game_trip_sub_state.draw()
        self.__map_hud.run()

    def handle_events(self, events, machine_observer):

            for event in events:
                self.__game_trip_sub_state.handle_events(event)

            state = self.__game_trip_sub_state.return_next_sub_state()

            if state == 'Exit':
                machine_observer.exit = True
                self._exit = True

            if state == 'Again':
                del self.__game_trip_sub_state

                if self.__map_hud.is_end():
                    self._exit = True
                    machine_observer.ui_class = 'arrival_cinematic'
                else:
                    self.__game_trip_sub_state = GameTrip(self.__screen, self.__map_hud.get_level_jump)
                    self.__map_hud.activate()

            if state == 'Jump':
                self.__map_hud.set_jump()
                del self.__game_trip_sub_state
                self.__game_trip_sub_state = JumpTrip(self.__screen)
                self.__map_hud.deactivate()

            if state == 'game_over':
                del self.__game_trip_sub_state
                self.__game_trip_sub_state = GameOverTrip(self.__screen)
                self.__map_hud.deactivate()

            if state == 'Home':
                self._exit = True
                machine_observer.ui_class = 'home'
            

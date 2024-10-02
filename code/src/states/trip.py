from src.states.abstract_state import AbstractState
from src.states.trip_sub_state.game_over_trip import GameOverTrip
from src.states.trip_sub_state.game_trip import GameTrip
from src.states.trip_sub_state.jump_cinematic import JumpTrip

class Trip(AbstractState):
    def __init__(self, screen_instance):
        AbstractState.__init__(self, screen_instance=screen_instance)
        
        self.__screen = screen_instance

        # test the jump interface
        self.__game_trip_sub_state = GameTrip(screen_instance)

    def draw(self):
        self.__game_trip_sub_state.draw()


    def handle_events(self, events, machine_observer):

            for event in events:
                self.__game_trip_sub_state.handle_events(event)

            state = self.__game_trip_sub_state.return_next_sub_state()

            if state == 'Exit':
                machine_observer.exit = True
                self._exit = True

            if state == 'Again':
                del self.__game_trip_sub_state
                self.__game_trip_sub_state = GameTrip(self.__screen)

            if state == 'Jump':
                del self.__game_trip_sub_state
                self.__game_trip_sub_state = JumpTrip(self.__screen)

            if state == 'game_over':
                del self.__game_trip_sub_state
                self.__game_trip_sub_state = GameOverTrip(self.__screen)

            if state == 'Home':
                self._exit = True
                machine_observer.ui_class = 'home'
            

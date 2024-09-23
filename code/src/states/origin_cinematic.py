from src.states.abstract_state import AbstractState

class OriginCinematic(AbstractState):
    def __init__(self, screen_instance):
        AbstractState.__init__(self, screen_instance=screen_instance,
                               background_color="Red")

    def draw(self):
        pass

    def handle_events(self, event, machine_observer):
        pass


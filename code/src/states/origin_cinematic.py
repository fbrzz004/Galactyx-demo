from moviepy.editor import VideoFileClip
from src.states.abstract_state import AbstractState
from pathlib import Path

from pygame.surfarray import make_surface
from pygame.transform import scale

class OriginCinematic(AbstractState):
    def __init__(self, screen_instance):
        AbstractState.__init__(self, screen_instance=screen_instance)

        self.__video = VideoFileClip(str(Path('assets') / 'video_cinematica_origin' / 'cinematic_video.mp4'))
        self.__frames = self.__video.iter_frames(fps=60, dtype='uint8')
        self.__video_is_end = False

    def draw(self):
        if not self.__video_is_end:
            try:
                frame = next(self.__frames)
                frame = make_surface(frame.swapaxes(0, 1))
                frame = scale(frame, self._screen_rect.size)
                self._screen.blit(frame, (0, 0))
            except StopIteration:
                self._exit = True
                self.__video_is_end = True

    def handle_events(self, events, machine_observer):
        if self._exit:
            machine_observer.ui_class = 'map_levels'



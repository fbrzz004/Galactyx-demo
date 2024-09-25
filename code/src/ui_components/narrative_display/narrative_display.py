from pygame import Rect
from pygame.font import Font

from pygame.draw import rect


class NarrativeDisplay:
    def __init__(self,
                 screen_instance,
                 narrative: list[str],
                 time_sleep_by_word: float = 1,  # time in seconds
                 text_color: str = 'White',
                 type_writer_effect: bool = False,
                 background_color=None):

        # screen
        self.__screen = screen_instance
        self.__rect_screen = screen_instance.get_rect()

        # times
        self.__time_sleep_by_word = time_sleep_by_word
        self.__time_sleep_by_paragraph = 0
        self.__average_reading_time_by_words = 6

        # rect
        self.__rect_padding = 10
        self.__size = (500, 2 * self.__rect_padding)
        self.__position = (self.__rect_screen.width - self.__size[0] - 10, 10)
        self.__rect = Rect(*self.__position, *self.__size)
        self.__text_rect = Rect(self.__rect.x + self.__rect_padding,
                                self.__rect.y + self.__rect_padding,
                                self.__rect.width - 2 * self.__rect_padding,
                                self.__rect.height - 2 * self.__rect_padding)
        self.__background_color = background_color

        # narrative (text)
        self.__font = Font(None, 25)
        self.__narrative_surfaces = []  # store all surface rendered [
        # [(Surface-object,(x, y)), ()]
        # ]
        self.__space_between_words = 4
        self.__space_between_lines = 3
        self.__text_color = text_color
        self.__render_text(narrative)

        # effects
        self.__type_writer_effect_state = type_writer_effect
        self.__type_writer_effect_state_by_paragraph = type_writer_effect

        # get_fps
        self.__fps = 60
        self.__fpw = self.__fps * self.__time_sleep_by_word
        self.__fpw_count = 0
        self.__fpp_count = 0

        # run narrative state
        self.__index_paragraph = 0
        self.__end = False
        self.__paragraph_tmp = self.__narrative_surfaces[self.__index_paragraph]  # initial paragraph
        # we calculate the time it will take us per paragraph
        self.__time_sleep_by_paragraph = self.__set_time_sleep_by_paragraph()
        # empty structure for paragraph for shown
        self.__shown_word_surfaces = [[] for i in range(len(self.__paragraph_tmp))]
        self.__index_line_shown = 0

    # method for run the narrative
    def run(self):

        # if not complete to display all paragraph
        if not self.__end:

            # if exists the color value then draw a rect
            if self.__background_color:
                rect(surface=self.__screen,
                     color=self.__background_color,
                     rect=self.__rect,
                     border_radius=4)

            # if the flag for effect is True then execute the progressive adding the surface object to
            # list structure for shown the Text Surface in the screen
            if self.__type_writer_effect_state_by_paragraph:
                self.__type_writer_effect()
            # if the effect si no longer running, then count the reading wait time
            else:

                # In case of an execution without the effect, all the words will be displayed immediately
                if not self.__shown_word_surfaces:
                    self.__shown_word_surfaces = self.__paragraph_tmp.copy()
                    self.__paragraph_tmp.clear()

                # calculate the current fps for calculate the fps by paragraph
                fpp = self.__fps * self.__time_sleep_by_paragraph

                # if we count the number FPS per paragraph, and it equals  the FPP, then switch to the next paragraph
                if self.__fpp_count >= fpp:

                    # clear list current paragraph and initialize the fpp_count
                    self.__shown_word_surfaces.clear()
                    self.__fpp_count = 0

                    # update paragraph effect flag based on the value of the global effect state flag
                    self.__type_writer_effect_state_by_paragraph = self.__type_writer_effect_state

                    # continue with the next paragraph if exist
                    if len(self.__narrative_surfaces) > self.__index_paragraph + 1:
                        self.__index_paragraph += 1
                        self.__paragraph_tmp = self.__narrative_surfaces[self.__index_paragraph]
                        self.__shown_word_surfaces = [[] for i in range(len(self.__paragraph_tmp))]
                        self.__index_line_shown = 0
                        # calculate time to read paragraph
                        self.__time_sleep_by_paragraph = self.__set_time_sleep_by_paragraph()
                    else:
                        # if shown all paragraph then
                        self.__end = True
                else:
                    # count frame por paragraph
                    self.__fpp_count += 1

            # show current paragraph
            for line in self.__shown_word_surfaces:
                for word, word_pos in line:
                    self.__screen.blit(word, word_pos)

        return self.__end

    def __render_text(self, narrative: list[str]):
        # initialize the list for surfaces rendered
        self.__narrative_surfaces = []

        # inter over all paragraph
        for paragraph in narrative:

            # initialize top left variables for configure surface's position
            left, top = self.__text_rect.topleft
            size_line = 0  # for identify if line is more than to width of text_rect
            # to point to the last line (list) stored in the paragraph
            last_index_line_paragraph = 0
            # to store the rendered surfaces
            list_paragraph = [[]]

            # iter over each word of paragraph
            for word in paragraph.split(" "):
                # render a word
                word_surface = self.__font.render(word, True, self.__text_color)

                # calculate if the line has exceeded the rectangle for the text
                if size_line + word_surface.get_width() + self.__space_between_words > self.__text_rect.width:
                    list_paragraph.append([])
                    last_index_line_paragraph += 1
                    size_line = 0
                    left = self.__text_rect.left
                    top += word_surface.get_height() + self.__space_between_lines

                # append in the last list of list paragraph (matrix lines-words)
                list_paragraph[last_index_line_paragraph].append((word_surface.copy(), (left, top)))
                size_line += word_surface.get_width() + self.__space_between_words
                left += word_surface.get_width() + self.__space_between_words

                # resize the rect and text_rect
                if (len(list_paragraph) * (word_surface.get_height() + self.__space_between_lines)
                        - self.__space_between_lines > self.__text_rect.height):
                    self.__text_rect.height += word_surface.get_height() + self.__space_between_lines
                    self.__rect.height += word_surface.get_height() + self.__space_between_lines

            # store a paragraph rendered
            self.__narrative_surfaces.append(list_paragraph.copy())

    def __set_time_sleep_by_paragraph(self):
        time = sum([l.__len__() for l in self.__paragraph_tmp]) * self.__average_reading_time_by_words
        return time

    # add word to the show_list_paragraph
    def __type_writer_effect(self):

        # verify if temporary paragraph is not empty
        if self.__paragraph_tmp:
            # verify if the line in paragraph is not empty
            if self.__paragraph_tmp[0]:

                # check if the frames per word have passed to add another word
                if self.__fpw_count >= self.__fpw:

                    # Transfer one more surface to the matrix used for painting on the scree
                    self.__shown_word_surfaces[self.__index_line_shown].append(self.__paragraph_tmp[0].pop(0))

                    # delete a list (line) is all words has been transfer
                    if not self.__paragraph_tmp[0]:
                        self.__paragraph_tmp.pop(0)
                        self.__index_line_shown += 1

                    # initialize the counter of frame
                    self.__fpw_count = 0
                else:
                    self.__fpw_count += 1
        else:

            # effect complete
            self.__type_writer_effect_state_by_paragraph = False

    def is_end(self):
        # all paragraph have been shown
        return self.__end

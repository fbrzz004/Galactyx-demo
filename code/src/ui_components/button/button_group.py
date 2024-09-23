from src.ui_components.button.button import Button, Rect

# This class is a group of buttons
class ButtonGroup:

    def __init__(self,
                 screen_rect: Rect,
                 labels: list[str],
                 dimension: list[float] | tuple[float, float] = None,
                 position: list[float] | tuple[float, float] = None,
                 vertical_center: bool = False,
                 horizontal_center: bool = False,
                 on_top: bool = False,
                 on_left: bool = False
                 ):

        self.__set_rect(screen_rect,
                        position, dimension,
                        vertical_center,
                        horizontal_center,
                        on_top, on_left)

        self.__buttons = self.__instance_buttons(labels)

    def __set_rect(self, screen_rect: Rect,
                   position: list[float] | tuple[float, float],
                   dimension: list[float] | tuple[float, float],
                   vertical_center: bool = False,
                   horizontal_center: bool = False,
                   on_top: bool = False,
                   on_left: bool = False
                   ):

        # set position
        if not position: position = [0, 0]

        if vertical_center:
            position[0] = float(screen_rect.centerx) - dimension[0] / 2

        elif on_left:
            position[0] =  float(screen_rect.left)

        if horizontal_center:
            position[1] =  float(screen_rect.centery)  - dimension[1] / 2

        elif on_top:
            position[1] =  float(screen_rect.top)

        # instance the Rect class
        self.__rect = Rect(*position, *dimension)

    def __instance_buttons(self, labels: list[str]) -> list[Button]:
        buttons = []

        # configure the position of all buttons
        space_between_buttons = 20
        dimension = [float(self.__rect.width), float((self.__rect.height - len(labels) * space_between_buttons) / len(labels))]
        positions = [[self.__rect.x, y] for y in range(self.__rect.y, self.__rect.y + self.__rect.height, space_between_buttons + int(dimension[1]))]

        # instance and add all buttons in list "buttons"
        for label, position in zip(labels, positions):
            buttons.append(Button(
                position=position,
                dimension=dimension,
                label=label,
                background_color='black',
                label_color='white'
            ))

        return buttons

    # this methods draw all buttons given in labels parameter
    def draw(self, screen_instance):
        for button in self.__buttons:
            button.draw(screen_instance)

    def handle_events(self):
        label_activate = None
        index = 0

        while not label_activate and index < len(self.__buttons):
            label_activate = self.__buttons[index].handle_event()
            index += 1

        return label_activate
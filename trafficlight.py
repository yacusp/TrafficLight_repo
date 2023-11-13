class TrafficLight:
    def __init__(self, position, tl_center, l_shift, l_radius, box_xy, color='red'):
        self.__color = color
        self.__timer = 0
        self.__working = False
        self.__yellow_light = tl_center
        self.__position = position
        self.__l_radius = l_radius

        if position == 'left':
            self.__green_light = (tl_center[0] - l_shift, tl_center[1])
            self.__red_light = (tl_center[0] + l_shift, tl_center[1])
            self.__box_xy = (box_xy[0], box_xy[1])

        if position == 'top':
            self.__green_light = (tl_center[0], tl_center[1] - l_shift)
            self.__red_light = (tl_center[0], tl_center[1] + l_shift)
            self.__box_xy = (box_xy[1], box_xy[0])

        if position == 'right':
            self.__green_light = (tl_center[0] + l_shift, tl_center[1])
            self.__red_light = (tl_center[0] - l_shift, tl_center[1])
            self.__box_xy = (box_xy[0], box_xy[1])

        if position == 'bottom':
            self.__green_light = (tl_center[0], tl_center[1] + l_shift)
            self.__red_light = (tl_center[0], tl_center[1] - l_shift)
            self.__box_xy = (box_xy[1], box_xy[0])

    def next_color(self):
        if self.__color == 'red':
            self.__color = 'red and yellow'
        elif self.__color == 'red and yellow':
            self.__color = 'green'
        elif self.__color == 'green':
            self.__color = 'yellow'
        elif self.__color == 'yellow':
            self.__color = 'red'

    def set_opposite_color(self, color):
        if color == 'red':
            self.__color = 'green'
        elif color == 'red and yellow':
            self.__color = 'yellow'
        elif color == 'green':
            self.__color = 'red'
        elif color == 'yellow':
            self.__color = 'red and yellow'

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def make_color_list(self, color):
        grey = (125, 125, 125)
        red = (225, 50, 50)
        yellow = (225, 225, 0)
        green = (0, 200, 64)

        red_light_red = (red, self.__red_light, self.__l_radius)
        red_light_grey = (grey, self.__red_light, self.__l_radius)
        yellow_light_yellow = (yellow, self.__yellow_light, self.__l_radius)
        yellow_light_grey = (grey, self.__yellow_light, self.__l_radius)
        green_light_green = (green, self.__green_light, self.__l_radius)
        green_light_grey = (grey, self.__green_light, self.__l_radius)

        color_set_list = []

        if color == 'red':
            color_set_list = [red_light_red, yellow_light_grey, green_light_grey]
        elif color == 'red and yellow':
            color_set_list = [red_light_red, yellow_light_yellow, green_light_grey]
        elif color == 'yellow':
            color_set_list = [red_light_grey, yellow_light_yellow, green_light_grey]
        elif color == 'green':
            color_set_list = [red_light_grey, yellow_light_grey, green_light_green]

        return color_set_list

    def get_box(self):
        box_x_pos = self.__yellow_light[0] - self.__box_xy[0] / 2
        box_y_pos = self.__yellow_light[1] - self.__box_xy[1] / 2
        box_x = self.__box_xy[0]
        box_y = self.__box_xy[1]
        box = (box_x_pos, box_y_pos, box_x, box_y)
        return box

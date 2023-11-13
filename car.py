import variables
import random


class Car:
    car_w = int(variables.road_w // 6)
    car_l = int(car_w * 2)

    h_car_counter = 0
    v_car_counter = 0

    max_cars_in_row = variables.sc_w // car_l

    def __init__(self, start_point, name, current_time):
        self.__speed = 0
        self.__acceleration = variables.max_acceleration
        self.color = variables.car_colors[int(random.random() * 7)]
        self.name = name
        self.__timer = current_time
        self.move = True

        if start_point == 'left':
            # start point
            self.__x_pos = 0
            self.__y_pos = (variables.sc_h // 2) + (variables.road_w // 4)
            # start direction
            self.__x_dir = 1
            self.__y_dir = 0
            self.__x_accel = 1
            self.__y_accel = 0
            self.__orient = 'h'

        elif start_point == 'right':
            # start point
            self.__x_pos = variables.sc_w - 1
            self.__y_pos = (variables.sc_h // 2) - (variables.road_w // 4)
            # start direction
            self.__x_dir = -1
            self.__y_dir = 0
            self.__x_accel = -1
            self.__y_accel = 0
            self.__orient = 'h'

        elif start_point == 'top':
            # start point
            self.__x_pos = (variables.sc_w // 2) - (variables.road_w // 4)
            self.__y_pos = 0
            # start direction
            self.__x_dir = 0
            self.__y_dir = 1
            self.__x_accel = 0
            self.__y_accel = 1
            self.__orient = 'v'

        elif start_point == 'bottom':
            # start point
            self.__x_pos = (variables.sc_w // 2) + (variables.road_w // 4)
            self.__y_pos = variables.sc_h - 1
            # start direction
            self.__x_dir = 0
            self.__y_dir = -1
            self.__x_accel = 0
            self.__y_accel = -1
            self.__orient = 'v'

    def go(self, current_time):
        self.move = True
        self.__acceleration = variables.max_acceleration - random.random() * 10
        self.__timer = current_time

    def stop(self):
        self.__acceleration = -1 * (variables.max_acceleration - random.random() * 10)
        self.__speed = 0
        self.move = False

    def update(self, current_time):
        if self.move:
            # speed update
            time_delta = current_time - self.__timer
            self.__timer = current_time
            self.__speed += time_delta * self.__acceleration
            if self.__speed < 0:
                self.__speed = 0
                self.move = False
            if self.__speed > variables.max_speed:
                self.__speed = variables.max_speed

            # position update
            self.__x_pos += self.__speed * time_delta * self.__x_accel
            self.__y_pos += self.__speed * time_delta * self.__y_accel

    def make_box(self):
        if self.__orient == 'h':
            x_p = int(self.__x_pos) - int(Car.car_l / 2)
            y_p = int(self.__y_pos) - int(Car.car_w / 2)
            x_d = Car.car_l
            y_d = Car.car_w
        else:
            x_p = int(self.__x_pos - Car.car_w / 2)
            y_p = int(self.__y_pos - Car.car_l / 2)
            x_d = Car.car_w
            y_d = Car.car_l

        box = (x_p, y_p, x_d, y_d)
        return box

    def get_front_bumper(self):
        if self.__x_dir >= 0 and self.__y_dir >= 0:
            return (self.__x_pos + (Car.car_l / 2)) * self.__x_dir + (self.__y_pos + (Car.car_l / 2)) * self.__y_dir
        else:
            return -1 * (((variables.sc_w - self.__x_pos) + (Car.car_l / 2)) * self.__x_dir +
                         ((variables.sc_h - self.__y_pos) + (Car.car_l / 2)) * self.__y_dir)

    def get_back_bumper(self):
        if self.__x_dir >= 0 and self.__y_dir >= 0:
            return (self.__x_pos - (Car.car_l / 2)) * self.__x_dir + (self.__y_pos - (Car.car_l / 2)) * self.__y_dir
        else:
            return -1 * (((variables.sc_w - self.__x_pos) - (Car.car_l / 2)) * self.__x_dir +
                         ((variables.sc_h - self.__y_pos) - (Car.car_l / 2)) * self.__y_dir)

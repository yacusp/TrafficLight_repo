import car
import variables


class TrafficLine:
    def __init__(self, start_point, stop_line, delete_line, buffer_zone):
        self.__start_point = start_point
        self.__stop_line = stop_line
        self.__delete_line = delete_line
        self.__buffer_zone = buffer_zone
        self.__car_list = []

    def add_car(self, current_time):
        if all(cur_car.get_back_bumper() > car.Car.car_l for cur_car in self.__car_list):
            self.__car_list.append(car.Car(self.__start_point, 'car_1', current_time))

    def update(self, current_time, light_color):
        for current_car in self.__car_list:
            current_car.update(current_time)

            if self.__stop_line > current_car.get_front_bumper() > variables.stop_line_dist - \
                    self.__buffer_zone and (light_color == 'red' or light_color == 'red and yellow'):
                current_car.stop()

            if light_color != 'red' and light_color != 'red and yellow':
                current_car.go(current_time)

            if all(0 > other_car.get_back_bumper() - current_car.get_front_bumper() or
                   other_car.get_back_bumper() - current_car.get_front_bumper() > variables.stop_buffer_zone
                   for other_car in self.__car_list):
                current_car.go(current_time)
            else:
                current_car.stop()

            if current_car.get_back_bumper() > self.__delete_line:
                self.__car_list.remove(current_car)

    def count_cars_before_stop_line(self):
        counter = 0
        for cur_car in self.__car_list:
            if cur_car.get_front_bumper() < variables.stop_line_dist:
                counter += 1
        return counter

    def get_car_list(self):
        return self.__car_list

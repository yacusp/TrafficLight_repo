class Logic:
    def __init__(self, current_time, yellow_time, base_green_time, increment, time_limit, h_traffic_light):
        self.__timer = current_time
        self.__y_time = yellow_time
        self.__base_time = base_green_time
        self.__h_time = base_green_time
        self.__v_time = base_green_time
        self.__increment = increment
        self.__time_limit = time_limit
        self.__h_traffic_light = h_traffic_light
        self.__h_unlimited_mode = False
        self.__v_unlimited_mode = False

    def start(self, current_time):
        pass

    def recount_time(self, h_count, v_count):
        if h_count == 0 or v_count == 0 or h_count == v_count:
            self.__h_time = self.__base_time
            self.__v_time = self.__base_time
        elif h_count > v_count:
            self.__h_time = self.__base_time + self.__increment * (h_count - v_count)
            if self.__h_time >= self.__time_limit:
                self.__h_time = self.__time_limit
        else:
            self.__v_time = self.__base_time + self.__increment * (v_count - h_count)
            if self.__v_time >= self.__time_limit:
                self.__v_time = self.__time_limit

    def update(self, current_time, h_count, v_count, color):
        if color == "green":
            if h_count == 0 and v_count > 0:
                self.__h_traffic_light.next_color()
                self.__timer = current_time
                self.recount_time(h_count, v_count)
                self.__h_unlimited_mode = False
            elif h_count > 0 and v_count == 0:
                self.__h_unlimited_mode = True
                self.__timer = current_time
            elif current_time - self.__timer > self.__h_time:
                self.__h_traffic_light.next_color()
                self.__timer = current_time
                self.recount_time(h_count, v_count)
                self.__h_unlimited_mode = False
        elif color == "red":
            if v_count == 0 and h_count > 0:
                self.__h_traffic_light.next_color()
                self.__timer = current_time
                self.recount_time(h_count, v_count)
                self.__v_unlimited_mode = False
            elif h_count == 0 and v_count > 0:
                self.__v_unlimited_mode = True
                self.__timer = current_time
            elif current_time - self.__timer > self.__v_time:
                self.__h_traffic_light.next_color()
                self.__timer = current_time
                self.recount_time(h_count, v_count)
                self.__v_unlimited_mode = False
        else:
            if current_time - self.__timer > self.__y_time:
                self.__h_traffic_light.next_color()
                self.__timer = current_time

    def return_times(self):
        return self.__h_time, self.__v_time

    def get_h_unlim(self):
        return self.__h_unlimited_mode

    def get_v_unlim(self):
        return self.__v_unlimited_mode

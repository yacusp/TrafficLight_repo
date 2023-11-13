# global
sc_w = 1000
sc_h = 1000
center_x = sc_w / 2
center_y = sc_h / 2

# elements dimensions
gras_wh = 430
road_w = 120
crosswalk_n = 8
crosswalk_w = 40
crosswalk_shift = 30
stop_line_thickness = 15
road_line_thickness = 6
# elements colors
grass_color = (0, 153, 0)
asphalt_color = (96, 96, 96)
line_color = (224, 224, 224)

# stop line
stop_line_shift = crosswalk_shift * 2 + crosswalk_w + road_w // 2
stop_line_dist = sc_w // 2 - stop_line_shift

# traffic light offsets
tl_x_shift = 120
tl_y_shift = 90
left_tl_center = [center_x - tl_x_shift, center_y + tl_y_shift]
top_tl_center = [center_x - tl_y_shift, center_y - tl_x_shift]
right_tl_center = [center_x + tl_x_shift, center_y - tl_y_shift]
bottom_tl_center = [center_x + tl_y_shift, center_y + tl_x_shift]

l_radius = 8
l_shift = 20
box_xy = (l_radius * 3 + l_shift * 2, l_radius * 2 + l_radius / 4)

# traffic light time
yellow_time = 2
base_green_time = 4
increment = 2
max_time_limit = 16

# buffer zone
stop_buffer_zone = 30
start_buffer_zone = 60

# car variables
max_speed = 200
max_acceleration = 50

# car colors
car_colors = ((0, 204, 204),
              (255, 128, 0),
              (0, 100, 0),
              (28, 28, 28),
              (51, 51, 255),
              (153, 51, 255),
              (32, 32, 32))

# Trafficlight text position
auto_mode_text_pos = (20, 20)
h_time_text_pos = (20, sc_h / 16)
h_unlim_text_pos = (20, sc_h / 16 + 40)
v_time_text_pos = (20, sc_h / 16 + 80)
v_unlim_text_pos = (20, sc_h / 16 + 120)

# # Description text position
arrow_k_text_pos = (20, sc_h / 2 + road_w / 2 + 80)
a_k_text_pos = (20, sc_h / 2 + road_w / 2 + 120)
l_k_text_pos = (20, sc_h / 2 + road_w / 2 + 160)

import pygame as pg
import variables

# elements dimensions
gras_wh = variables.gras_wh
asphalt_w = variables.road_w
crosswalk_n = variables.crosswalk_n
crosswalk_w = variables.crosswalk_w
crosswalk_shift = variables.crosswalk_shift
stop_line_thickness = variables.stop_line_thickness
road_line_thickness = variables.road_line_thickness
# elements colors
grass_color = variables.grass_color
asphalt_color = variables.asphalt_color
line_color = variables.line_color


def draw_stop_line(screen, sc_w, sc_h):
    stop_line_w = asphalt_w // 2
    stop_line_shift = variables.stop_line_shift
    pg.draw.rect(screen, line_color,
                 (sc_w // 2 - stop_line_shift - stop_line_thickness, sc_h // 2, stop_line_thickness, stop_line_w))
    pg.draw.rect(screen, line_color,
                 (sc_w // 2 + stop_line_shift, sc_h // 2 - stop_line_w, stop_line_thickness, stop_line_w))
    pg.draw.rect(screen, line_color,
                 (sc_w // 2 - stop_line_w, sc_h // 2 - stop_line_shift - stop_line_thickness,
                  stop_line_w, stop_line_thickness))
    pg.draw.rect(screen, line_color,
                 (sc_w // 2, sc_h // 2 + stop_line_shift, stop_line_w, stop_line_thickness))


def draw_road_line(screen, sc_w, sc_h):
    road_line_shift = stop_line_thickness + crosswalk_shift * 2 + crosswalk_w + asphalt_w // 2
    road_line_length = sc_w // 2 - road_line_shift
    pg.draw.rect(screen, line_color,
                 (0, sc_h // 2 - road_line_thickness // 2, road_line_length, road_line_thickness))
    pg.draw.rect(screen, line_color,
                 (sc_w // 2 + road_line_shift, sc_h // 2 - road_line_thickness // 2,
                  road_line_length, road_line_thickness))
    pg.draw.rect(screen, line_color,
                 (sc_w // 2 - road_line_thickness // 2, 0, road_line_thickness, road_line_length))
    pg.draw.rect(screen, line_color,
                 (sc_w // 2 - road_line_thickness // 2, sc_h // 2 + road_line_shift,
                  road_line_thickness, road_line_length))


def draw_crosswalk(screen, sc_w, sc_h):
    line_t = asphalt_w // (crosswalk_n * 2 + 1)
    vertical_x_start_point = sc_w // 2 - asphalt_w // 2 - crosswalk_shift
    vertical_y_start_point = sc_h // 2 - asphalt_w // 2 + line_t
    horizontal_y_start_point = sc_h // 2 - asphalt_w // 2 - crosswalk_shift
    horizontal_x_start_point = sc_w // 2 - asphalt_w // 2 + line_t
    for i in range(crosswalk_n):
        # vertical crosswalk drawing
        pg.draw.rect(screen, line_color,
                     (vertical_x_start_point - crosswalk_w, vertical_y_start_point, crosswalk_w, line_t))
        pg.draw.rect(screen, line_color,
                     (sc_w - vertical_x_start_point, vertical_y_start_point, crosswalk_w, line_t))
        vertical_y_start_point += line_t * 2
        # horizontal crosswalk drawing
        pg.draw.rect(screen, line_color,
                     (horizontal_x_start_point, horizontal_y_start_point - crosswalk_w, line_t, crosswalk_w))
        pg.draw.rect(screen, line_color,
                     (horizontal_x_start_point, sc_h - horizontal_y_start_point, line_t, crosswalk_w))
        horizontal_x_start_point += line_t * 2


def draw_grass(screen, sc_w, sc_h):
    pg.draw.rect(screen, grass_color, (0, 0, gras_wh, gras_wh))
    pg.draw.rect(screen, grass_color, (sc_w - gras_wh, 0, gras_wh, gras_wh))
    pg.draw.rect(screen, grass_color, (0, sc_h - gras_wh, gras_wh, gras_wh))
    pg.draw.rect(screen, grass_color, (sc_w - gras_wh, sc_h - gras_wh, gras_wh, gras_wh))


def draw_roads(screen, sc_w, sc_h):
    pg.draw.rect(screen, asphalt_color, (sc_w / 2 - asphalt_w / 2, 0, asphalt_w, sc_h))
    pg.draw.rect(screen, asphalt_color, (0, sc_h / 2 - asphalt_w / 2, sc_w, asphalt_w))


def draw_scene(screen, sc_w, sc_h):
    draw_grass(screen, sc_w, sc_h)
    draw_roads(screen, sc_w, sc_h)
    draw_crosswalk(screen, sc_w, sc_h)
    draw_stop_line(screen, sc_w, sc_h)
    draw_road_line(screen, sc_w, sc_h)

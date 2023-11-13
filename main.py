import time
import pygame as pg
import sys
import road_scene
import traffic
import variables as va
import trafficlight
import logic


def main():
    pg.init()
    run = True
    sc_w = va.sc_w
    sc_h = va.sc_h
    sc = pg.display.set_mode((sc_w, sc_h))
    auto_mode = True

    road_lines = []
    left_traffic = traffic.TrafficLine('left', va.stop_line_dist, va.sc_w, va.stop_buffer_zone)
    right_traffic = traffic.TrafficLine('right', va.stop_line_dist, va.sc_w, va.stop_buffer_zone)
    top_traffic = traffic.TrafficLine('top', va.stop_line_dist, va.sc_w, va.stop_buffer_zone)
    bottom_traffic = traffic.TrafficLine('bottom', va.stop_line_dist, va.sc_w, va.stop_buffer_zone)

    left_light = trafficlight.TrafficLight('left', va.left_tl_center, va.l_shift, va.l_radius, va.box_xy, 'green')
    right_light = trafficlight.TrafficLight('right', va.right_tl_center, va.l_shift, va.l_radius, va.box_xy, 'green')
    top_light = trafficlight.TrafficLight('top', va.top_tl_center, va.l_shift, va.l_radius, va.box_xy)
    bottom_light = trafficlight.TrafficLight('bottom', va.bottom_tl_center, va.l_shift, va.l_radius, va.box_xy)

    left_logic = logic.Logic(time.time(), va.yellow_time, va.base_green_time,
                             va.increment, va.max_time_limit, left_light)

    font = pg.font.Font(None, 32)
    font_2 = pg.font.Font(None, 26)

    while run:
        pg.time.delay(10)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_l and not auto_mode:
                    left_light.next_color()

                if event.key == pg.K_a:
                    if auto_mode:
                        auto_mode = False
                    else:
                        auto_mode = True

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            left_traffic.add_car(time.time())
        if keys[pg.K_RIGHT]:
            right_traffic.add_car(time.time())
        if keys[pg.K_UP]:
            top_traffic.add_car(time.time())
        if keys[pg.K_DOWN]:
            bottom_traffic.add_car(time.time())

        road_scene.draw_scene(sc, sc_w, sc_h)

        right_light.set_color(left_light.get_color())
        top_light.set_opposite_color(left_light.get_color())
        bottom_light.set_color(top_light.get_color())

        pg.draw.rect(sc, 'black', left_light.get_box())
        for light in left_light.make_color_list(left_light.get_color()):
            pg.draw.circle(sc, light[0], light[1], light[2])
        pg.draw.rect(sc, 'black', right_light.get_box())
        for light in right_light.make_color_list(right_light.get_color()):
            pg.draw.circle(sc, light[0], light[1], light[2])
        pg.draw.rect(sc, 'black', top_light.get_box())
        for light in top_light.make_color_list(top_light.get_color()):
            pg.draw.circle(sc, light[0], light[1], light[2])
        pg.draw.rect(sc, 'black', bottom_light.get_box())
        for light in bottom_light.make_color_list(bottom_light.get_color()):
            pg.draw.circle(sc, light[0], light[1], light[2])

        left_traffic.update(time.time(), left_light.get_color())
        right_traffic.update(time.time(), right_light.get_color())
        top_traffic.update(time.time(), top_light.get_color())
        bottom_traffic.update(time.time(), bottom_light.get_color())

        for cur_car in left_traffic.get_car_list():
            pg.draw.rect(sc, cur_car.color, cur_car.make_box())
        for cur_car in right_traffic.get_car_list():
            pg.draw.rect(sc, cur_car.color, cur_car.make_box())
        for cur_car in top_traffic.get_car_list():
            pg.draw.rect(sc, cur_car.color, cur_car.make_box())
        for cur_car in bottom_traffic.get_car_list():
            pg.draw.rect(sc, cur_car.color, cur_car.make_box())

        if auto_mode:
            h_count = left_traffic.count_cars_before_stop_line() + right_traffic.count_cars_before_stop_line()
            v_count = top_traffic.count_cars_before_stop_line() + bottom_traffic.count_cars_before_stop_line()
            print('H_cars: ' + str(h_count) + '   V_cars: ' + str(v_count))
            left_logic.update(time.time(), h_count, v_count, left_light.get_color())

        auto_mode_text = str('Auto mode: ' + str(auto_mode))
        h_time_text = str('Horizontal line traffic light time: ' + str(left_logic.return_times()[0]))
        h_unlim_text = str('Horizontal unlimited mode: ' + str(left_logic.get_h_unlim()))
        v_time_text = str('Vertical line traffic light time: ' + str(left_logic.return_times()[1]))
        v_unlim_text = str('Vertical unlimited mode: ' + str(left_logic.get_v_unlim()))

        text_auto_mode = font.render(auto_mode_text, True, (255, 150, 0))
        time_text_h = font.render(h_time_text, True, (255, 150, 0))
        unlim_text_h = font.render(h_unlim_text, True, (255, 150, 0))
        time_text_v = font.render(v_time_text, True, (255, 150, 0))
        unlim_text_v = font.render(v_unlim_text, True, (255, 150, 0))

        arrow_k_text = font_2.render('Press or hold arrow keys to add cars', True, (255, 150, 0))
        a_k_text = font_2.render('Press \'a\' key to change auto/manual mode', True, (255, 150, 0))
        l_k_text = font_2.render('Press \'l\' key to change light in manual mode', True, (255, 150, 0))

        sc.blit(text_auto_mode, va.auto_mode_text_pos)
        sc.blit(time_text_h, va.h_time_text_pos)
        sc.blit(unlim_text_h, va.h_unlim_text_pos)
        sc.blit(time_text_v, va.v_time_text_pos)
        sc.blit(unlim_text_v, va.v_unlim_text_pos)
        sc.blit(arrow_k_text, va.arrow_k_text_pos)
        sc.blit(a_k_text, va.a_k_text_pos)
        sc.blit(l_k_text, va.l_k_text_pos)

        pg.display.update()


if __name__ == "__main__":
    main()

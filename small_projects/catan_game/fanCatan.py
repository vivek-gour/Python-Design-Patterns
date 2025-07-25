import pygame
import sys
from math import sin, cos, pi
import random


class myGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Fan Catan')
        self.screen = pygame.display.set_mode((1920, 1080))

        self.clock = pygame.time.Clock()
        self.hex_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.dt = 0
        self.cloud1_pos_x = 20
        self.cloud2_pos_x = 0
        self.cloud3_pos_x = 0

        self.go1_left = False
        self.go2_left = False
        self.go3_left = False
        self.number_of_players = 3

    def draw_regular_polygon(self, surface, color, vertex_count, radius, position, width=0):
        n, r = vertex_count, radius
        x, y = position
        # print([(x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n)) for i in range(n)])
        pygame.draw.polygon(surface, color,
                            [(x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n)) for i in range(n)], width)

    def load_draw_img(self, name, location, sizep=None, angle=None):
        img = pygame.image.load(f'images/{name}.png').convert_alpha()
        if sizep:
            img = pygame.transform.smoothscale(img, (img.get_width() * sizep, img.get_height() * sizep))
        if angle:
            img = pygame.transform.rotate(img, angle)
        return self.screen.blit(img, location)

    def re_arrange_number(self, num_list):
        rule_book = {0: [1, 3, 4],
                     1: [0, 2, 4, 5],
                     2: [1, 5, 6],
                     3: [0, 4, 7, 8],
                     4: [0, 1, 3, 5, 8, 9],
                     5: [1, 2, 4, 6, 9, 10],
                     6: [2, 5, 10, 11],
                     7: [3, 8, 12],
                     8: [3, 4, 7, 9, 12, 13],
                     9: [4, 5, 8, 10, 13, 14],
                     10: [5, 6, 9, 11, 14, 15],
                     11: [6, 10, 15],
                     12: [7, 8, 13, 16],
                     13: [8, 9, 12, 14, 16, 17],
                     14: [9, 10, 13, 15, 17, 18],
                     15: [10, 11, 14, 18],
                     16: [12, 13, 17],
                     17: [14, 15, 18]
                     }
        safe_num_pos = []
        num_to_switch = []
        for key, val in rule_book.items():
            tempList = [num_list[v] for v in val]
            if num_list[key] in ['6', '8'] or ('6' in tempList or '8' in tempList):
                if num_list[key] in ['6', '8'] and ('6' in tempList or '8' in tempList):
                    num_to_switch.append(key)
            elif num_list[key] != '0':
                safe_num_pos.append(key)
        for ns, s in zip(num_to_switch, safe_num_pos):
            num_list[s], num_list[ns] = num_list[ns], num_list[s]
            break
        if len(num_to_switch) != 0:
            num_list = self.re_arrange_number(num_list)
        return num_list

    def cloud_animation(self, cloud_animation):
        if self.go1_left:
            self.cloud1_pos_x -= 2
            if self.cloud1_pos_x < 20:
                self.go1_left = False
        else:
            self.cloud1_pos_x += 2
            if self.cloud1_pos_x > 80:
                self.go1_left = True
        if self.go2_left:
            self.cloud2_pos_x -= 3
            if self.cloud2_pos_x < 0:
                self.go2_left = False
        else:
            self.cloud2_pos_x += 3
            if self.cloud2_pos_x > 100:
                self.go2_left = True
        if self.go3_left:
            self.cloud3_pos_x += 1
            if self.cloud3_pos_x > 100:
                self.go3_left = False
        else:
            self.cloud3_pos_x -= 1
            if self.cloud3_pos_x < 0:
                self.go3_left = True
        for cc in cloud_animation:
            self.load_draw_img(f'cloud/cloud_1', (self.cloud1_pos_x + cc[0] + 100, cc[1] + 30), 0.1)
            self.load_draw_img(f'cloud/cloud_2', (self.cloud2_pos_x + cc[0] + 100, cc[1] + 40), 0.1)
            self.load_draw_img(f'cloud/cloud_3', (self.cloud3_pos_x + cc[0] + 100, cc[1] + 50), 0.1)

    def run(self):
        col1 = 481
        col2 = 557
        col3 = 634
        col4 = 710
        col5 = 787
        col6 = 862
        col7 = 940
        col8 = 1014
        col9 = 1090

        row1 = 174
        row2 = 307
        row3 = 439
        row4 = 572
        row5 = 704
        logo_list = ['blue', 'green', 'orange', 'red']
        res_list = ['forest', 'forest', 'forest', 'forest', 'wheat', 'wheat', 'wheat', 'wheat',
                    'desert', 'brick', 'brick', 'brick', 'sheep', 'sheep', 'sheep', 'sheep',
                    'ore', 'ore', 'ore']
        num_list = ['2', '3', '3', '4', '4', '5', '5', '6', '6', '8', '8', '9', '9', '10', '10', '11', '11', '12', '0']
        res_pos = [(col3, row1), (col5, row1), (col7, row1),
                   (col2, row2), (col4, row2), (col6, row2), (col8, row2),
                   (col1, row3), (col3, row3), (col5, row3), (col7, row3), (col9, row3),
                   (col2, row4), (col4, row4), (col6, row4), (col8, row4),
                   (col3, row5), (col5, row5), (col7, row5)]
        logo_pos = [(0, 0), (1500, 0), (0, 600), (1500, 600)]
        random.shuffle(res_list)
        random.shuffle(num_list)
        random.shuffle(logo_list)
        print(logo_list)
        des_pos = res_list.index('desert')
        zero_pos = num_list.index('0')
        # swapping position of 0 as per desert
        num_list[des_pos], num_list[zero_pos] = num_list[zero_pos], num_list[des_pos]
        num_list = self.re_arrange_number(num_list)

        cloud_animation = []
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill("cyan")
            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_w]:
            #     self.hex_pos.y -= 30 * self.dt
            # if keys[pygame.K_s]:
            #     self.hex_pos.y += 30 * self.dt
            # if keys[pygame.K_a]:
            #     self.hex_pos.x -= 30 * self.dt
            # if keys[pygame.K_d]:
            #     self.hex_pos.x += 30 * self.dt
            # self.draw_regular_polygon(self.screen, 'red', 6, 40, self.hex_pos)
            rtile_size = 0.55
            ltile_size = 0.2
            ntile_size = 0.2
            board_size = 1
            board_loc = (970, 550)
            # board_loc = (150, 80)
            port_loc = (135, 80)

            # board
            self.draw_regular_polygon(self.screen, 'white', 6, 420, board_loc)
            # self.load_draw_img('board/board', board_loc)
            # self.load_draw_img('trade/tradeport', port_loc, board_size)
            # self.load_draw_img('trade/port', port_loc, board_size * 2.456)

            # player and their pieces
            for l, lp in zip(logo_list, logo_pos):
                self.load_draw_img(f'logo/{l}', lp, ltile_size)

                self.load_draw_img(f'pieces/H_{l}', (lp[0], lp[1] + 50), ltile_size)
                # self.load_draw_img(f'pieces/H_{l}', (lp[0] + 50, lp[1] + 50), ltile_size)
                # self.load_draw_img(f'pieces/H_{l}', (lp[0] + 100, lp[1] + 50), ltile_size)
                # self.load_draw_img(f'pieces/H_{l}', (lp[0] + 150, lp[1] + 50), ltile_size)
                # self.load_draw_img(f'pieces/H_{l}', (lp[0] + 200, lp[1] + 50), ltile_size)

                self.load_draw_img(f'pieces/C_{l}', (lp[0], lp[1] + 100), ltile_size)
                # self.load_draw_img(f'pieces/C_{l}', (lp[0] + 50, lp[1] + 100), ltile_size)
                # self.load_draw_img(f'pieces/C_{l}', (lp[0] + 100, lp[1] + 100), ltile_size)
                # self.load_draw_img(f'pieces/C_{l}', (lp[0] + 150, lp[1] + 100), ltile_size)

                self.load_draw_img(f'pieces/R_{l}', (lp[0] + 20, lp[1] + 130), ltile_size, 90)
                # self.load_draw_img(f'pieces/R_{l}', (lp[0] + 40, lp[1] + 130), ltile_size, 90)
                # self.load_draw_img(f'pieces/R_{l}', (lp[0] + 60, lp[1] + 130), ltile_size, 90)
                # self.load_draw_img(f'pieces/R_{l}', (lp[0] + 80, lp[1] + 130), ltile_size, 90)
                # self.load_draw_img(f'pieces/R_{l}', (lp[0] + 100, lp[1] + 130), ltile_size, 90)
                # self.load_draw_img(f'pieces/R_{l}', (lp[0] + 120, lp[1] + 130), ltile_size, 90)
                # self.load_draw_img(f'pieces/R_{l}', (lp[0] + 140, lp[1] + 130), ltile_size, 90)
                # self.load_draw_img(f'pieces/R_{l}', (lp[0] + 160, lp[1] + 130), ltile_size, 90)
                # self.load_draw_img(f'pieces/R_{l}', (lp[0] + 20, lp[1] + 200), ltile_size, 90)
                # self.load_draw_img(f'pieces/R_{l}', (lp[0] + 40, lp[1] + 200), ltile_size, 90)
                # self.load_draw_img(f'pieces/R_{l}', (lp[0] + 60, lp[1] + 200), ltile_size, 90)
                # self.load_draw_img(f'pieces/R_{l}', (lp[0] + 80, lp[1] + 200), ltile_size, 90)
                # self.load_draw_img(f'pieces/R_{l}', (lp[0] + 100, lp[1] + 200), ltile_size, 90)
                # self.load_draw_img(f'pieces/R_{l}', (lp[0] + 120, lp[1] + 200), ltile_size, 90)
                # self.load_draw_img(f'pieces/R_{l}', (lp[0] + 140, lp[1] + 200), ltile_size, 90)

            for r, rp, n in zip(res_list, res_pos, num_list):
                self.load_draw_img(f'resource/{r}', rp, rtile_size)
                if r in ['sheep', 'ore', 'forest', 'desert']:
                    cloud_animation.append(rp)
                if r != 'desert':
                    self.load_draw_img(f'numbers/{n}', (rp[0] + 115, rp[1] + 70), ntile_size)
                else:
                    self.load_draw_img(f'pieces/robber', (rp[0] + 50, rp[1] + 35), ntile_size * 2)

            # self.cloud_animation(cloud_animation)

            pygame.display.update()
            self.clock.tick(60)
            self.dt = self.clock.tick(60) / 1000


if __name__ == "__main__":
    obj = myGame()
    obj.run()

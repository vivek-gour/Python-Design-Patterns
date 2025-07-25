import pygame
import sys
from math import sin, cos, pi
import random
from icecream import ic
import copy


class myGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake')
        self.screen = pygame.display.set_mode((900, 600))
        self.hex_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.clock = pygame.time.Clock()
        self.dt = 0

    def run(self):
        w = a = s = d = False
        speed = 100
        snake_len = 50
        tail = [copy.copy(self.hex_pos)]

        x = random.randint(0, 900)
        y = random.randint(0, 600)

        speed_timer = 0
        space_pressed = False
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill("black")
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] or w:
                w = True
                a = s = d = False
                self.hex_pos.y -= speed * self.dt
            if keys[pygame.K_s] or s:
                s = True
                a = w = d = False
                self.hex_pos.y += speed * self.dt
            if keys[pygame.K_a] or a:
                a = True
                w = s = d = False
                self.hex_pos.x -= speed * self.dt
            if keys[pygame.K_d] or d:
                d = True
                a = w = s = False
                self.hex_pos.x += speed * self.dt
            if keys[pygame.K_SPACE] and space_pressed is False:
                speed = 200
                space_pressed = True
            if speed_timer == 500:
                speed = 100
                space_pressed = False
                speed_timer = 0
            speed_timer += 1
            if self.hex_pos.x < 0: self.hex_pos.x = 900
            if self.hex_pos.x > 900: self.hex_pos.x = 0
            if self.hex_pos.y < 0: self.hex_pos.y = 600
            if self.hex_pos.y > 600: self.hex_pos.y = 0
            bug_rec = self.draw_regular_polygon(self.screen, 'red', 4, 10, (x, y))
            snake_rec = self.draw_regular_polygon(self.screen, 'red', 4, 10, self.hex_pos)
            for op in tail:
                if op:
                    self.draw_regular_polygon(self.screen, 'red', 4, 10, op)
            if self.hex_pos not in tail:
                tail.append((self.hex_pos[0], self.hex_pos[1]))
            if len(tail) > snake_len:
                tail = tail[-snake_len:]

            if snake_rec.colliderect(bug_rec):
                x = random.randint(0, 900)
                y = random.randint(0, 600)
                snake_len += 5
            pygame.display.update()
            self.clock.tick(60)
            self.dt = self.clock.tick(60) / 500

    def draw_regular_polygon(self, surface, color, vertex_count, radius, position, width=0):
        n, r = vertex_count, radius
        x, y = position
        # print([(x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n)) for i in range(n)])
        return pygame.draw.polygon(surface, color,
                                   [(x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n)) for i in range(n)],
                                   width)


if __name__ == "__main__":
    obj = myGame()
    obj.run()

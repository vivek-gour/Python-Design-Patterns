import pygame
import sys
from math import sin, cos, pi
import random
from icecream import ic
import copy


class myGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Car-Race')
        self.screen = pygame.display.set_mode((600, 900))
        self.car_pos = pygame.Vector2(250, 600)
        self.clock = pygame.time.Clock()
        self.dt = 0

    def load_draw_img(self, name, location, sizep=None, angle=None):
        img = pygame.image.load(f'images/{name}.png').convert_alpha()
        if sizep:
            img = pygame.transform.smoothscale(img, (img.get_width() * sizep, img.get_height() * sizep))
        if angle:
            img = pygame.transform.rotate(img, angle)
        return self.screen.blit(img, location)

    def run(self):
        speed_timer = 1
        space_pressed = False
        road = 0
        left = False
        road_turn = 0.5
        flame_on = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill("black")
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.car_pos.y -= 1
            if keys[pygame.K_s]:
                self.car_pos.y += 1
            if keys[pygame.K_a]:
                self.car_pos.x -= 1
            if keys[pygame.K_d]:
                self.car_pos.x += 1
            if keys[pygame.K_SPACE] and space_pressed is False:
                space_pressed = True
            if speed_timer == 500:
                space_pressed = False
                speed_timer = 0.5
            if road == 200:
                left = True
            if road == 0:
                left = False
            if left:
                road -= road_turn
            else:
                road += road_turn
            pygame.draw.line(self.screen, 'grey', (road + 100, 0), (200 - road, 900), 5)
            pygame.draw.line(self.screen, 'grey', (road + 300, 0), (400 - road, 900), 5)
            pygame.draw.rect(self.screen, 'red', (self.car_pos.x, self.car_pos.y, 50, 80))
            if flame_on:
                self.load_draw_img('flame', (100, 200), .03, 120)
                flame_on = False
            else:
                flame_on = True
                self.load_draw_img('flame', (100, 200), .02, 120)
            pygame.display.update()
            self.clock.tick(60)
            self.dt = self.clock.tick(60) / 1000


if __name__ == "__main__":
    obj = myGame()
    obj.run()

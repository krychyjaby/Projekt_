import pygame as pg

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 800
        self.y = 450


    def draw(self):
        pg.draw.circle(self.screen, (255, 0, 0), (self.x, self.y),   20)


    def move(self, keys):
        if keys[pg.K_a]:
            self.x -= 10
        if keys[pg.K_d]:
            self.x += 10

    def update(self):
        pg.display.update()
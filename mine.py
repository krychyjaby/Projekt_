import pygame as pg
from player import Player


class Game:
    def __init__(self): 
        pg.init()
        self.screen = pg.display.set_mode((800, 450))
        self.clock = pg.time.Clock()
        self.player = Player(self.screen) 

    def game(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            keys = pg.key.get_pressed()
            self.player.move(keys)
            self.draw() 
            self.update()
            self.clock.tick(0)

        pg.quit()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.player.draw()

    def update(self):
        pg.display.update()

game = Game()
game.game()
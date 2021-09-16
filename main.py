import pygame as pg
from models.base import *
from models.world import *


class Game:
    WIDTH, HEIGHT = 600, 600
    FPS = 60
    TILE = 60

    def __init__(self):
        pg.init()
        self.color = Color()
        self.map = Map()
        self.blocks = Blocks()
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pg.time.Clock()

    def render(self):
        """This function render all world."""
        for y, line in enumerate(self.map.map):
            for x, value in enumerate(line):
                if value == self.blocks.DIRT:
                    rect = (x * self.TILE, y * self.TILE, self.TILE, self.TILE)
                    pg.draw.rect(self.screen, self.color.BROWN, rect)

    def run(self):
        """Main cycle. It includes: render scene, loop update, update processes, controller."""
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            self.screen.fill(self.color.WHITE)

            self.render()

            pg.display.flip()
            self.clock.tick(self.FPS)
            #   show FPS
            pg.display.set_caption(str(self.clock.get_fps()))


if __name__ == '__main__':
    game = Game()
    game.run()

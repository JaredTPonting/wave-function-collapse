import sys
import random

import pygame
import pygame.draw
import yaml

from tile_class import Tile


def main():
    with open('source/tile_data/knots.yaml', 'r') as file:
        tile_set_data = yaml.safe_load(file)

    TILES = [Tile(img_path=f'source/Knots/{section}.png', data=tile_set_data[section], name=section) for section in
             tile_set_data]

    DIM = 600
    HEIGHT = DIM
    WIDTH = DIM

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    SCREEN_WIDTH = WIDTH
    SCREEN_HEIGHT = HEIGHT

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('wave-function-collapse')
    screen.fill(BLACK)

    TILES_PER_AXIS = 2

    GRID = [[len(TILES) for _ in range(TILES_PER_AXIS)] for __ in range(TILES_PER_AXIS)]

    def scale_image(img):
        return pygame.transform.scale(img, (SCREEN_WIDTH / TILES_PER_AXIS, SCREEN_WIDTH / TILES_PER_AXIS))

    def draw_grid(n):
        """
        draws grid on screen
        only works if SCREEN_WIDTH == SCREEN_HEIGHT = True

        :param n:
        :return:
        """
        block_width = SCREEN_WIDTH / n

        for x in range(n):
            for y in range(n):
                rect = pygame.Rect(x * block_width, y * block_width, block_width, block_width)
                pygame.draw.rect(screen, WHITE, rect, 1)

    def draw_tile_in_grid(x, y, tile):
        GRID[y][x] = tile.data
        screen.blit(scale_image(tile.image),
                    (SCREEN_WIDTH * x / TILES_PER_AXIS, SCREEN_WIDTH * y / TILES_PER_AXIS))

    def initiate_collapse():
        """
        Take random tile_plot and add a random tile
        :return:
        """
        first_tile = TILES[random.randint(0, len(TILES) - 1)]
        x = random.randint(0, TILES_PER_AXIS - 1)
        y = random.randint(0, TILES_PER_AXIS - 1)

        draw_tile_in_grid(x, y, first_tile)

    draw_grid(TILES_PER_AXIS)

    initiate_collapse()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


if __name__ == '__main__':
    main()

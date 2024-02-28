import sys

import pygame
import pygame.draw
import yaml

from tile_class import Tile


def main():
    with open('source/tile_data/knots.yaml', 'r') as file:
        tile_set_data = yaml.safe_load(file)

    TILES = [Tile(img_path=f'source/Knots/{section}.png', data=tile_set_data[section]) for section in tile_set_data]

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

    def draw_grid(n):
        block_size = n
        blocks_per_axis = n
        block_width = SCREEN_WIDTH / blocks_per_axis

        for x in range(n):
            for y in range(n):
                rect = pygame.Rect(x*block_width, y*block_width, block_width, block_width)
                pygame.draw.rect(screen, WHITE, rect, 1)

    while True:
        draw_grid(2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


if __name__ == '__main__':
    main()

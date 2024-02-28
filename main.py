import pygame
import yaml


def main():
    with open('source/tile_data/knots.yaml', 'r') as file:
        tile_set_data = yaml.safe_load(file)


    DIM = 600
    HEIGHT = DIM
    WIDTH = DIM

    SCREEN_WIDTH = WIDTH
    SCREEN_HEIGHT = HEIGHT

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('wave-function-collapse')

    run = True

    while run:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.display.flip()


if __name__ == '__main__':
    main()

import pygame


# Press the green button in the gutter to run the script.

def main():
    DIM = 600
    HEIGHT = DIM
    WIDTH = DIM

    SCREEN_WIDTH = WIDTH
    SCREEN_HEIGHT = HEIGHT

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('wave-function-colapse')

    run = True

    while run:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.display.flip()


if __name__ == '__main__':
    main()

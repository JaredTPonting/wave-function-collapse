import pygame


class Tile:
    def __init__(self, img_path, data):
        self.image = pygame.image.load(img_path)
        self.data = data

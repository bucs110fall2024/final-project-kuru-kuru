import pygame

class Projectile:
    def __init__(self, x, y):
        self.image = pygame.Surface((50,20))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        
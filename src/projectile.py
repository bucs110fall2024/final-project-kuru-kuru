import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, img_name):
        super().__init__()
        self.image = pygame.image.load(img_name).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10
            
    def update(self):
        pass
        
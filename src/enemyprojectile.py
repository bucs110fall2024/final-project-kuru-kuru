import pygame
import math

class EnemyProjectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Initializes enemy projectiles and its attributes

        Args:
            x (int): initial x pos
            y (int): initial y pos
            t (int): parametric variable to change projectile pos (Work in Progress)
        """
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load("assets/eprojectile.png").convert_alpha(), 2)
        self.rect = self.image.get_rect(center = (x,y))
        self.speed = 15
        
    def update(self):
        """Updates projectile pos and boundary collision
        """
        self.rect.center += pygame.math.Vector2((1/2, 0)) * self.speed
        if self.rect.left > 1024 or self.rect.right < 0 or self.rect.top > 1024 or self.rect.bottom < 0:
            self.kill()
import pygame
from enemyprojectile import EnemyProjectile

class Enemy:
    def __init__(self, x, y):
        """Initializes enemy and its attributes

        Args:
            x (int): initial x pos
            y (int): initial y pos
        """
        self.image = pygame.Surface((200,200))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (x,y))
        self.health = 100
        

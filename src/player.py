import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.health = 5
        self.speed = 5
        self.direction = pygame.math.Vector2()
        
    def movement(self):
        movement_key = pygame.key.get_pressed()
        if movement_key[pygame.K_d]:
            self.direction.x = 1
        elif movement_key[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if movement_key[pygame.K_s]:
            self.direction.y = 1
        elif movement_key[pygame.K_w]:
            self.direction.y = -1
        else:
            self.direction.y = 0
        
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.center += self.direction * self.speed
        

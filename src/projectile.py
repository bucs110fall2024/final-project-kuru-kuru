import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, img_name, mouse_pos):
        super().__init__()
        self.image = pygame.image.load(img_name).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10
        
        self.coord = (mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery)
        self.direction = pygame.math.Vector2(self.coord)
        self.direction = self.direction.normalize()
            
    def update(self):
        self.rect.center += self.direction * self.speed
        if self.rect.left > 1000 or self.rect.right < 0 or self.rect.top > 1000 or self.rect.bottom < 0:
            self.kill()
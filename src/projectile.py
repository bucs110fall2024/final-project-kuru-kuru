import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_pos):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load("assets/pprojectile.png").convert_alpha(), 2)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 20
        
        self.coord = (mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery)
        self.direction = pygame.math.Vector2(self.coord)
        self.direction = self.direction.normalize()
            
    def update(self, collide_group):
        self.rect.center += self.direction * self.speed
        if pygame.sprite.spritecollideany(self, collide_group):
            self.kill()
        if self.rect.left > 1000 or self.rect.right < 0 or self.rect.top > 1000 or self.rect.bottom < 0:
            self.kill()
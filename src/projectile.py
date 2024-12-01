import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_pos):
        """Initializes a projectile sprite and its attributes

        Args:
            x (int): initial x pos
            y (int): initial y pos
            mouse_pos (tuple): mouse pos as (x,y)
        """
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load("assets/pprojectile.png").convert_alpha(), 2)
        self.rect = self.image.get_rect(center = (x,y))
        self.speed = 20
        
        self.coord = (mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery)
        self.direction = pygame.math.Vector2(self.coord)
        self.direction = self.direction.normalize()
        
    def collision(self, collide_group):
        if pygame.sprite.spritecollideany(self, collide_group):
            if pygame.sprite.spritecollideany(self, collide_group, pygame.sprite.collide_mask): 
                self.kill()
            
    def update(self, collide_group):
        """Updates the projectile pos as well as checking collision

        Args:
            collide_group (sprite group)
        """
        self.rect.center += self.direction * self.speed
        self.collision(collide_group)
        if self.rect.left > 1024 or self.rect.right < 0 or self.rect.top > 1024 or self.rect.bottom < 0:
            self.kill()
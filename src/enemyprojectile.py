import pygame

class EnemyProjectile(pygame.sprite.Sprite):
    def __init__(self, x, y, speed = 8, scale = 1.5):
        """Initializes enemy projectiles and its attributes

        Args:
            x (int): initial x pos
            y (int): initial y pos
            speed (int)
            scale (float)
        """
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load("assets/game-sprites/enemyprojectile.png").convert_alpha(), scale)
        self.rect = self.image.get_rect(center = (x,y))
        
        self.speed = speed
        self.vector = pygame.math.Vector2()
        
    def update(self):
        """Updates projectile pos and boundary collision
        """
        self.rect.center += self.vector * self.speed
        if self.rect.left > 1024 or self.rect.right < 0 or self.rect.top > 1024 or self.rect.bottom < 0:
            self.kill()
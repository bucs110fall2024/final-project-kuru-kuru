import pygame

class Placeables(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_pos):
        super().__init__()
        self.image_list = ["assets/rock1.png", "assets/rock2.png", "assets/rock3.png"]
        self.image = pygame.image.load(self.image_list[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.durability = 3
        
        self.coord = (mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery)
        self.direction = pygame.math.Vector2(self.coord)
        self.direction = self.direction.normalize()
        
        self.rect.center += self.direction * 100
        
    def update(self, collide_group):
        if pygame.sprite.spritecollide(self, collide_group, True):
            self.durability -= 1
            if self.durability == 2:
                self.image = pygame.image.load(self.image_list[1]).convert_alpha()
            elif self.durability == 1:
                self.image = pygame.image.load(self.image_list[2]).convert_alpha()
            else:
                self.kill()
        
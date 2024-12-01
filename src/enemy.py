import pygame
import random
#from enemyprojectile import EnemyProjectile

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Initializes enemy and its attributes

        Args:
            x (int): initial x pos
            y (int): initial y pos
        """
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load("assets/slime.png").convert_alpha(), 2)
        self.rect = self.image.get_rect(center = (x,y))
        
        self.health = 100
        self.speed = 10
        self.moving = False
        self.move_timer = 0
        
    def movement(self):
        self.move_timer += 1
        if self.move_timer == 300:
            self.moving = True
            self.next_pos_x, self.next_pos_y = random.randint(100, 900), random.randint(100, 900)
            self.direction_vector = pygame.math.Vector2(self.next_pos_x - self.rect.centerx, self.next_pos_y - self.rect.centery)
            self.direction_vector = self.direction_vector.normalize()
        if self.moving:
            self.rect.centerx += int(self.direction_vector.x * self.speed)
            self.rect.centery += int(self.direction_vector.y * self.speed)
            if 0 <= abs(self.next_pos_x - self.rect.centerx) <= 10 or 0 <= abs(self.next_pos_y - self.rect.centery) <= 10:
                self.moving = False
                self.move_timer = 0
            
    def collision(self, collide_group):
        if pygame.sprite.spritecollideany(self, collide_group):
            if pygame.sprite.spritecollide(self, collide_group, True, pygame.sprite.collide_mask):
                self.health -= 1
                
    def facing_player(self, player):
        if self.rect.centerx > player.rect.centerx:
            self.image =  pygame.transform.flip(pygame.transform.scale_by(pygame.image.load("assets/slime.png").convert_alpha(), 2), True, False)
        if self.rect.centerx < player.rect.centerx:
            self.image = pygame.transform.scale_by(pygame.image.load("assets/slime.png").convert_alpha(), 2)
            
    def update(self, player, collide_group):
        self.facing_player(player)
        self.movement()
        self.collision(collide_group)
        if self.health == 0:
            self.kill()
        

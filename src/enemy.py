import pygame
import random
from src.spawner import Spawner

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Initializes enemy and its attributes

        Args:
            x (int): initial x pos
            y (int): initial y pos
        """
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load("assets/game-sprites/slime.png").convert_alpha(), 2)
        self.rect = self.image.get_rect(center = (x,y))
        
        self.health = 100
        self.speed = 10
        self.moving = False
        self.move_timer = 0
        
        self.main_spawner = Spawner(self.rect.centerx, self.rect.centery, 25, 4, 0.1)
        self.spawner2 = Spawner(200, 300, 25, 2, 0.1)
        self.spawner3 = Spawner(700, 650, 15, 1, 0.1)
        
    def movement(self):
        """Defines enemy movement from current pos to a random pos
        """
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
                
    def attack(self, projectile_group):
        """Defines enemy attack patterns

        Args:
            projectile_group (sprite group)
        """
        self.main_spawner.rect.x = self.rect.centerx
        self.main_spawner.rect.y = self.rect.centery
        self.main_spawner.shoot(projectile_group, 10)
        if 50 < self.health <= 75:
            self.main_spawner.rotation = 25
            self.main_spawner.spawn_count = 6
        if 25 < self.health <= 50:
            self.main_spawner.rotation = 35
            self.main_spawner.spawn_count = 3
            self.spawner2.shoot(projectile_group, 10)
        if self.health <= 25:
            self.main_spawner.rotation = 50
            self.main_spawner.spawn_count = 5
            self.spawner2.shoot(projectile_group, 5)
            self.spawner3.shoot(projectile_group, 10)
            
    def collision(self, collision_group):
        """Checks enemy collision with player projectiles

        Args:
            collision_group (sprite group)
        """
        if pygame.sprite.spritecollideany(self, collision_group):
            if pygame.sprite.spritecollide(self, collision_group, True, pygame.sprite.collide_mask):
                self.health -= 1
                
    def facing_player(self, player):
        """Adjusting where enemy is facing depending on where the player is

        Args:
            player (pygame sprite (rect))
        """
        if self.rect.centerx > player.rect.centerx:
            self.image =  pygame.transform.flip(pygame.transform.scale_by(pygame.image.load("assets/game-sprites/slime.png").convert_alpha(), 2), True, False)
        if self.rect.centerx < player.rect.centerx:
            self.image = pygame.transform.scale_by(pygame.image.load("assets/game-sprites/slime.png").convert_alpha(), 2)
            
    def update(self, player, collision_group, projectile_group):
        """Updates the enemy by calling its movement, collision, and facing methods

        Args:
            player (pygame sprite (rect))
            collision_group (sprite group)
        """
        self.facing_player(player)
        self.movement()
        self.attack(projectile_group)
        self.collision(collision_group)
        if self.health == 0:
            self.kill()
        

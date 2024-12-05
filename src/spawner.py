import pygame
from src.enemyprojectile import EnemyProjectile

class Spawner:
    def __init__(self, x, y, rotation, spawn_count, fire_rate):
        """Creates a spawner and its attributes

        Args:
            x (int): x pos of spawner
            y (int): y pos of spawner
            rotation (int): how much the spawner is rotated
            spawn_count (int): amount of projectiles spawned each iteration
            fire_rate (int): how fast the spawner spawn projectiles
        """
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.rect.x = x
        self.rect.y = y
        self.rotation = rotation
        self.spawn_count = spawn_count
        self.fire_rate = fire_rate
        self.vector = pygame.math.Vector2((0,1))
        self.timer = 0
        
    def create(self, projectile_group, speed, scale):
        """Creates the projectiles through iteration and rotation

        Args:
            projectile_group (sprite group)
            speed (int): speed of projectiles
            scale (float)
        """
        self.vector = self.vector.rotate(self.rotation)
        for i in range(self.spawn_count):
            self.projectile = EnemyProjectile(self.rect.x, self.rect.y, speed, scale)
            self.projectile.vector = self.vector.rotate(360/self.spawn_count * i)
            projectile_group.add(self.projectile)
            
    def shoot(self, projectile_group, speed, scale):
        """Shoots the created projectiles

        Args:
            projectile_group (sprite group)
            speed (int): speed of projectiles
            scale (float)
        """
        self.timer += 1
        if self.timer >= (self.fire_rate * 60):
            self.create(projectile_group, speed, scale)
            projectile_group.update()
            self.timer = 0
            
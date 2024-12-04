import pygame
from src.enemyprojectile import EnemyProjectile

class Spawner:
    def __init__(self, rotation, spawn_count):
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.rotation = rotation
        self.spawn_count = spawn_count
        self.vector = pygame.math.Vector2((1,0))
        
        self.timer = 0
        self.fire_rate = 0.3
        
    def ready(self, projectile_group):
        self.vector = self.vector.rotate(self.rotation)
        for i in range(self.spawn_count):
            self.projectile = EnemyProjectile(self.rect.x, self.rect.y, 15)
            self.projectile.vector = self.vector.rotate(360/self.spawn_count * i)
            projectile_group.add(self.projectile)
            
    def shoot(self, projectile_group, x, y):
        self.rect.x = x
        self.rect.y = y
        self.timer += 1
        if self.timer == (self.fire_rate * 60):
            self.ready(projectile_group)
            projectile_group.update()
            self.timer = 0
            
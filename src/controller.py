import pygame
from src.player import Player
from src.projectile import Projectile

class Controller:
    def __init__(self, screen_width, screen_height, fps):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fps = fps
        self.running = True
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        
        self.player = Player(100,100)
        self.player_bullets = []
        
    def mainloop(self):
        self.gameloop()
        
    def menuloop(self):
        pass
    
    def gameloop(self):
        pygame.display.set_caption("Game")
        
        while self.running:
            self.clock.tick(self.fps)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = Projectile(self.player.rect.x, self.player.rect.centery - 10)
                        self.player_bullets.append(bullet)
                        
            self.screen.fill((176,219,255))
            self.player.update(self.screen)
            
            for bullet in self.player_bullets:
                self.screen.blit(bullet.image, bullet.rect)
                bullet.rect.x += bullet.speed
                
            pygame.display.flip()
        pygame.quit()
        
    def gameoverloop(self):
        pass
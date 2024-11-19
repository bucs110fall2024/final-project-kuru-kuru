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
        self.player_projectiles = pygame.sprite.Group()
        
    def mainloop(self):
        self.gameloop()
        
    def menuloop(self):
        pass
    
    def gameloop(self):
        pygame.display.set_caption("Game")
        
        while self.running:
            self.clock.tick(self.fps)
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        projectile = Projectile(self.player.rect.centerx, self.player.rect.centery, "assets/pprojectile.png")
                        self.player_projectiles.add(projectile)
                        
            self.screen.fill((176,219,255))
            self.player.update(self.screen)
            
            for projectile in self.player_projectiles:
                projectile.rect.x += projectile.speed
            self.player_projectiles.draw(self.screen)
            
            pygame.display.flip()
        pygame.quit()
        
    def gameoverloop(self):
        pass
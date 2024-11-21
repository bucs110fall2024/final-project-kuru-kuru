import pygame
from src.player import Player
from src.projectile import Projectile
from src.placeables import Placeables
from src.enemyprojectile import EnemyProjectile

class Controller:
    def __init__(self, screen_width, screen_height, fps):
        """Initializes many game elements such as the screen, fps, and sprite groups, etc.

        Args:
            screen_width (int)
            screen_height (int)
            fps (int)
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fps = fps
        self.running = True
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        self.player = Player(100,100)
        self.player_projectiles = pygame.sprite.Group()
        self.player_placeables = pygame.sprite.Group()
        self.enemy_projectiles = pygame.sprite.Group()
        
    def mainloop(self):
        """Runs the different loops of the program depending on game state
        """
        self.gameloop()
        
    def menuloop(self):
        """Runs the menuloop at program startup
        """
        pass      
    
    def gameloop(self):
        """Runs the gameloop and handles gameplay elements and events
        """
        pygame.display.set_caption("Game")
        
        while self.running:
            self.clock.tick(self.fps)
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        projectile = Projectile(self.player.rect.centerx, self.player.rect.centery, mouse_pos)
                        self.player_projectiles.add(projectile)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        placeable = Placeables(self.player.rect.centerx, self.player.rect.centery, mouse_pos)
                        self.player_placeables.add(placeable)
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_q:
                        for i in range(10):
                            eprojectile = EnemyProjectile(500 - i*25, 500 - i*50, 5)
                            self.enemy_projectiles.add(eprojectile)
                        
            self.screen.fill((176,219,255))
            
            
            self.player.update(self.screen)
            self.player_projectiles.update(self.player_placeables)
            self.player_placeables.update(self.enemy_projectiles)
            self.enemy_projectiles.update()
            
            
            self.player_projectiles.draw(self.screen)
            self.player_placeables.draw(self.screen)
            self.enemy_projectiles.draw(self.screen)
            
            
        
            pygame.display.flip()
        pygame.quit()
        
    def gamepauseloop(self):
        """Runs the game pause loop when player pauses the game
        """
        pass
        
    def gameoverloop(self):
        """Runs the game over loop when player dies
        """
        pass
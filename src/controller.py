import pygame
from src.player import Player
from src.projectile import Projectile
from src.placeables import Placeables
from src.enemyprojectile import EnemyProjectile
from src.tilemap import Tilemap

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
        self.font = pygame.font.SysFont("Arial", 50)
        self.running = True
        self.game_state = "Menu"
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill((176,219,255))
        
        self.tilemap = Tilemap()
        self.player = Player(100,100)
        self.player_group = pygame.sprite.Group()
        self.player_projectiles = pygame.sprite.Group()
        self.player_placeables = pygame.sprite.Group()
        self.enemy_projectiles = pygame.sprite.Group()
        
        self.placeables_cooldown = 3600
        
    def mainloop(self):
        """Runs the different loops of the program depending on game state
        """
        self.gameloop()
        
        
    def menuloop(self):
        """Runs the menuloop at program startup
        """
        # pygame.display.set_caption("Main Menu")
        
        # while self.game_state == "Menu":
        #     self.clock.tick(self.fps)
        #     mouse_pos = pygame.mouse.get_pos()
            
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             self.running = False
        #             pygame.quit()
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             if event.button == 1:
        #                 if game.collidepoint(mouse_pos): 
        #                     self.gameloop()
                        
        #     game = pygame.draw.rect(self.screen, (0,0,0), (1024/2 - 150, 200, 300, 100), 1)
            
        #     pygame.display.flip()
        # pygame.quit()
    
    def gamepauseloop(self):
        """Runs the game pause loop when player pauses the game
        """
        # pygame.display.set_caption("Game Paused")
        
        # while self.game_state == "Paused":
        #     pygame.draw.rect(self.screen, (0,0,0), (1024/2 - 150, 200, 300, 300), 1)
        #     pygame.display.flip()
    
    def gameloop(self):
        """Runs the gameloop and handles gameplay elements and events
        """
        pygame.display.set_caption("Game")
        
        while self.running:
            self.clock.tick(self.fps)
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        projectile = Projectile(self.player.rect.centerx, self.player.rect.centery, mouse_pos)
                        self.player_projectiles.add(projectile)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.placeables_cooldown >= 3600:
                        placeable = Placeables(self.player.rect.centerx, self.player.rect.centery, mouse_pos)
                        self.player_placeables.add(placeable)
                        self.placeables_cooldown = 0
                    if event.key == pygame.K_q:
                        for i in range(10):
                            eprojectile = EnemyProjectile(500 - i*25, 500 - i*50, 5)
                            self.enemy_projectiles.add(eprojectile)
                        
            self.player_group.add(self.player)
            
            self.tilemap.update(self.screen)
            self.player_group.update(mouse_pos, self.player_placeables, self.enemy_projectiles)
            self.player_projectiles.update(self.player_placeables)
            self.player_placeables.update(self.enemy_projectiles)
            self.enemy_projectiles.update()
            
            self.player_projectiles.draw(self.screen)
            self.player_placeables.draw(self.screen)
            self.enemy_projectiles.draw(self.screen)
            self.player_group.draw(self.screen)
        
            self.placeables_cooldown += 1
            print(self.placeables_cooldown)
            pygame.display.flip()
        pygame.quit()
        
    def gameoverloop(self):
        """Runs the game over loop when player dies
        """
        pass
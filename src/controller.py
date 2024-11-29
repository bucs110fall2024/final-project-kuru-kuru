import pygame
import sys
from src.player import Player
from src.projectile import Projectile
from src.placeables import Placeables
from src.enemyprojectile import EnemyProjectile
from src.tilemap import Tilemap
from src.button import Button

class Controller:
    def __init__(self):
        """Initializes many game elements such as the screen, fps, and sprite groups, etc.

        Args:
            screen_width (int)
            screen_height (int)
            fps (int)
        """
        self.screen_width = 1024
        self.screen_height = 1024
        self.fps = 60
        self.font = pygame.font.SysFont("Arial", 50)
        self.game_state = "Menu"
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        self.play_button = Button(self.screen_width/2 - 150, 300, "assets/playbutton.png")
        self.quit_button = Button(self.screen_width/2 - 150, 500, "assets/quitbutton.png")
        self.menu_button = Button(self.screen_width/2 - 150, 500, "assets/menubutton.png")
        self.continue_button = Button(self.screen_width/2 - 150, 300, "assets/continuebutton.png")
        self.retry_button = Button(self.screen_width/2 - 150, 300, "assets/retrybutton.png")
        
        
        self.tilemap = Tilemap()
        self.player = Player(200,200)
        
        self.player_group = pygame.sprite.GroupSingle(self.player)
        self.player_projectiles = pygame.sprite.Group()
        self.player_placeables = pygame.sprite.Group()
        self.enemy_projectiles = pygame.sprite.Group()
        
        self.placeables_cooldown = 3600
        
    def mainloop(self):
        """Runs the different loops of the program depending on game state
        """
        while True:
            if self.game_state == "Menu":
                self.menuloop()
            elif self.game_state == "Paused":
                self.gamepauseloop()
            elif self.game_state == "Game":
                self.gameloop()
            elif self.game_state == "Over":
                self.gameoverloop()
        
    def menuloop(self):
        """Runs the menuloop at program startup
        """
        pygame.display.set_caption("Main Menu")
        
        while self.game_state == "Menu":
            self.clock.tick(self.fps)
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.play_button.rect.collidepoint(mouse_pos):
                            self.game_state = "Game"
                            if self.player.health <= 0:
                                self.player = Player(500,500)
                                self.player_group.add(self.player)
                        if self.quit_button.rect.collidepoint(mouse_pos):
                            pygame.quit()
                            sys.exit()
                            
            self.screen.fill((176,219,255))
            
            self.play_button.draw(self.screen)
            self.quit_button.draw(self.screen)
            
            pygame.display.flip()
        
    
    def gamepauseloop(self):
        """Runs the game pause loop when player pauses the game
        """
        pygame.display.set_caption("Game Paused")
        
        while self.game_state == "Paused":
            self.clock.tick(self.fps)
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.continue_button.rect.collidepoint(mouse_pos): 
                            self.game_state = "Game"
                        if self.menu_button.rect.collidepoint(mouse_pos):
                            self.game_state = "Menu"
                            
            self.screen.fill((126,169,205))
            
            self.continue_button.draw(self.screen)
            self.menu_button.draw(self.screen)
            
            pygame.display.flip()
    
    def gameloop(self):
        """Runs the gameloop and handles gameplay elements and events
        """
        pygame.display.set_caption("Game")
        
        while self.game_state == "Game" and self.player.health > 0:
            self.clock.tick(self.fps)
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        projectile = Projectile(self.player.rect.centerx, self.player.rect.centery, mouse_pos)
                        self.player_projectiles.add(projectile)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: #and self.placeables_cooldown >= 3600:
                        placeable = Placeables(self.player.rect.centerx, self.player.rect.centery, mouse_pos)
                        self.player_placeables.add(placeable)
                        self.placeables_cooldown = 0
                    if event.key == pygame.K_q:
                        for i in range(10):
                            eprojectile = EnemyProjectile(500 - i*25, 500 - i*50, 5)
                            self.enemy_projectiles.add(eprojectile)
                    if event.key == pygame.K_ESCAPE:
                        self.game_state = "Paused"
            
            self.screen.fill((255,255,255))
            
            self.tilemap.update(self.screen)
            self.player_group.update(mouse_pos, self.player_placeables, self.enemy_projectiles)
            self.player_projectiles.update(self.player_placeables)
            self.player_placeables.update(self.enemy_projectiles)
            self.enemy_projectiles.update()
            
            self.player_projectiles.draw(self.screen)
            self.player_placeables.draw(self.screen)
            self.enemy_projectiles.draw(self.screen)
            self.player_group.draw(self.screen)

            #self.placeables_cooldown += 1
            #print(self.placeables_cooldown)
            pygame.display.flip()
        if self.player.health <= 0:
            self.game_state = "Over"
        
    def gameoverloop(self):
        """Runs the game over loop when player dies
        """
        pygame.display.set_caption("Game Over")
        
        while self.game_state == "Over":
            self.clock.tick(self.fps)
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.retry_button.rect.collidepoint(mouse_pos):
                            self.player = Player(800,800)
                            self.player_group.add(self.player)
                            self.game_state = "Game"
                        if self.menu_button.rect.collidepoint(mouse_pos):
                            self.game_state = "Menu"
                    
            self.screen.fill((56,119,155))
            
            self.retry_button.draw(self.screen)
            self.menu_button.draw(self.screen)
            
            pygame.display.flip()
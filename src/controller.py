import pygame
import sys
import json
from src.player import Player
from src.projectile import Projectile
from src.placeables import Placeables
from src.enemy import Enemy
from src.tilemap import Tilemap
from src.button import Button

class Controller:
    def __init__(self):
        """Initializes many game elements such as the screen, fps, and sprite groups, etc.
        """
        self.screen_width = 1024
        self.screen_height = 1024
        self.fps = 60
        self.menu_font = pygame.font.SysFont("Arial", 75)
        self.game_font = pygame.font.SysFont("Arial", 25)
        self.game_state = "Menu"
        self.error = False
        #self.game_begin = False
        #self.start_timer = 180
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        self.play_button = Button(self.screen_width/2, 325, "assets/buttons/playbutton.png", 1)
        self.quit_button = Button(self.screen_width/2, 575, "assets/buttons/quitbutton.png", 1)
        self.menu_button = Button(self.screen_width/2, 575, "assets/buttons/menubutton.png", 1)
        self.continue_button = Button(self.screen_width/2, 325, "assets/buttons/continuebutton.png", 1)
        self.retry_button = Button(self.screen_width/2, 450, "assets/buttons/retrybutton.png", 1)
        self.new_game_button = Button(self.screen_width/2, 450, "assets/buttons/newgamebutton.png", 1)
        
        self.tilemap = Tilemap()
        self.enemy = Enemy(900, 512, 2)
        
        self.player_group = pygame.sprite.GroupSingle()
        self.player_projectiles = pygame.sprite.Group()
        self.player_placeables = pygame.sprite.Group()
        self.enemy_projectiles = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.GroupSingle(self.enemy)
        
        self.current_deathcount = 0
        
        self.gun_icon = Button(self.screen_width/2 - 50, 1000, "assets/misc/gun.png", 2)
        self.block_icon = Button(self.screen_width/2, 1000, "assets/misc/block.png", 2)
        self.potion_icon = Button(self.screen_width/2 + 50, 1000, "assets/misc/potion.png", 2)
        
        self.can_shoot = True
        self.can_place = True
        self.can_heal = True
        
        self.shoot_timer = 0
        self.place_timer = 0
        self.heal_timer = 0
        
    def create_text(self, font_type, text_msg, pos, text_color, text_bg_color = None):
        """Creates text on the screen based on the given parameters

        Args:
            text_msg (str)
            text_color (tuple)
            text_bg_color (tuple)
            pos (tuple)
        """
        if font_type == "Main":
            text = self.menu_font.render(text_msg, True, text_color, text_bg_color)
            text_rect = text.get_rect(center = pos)
            self.screen.blit(text, text_rect)
        if font_type == "Game":
            text = self.game_font.render(text_msg, True, text_color, text_bg_color)
            text_rect = text.get_rect(center = pos)
            self.screen.blit(text, text_rect)
            
    def begin_game(self):
        self.game_begin = False
        self.start_timer = 180
        
    def reset(self):
        """Resets game elements
        """
        self.player = Player(200, 512)
        self.player_group.add(self.player)
        self.enemy = Enemy(900, 512, 2)
        self.enemy_group.add(self.enemy)
        self.player_projectiles.empty()
        self.player_placeables.empty()
        self.enemy_projectiles.empty()
        self.can_place = True
        self.can_heal = True
        self.place_timer = 0
        self.heal_timer = 0
        
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
                        if self.new_game_button.rect.collidepoint(mouse_pos) and not self.error:
                            file = open("src/deathcount.json")
                            deathcount_info = json.load(file)
                            file.close()
                            deathcount_info["deathcount"]["previous_player"] = deathcount_info["deathcount"]["current_player"]
                            deathcount_info["deathcount"]["current_player"] = 0
                            file = open("src/deathcount.json", "w")
                            json.dump(deathcount_info, file)
                            file.close()
                            
                            self.reset()
                            self.begin_game()
                            self.game_state = "Game"
                        if self.quit_button.rect.collidepoint(mouse_pos) and not self.error:
                            pygame.quit()
                            sys.exit()
                            
                        self.error = False
                        if self.play_button.rect.collidepoint(mouse_pos) and not self.error: 
                            if getattr(self, "player", None):
                                if self.player.health == 0 or self.enemy.health == 0:
                                    self.reset()
                                self.begin_game()
                                self.game_state = "Game"
                            else:
                                self.error = True
                        
            self.screen.fill((176,219,255))
            
            self.play_button.draw(self.screen)
            self.new_game_button.draw(self.screen)
            self.quit_button.draw(self.screen)
            
            self.create_text("Main", "Main Menu", (512, 100), (0,0,0))
            if self.error:
                self.create_text("Main", "No Player Data, Click New Game", (512, 300), (255,255,255), (0,0,0))
                self.create_text("Main", "Click anywhere to close message", (512, 380), (255,255,255), (0,0,0))
                    
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
                            self.begin_game()
                            self.game_state = "Game"
                        if self.retry_button.rect.collidepoint(mouse_pos):
                            self.begin_game()
                            self.reset()
                            self.game_state = "Game"
                        if self.menu_button.rect.collidepoint(mouse_pos):
                            self.game_state = "Menu"
                            
            self.screen.fill((126,169,205))
            
            self.continue_button.draw(self.screen)
            self.retry_button.draw(self.screen)
            self.menu_button.draw(self.screen)
            
            self.create_text("Main", "Game Paused", (512, 100), (0,0,0))
            
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.can_place and self.game_begin:
                        placeable = Placeables(self.player.rect.centerx, self.player.rect.centery, mouse_pos, 1.5)
                        self.player_placeables.add(placeable)
                        self.can_place = False
                        self.place_timer = 0
                    if event.key == pygame.K_e and self.can_heal and self.game_begin:
                        self.player.health += 2
                        if self.player.health > 5:
                            self.player.health = 5
                        self.can_heal = False
                        self.heal_timer = 0
                    if event.key == pygame.K_ESCAPE:
                        self.game_state = "Paused"
                        
            if pygame.mouse.get_pressed()[0] and self.can_shoot and self.game_begin:
                    projectile = Projectile(self.player.rect.centerx, self.player.rect.centery, mouse_pos, 1.5)
                    self.player_projectiles.add(projectile)
                    self.can_shoot = False
                    self.shoot_timer = 0
                    
            self.screen.fill((255,255,255))
            self.tilemap.draw(self.screen)
            
            if not self.game_begin:
                self.create_text("Main", f"{-(-self.start_timer//60)}", (512, 512), (255,255,255))
                self.start_timer -= 1
                if self.start_timer == 0:
                    self.game_begin = True
        
            if self.game_begin:
                self.player_group.update(mouse_pos, self.player_placeables, self.enemy_projectiles, self.enemy_group)
                self.player_placeables.update(self.enemy_projectiles)
                self.player_projectiles.update()
                self.enemy_projectiles.update()
                self.enemy_group.update(self.player, self.player_projectiles, self.enemy_projectiles)
            
            self.player_placeables.draw(self.screen)
            self.player_projectiles.draw(self.screen)
            self.enemy_projectiles.draw(self.screen)
            self.player_group.draw(self.screen)
            self.enemy_group.draw(self.screen)
            
            self.gun_icon.draw(self.screen)
            self.block_icon.draw(self.screen)
            self.potion_icon.draw(self.screen)
        
            health_bar = pygame.rect.Rect(362, 800, 3 * self.enemy.health, 30)
            pygame.draw.rect(self.screen, (255,0,0), health_bar)
            
            self.create_text("Game", f"Boss Health: {self.enemy.health}", (512, 815), (255,255,255))
            self.create_text("Game", f"Player Health: {self.player.health}", (100, 50), (0,0,0))
            
            if not self.can_place:
                self.create_text("Game", f"{round(((60 - self.place_timer)/60), 1)}s", (self.block_icon.rect.center), (255,255,255))
            if not self.can_heal:
                self.create_text("Game", f"{round(((600 - self.heal_timer)/60), 1)}s", (self.potion_icon.rect.center), (255,255,255))
            
            if self.enemy.health == 0:
                self.create_text("Main", "You Win!", (512, 512), (0,0,0), (255,255,255))
                self.enemy_projectiles.empty()
            
            if not self.can_shoot:
                self.shoot_timer += 1
                if self.shoot_timer == 30:
                    self.can_shoot = True
            if not self.can_place:
                self.place_timer += 1
                if self.place_timer == 60:
                    self.can_place = True
            if not self.can_heal:
                self.heal_timer += 1
                if self.heal_timer == 600:
                    self.can_heal = True
                    
            pygame.display.flip()
            
        if self.player.health == 0:
            file = open("src/deathcount.json")
            deathcount_info = json.load(file)
            file.close()
            deathcount_info["deathcount"]["current_player"] += 1
            self.current_deathcount = deathcount_info["deathcount"]["current_player"]
            file = open("src/deathcount.json", "w")
            json.dump(deathcount_info, file)
            file.close()
            
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
                            self.reset()
                            self.begin_game()
                            self.game_state = "Game"
                        if self.menu_button.rect.collidepoint(mouse_pos):
                            self.game_state = "Menu"
                    
            self.screen.fill((56,119,155))
            
            self.retry_button.draw(self.screen)
            self.menu_button.draw(self.screen)
            
            self.create_text("Main", "Game Over", (512, 100), (0,0,0))
            self.create_text("Main", f"Death Count: {self.current_deathcount}", (512, 800), (0,0,0))
            
            pygame.display.flip()
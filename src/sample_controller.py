import pygame
from src.player import Player
from src.projectile import Projectile

class Controller:
  def __init__(self, screen_width, screen_height, fps):
    self.screen_width = screen_width
    self.screen_height = screen_height
    self.fps = fps
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    
    #setup pygame data
  
  def mainloop(self):
      self.gameloop()
    #select state loop
    
  
  ### below are some sample loop states ###
  

  def menuloop(self):
    pass
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    pygame.display.set_caption("Game")
    
    player = Player(100,100)
    bullets = []
    
    running = True
    while running:
      self.clock.tick(self.fps)
      
      mouse_pos = pygame.mouse.get_pos()
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            bullet = Projectile(player.rect.x, player.rect.centery - 10)
            bullets.append(bullet)
            
      self.screen.fill((176, 219, 255))
      player.update(self.screen)
      for bullet in bullets:
              self.screen.blit(bullet.image, bullet.rect)
              bullet.rect.x += bullet.speed
              if bullet.rect.x > 1000:
                bullets.remove(bullet)
      
      
      pygame.display.flip()
    pygame.quit()
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
    pass
      #event loop

      #update data

      #redraw

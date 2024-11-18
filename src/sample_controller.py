import pygame
from src.player import Player

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
    
    player = Player()
    
    running = True
    while running:
      self.clock.tick(self.fps)
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          
      self.screen.fill((176, 219, 255))
      pygame.draw.rect(self.screen, (200,255,200), player)
      
      player.movement()
      
      
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

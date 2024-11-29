import pygame

class Button:
    def __init__(self, x, y, img_name):
        self.image = pygame.image.load(img_name)
        self.rect = self.image.get_rect(topleft = (x,y))
        #self.x = x
        #self.y = y
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
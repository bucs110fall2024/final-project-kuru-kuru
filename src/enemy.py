import pygame

class Enemy:
    def __init__(self, x, y):
        """Initializes enemy and its attributes

        Args:
            x (int): initial x pos
            y (int): initial y pos
        """
        #self.image = pygame.image.load().convert_alpha( need to make sprite )
        self.x = x
        self.y = y
        self.health = 100
        
    def movement(self):
        """Moves to invisible flags on the screen for its movement
        """
    
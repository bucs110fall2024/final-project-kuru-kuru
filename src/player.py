import pygame

class Player:
    def __init__(self, x, y):
        """Initializes the player character and their attributes

        Args:
            x (int): sets the player's initial x pos 
            y (int): sets the player's initial y pos
        """
        #self.image = pygame.image.load().convert_alpha( need to make sprite )
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.health = 5
        self.speed = 5
        self.direction = pygame.math.Vector2()
        
    def movement(self):
        """Defines player movement using WASD. Uses normalized vectors so player moves at constant speed in all directions
        """
        movement_key = pygame.key.get_pressed()
        if movement_key[pygame.K_d]:
            self.direction.x = 1
        elif movement_key[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if movement_key[pygame.K_s]:
            self.direction.y = 1
        elif movement_key[pygame.K_w]:
            self.direction.y = -1
        else:
            self.direction.y = 0
        
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.center += self.direction * self.speed
    
    def update(self, screen):
        """Updates the player by drawing the player character and well as calling its movement method

        Args:
            screen (pygame surface)
        """
        pygame.draw.rect(screen, (200,255,200), self)
        self.movement()
        

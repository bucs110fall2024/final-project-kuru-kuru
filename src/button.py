import pygame

class Button:
    def __init__(self, x, y, img_name, scale):
        """Creates a button with its img, and its center at x, y

        Args:
            x (int)
            y (int)
            img_name (str)
        """
        self.image = pygame.transform.scale_by(pygame.image.load(img_name).convert_alpha(), scale)
        self.rect = self.image.get_rect(center = (x,y))
        
    def draw(self, screen):
        """Draws the button onto the screen

        Args:
            screen (pygame surface)
        """
        screen.blit(self.image, self.rect)
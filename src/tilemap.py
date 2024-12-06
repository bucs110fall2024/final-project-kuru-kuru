import pygame

class Tilemap:
    def __init__(self):
        """Creates a tilemap for the game using a grid system that is 16x16 with each tile being 64 pixels
        """
        self.grass_tile = pygame.image.load("assets/misc/grass.png")
        self.dirt_tile = pygame.image.load("assets/misc/dirt.png")
        self.tile_size = 64
        self.tile_map = [
            ["g", "g", "d", "d", "g", "g", "g", "g", "g", "g", "g", "g", "d", "d", "g", "g",],
            ["g", "g", "g", "d", "g", "g", "g", "g", "g", "g", "g", "g", "g", "d", "g", "g",],
            ["g", "g", "g", "d", "g", "d", "g", "g", "g", "g", "d", "g", "g", "d", "g", "g",],
            ["g", "g", "g", "d", "g", "d", "g", "g", "g", "g", "d", "g", "g", "d", "d", "d",],
            ["g", "g", "g", "d", "g", "d", "g", "g", "g", "g", "d", "g", "g", "g", "g", "g",],
            ["g", "d", "d", "d", "g", "d", "g", "g", "g", "g", "d", "g", "g", "g", "g", "g",],
            ["d", "d", "g", "g", "g", "d", "g", "g", "g", "g", "d", "g", "g", "g", "g", "g",],
            ["d", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",],
            ["g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",],
            ["g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "d", "d",],
            ["g", "g", "g", "g", "d", "g", "g", "g", "g", "g", "g", "d", "g", "g", "d", "g",],
            ["g", "g", "g", "g", "d", "d", "g", "g", "g", "g", "d", "d", "g", "d", "d", "g",],
            ["g", "g", "g", "g", "g", "d", "d", "d", "d", "d", "d", "g", "g", "d", "g", "g",],
            ["g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "d", "d", "g", "g",],
            ["g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "d", "d", "g", "g", "g",],
            ["g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "d", "g", "g", "g", "g",],
        ]
        
    def draw(self, screen):
        """Draws the tilemap on the screen

        Args:
            screen (pygame surface)
        """
        for row_index, row in enumerate(self.tile_map):
            for col_index, tile in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size
                if tile == "g":
                    screen.blit(self.grass_tile, (x, y))
                if tile == "d":
                    screen.blit(self.dirt_tile, (x, y))                
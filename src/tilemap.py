import pygame

class Tilemap:
    def __init__(self):
        self.grass_tile = pygame.image.load("assets/grass.png")
        self.dirt_tile = pygame.image.load("assets/dirt.png")
        self.tile_size = 64
        self.tile_map = [
            ["g", "g", "g", "d", "d", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",],
            ["g", "g", "g", "d", "d", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",],
            ["g", "g", "g", "d", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",],
            ["g", "g", "d", "d", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",],
            ["g", "g", "d", "d", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",],
            ["g", "g", "d", "d", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",],
            ["g", "d", "d", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",],
            ["d", "d", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",],
            ["d", "d", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",],
            ["d", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",],
            ["g", "g", "g", "g", "g", "g", "g", "g", "g", "d", "d", "d", "d", "d", "g", "g",],
            ["g", "g", "g", "g", "g", "g", "g", "g", "d", "d", "d", "d", "d", "d", "d", "g",],
            ["g", "g", "g", "g", "g", "g", "g", "g", "d", "d", "g", "g", "g", "g", "d", "d",],
            ["g", "g", "g", "g", "g", "g", "g", "d", "d", "g", "g", "g", "g", "g", "g", "d",],
            ["g", "g", "g", "g", "g", "g", "g", "d", "d", "g", "g", "g", "g", "g", "g", "g",],
            ["g", "g", "g", "g", "g", "g", "d", "d", "g", "g", "g", "g", "g", "g", "g", "g",],
        ]
        
    def update(self, screen):
        for row_index, row in enumerate(self.tile_map):
            for col_index, tile in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size
                if tile == "g":
                    screen.blit(self.grass_tile, (x, y))
                if tile == "d":
                    screen.blit(self.dirt_tile, (x, y))                
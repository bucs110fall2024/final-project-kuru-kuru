import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Initializes the player character and their attributes

        Args:
            x (int): sets the player's initial x pos 
            y (int): sets the player's initial y pos
        """
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))
        
        self.health = 5
        self.speed = 5
        self.direction = pygame.math.Vector2()
        
    def movement(self, collision_group):
        """Defines player movement using WASD. Uses normalized vectors so player moves at constant speed in all directions. Uses block_collision method to check collision
        
        Args:
            collision_group (sprite group)
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
        self.rect.x += self.direction.x * self.speed
        self.block_collision("horizontal", collision_group)
        self.rect.y += self.direction.y * self.speed
        self.block_collision("vertical", collision_group)
        
    def block_collision(self, direction, collision_group):
        """Calculates player collision with placeable block. Stops player from moving based on their relative position to the block

        Args:
            direction (str): is player moving horizontally or vertically
            collision_group (sprite group)
        """
        placeables_list = collision_group.sprites()
        for placeable in placeables_list:
            if self.rect.colliderect(placeable) and direction == "horizontal":
                if self.direction.x > 0:
                    self.rect.right = placeable.rect.left
                if self.direction.x < 0:
                    self.rect.left = placeable.rect.right
            if self.rect.colliderect(placeable) and direction == "vertical":
                if self.direction.y > 0:
                    self.rect.bottom = placeable.rect.top
                if self.direction.y < 0:
                    self.rect.top = placeable.rect.bottom
                
    def projectile_collision(self, collision_group):
        """Determines player collision with enemy projectiles

        Args:
            collision_group (sprite group)
        """
        if pygame.sprite.spritecollideany(self, collision_group):
            if pygame.sprite.spritecollide(self, collision_group, True, pygame.sprite.collide_mask):
                self.health -= 1
    
    def screen_collision(self):
        if self.rect.right > 1024:
            self.rect.right = 1024
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > 1024:
            self.rect.bottom = 1024
        if self.rect.top < 0:
            self.rect.top = 0
                
    def update(self, mouse_pos, collision_group, collision_group2):
        """Updates the player by drawing the player character and well as calling its movement method and projectile_collision method

        Args:
            mouse_pos (tuple)
            collision_group (sprite group): group for block collision
            collision_group2 (sprite group): group for projectile collision
        """
        if mouse_pos[0] > self.rect.centerx:
            self.image = pygame.image.load("assets/player.png").convert_alpha()
        if mouse_pos[0] < self.rect.centerx:
            self.image = pygame.transform.flip(pygame.image.load("assets/player.png").convert_alpha(), True, False)
            
        self.movement(collision_group)
        self.projectile_collision(collision_group2)
        self.screen_collision()

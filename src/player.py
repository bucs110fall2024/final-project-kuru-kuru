import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Initializes the player character and their attributes

        Args:
            x (int): sets the player's initial x pos 
            y (int): sets the player's initial y pos
        """
        super().__init__()
        self.image = pygame.image.load("assets/game-sprites/player.png").convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))
        
        self.health = 5
        self.speed = 6
        self.i_frame = False
        self.i_frame_timer = 0
        self.i_frame_length = 90
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

    def enemy_collision(self, projectile_group, enemy_group):
        """Determines collision with the enemy and its projectiles

        Args:
            projectile_group (sprite group)
            enemy_group (sprite group)
        """
        if not self.i_frame:
            if pygame.sprite.spritecollideany(self, projectile_group):
                if pygame.sprite.spritecollide(self, projectile_group, True, pygame.sprite.collide_mask):
                    self.health -= 1
                    self.i_frame = True
            if pygame.sprite.spritecollideany(self, enemy_group):
                if pygame.sprite.spritecollideany(self, enemy_group, pygame.sprite.collide_mask):
                    self.health -= 1
                    self.i_frame = True
        else:
            self.i_frame_timer += 1
            if self.i_frame_timer == self.i_frame_length:
                self.i_frame = False
                self.i_frame_timer = 0
            
    def screen_collision(self):
        """Checks player collision with edge of the screen
        """
        if self.rect.right > 1024:
            self.rect.right = 1024
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > 1024:
            self.rect.bottom = 1024
        if self.rect.top < 0:
            self.rect.top = 0
                
    def facing_mouse(self, mouse_pos):
        """Adjust where player is facing based on where the mouse is

        Args:
            mouse_pos (tuple): x, y pos of mouse pointer
        """
        if mouse_pos[0] > self.rect.centerx:
            self.image = pygame.image.load("assets/game-sprites/player.png").convert_alpha()
            if self.i_frame:
                self.image = pygame.image.load("assets/game-sprites/player-hurt.png").convert_alpha()
        if mouse_pos[0] < self.rect.centerx:
            self.image = pygame.transform.flip(pygame.image.load("assets/game-sprites/player.png").convert_alpha(), True, False)
            if self.i_frame:
                self.image = pygame.transform.flip(pygame.image.load("assets/game-sprites/player-hurt.png").convert_alpha(), True, False)
            
    def update(self, mouse_pos, collision_group, collision_group2, collision_group3):
        """Updates the player by calling its movement, collision, and facing methods

        Args:
            mouse_pos (tuple)
            collision_group (sprite group): group for block collision
            collision_group2 (sprite group): group for projectile collision
        """
        self.facing_mouse(mouse_pos)
        self.movement(collision_group)
        self.enemy_collision(collision_group2, collision_group3)
        self.screen_collision()

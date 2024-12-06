# Dodge and Shoot (Badly)
## CS110 Final Project  Fall, 2024

## Team Members

Wei Yang Zhu

***

## Project Description

A game where the player fight a boss while dodging its attacks. The player can place objects to block boss projectiles and have access to potions to heal the player. 

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Title screen
2. Moveable Player
3. Obstacle collision / collision detection
4. Placeable object and Consumables
5. Game over screen

### Classes

- Controller:
  - Contains all the code to make the game functional. Handles majorly of pygame event loops, game loops, timers, etc.
- Player:
  - Handles player interaction with the game such as movement and collision.
- Projectile:
  - Handles player projectile movement and direction.
- Placeables:
  - Handes player placed obstacles collision and damaged state.
- Enemy:
  - Handles enemy movement, attack patterns, and collision with player projectiles.
- EnemyProjectile:
  - Handles enemy projectile movement.
- Spawner:
  - Handles enemy projectile spawning and direction. It is what gives the enemy attack patterns.
- Tilemap:
  - Creates the tilemap for the game using a grid system.
- Button:
  - Loads button images and draw them onscreen.

## ATP

### Test 1: Starting the Game
- Test Description:
  - Verify that starting the game on launch works as intended.
- Test Steps:
  - Go to the project folder and in the terminal enter: python main.py
  - Click on "Play"
  - You should get an error telling you to click on "New Game"
  - Click to anywhere to get rid of error
  - Click on "New Game"
  - Game screen should appear with the player on the screen
- Expected Outcome:
  - When launching and relaunching the program through python main.py, the "Play" button will prompt an error telling players to click the "New Game" button.

### Test 2: Player Movement
- Test Description:
  - Verify player moves as intended.
- Test Steps:
  - Start the game
  - User press "D"
    - Player moves right
  - User press "A"
    - Player moves left
  - User press "W"
    - Player moves up
  - User press "S"
    - Player moves down
- Expected Outcome:
  - Pressing WASD should move the player to the corresponding direction.
 
### Test 3: Player Shooting
- Test Description:
  - Verify player shoots as intended.
- Test Steps:
  - Start the game
  - Hold down left mouse button
  - Move the player and mouse around the screen
  - Observe where the projectile is being shot to
  - Observe the time between each fired projectile
- Expected Outcome:
  - Player should shoot at the direction of the mouse at a constant rate regardless of where they are moving.
 
### Test 4: Collisions
- Test Description:
  - Verify player collision with enemy and its projectiles
- Test Steps:
  - Start the game
  - Observe player HP
  - Walk into the enemy projectile (colored red)
  - Observe the projectile that collides with the player
  - Check player HP
  - Dodge an enemy projectile
  - Check player HP
  - Walk into the enemy itself
  - Check player HP
- Expected Outcome:
  - Player should lose HP when coming into contact with the enemy and its projectiles. The collided projectile should disappear. There should be a window of time where player is actively colliding with the enemy and/or projectiles but not lose HP.
 
### Test 5: Game Over Screen
- Test Description:
  - Verify the game over screen works as intended
- Test Steps:
  - Start the game
  - Lose all player HP
  - Observe if a screen labeled "Game Over" appears
  - Click on "Menu"
  - Observe if the menu screen appears
  - Get back to game over screen by clicking "Play" or "New Game" and lose all HP
  - Click on "Retry"
  - Observe if the player and all game elements reset to their initial position
- Expected Outcome:
  - Player should get sent to the game over screen when their HP reaches 0. The "Menu" button should take the player to the menu and "Retry" button should load the game screen again with all elements resetted.

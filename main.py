import pygame
from src.sample_controller import Controller
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    game = Controller(1000, 1000, 60)
    #Call your mainloop
    game.mainloop()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():

    #Initialize Game and create Screen Object
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode()  #Specify screen size in set_mode(width,height) , default full screen.
    ship = Ship(ai_settings,screen)
    bullets = Group()

    pygame.display.set_caption("Alien Invasion")

    #Start mainloop for game...
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,bullets)



run_game()



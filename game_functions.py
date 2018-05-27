import pygame
import sys
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Clearing Game Cache...\nExiting...")
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)


def update_screen(ai_settings,screen,ship,bullets):
    '''  Update Images on Screen and flip the screen   '''
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    #Redraw most recent screen
    pygame.display.flip()


def check_keydown_event(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.movement_right = True
    elif event.key == pygame.K_LEFT:
        ship.movement_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.movement_right = False
    elif event.key == pygame.K_LEFT:
        ship.movement_left = False

def update_bullets(bullets):
    bullets.update()
    #Get rid of Bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    print(len(bullets))

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullet_allowed :
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)

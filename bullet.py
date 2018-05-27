from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    ''' Handles Bullets shot by the SpaceShip '''

    def __init__(self,ai_settings,screen,ship):
        # Create a bullet object at spaceship's current location.
        super(Bullet,self).__init__()
        self.screen = screen

        # Create a Bullet rect at 0,0 and set it at Ship's position
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store bullets pos as Decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        """Move the bullet up the screen."""

        # Update the decimal position of the bullet.
        self.y -= self.speed

        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


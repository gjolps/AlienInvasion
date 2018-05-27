import pygame


class Ship():



    def __init__(self,ai_settings ,screen):

        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('Images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Ship speed
        self.ai_settings = ai_settings

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal value for Ship's Center
        self.center = float(self.screen_rect.centerx)

        # Movement of Ship
        self.movement_right = False
        self.movement_left = False

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        ''' Update Ship's Movement  '''
        if self.movement_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.movement_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed

        #Update centerx from rect.cent
        self.rect.centerx = self.center



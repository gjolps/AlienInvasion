class Settings():
    '''   All Game Settings to be found HERE  '''

    def __init__(self):
        '''  Initialize Game Settings  '''
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # Ship Settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 5


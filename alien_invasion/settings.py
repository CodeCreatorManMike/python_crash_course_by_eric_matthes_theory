class Settings:
    """A class which stores all of the settings"""

    def __init__(self):
        "initialize game settings"
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.bullets_allowed = 5

        # ship settings
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

import pygame
import sys



from settings import Settings
from ship import Ship


class AlienInvasion:
    """overall class to manage assets/behaviour"""

    def __init__(self):
        """Initialize the game, create resources"""
        pygame.init()
        self.settings = Settings()
    
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
    
    
    def run_game(self):
        "main game loop"
        while True:
            # watch for keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme

            # make the most recently drawn screen available
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, run the game
    ai = AlienInvasion()
    ai.run_game()
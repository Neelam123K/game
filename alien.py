import pygame, sys
from player import Player1  # Assuming your file is named 'player.py' and contains a class 'Player1'

class Game:
    def __init__(self):
        player_sprite = Player1((300, 300))
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self, screen):
        self.player.update()  # Assuming your Player1 class has an update method
        screen.fill((30, 30, 30))  # Clear the screen with a dark background
        self.player.draw(screen)  # Draw the player sprite
        pygame.display.flip()  # Update the full display Surface to the screen

if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()  # Corrected to Clock()

    game = Game()  # Instantiate your game

    while True:
        for event in pygame.event.get():  # Corrected the typo in 'event'
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.run(screen)  # Call the run method inside the main loop

        clock.tick(60)  # Maintain 60 frames per second

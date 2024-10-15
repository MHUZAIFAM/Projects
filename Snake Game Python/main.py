import pygame
from game_engine import GameEngine


def main():
    pygame.init()
    game = GameEngine()

    while not game.is_game_over():
        game.handle_events()
        game.update()
        game.draw()
        pygame.time.delay(100)  # Control the game speed

    pygame.quit()


if __name__ == "__main__":
    main()

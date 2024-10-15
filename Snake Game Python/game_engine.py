import pygame
import random
from file_handler import FileHandler

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
CELL_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class GameEngine:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")

        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.food_pos = [random.randrange(1, (SCREEN_WIDTH // CELL_SIZE)) * CELL_SIZE,
                         random.randrange(1, (SCREEN_HEIGHT // CELL_SIZE)) * CELL_SIZE]
        self.food_spawn = True
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0

        self.high_score = self.load_high_score()

    def load_high_score(self):
        file_handler = FileHandler()
        return file_handler.load_high_score()

    def save_high_score(self):
        file_handler = FileHandler()
        file_handler.save_high_score(self.score)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != 'DOWN':
                    self.change_to = 'UP'
                elif event.key == pygame.K_DOWN and self.direction != 'UP':
                    self.change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                    self.change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                    self.change_to = 'RIGHT'

    def update(self):
        if self.change_to == 'UP':
            self.direction = 'UP'
        if self.change_to == 'DOWN':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT':
            self.direction = 'RIGHT'

        # Update snake position based on the current direction
        if self.direction == 'UP':
            self.snake_pos[1] -= CELL_SIZE
        if self.direction == 'DOWN':
            self.snake_pos[1] += CELL_SIZE
        if self.direction == 'LEFT':
            self.snake_pos[0] -= CELL_SIZE
        if self.direction == 'RIGHT':
            self.snake_pos[0] += CELL_SIZE

        # Insert the new head of the snake
        self.snake_body.insert(0, list(self.snake_pos))

        # Check if the snake has eaten the food
        if self.snake_pos == self.food_pos:
            self.score += 1
            self.food_spawn = False  # We need to spawn new food
        else:
            # Remove the last segment of the snake's body if no food was eaten
            self.snake_body.pop()

        # Spawn new food if it was eaten
        if not self.food_spawn:
            self.food_pos = [random.randrange(1, (SCREEN_WIDTH // CELL_SIZE)) * CELL_SIZE,
                             random.randrange(1, (SCREEN_HEIGHT // CELL_SIZE)) * CELL_SIZE]
            self.food_spawn = True

        # Check if the snake hits the boundaries
        if (self.snake_pos[0] < 0 or self.snake_pos[0] >= SCREEN_WIDTH or
                self.snake_pos[1] < 0 or self.snake_pos[1] >= SCREEN_HEIGHT):
            self.game_over()

        # Check if the snake hits itself
        for block in self.snake_body[1:]:
            if self.snake_pos == block:
                self.game_over()

    def draw(self):
        self.screen.fill(WHITE)
        for pos in self.snake_body:
            pygame.draw.rect(self.screen, GREEN, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(self.screen, RED, pygame.Rect(self.food_pos[0], self.food_pos[1], CELL_SIZE, CELL_SIZE))

        font = pygame.font.Font(None, 35)
        score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        high_score_text = font.render(f"High Score: {self.high_score}", True, (0, 0, 0))
        self.screen.blit(score_text, [0, 0])
        self.screen.blit(high_score_text, [0, 30])

        pygame.display.flip()

    def game_over(self):
        if self.score > self.high_score:
            self.save_high_score()
        pygame.quit()
        quit()

    def is_game_over(self):
        return False  # We'll handle the game over within `game_over` function itself

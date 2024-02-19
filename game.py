import pygame
import sys
from snake import Snake
from food import Food
from score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 640, 480
        self.cell_size = 10
        self.fps = 5
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()
        self.snake = Snake(self.cell_size, self.width, self.height)
        self.food = Food(self.cell_size, self.width, self.height)
        self.score = Score()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != (0, 1):
                    self.snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                    self.snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                    self.snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):
                    self.snake.change_direction((1, 0))

    def draw_border(self):
        pygame.draw.rect(
            self.screen, self.white, (0, 0, self.width, 2.5 * self.cell_size)
        )
        pygame.draw.rect(self.screen, self.white, (0, 0, self.cell_size, self.height))
        pygame.draw.rect(
            self.screen,
            self.white,
            (self.width - self.cell_size, 0, self.cell_size, self.height),
        )
        pygame.draw.rect(
            self.screen,
            self.white,
            (0, self.height - self.cell_size, self.width, self.cell_size),
        )

    def run(self):
        while True:
            self.handle_events()

            self.snake.move()

            if self.snake.check_collision():
                print("Game Over! Score:", self.score.current_score)
                pygame.quit()
                sys.exit()

            # Check if the snake eats the food
            head = self.snake.body[0]
            if (
                head == self.food.position
                and 0 < head[0] < self.width - self.cell_size
                and self.cell_size < head[1] < self.height - self.cell_size
            ):
                self.snake.grow_pending += 1
                self.food.position = self.food.generate_food_position()
                self.score.increment_score()
                self.fps += 1

            self.screen.fill(self.black)

            # Draw the border
            self.draw_border()

            # Draw the food
            self.food.draw(self.screen, self.red)

            # Draw the snake
            for segment in self.snake.body:
                pygame.draw.rect(
                    self.screen,
                    self.white,
                    (segment[0], segment[1], self.cell_size, self.cell_size),
                )

            # Display the score on the top part of the game in red
            self.score.display_score(
                self.screen, self.red, (self.width // 2, self.cell_size // 4)
            )

            pygame.display.flip()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.run()

import pygame
import random

pygame.init()

# screen variables
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
INFO_HEIGHT = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
FOOD_COLORS = {1: (255, 100, 100), 2: (255, 165, 0), 3: (255, 255, 0)}  # Light red, orange, yellow

# snake setup
snake = [(100, 100), (80, 100), (60, 100)]
snake_dir = (GRID_SIZE, 0)

# game variables
score = 0
level = 1
speed = 10
food_count = 0  # Tracks food eaten
clock = pygame.time.Clock()
running = True


def draw_text(text, size, color, x, y, center=True):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y) if center else (x, y))
    screen.blit(text_surface, text_rect)


# food class
class Food:
    def __init__(self):
        self.generate()
        self.timer = pygame.time.get_ticks()

    def generate(self):
        self.position = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                         random.randint(INFO_HEIGHT // GRID_SIZE, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
        self.value = random.randint(1, 3)
        self.timer = pygame.time.get_ticks()

    def draw(self):
        pygame.draw.rect(screen, FOOD_COLORS[self.value], (*self.position, GRID_SIZE, GRID_SIZE))

    def expired(self):
        return pygame.time.get_ticks() - self.timer > 7000


food = Food()

while running:
    screen.fill(WHITE)

    # score panel
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, INFO_HEIGHT))
    pygame.draw.line(screen, WHITE, (0, INFO_HEIGHT), (WIDTH, INFO_HEIGHT), 3)
    draw_text(f"Score: {score}  Level: {level}", 30, WHITE, WIDTH // 2, INFO_HEIGHT // 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                snake_dir = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                snake_dir = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                snake_dir = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                snake_dir = (GRID_SIZE, 0)

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    # collision check
    if new_head in snake or new_head[0] < 0 or new_head[1] < INFO_HEIGHT or new_head[0] >= WIDTH or new_head[
        1] >= HEIGHT:
        running = False

    snake.insert(0, new_head)

    if new_head == food.position:
        score += food.value
        food.generate()
        food_count += 1  # food tracking

        if food_count % 3 == 0:  # every 5 foods level up
            level += 1
            speed += 2
    else:
        snake.pop()

    if food.expired():
        food.generate()

    food.draw()

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(speed)

# game over
screen.fill(BLACK)
draw_text("Game Over", 50, WHITE, WIDTH // 2, HEIGHT // 2 - 40)
draw_text(f"Final Score: {score}  Level: {level}", 30, WHITE, WIDTH // 2, HEIGHT // 2)
draw_text("Press any key to exit", 25, WHITE, WIDTH // 2, HEIGHT // 2 + 40)
pygame.display.flip()

# quit
game_over = True
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            game_over = False

pygame.quit()

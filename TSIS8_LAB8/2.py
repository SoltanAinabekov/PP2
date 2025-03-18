import pygame
import random

pygame.init()

WIDTH, HEIGHT = 700, 500
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

snake = [(100, 100), (80, 100), (60, 100)]
snake_dir = (GRID_SIZE, 0)


def random_food():
    while True:
        pos = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
               random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
        if pos not in snake:
            return pos


food = random_food()
score = 0
level = 1
speed = 10
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

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
    if new_head in snake or new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= WIDTH or new_head[1] >= HEIGHT:
        running = False

    snake.insert(0, new_head)

    if new_head == food:
        food = random_food()
        score += 1
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()

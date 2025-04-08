import pygame
import random
from user import get_or_create_user, get_user_score, save_score

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
FOOD_COLORS = {1: (255, 100, 100), 2: (255, 165, 0), 3: (255, 255, 0)}

# level config
level_data = {
    1: {'speed': 10, 'walls': []},
    2: {'speed': 12, 'walls': [(200, 200, 400, 20)]},
    3: {'speed': 14, 'walls': [(100, 300, 600, 20), (300, 100, 20, 400)]},
}

# snake setup
snake = [(100, 100), (80, 100), (60, 100)]
snake_dir = (GRID_SIZE, 0)

# game variables
food_count = 0
clock = pygame.time.Clock()
running = True
paused = False


# draw text
def draw_text(text, size, color, x, y, center=True):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y) if center else (x, y))
    screen.blit(text_surface, text_rect)


# username input screen
def get_username():
    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(None, 32)

    while True:
        screen.fill(WHITE)
        draw_text("Enter your username:", 36, BLACK, WIDTH // 2, HEIGHT // 2 - 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text.strip()
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)


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


# user setup
username = get_username()
user_id = get_or_create_user(username)
score, level, speed = get_user_score(user_id)
speed = level_data.get(level, {'speed': 10})['speed']

# food init
food = Food()

# game loop
while running:
    screen.fill(WHITE)

    # info bar
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, INFO_HEIGHT))
    pygame.draw.line(screen, WHITE, (0, INFO_HEIGHT), (WIDTH, INFO_HEIGHT), 3)
    draw_text(f"Score: {score}  Level: {level}", 30, WHITE, WIDTH // 2, INFO_HEIGHT // 2)

    # walls
    walls = level_data.get(level, {}).get('walls', [])
    for wall in walls:
        pygame.draw.rect(screen, BLACK, wall)

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
            elif event.key == pygame.K_p:
                paused = not paused
                save_score(user_id, score, level, speed)
                print("Game paused and saved.")

    if paused:
        draw_text("PAUSED", 60, BLACK, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
        clock.tick(5)
        continue

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    # collision detection
    if (new_head in snake or new_head[0] < 0 or new_head[1] < INFO_HEIGHT or
            new_head[0] >= WIDTH or new_head[1] >= HEIGHT or
            any(pygame.Rect(*wall).collidepoint(new_head) for wall in walls)):
        running = False

    snake.insert(0, new_head)

    if new_head == food.position:
        score += food.value
        food.generate()
        food_count += 1
        if food_count % 3 == 0:
            level += 1
            speed = level_data.get(level, {'speed': speed})['speed']
    else:
        snake.pop()

    if food.expired():
        food.generate()

    food.draw()

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(speed)

# game over screen
screen.fill(BLACK)
draw_text("Game Over", 50, WHITE, WIDTH // 2, HEIGHT // 2 - 40)
draw_text(f"Final Score: {score}  Level: {level}", 30, WHITE, WIDTH // 2, HEIGHT // 2)
draw_text("Press any key to exit", 25, WHITE, WIDTH // 2, HEIGHT // 2 + 40)
pygame.display.flip()

save_score(user_id, score, level, speed)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            pygame.quit()
            exit()

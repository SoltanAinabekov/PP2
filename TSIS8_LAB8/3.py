import pygame
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

radius = 15
mode = "circle"
color = BLACK
eraser_mode = False
bg_color = WHITE

show_help = True
help_start_time = time.time()

font = pygame.font.SysFont("Arial", 20)
help_text = [
    "Pygame Paint Controls:",
    "Left Mouse - Draw",
    "Right Mouse - Eraser",
    "Mouse Wheel - Resize Brush",
    "+ / -   - Resize Brush",
    "R - Rectangle Brush",
    "C - Circle Brush",
    "1 - Red Color",
    "2 - Green Color",
    "3 - Blue Color",
    "4 - Black Color",
    "E - Toggle Eraser",
    "SPACE - Clear Screen",
    "ESC - Close Help Window"
]

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(bg_color)

def draw_help_screen():
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(220)
    overlay.fill(WHITE)
    screen.blit(overlay, (0, 0))

    y_offset = 100
    for line in help_text:
        text = font.render(line, True, BLACK)
        screen.blit(text, (WIDTH // 3, y_offset))
        y_offset += 30

running = True
while running:
    screen.blit(canvas, (0, 0))

    if show_help and time.time() - help_start_time < 10:
        draw_help_screen()
    else:
        show_help = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mode == "circle":
                    pygame.draw.circle(canvas, WHITE if eraser_mode else color, event.pos, radius)
                elif mode == "rectangle":
                    pygame.draw.rect(canvas, WHITE if eraser_mode else color, (*event.pos, radius, radius))

            elif event.button == 3:  # Right Click: Erase
                pygame.draw.circle(canvas, bg_color, event.pos, radius)

        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            if mode == "circle":
                pygame.draw.circle(canvas, WHITE if eraser_mode else color, event.pos, radius)
            elif mode == "rectangle":
                pygame.draw.rect(canvas, WHITE if eraser_mode else color, (*event.pos, radius, radius))

        elif event.type == pygame.MOUSEWHEEL:
            radius = max(5, min(100, radius + event.y))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                show_help = False
            elif event.key == pygame.K_SPACE:
                canvas.fill(bg_color)
            elif event.key == pygame.K_r:
                mode = "rectangle"
                eraser_mode = False
            elif event.key == pygame.K_c:
                mode = "circle"
                eraser_mode = False
            elif event.key == pygame.K_e:
                eraser_mode = not eraser_mode
            elif event.key == pygame.K_1:
                color = RED
                eraser_mode = False
            elif event.key == pygame.K_2:
                color = GREEN
                eraser_mode = False
            elif event.key == pygame.K_3:
                color = BLUE
                eraser_mode = False
            elif event.key == pygame.K_4:
                color = BLACK
                eraser_mode = False
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                radius = min(100, radius + 5)
            elif event.key == pygame.K_MINUS:
                radius = max(5, radius - 5)

    pygame.display.flip()

pygame.quit()

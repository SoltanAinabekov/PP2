import pygame

pygame.init()

# screen variables
WIDTH, HEIGHT = 900, 600
ICON_SIZE = 50  # Icon size
TOOLBAR_HEIGHT = ICON_SIZE + 20
DRAW_AREA_TOP = TOOLBAR_HEIGHT + 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# tools
BRUSH_CIRCLE = "brush_circle"
BRUSH_SQUARE = "brush_square"
ERASER = "eraser"
RECTANGLE = "rectangle"
RIGHT_TRIANGLE = "right_triangle"
EQUILATERAL_TRIANGLE = "equilateral_triangle"
RHOMBUS = "rhombus"
CLEAR = "clear"

selected_tool = BRUSH_CIRCLE
color = BLACK
brush_size = 20
drawing = False
start_pos = None

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# icon dictionary
icons = {
    BRUSH_CIRCLE: pygame.Rect(10, 10, ICON_SIZE, ICON_SIZE),
    BRUSH_SQUARE: pygame.Rect(70, 10, ICON_SIZE, ICON_SIZE),
    ERASER: pygame.Rect(130, 10, ICON_SIZE, ICON_SIZE),
    RECTANGLE: pygame.Rect(190, 10, ICON_SIZE, ICON_SIZE),
    RIGHT_TRIANGLE: pygame.Rect(250, 10, ICON_SIZE, ICON_SIZE),
    EQUILATERAL_TRIANGLE: pygame.Rect(310, 10, ICON_SIZE, ICON_SIZE),
    RHOMBUS: pygame.Rect(370, 10, ICON_SIZE, ICON_SIZE),
    CLEAR: pygame.Rect(WIDTH - 120, 10, 100, ICON_SIZE)
}

# color for icons
color_icons = {
    RED: pygame.Rect(450, 10, 30, 30),
    GREEN: pygame.Rect(490, 10, 30, 30),
    BLUE: pygame.Rect(530, 10, 30, 30),
    BLACK: pygame.Rect(570, 10, 30, 30)
}

def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))
    pygame.draw.line(screen, BLACK, (0, TOOLBAR_HEIGHT), (WIDTH, TOOLBAR_HEIGHT), 3)

    for tool, rect in icons.items():
        pygame.draw.rect(screen, WHITE if selected_tool == tool else BLACK, rect, 2)

    # brush icon
    pygame.draw.circle(screen, BLACK, icons[BRUSH_CIRCLE].center, 10)  # circle brush
    pygame.draw.rect(screen, BLACK, icons[BRUSH_SQUARE].inflate(-20, -20))  # square brush

    # eraser icon
    pygame.draw.line(screen, BLACK, icons[ERASER].topleft, icons[ERASER].bottomright, 3)
    pygame.draw.line(screen, BLACK, icons[ERASER].topright, icons[ERASER].bottomleft, 3)

    # rectangle icon
    pygame.draw.rect(screen, BLACK, icons[RECTANGLE].inflate(-10, -20))
    # right triangle icon
    pygame.draw.polygon(screen, BLACK, [
        icons[RIGHT_TRIANGLE].topleft, icons[RIGHT_TRIANGLE].bottomleft, icons[RIGHT_TRIANGLE].topright
    ])
    # equilateral triangle icon
    pygame.draw.polygon(screen, BLACK, [
        (icons[EQUILATERAL_TRIANGLE].centerx, icons[EQUILATERAL_TRIANGLE].top),
        icons[EQUILATERAL_TRIANGLE].bottomleft,
        icons[EQUILATERAL_TRIANGLE].bottomright
    ])
    # rombik icon
    pygame.draw.polygon(screen, BLACK, [
        (icons[RHOMBUS].centerx, icons[RHOMBUS].top),
        icons[RHOMBUS].midleft,
        (icons[RHOMBUS].centerx, icons[RHOMBUS].bottom),
        icons[RHOMBUS].midright
    ])

    # clear button icon
    pygame.draw.rect(screen, WHITE, icons[CLEAR])
    font = pygame.font.Font(None, 24)
    text = font.render("CLEAR", True, BLACK)
    text_rect = text.get_rect(center=icons[CLEAR].center)
    screen.blit(text, text_rect)

    # color icons
    for col, rect in color_icons.items():
        pygame.draw.rect(screen, col, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)  # Border


def draw_shape(surface, shape, start, end, erase=False):
    rect = pygame.Rect(*start, end[0] - start[0], end[1] - start[1])
    rect.normalize()
    color_to_use = WHITE if erase else color

    if shape == RECTANGLE:
        pygame.draw.rect(surface, color_to_use, rect, 2)
    elif shape == RIGHT_TRIANGLE:
        pygame.draw.polygon(surface, color_to_use, [(rect.left, rect.bottom), (rect.left, rect.top), (rect.right, rect.bottom)], 2)
    elif shape == EQUILATERAL_TRIANGLE:
        pygame.draw.polygon(surface, color_to_use, [
            (rect.centerx, rect.top),
            (rect.left, rect.bottom),
            (rect.right, rect.bottom)
        ], 2)
    elif shape == RHOMBUS:
        pygame.draw.polygon(surface, color_to_use, [
            (rect.centerx, rect.top),
            (rect.left, rect.centery),
            (rect.centerx, rect.bottom),
            (rect.right, rect.centery)
        ], 2)

# paint loop
running = True
while running:
    screen.blit(canvas, (0, 0))
    draw_toolbar()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for tool, rect in icons.items():
                    if rect.collidepoint(event.pos):
                        if tool == CLEAR:
                            canvas.fill(WHITE)
                        else:
                            selected_tool = tool
                        break
                else:
                    for col, rect in color_icons.items():
                        if rect.collidepoint(event.pos):
                            color = col
                            break
                    else:
                        drawing = True
                        start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                drawing = False
                if start_pos:
                    end_pos = event.pos
                    if selected_tool in {RECTANGLE, RIGHT_TRIANGLE, EQUILATERAL_TRIANGLE, RHOMBUS}:
                        draw_shape(canvas, selected_tool, start_pos, end_pos)
                    elif selected_tool == BRUSH_CIRCLE:
                        pygame.draw.circle(canvas, color, start_pos, brush_size)
                    elif selected_tool == BRUSH_SQUARE:
                        pygame.draw.rect(canvas, color, (*start_pos, brush_size, brush_size))
                    elif selected_tool == ERASER:
                        pygame.draw.circle(canvas, WHITE, start_pos, brush_size)

        elif event.type == pygame.MOUSEMOTION and drawing:
            if selected_tool == BRUSH_CIRCLE:
                pygame.draw.circle(canvas, color, event.pos, brush_size)
            elif selected_tool == BRUSH_SQUARE:
                pygame.draw.rect(canvas, color, (*event.pos, brush_size, brush_size))
            elif selected_tool == ERASER:
                pygame.draw.circle(canvas, WHITE, event.pos, brush_size)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                brush_size = min(50, brush_size + 5)
            elif event.key == pygame.K_MINUS:
                brush_size = max(5, brush_size - 5)

    pygame.display.flip()

#quit
pygame.quit()

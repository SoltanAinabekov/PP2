import pygame
import sys
from datetime import datetime

pygame.init()

clock = pygame.image.load("clock.png")
min_hand = pygame.image.load("min_hand.png")
sec_hand = pygame.image.load("sec_hand.png")

WIDTH, HEIGHT = clock.get_size()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
CENTER = (WIDTH // 2, HEIGHT // 2)

def rotate_image(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pivot)
    return rotated_image, new_rect

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    min_angle = - (minutes * 6) - 48
    sec_angle = - (seconds * 6) + 54

    screen.blit(clock, (0, 0))

    min_rotated, min_rect = rotate_image(min_hand, min_angle, CENTER)
    screen.blit(min_rotated, min_rect)

    sec_rotated, sec_rect = rotate_image(sec_hand, sec_angle, CENTER)
    screen.blit(sec_rotated, sec_rect)

    pygame.display.flip()
    pygame.time.Clock()

pygame.quit()
sys.exit()

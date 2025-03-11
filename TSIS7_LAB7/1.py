import pygame
import time
import math
from datetime import datetime

pygame.init()

clock_img = pygame.image.load("mickeyclock.png")

original_width, original_height = clock_img.get_size()

new_width = int(original_width * 0.7)
new_height = int(original_height * 0.7)

clock_img = pygame.transform.smoothscale(clock_img, (new_width, new_height))

screen = pygame.display.set_mode((new_width, new_height))
pygame.display.set_caption("Mickey Mouse Clock")

clock_center = (new_width // 2, new_height // 2)

minute_length = new_width // 5
second_length = new_width // 4

def get_hand_position(angle, length):
    rad = math.radians(angle)
    x = clock_center[0] + length * math.cos(rad)
    y = clock_center[1] - length * math.sin(rad)
    return int(x), int(y)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_img, (0, 0))

    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = 90 - (minutes % 60) * 6
    second_angle = 90 - (seconds % 60) * 6

    minute_end = get_hand_position(minute_angle, minute_length)
    second_end = get_hand_position(second_angle, second_length)

    pygame.draw.line(screen, (0, 0, 255), clock_center, minute_end, 8)
    pygame.draw.line(screen, (255, 0, 0), clock_center, second_end, 4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    time.sleep(1)

pygame.quit()

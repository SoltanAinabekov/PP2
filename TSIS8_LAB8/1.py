import pygame
import sys
import random
import time

pygame.init()

# screen variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SPEED = 5
SCORE = 0
COINS = 0
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, RED)

# images
road_img = pygame.image.load("Road.png")
road_img = pygame.transform.scale(road_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (50, 100))

enemy_img = pygame.image.load("enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (50, 100))

coin_img = pygame.image.load("coin.png")
coin_img = pygame.transform.scale(coin_img, (30, 30))

# sound
crash_sound = pygame.mixer.Sound("crash_8bit.wav")

# display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racing Game")
FramePerSec = pygame.time.Clock()

# background class
class Background:
    def __init__(self):
        self.y1 = 0
        self.y2 = -SCREEN_HEIGHT
        self.speed = SPEED

    def update(self):
        self.y1 += self.speed
        self.y2 += self.speed
        if self.y1 >= SCREEN_HEIGHT:
            self.y1 = self.y2 - SCREEN_HEIGHT
        if self.y2 >= SCREEN_HEIGHT:
            self.y2 = self.y1 - SCREEN_HEIGHT

    def render(self):
        DISPLAYSURF.blit(road_img, (0, self.y1))
        DISPLAYSURF.blit(road_img, (0, self.y2))

# player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

# enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)

# coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), random.randint(-100, 0))

    def move(self):
        global COINS
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), random.randint(-100, 0))

        if self.rect.colliderect(P1.rect):
            COINS += 1
            self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), random.randint(-100, 0))

# objects
background = Background()
P1 = Player()
E1 = Enemy()
C1 = Coin()

# group sprites
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# speed increase
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
            background.speed = SPEED
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    background.update()
    background.render()

    # score and coins
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (10, 40))

    # display and move sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # collision check
    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        time.sleep(0.5)

        DISPLAYSURF.fill(BLACK)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        DISPLAYSURF.blit(game_over_text, text_rect)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Update Display
    pygame.display.update()
    FramePerSec.tick(FPS)

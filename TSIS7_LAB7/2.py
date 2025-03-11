import pygame
import os

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Music Player")

MUSIC_FOLDER = "music"
tracks = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
curr_track_index = 0 if tracks else None

def play_music():
    if curr_track_index is not None:
        pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, tracks[curr_track_index]))
        pygame.mixer.music.play()


def next_track():
    global curr_track_index
    if tracks:
        curr_track_index = (curr_track_index + 1) % len(tracks)
        play_music()


def prev_track():
    global curr_track_index
    if tracks:
        curr_track_index = (curr_track_index - 1) % len(tracks)
        play_music()

if curr_track_index is not None:
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                pygame.mixer.music.rewind()
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                prev_track()
            elif event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

pygame.quit()

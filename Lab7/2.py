import pygame

white = (255, 255, 255)
x=330
y=270

def tupaya_knopka():
    if pygame.mixer.music.get_busy() and not paused:
        screen.blit(start_but, (x, y))
    else:
        screen.blit(pause_but, (x, y))
    screen.blit(next_but, (x + pause_but.get_width(), y))
    screen.blit(prev_but, (x - prev_but.get_width(), y))

def play_next_song():
    global current_song_index, paused
    current_song_index = (current_song_index + 1) % len(_songs)
    pygame.mixer.music.load(_songs[current_song_index])
    pygame.mixer.music.play()
    paused = False 
    tupaya_knopka()

def play_previous_song():
    global current_song_index, paused
    current_song_index = (current_song_index - 1) % len(_songs)
    pygame.mixer.music.load(_songs[current_song_index])
    pygame.mixer.music.play()
    paused = False 
    tupaya_knopka()

def toggle_pause():
    global paused
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        paused = True
    else:
        pygame.mixer.music.unpause()
        paused = False
    tupaya_knopka()

def check_song_end():
    if not pygame.mixer.music.get_busy() and not paused:
        play_next_song()
        tupaya_knopka()

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

_songs = ["white_space.mp3", "trees.mp3", "crossroads.mp3", "duet.mp3", "by_your_side.mp3", "title.mp3", "lost_then_found.mp3"]
current_song_index = 0
shuffle = False

start_but = pygame.image.load("pause.png")
pause_but = pygame.image.load("play.png")
next_but = pygame.image.load("next-button.png")
prev_but = pygame.image.load("previous-button.png")
bg = pygame.image.load("bg_player.png")

pause_but = pygame.transform.scale(pause_but, (int(pause_but.get_width() * 0.2), int(pause_but.get_height() * 0.2)))
start_but = pygame.transform.scale(start_but, (int(start_but.get_width() * 0.2), int(start_but.get_height() * 0.2)))
next_but = pygame.transform.scale(next_but, (int(next_but.get_width() * 0.2), int(next_but.get_height() * 0.2)))
prev_but = pygame.transform.scale(prev_but, (int(prev_but.get_width() * 0.2), int(prev_but.get_height() * 0.2)))

paused = False

pygame.mixer.music.load(_songs[current_song_index])
pygame.mixer.music.play() 

while True:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if pause_but.get_rect(topleft=(300, 250)).collidepoint(mouse_pos):
                toggle_pause()
            elif start_but.get_rect(topleft=(300, 250)).collidepoint(mouse_pos):
                toggle_pause()
            elif next_but.get_rect(topleft=(300 + pause_but.get_width(), 250)).collidepoint(mouse_pos):
                play_next_song()
            elif prev_but.get_rect(topleft=(300 - prev_but.get_width(), 250)).collidepoint(mouse_pos):
                play_previous_song()

    check_song_end()
    screen.blit(bg, (0, 0))
    tupaya_knopka()

    pygame.display.flip()
    clock.tick(60)

import pygame
import math
from datetime import datetime

pygame.init()

def rotate_image(image, rect, angle):
    new_image = pygame.transform.rotate(image, angle)
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect

def get_angle_for_minute(minute):
    return 360-((minute / 60) * 360 + 45) 

def get_angle_for_second(second):
    return 360-((second / 60) * 360 - 60 )

screen = pygame.display.set_mode((800, 600))
done = False
white = (255, 255, 255)

min_hand = pygame.image.load("min_hand.png")
sec_hand = pygame.image.load("sec_hand.png")
bg_clock = pygame.image.load("clock.png")

min_rect = min_hand.get_rect(center=(400, 300))
sec_rect = sec_hand.get_rect(center=(400, 300))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.now()
    minutes_now = float(now.minute) + (now.second / 60) 
    seconds_now = float(now.second)

    angle_minutes = get_angle_for_minute(minutes_now)
    angle_seconds = get_angle_for_second(seconds_now)

    screen.fill(white)
    screen.blit(bg_clock, (0, 0))

    image_min, min_rect = rotate_image(min_hand, min_rect, angle_minutes)
    image_sec, sec_rect = rotate_image(sec_hand, sec_rect, angle_seconds)


    screen.blit(image_min, min_rect)
    screen.blit(image_sec, sec_rect)

    pygame.display.flip()

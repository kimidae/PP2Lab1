import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

startX = 0
startY = 0

endX = 0
endY = 0

done = False

while not done:
    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            startX, startY = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:", pygame.mouse.get_pos())
            if LMBpressed:
                endX, endY = pygame.mouse.get_pos()
                a=min(abs(startX - endX), abs(startY - endY))
                pygame.draw.line(screen, colorRED, (startX, startY+a*math.sqrt(3)/2), (startX + a, startY+a*math.sqrt(3)/2), THICKNESS)
                pygame.draw.line(screen, colorRED, (startX, startY+a*math.sqrt(3)/2), (startX + a/2, startY), THICKNESS)
                pygame.draw.line(screen, colorRED, (startX + a/2, startY), (startX + a, startY+a*math.sqrt(3)/2), THICKNESS)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            endX, endY = pygame.mouse.get_pos()
            a=min(abs(startX - endX), abs(startY - endY))
            pygame.draw.line(screen, colorRED, (startX, startY+a*math.sqrt(3)/2), (startX + a, startY+a*math.sqrt(3)/2), THICKNESS)
            pygame.draw.line(screen, colorRED, (startX, startY+a*math.sqrt(3)/2), (startX + a/2, startY), THICKNESS)
            pygame.draw.line(screen, colorRED, (startX + a/2, startY), (startX + a, startY+a*math.sqrt(3)/2), THICKNESS)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

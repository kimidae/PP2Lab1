import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400


screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

LMBpressed = False
THICKNESS = 20
image=pygame.image.load("catingrass.png")
done = False
screen.blit(image, (0, 0))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:", event.pos)
            if LMBpressed:
                pygame.draw.rect(screen, colorBLACK, (event.pos[0], event.pos[1], THICKNESS, THICKNESS))
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1
    
    pygame.display.flip()
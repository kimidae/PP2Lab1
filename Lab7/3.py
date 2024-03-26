import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

done = False
pygame.mixer.music.load('white_space.mp3')
pygame.mixer.music.play(-1)

white = (255, 255, 255)

x=350
y=350
speed = 8 

sprite_down = pygame.image.load("sprite_down.png")
sprite_go_down1 = pygame.image.load("sprite_go_down1.png")
sprite_go_down2 = pygame.image.load("sprite_go_down2.png")
sprite_right = pygame.image.load("sprite_right.png")
sprite_go_right1 = pygame.image.load("sprite_go_right1.png")
sprite_go_right2 = pygame.image.load("sprite_go_right2.png")
sprite_left = pygame.image.load("sprite_left.png")
sprite_go_left1 = pygame.image.load("sprite_go_left1.png")
sprite_go_left2 = pygame.image.load("sprite_go_left2.png")
sprite_up = pygame.image.load("sprite_up.png")
sprite_go_up1 = pygame.image.load("sprite_go_up1.png")
sprite_go_up2 = pygame.image.load("sprite_go_up2.png")
background2 = pygame.image.load("bgsprite2.png")
background = pygame.image.load("bgsprite.png")

sprite_down = pygame.transform.scale(sprite_down, (sprite_down.get_width() * 2, sprite_down.get_height() * 2))
sprite_go_down1 = pygame.transform.scale(sprite_go_down1, (sprite_go_down1.get_width() * 2, sprite_go_down1.get_height() * 2))
sprite_go_down2 = pygame.transform.scale(sprite_go_down2, (sprite_go_down2.get_width() * 2, sprite_go_down2.get_height() * 2))
sprite_right = pygame.transform.scale(sprite_right, (sprite_right.get_width() * 2, sprite_right.get_height() * 2))
sprite_go_right1 = pygame.transform.scale(sprite_go_right1, (sprite_go_right1.get_width() * 2, sprite_go_right1.get_height() * 2))
sprite_go_right2 = pygame.transform.scale(sprite_go_right2, (sprite_go_right2.get_width() * 2, sprite_go_right2.get_height() * 2))
sprite_left = pygame.transform.scale(sprite_left, (sprite_left.get_width() * 2, sprite_left.get_height() * 2))
sprite_go_left1 = pygame.transform.scale(sprite_go_left1, (sprite_go_left1.get_width() * 2, sprite_go_left1.get_height() * 2))
sprite_go_left2 = pygame.transform.scale(sprite_go_left2, (sprite_go_left2.get_width() * 2, sprite_go_left2.get_height() * 2))
sprite_up = pygame.transform.scale(sprite_up, (sprite_up.get_width() * 2, sprite_up.get_height() * 2))
sprite_go_up1 = pygame.transform.scale(sprite_go_up1, (sprite_go_up1.get_width() * 2, sprite_go_up1.get_height() * 2))
sprite_go_up2 = pygame.transform.scale(sprite_go_up2, (sprite_go_up2.get_width() * 2, sprite_go_up2.get_height() * 2))

image = sprite_down
image_rect = image.get_rect()

key_right_pressed = False
key_left_pressed = False
key_up_pressed = False
key_down_pressed = False


clock = pygame.time.Clock()
screen.blit(background, (0, 0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT:
                key_right_pressed = True
                key_left_pressed = False
                key_up_pressed = False
                key_down_pressed = False
            elif event.key == pygame.K_LEFT:
                key_left_pressed = True
                key_right_pressed = False
                key_up_pressed = False
                key_down_pressed = False
            elif event.key == pygame.K_UP:
                key_up_pressed = True
                key_down_pressed = False
                key_left_pressed = False
                key_right_pressed = False
            elif event.key == pygame.K_DOWN:
                key_down_pressed = True
                key_up_pressed = False
                key_left_pressed = False
                key_right_pressed = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                key_right_pressed = False
                image = sprite_right
            elif event.key == pygame.K_LEFT:
                key_left_pressed = False
                image = sprite_left
            elif event.key == pygame.K_UP:
                key_up_pressed = False
                image = sprite_up
            elif event.key == pygame.K_DOWN:
                key_down_pressed = False
                image = sprite_down
    if key_right_pressed:
        image_rect = image.get_rect(topleft=(x, y))
        if image_rect.x < 800 - image.get_width():
            x += speed
        if pygame.time.get_ticks() % 600 < 150:
            image = sprite_go_right1
        elif pygame.time.get_ticks() % 600 < 300:
            image = sprite_right
        elif pygame.time.get_ticks() % 600 < 450:
            image = sprite_go_right2
        else:
            image = sprite_right
    elif key_left_pressed:
        image_rect = image.get_rect(topleft=(x, y))
        if image_rect.x > 0:
            x -= speed
        if pygame.time.get_ticks() % 600 < 150:
            image = sprite_go_left1
        elif pygame.time.get_ticks() % 600 < 300:
            image = sprite_left
        elif pygame.time.get_ticks() % 600 < 450:
            image = sprite_go_left2
        else:
            image = sprite_left
    elif key_up_pressed:
        image_rect = image.get_rect(topleft=(x, y))
        if image_rect.y > 0:
            y -= speed
        if pygame.time.get_ticks() % 600 < 150:
            image = sprite_go_up1
        elif pygame.time.get_ticks() % 600 < 300:
            image = sprite_up
        elif pygame.time.get_ticks() % 600 < 450:
            image = sprite_go_up2
        else:
            image = sprite_up
    elif key_down_pressed:
        image_rect = image.get_rect(topleft=(x, y))
        if image_rect.y < 600 - image.get_height():
            y += speed
        if pygame.time.get_ticks() % 600 < 150:
            image = sprite_go_down1
        elif pygame.time.get_ticks() % 600 < 300:
            image = sprite_down
        elif pygame.time.get_ticks() % 600 < 450:
            image = sprite_go_down2
        else:
            image = sprite_down
    
    if pygame.time.get_ticks() % 1000 < 500:
        screen.blit(background, (0, 0))
    else:
        screen.blit(background2, (0, 0))
    
    screen.blit(image, (x, y))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
COIN_SPEED=5
SCORE = 0
COINS=0
DIDGET=False

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 693):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(29,SCREEN_WIDTH-29), 0)
        while self.check_collision(enemies):
            self.rect.center = (random.randint(29,SCREEN_WIDTH-29), 0)

    def check_collision(self, enemies):
        return pygame.sprite.spritecollideany(self, enemies)


    

    def move(self):
        global COINS
        global DIDGET
        if not DIDGET:
            self.rect.move_ip(0,COIN_SPEED)
            if (self.rect.bottom > SCREEN_HEIGHT):
                self.rect.top = 0
                self.rect.center = (random.randint(29, SCREEN_WIDTH - 29), 0)
        else:
            self.rect.top = 0
            self.rect.center = (random.randint(29, SCREEN_WIDTH - 29), 0)
            DIDGET=False
            


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5-SPEED/2, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5+SPEED/2, 0)
        if self.rect.right > 0:        
              if pressed_keys[K_UP]:
                  self.rect.move_ip(0, -5-SPEED/2)
        if self.rect.right <SCREEN_HEIGHT:        
              if pressed_keys[K_DOWN]:
                  self.rect.move_ip(0, 5+SPEED/2)

enemies = pygame.sprite.Group()
coins_obj = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies.add(E1)
coins_obj.add(C1)

all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
      
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render( "Score: "+ str(SCORE), True, BLACK)
    coins = font_small.render("Coins: "+ str(COINS), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coins, (250,10))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        
    if pygame.sprite.spritecollideany(P1, coins_obj):
        COINS+=1
        DIDGET=True

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)
                
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        scores = font_small.render( "Score: "+ str(SCORE), True, BLACK)
        coins = font_small.render("Coins: "+ str(COINS), True, BLACK)
        DISPLAYSURF.blit(scores, (SCREEN_WIDTH/2-50, 400))
        DISPLAYSURF.blit(coins, (SCREEN_WIDTH/2-50, 420))
          
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(0.5)
        pygame.quit()
        sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)

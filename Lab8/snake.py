import pygame
from color_palette import *
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
FOOD_X=random.randint(0,19)
FOOD_Y=random.randint(0, 19)
CELL = 30
SCORE=0
LEVEL=1
SNAKE_SPEED=5
head_x=10
head_y=11
font_small = pygame.font.SysFont("Verdana", 20)

def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

screen = pygame.display.set_mode((HEIGHT, WIDTH))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    # def move(self):
    #     head = self.body[0]
    #     self.body.pop()

    #     new_x = head.x + self.dx
    #     new_y = head.y + self.dy

    #     new_head = Point(new_x, new_y)
    #     self.body.insert(0, new_head)

    def move(self):
            
            
            if self.body[0].x<19 and self.dx==1:
                
                for i in range(len(self.body) - 1, 0, -1):
                    self.body[i].x = self.body[i - 1].x
                    self.body[i].y = self.body[i - 1].y
                self.body[0].x += self.dx
            if self.body[0].x>0 and self.dx==-1:
                
                for i in range(len(self.body) - 1, 0, -1):
                    self.body[i].x = self.body[i - 1].x
                    self.body[i].y = self.body[i - 1].y
                self.body[0].x += self.dx
            if self.body[0].y<19 and self.dy==1:
                
                for i in range(len(self.body) - 1, 0, -1):
                    self.body[i].x = self.body[i - 1].x
                    self.body[i].y = self.body[i - 1].y
                self.body[0].y += self.dy
            if self.body[0].y>0 and self.dy==-1:
                
                for i in range(len(self.body) - 1, 0, -1):
                    self.body[i].x = self.body[i - 1].x
                    self.body[i].y = self.body[i - 1].y
                self.body[0].y += self.dy
            return self.body[0].x, self.body[0].y

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food, SCORE, LEVEL, FOOD_X, FOOD_Y):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            SCORE+=1
            LEVEL=1 + int(SCORE/3)
            FOOD_X=random.randint(0,19)
            FOOD_Y=random.randint(0, 19)
            self.body.append(Point(head.x, head.y))

        return LEVEL, SCORE, FOOD_X, FOOD_Y

class Food:
    def __init__(self):
        self.pos = Point(FOOD_X, FOOD_Y)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


FPS = 5
clock = pygame.time.Clock()

food = Food()
snake = Snake()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    draw_grid_chess()
    head_x, head_y = snake.move()
    LEVEL, SCORE, FOOD_X, FOOD_Y = snake.check_collision(food, SCORE, LEVEL, FOOD_X, FOOD_Y)
    food = Food()
    snake.draw()
    food.draw()
    scores = font_small.render( "Score: "+ str(SCORE), True, colorBLACK)
    level = font_small.render("Level: "+ str(LEVEL), True, colorBLACK)
    screen.blit(scores, (10,10))
    screen.blit(level, (450,10))
    pygame.display.flip()
    clock.tick(5+ LEVEL)
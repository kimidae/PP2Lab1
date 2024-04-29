import psycopg2
import pygame
from color_palette import *
import random
import time

newusername= input("Your username:  ")
print("To stop and save the game - press 's' key")

pygame.init()

WIDTH = 600
HEIGHT = 600
FOOD_X = random.randint(0, 19)
FOOD_Y = random.randint(0, 19)
CELL = 30

conn = psycopg2.connect(
    host='localhost',
    dbname='snake',
    user='postgres',
    password='040403'
)

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS snake_table (
        username VARCHAR(255) PRIMARY KEY,
        time VARCHAR(255),
        score INT,
        level INT,
        snake_speed INT,
        length INT
    )
''')

cur.execute('SELECT username FROM snake_table')
rows = cur.fetchall()

EXIST = False
for row in rows:
    if newusername in row:
        EXIST = True

SCORE = 0
LEVEL = 1
SNAKE_SPEED = 5
head_x = 10
head_y = 11
LENGTH=3
font_small = pygame.font.SysFont("Verdana", 20)
if EXIST:
    cur.execute('SELECT score, level, snake_speed, length FROM snake_table WHERE username=%s', (newusername, ))
    row = cur.fetchone()
    SCORE, LEVEL, SNAKE_SPEED, LENGTH = row

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
        self.body = [Point(10, 11)]
        for i in range (1, LENGTH):
            self.body.append(Point (10, 11+i))
        self.dx = 1
        self.dy = 0

    def move(self):
        if self.body[0].x < 19 and self.dx == 1:
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i].x = self.body[i - 1].x
                self.body[i].y = self.body[i - 1].y
            self.body[0].x += self.dx
        if self.body[0].x > 0 and self.dx == -1:
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i].x = self.body[i - 1].x
                self.body[i].y = self.body[i - 1].y
            self.body[0].x += self.dx
        if self.body[0].y < 19 and self.dy == 1:
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i].x = self.body[i - 1].x
                self.body[i].y = self.body[i - 1].y
            self.body[0].y += self.dy
        if self.body[0].y > 0 and self.dy == -1:
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
            SCORE += 1
            LEVEL = 1 + int(SCORE / 3)
            FOOD_X = random.randint(0, 19)
            FOOD_Y = random.randint(0, 19)
            for i in range(0, random.randint(1, 3)):
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
            elif event.key == pygame.K_s:
                done= True

    draw_grid_chess()
    head_x, head_y = snake.move()
    LEVEL, SCORE, FOOD_X, FOOD_Y = snake.check_collision(food, SCORE, LEVEL, FOOD_X, FOOD_Y)
    food = Food()
    snake.draw()
    food.draw()
    scores = font_small.render("Score: " + str(SCORE), True, colorBLACK)
    level = font_small.render("Level: " + str(LEVEL), True, colorBLACK)
    screen.blit(scores, (10, 10))
    screen.blit(level, (450, 10))
    pygame.display.flip()
    clock.tick(5 + LEVEL)
    LENGTH = len(snake.body)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if EXIST:
        cur.execute("""
            UPDATE snake_table 
            SET time = %s, score = %s, level = %s, snake_speed = %s, length = %s 
            WHERE username = %s
        """, (current_time, SCORE, LEVEL, SNAKE_SPEED, LENGTH, newusername))
    else:
        cur.execute("""
            INSERT INTO snake_table (username, time, score, level, snake_speed, length) 
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (username) DO UPDATE 
        SET time = %s, score = %s, level = %s, snake_speed = %s, length = %s
    """, (newusername, current_time, SCORE, LEVEL, SNAKE_SPEED, LENGTH, 
          current_time, SCORE, LEVEL, SNAKE_SPEED, LENGTH))

    conn.commit()

import csv

cur.execute("SELECT * FROM snake_table")
rows = cur.fetchall()
csv_file_path = "snake_table_data.csv"
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["username", "time", "score", "level", "snake_speed", "length"])
    for row in rows:
        writer.writerow(row)

print(f"All data has been exported to {csv_file_path}")

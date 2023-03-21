import pygame
import random
import math

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((500,500))



#food image
food = pygame.image.load('square.png')

def foodAppear():
    global foodX
    global foodY
    foodX = (random.randint(0,19)) *25
    foodY = (random.randint(0,19)) *25

foodAppear()    

def foodScreen():
    screen.blit(food,(foodX,foodY))

#background
background = pygame.image.load("background.png")

#snake image
snake = pygame.image.load('square (1).png')

snake_X_change = 25
snake_Y_change = 0

snake_array = [[25,0],[0,0]]

def snakeMove():
    global snake_array
    for i in range(len(snake_array)-1):
        s = len(snake_array)-1
        snake_array[s-i][0] = snake_array[s-i-1][0] 
        snake_array[s-i][1] = snake_array[s-i-1][1]
        snake_array[0][0] += snake_X_change
        snake_array[0][1] += snake_Y_change

    if(snake_array[0][0] >=  500):
        snake_array[0][0] = 0
        right()

    if(snake_array[0][0] < 0):
        snake_array[0][0] = 500
        left()

    if(snake_array[0][1] >= 500):
        snake_array[0][1] = 0
        down()

    if(snake_array[0][1] < 0):
        snake_array[0][1] = 500
        up()

def up():
    global snake_X_change
    global snake_Y_change
    snake_X_change = 0
    snake_Y_change = -25

def down():
    global snake_X_change
    global snake_Y_change
    snake_X_change = 0
    snake_Y_change = 25

def left():
    global snake_X_change
    global snake_Y_change
    snake_X_change = -25
    snake_Y_change = 0

def right():
    global snake_X_change
    global snake_Y_change
    snake_X_change = 25
    snake_Y_change = 0

def displaySnake() :
    for block in snake_array:
        screen.blit(snake,(block))

def foodAte():
    foodAppear() 
    snake_array.append([0,0])
    snake_array[len(snake_array)-1][0] = snake_array[len(snake_array)-2][0]
    snake_array[len(snake_array)-1][1] = snake_array[len(snake_array)-2][1]

def colisionCheck():
    for i in range (1,len(snake_array)):
        if snake_array[0][1] == snake_array[i][1] and snake_array[0][0] == snake_array[i][0] :
            global running
            running = False


#collision detection between food and snake
def isCollision():
    global foodX
    global foodY
    distance =  math.sqrt(math.pow((snake_array[0][0] - foodX),2) + math.pow((snake_array[0][1] - foodY),2))
    if distance < 15:
        return True
    return False


count = 0

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        #if keystroke is pressend check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left()
            if event.key == pygame.K_RIGHT:
                right()
            if event.key == pygame.K_UP:
                up()
            if event.key == pygame.K_DOWN:
                down()

    count += 1
    if count==25 : 
        snakeMove()
        count = 0
        print(snake_array)

    if(isCollision()):
        print("kusdiughsiogsligjsglisgihgihgg")
        foodAte()

    colisionCheck()
    if(count == 0):
        print(snake_array)

    #RGB - Red, Green ,Blue
    screen.fill((0,0,0))
    #background image
    screen.blit(background,(-200,-60))

    displaySnake()
    foodScreen()

    pygame.display.update()



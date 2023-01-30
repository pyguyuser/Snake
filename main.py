import pygame

X,Y = (700,700)
DISPLAY = pygame.display.set_mode((X,Y))

SNAKE_COLOR =  (0, 0, 200)
SNAKE_SIZE = 50
SNAKE_SPEED = 10

class Snake_Head:

    def __init__(self, color, size, speed,display,x,y,index):
        self.SIZE = size
        self.COLOR = color
        self.SPEED = speed
        self.X = x
        self.Y = y
        self.DISPLAY = display
        self.index = index

    cord_x,cord_y = (100, 350)
    list_value = [False, False, False, False]
    list_value_old = None

    def set_value(self,number):
        self.list_value_old = [i for i in self.list_value]

        for num in range(len(self.list_value)):
            self.list_value[num] = False
        self.list_value[number] = True

        print(self.list_value_old)

    def update(self):
        snake_surface = pygame.Surface((self.SIZE, self.SIZE))
        snake_cords = snake_surface.get_rect(center=(self.cord_x, self.cord_y))

        if self.list_value[0]:
            self.cord_x -= self.SPEED
        elif self.list_value[1]:
            self.cord_y -= self.SPEED
        elif self.list_value[2]:
            self.cord_y += self.SPEED
        elif self.list_value[3]:
            self.cord_x += self.SPEED

        # if self.cord_x+(self.SIZE//2) > self.X:
        #     self.cord_x = self.SIZE//2
        # if self.cord_x+(self.SIZE//2) < self.X:
        #     self.cord_x = self.SIZE//2
        # if self.cord_x+(self.SIZE//2) > self.X:
        #     self.cord_x = self.SIZE//2
        # if self.cord_x+(self.SIZE//2) > self.X:
        #     self.cord_x = self.SIZE//2

        snake_surface.fill('green')
        self.DISPLAY.blit(snake_surface, snake_cords)




snake = Snake_Head(SNAKE_COLOR,SNAKE_SIZE,SNAKE_SPEED,DISPLAY,X,Y,0)
time = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.set_value(1)
            elif event.key == pygame.K_DOWN:
                snake.set_value(2)
            elif event.key == pygame.K_LEFT:
                snake.set_value(0)
            elif event.key == pygame.K_RIGHT:
                snake.set_value(3)

    DISPLAY.fill('black')
    snake.update()

    time.tick(60)
    pygame.display.update()

pygame.quit()
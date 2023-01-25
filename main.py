import pygame

class Snake:
    def __init__(self,color,x,y):
        self.COLOR = color
        self.X = x
        self.Y = y
        self.display = pygame.display.set_mode((self.X,self.Y))

    def update(self):
        pass

snake = Snake((0,0,255),700,700)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    snake.update()

    pygame.display.update()

pygame.quit()
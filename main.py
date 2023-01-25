import pygame

class Snake:
    def __init__(self,color,x,y):
        self.COLOR = color
        self.X = x
        self.Y = y
        self.DISPLAY = pygame.display.set_mode((self.X,self.Y))

        self.SIZE_SNAKE_BODY = (25, 25)

        self.VECTOR = 0



    def update(self):
        self.SNAKE_BODY = pygame.Surface(self.SIZE_SNAKE_BODY)
        self.INIT_CORDS = self.SNAKE_BODY.get_rect(center=(self.X // 2 - 100, self.Y // 2))
        self.SNAKE_BODY.fill(self.COLOR)
        self.DISPLAY.blit(self.SNAKE_BODY,self.INIT_CORDS)

        if self.VECTOR == 1:
            self.Y-=5


snake = Snake((0,0,255),700,700)
pygame.display.set_caption("Snake")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.VECTOR = 1

    snake.update()

    pygame.display.update()

pygame.quit()
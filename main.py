import pygame,random






class Snake_Head:
    def __init__(self, color, size, speed,display,x,y):
        self.SIZE = size
        self.COLOR = color
        self.SPEED = speed
        self.X = x
        self.Y = y
        self.DISPLAY = display

    ACTIVE = False
    x,y = (300,200)
    x_,y_ = (270, 200)

    list_value = [False, False, False, False]

    # tail
    tail = []
    corners = []

    def set_value(self,number):
        self.list_value = [i==number for i in range(4)]

        if self.ACTIVE:self.corners.append((self.x, self.y))
        self.ACTIVE =  True

    def add_segment(self):
        self.tail.append(Segment("red",self.SIZE,self.SPEED,self.DISPLAY))


    def head_up(self):
        snake_surface = pygame.Surface((self.SIZE, self.SIZE))
        snake_cords = snake_surface.get_rect(center=(self.x, self.y))

        if self.list_value[0]:self.x -= self.SPEED
        elif self.list_value[1]:self.y -= self.SPEED
        elif self.list_value[2]:self.y += self.SPEED
        elif self.list_value[3]:self.x += self.SPEED

        snake_surface.fill('blue')
        self.DISPLAY.blit(snake_surface, snake_cords)

        # x,y = (self.x-35,self.y)
        # for i in self.tail:
        #     i.render((x,y))
        #     x-=35


        if len(self.corners)==0:
            if self.x_ == self.x:
                if self.list_value[1]:self.y_ -= self.SPEED
                elif self.list_value[2]:self.y_+=self.SPEED
            elif self.y_ == self.y:
                if self.list_value[0]:self.x_ -= self.SPEED
                elif self.list_value[3]:self.x_+=self.SPEED
        else:

            if self.x_<self.corners[0][0]:self.x_+=self.SPEED
            elif self.x_>self.corners[0][0]:self.x_-=self.SPEED
            elif self.y_<self.corners[0][1]:self.y_+=self.SPEED
            elif self.y_>self.corners[0][1]:self.y_-=self.SPEED

            if (self.x_,self.y_) == self.corners[0]:
                del self.corners[0]

            # sur = pygame.Surface((30, 30))
            # sur.fill("blue")
            # sur.blit(self.DISPLAY, self.corners[0])

        if len(self.tail)!=0:self.tail[0].render((self.x_,self.y_))



class Segment():
    def __init__(self,color,size,speed,display):
        self.COLOR = color
        self.SIZE = size
        self.SPEED  = speed
        self.DISPLAY = display

    def render(self,coords):
        surf = pygame.Surface((self.SIZE, self.SIZE))
        rect = surf.get_rect(center=coords)

        surf.fill(self.COLOR)
        self.DISPLAY.blit(surf, rect)





def main():
    X,Y = (700,700)
    DISPLAY = pygame.display.set_mode((X,Y))

    SNAKE_COLOR =  (0, 0, 200)
    SNAKE_SIZE = 30
    SNAKE_SPEED = 5
    snake = Snake_Head(SNAKE_COLOR,SNAKE_SIZE,SNAKE_SPEED,DISPLAY,X,Y)

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

                if event.key == pygame.K_KP_PLUS:
                    snake.add_segment()

        DISPLAY.fill('black')
        snake.head_up()

        time.tick(60)
        pygame.display.update()

    pygame.quit()





if __name__ == "__main__":
    main()
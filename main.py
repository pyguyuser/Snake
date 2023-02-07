import pygame,random

class Snake_Head:
    def __init__(self, color, size,display,x,y):
        self.SIZE = size
        self.COLOR = color
        self.STEP = 1
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
    count_complete = 0

    def set_value(self,number):
        self.list_value = [i==number for i in range(4)]

        if self.ACTIVE:
            self.corners.append((self.x, self.y))
        self.ACTIVE =  True

    def coords_gen(self,x,y,list):
        if list[0]:x += 40
        elif list[1]:y += 40
        elif list[2]:y -= 40
        elif list[3]:x -= 40

        return (x,y)

    def add_segment(self):
        if len(self.tail) == 0:
            self.tail.append(Segment("red", self.SIZE, self.DISPLAY, self.coords_gen(self.x,self.y,self.list_value)))
        else:
            last_seg = self.tail[-1]
            self.tail.append(Segment("red", self.SIZE, self.DISPLAY,self.coords_gen(last_seg.x,last_seg.y,last_seg.vector)))


    def move_segments(self,item):
        if len(self.corners) == 0:

            # LEFT
            if self.list_value[0]:
                item.x -= self.STEP
                item.vector = [True, False, False, False]

            # UP
            elif self.list_value[1]:
                item.y -= self.STEP
                item.vector = [False, True, False, False]

            # DOWN
            elif self.list_value[2]:
                item.y += self.STEP
                item.vector = [False, False, True, False]

            #RIGHT
            elif self.list_value[3]:
                item.x += self.STEP
                item.vector = [False, False, False, True]

        else:
            if item.x < self.corners[0][0]:
                item.x += self.STEP
                item.vector = [False, False, False, True]

            elif item.x >  self.corners[0][0]:
                item.x -= self.STEP
                item.vector = [True, False, False, False]

            elif item.y < self.corners[0][1]:
                item.y += self.STEP
                item.vector = [False, False, True, False]

            elif item.y > self.corners[0][1]:
                item.y -= self.STEP
                item.vector = [False, True, False, False]

            else:
                self.count_complete += 1


    def body(self):
        sur = pygame.Surface((self.SIZE,self.SIZE))
        coords = sur.get_rect(center = (self.x,self.y))

        if self.list_value[0]:
            self.x -= self.STEP
        elif self.list_value[1]:
            self.y -= self.STEP
        elif self.list_value[2]:
            self.y += self.STEP
        elif self.list_value[3]:
            self.x += self.STEP

        sur.fill(self.COLOR)
        self.DISPLAY.blit(sur,coords)


        for i in self.tail:
            if self.count_complete == len(self.tail):
                self.corners = []
                self.count_complete = 0
            self.move_segments(i)
            i.render()


class Segment():
    def __init__(self,color,size,display,direction):
        self.COLOR = color
        self.SIZE = size
        self.DISPLAY = display
        self.x,self.y = direction

    vector = [False,False,False,False]

    def render(self):
        surf = pygame.Surface((self.SIZE, self.SIZE))
        rect = surf.get_rect(center=(self.x,self.y))

        surf.fill(self.COLOR)
        self.DISPLAY.blit(surf, rect)

def main():
    X,Y = (700,700)
    DISPLAY = pygame.display.set_mode((X,Y))

    SNAKE_COLOR =  (0, 0, 200)
    SNAKE_SIZE = 30
    snake = Snake_Head(SNAKE_COLOR,SNAKE_SIZE,DISPLAY,X,Y)

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
        snake.body()

        time.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
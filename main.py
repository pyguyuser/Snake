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

    def set_value(self,number):
        self.list_value = [i==number for i in range(4)]

        if self.ACTIVE:
            self.corners.append((self.x, self.y))
            for seg in self.tail:
                seg.corners.append((self.x, self.y))
        self.ACTIVE =  True


    #
    def add_segment(self):
        if len(self.tail)==0:
            self.tail.append(Segment("red",self.SIZE,self.DISPLAY,(self.x,self.y,self.list_value,self.corners)))
        else:
            last_seg = self.tail[-1]
            self.tail.append(Segment("red", self.SIZE, self.DISPLAY,(last_seg.x,last_seg.y,last_seg.vector,last_seg.corners)))


    def move_segments(self,seg1,seg2):
        if len(self.corners) == 0:

            if seg1.corners[1]:seg2.y -= self.STEP

            elif seg1.corners[2]:seg2.y += self.STEP

            elif seg1.corners[0]:seg2.x -= self.STEP

            elif seg1.corners[3]:seg2.x += self.STEP

        else:

            if seg2.x < seg1.corners[0][0]:seg2.x += self.STEP

            elif seg2.x >  seg1.corners[0][0]:seg2.x -= self.STEP

            elif seg2.y < seg1.corners[0][1]:seg2.y += self.STEP

            elif seg2.y > seg1.corners[0][1]:seg2.y -= self.STEP

        if (seg2.x,seg2.y) == seg1.corners[0]:
            del seg1.corners[0]



    def head_up(self):
        snake_surface = pygame.Surface((self.SIZE, self.SIZE))
        snake_cords = snake_surface.get_rect(center=(self.x, self.y))

        if self.list_value[0]:self.x -= self.STEP
        elif self.list_value[1]:self.y -= self.STEP
        elif self.list_value[2]:self.y += self.STEP
        elif self.list_value[3]:self.x += self.STEP

        snake_surface.fill('blue')
        self.DISPLAY.blit(snake_surface, snake_cords)

        if len(self.tail) > 2:
            for i in range(0,len(self.tail)):


                self.move_segments(self.tail[i],self.tail[i+1])
                self.tail[i].render()



class Segment():
    def __init__(self,color,size,display,direction):
        self.COLOR = color
        self.SIZE = size
        self.DISPLAY = display
        self.x,self.y,self.vector,self.corners = direction

    def render(self):
        surf = pygame.Surface((self.SIZE, self.SIZE))
        rect = surf.get_rect(center=(self.x-40,self.y))

        surf.fill(self.COLOR)
        self.DISPLAY.blit(surf, rect)

    #
    def update(self):
        pass






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
        snake.head_up()

        time.tick(60)
        pygame.display.update()

    pygame.quit()





if __name__ == "__main__":
    main()
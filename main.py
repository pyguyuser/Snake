import pygame

X,Y = (700,700)
DISPLAY = pygame.display.set_mode((X,Y))

SNAKE_COLOR =  (0, 0, 200)
SNAKE_SIZE = 25
SNAKE_SPEED = 10

THRASHOLD = 0.01


class Segment:
    def __init__(self, color, size, speed,display,x,y,index,direction):
        self.SIZE = size
        self.COLOR = color
        self.SPEED = speed
        self.x = x
        self.y = y
        self.DISPLAY = display
        self.index = index
        self.direction1 = direction

        self.surf = pygame.Surface((self.SIZE, self.SIZE))
        self.surf.fill(self.COLOR)

    direction0 = [None,None,None,None]
    checkpoints = []


    # def create(self):
    #     seg = pygame.Surface((self.SIZE, self.SIZE))
    #     seg.fill('blue')
    #     self.tail.append(seg)

    def update(self):
        if len(self.checkpoints) < 1:
            return
        x,y,new_direction = self.checkpoints[-1]
        r = ((self.y-y)**2+(self.x-x)**2)**0.5
        if r<= THRASHOLD:
            print(f'r=={r}')
            self.direction0 = [i for i in self.direction1]
            self.direction1 = new_direction
            self.checkpoints.pop()




    def render(self):
        self.update()
        coord = self.surf.get_rect(center=(self.x, self.y))
        # snake_surface = pygame.Surface((self.SIZE, self.SIZE))
        # snake_cords = snake_surface.get_rect(center=(self.x, self.y))

        if self.direction1[0]:self.x -= self.SPEED
        elif self.direction1[1]:self.y -= self.SPEED
        elif self.direction1[2]:self.y += self.SPEED
        elif self.direction1[3]:self.x += self.SPEED

        self.DISPLAY.blit(self.surf, coord)

class Snake_Head:

    def __init__(self, color, size, speed,display,x,y,index):
        self.SIZE = size
        self.COLOR = color
        self.SPEED = speed
        self.X = x
        self.Y = y
        self.DISPLAY = display
        self.index = index

    ACTIVE = False
    x,y = (100, 350)
    s_x, s_y = (x, y)
    count = 0

    list_value = [False, False, False, False]
    list_value_old = [False, False, False, False]

    # tail
    tail = []
    list = []

    def set_value(self,number):
        self.list_value = [i==number for i in range(4)]
        self.list_value_old = [i for i in self.list_value]
        self.add_checkpoint()

        # for num in range(len(self.list_value)):
        #     if self.list_value[num]:self.list.append((self.x,self.y))
        #     self.list_value[num] = False
        # self.list_value[number] = True
        self.ACTIVE = True

    def grow(self):
        print("bigger snake!")
        self.add_segment()

    def add_segment(self):

        self.count+=1
        seg = Segment('blue', self.SIZE, self.SPEED,self.DISPLAY,self.x-25,self.y,self.count,self.list_value_old)
        # seg = pygame.Surface((self.SIZE, self.SIZE))
        # seg.fill('blue')
        self.tail.append(seg)

    def add_checkpoint(self):
        for seg in self.tail:
            seg.checkpoints.append((self.x,self.y,self.list_value_old))


    def head_up(self):
        snake_surface = pygame.Surface((self.SIZE, self.SIZE))
        snake_cords = snake_surface.get_rect(center=(self.x, self.y))

        if self.list_value[0]:self.x -= self.SPEED
        elif self.list_value[1]:self.y -= self.SPEED
        elif self.list_value[2]:self.y += self.SPEED
        elif self.list_value[3]:self.x += self.SPEED

        # if self.x+(self.SIZE//2) > self.X:
        #     self.x = self.SIZE//2
        # if self.x+(self.SIZE//2) < self.X:
        #     self.x = self.SIZE//2
        # if self.x+(self.SIZE//2) > self.X:
        #     self.x = self.SIZE//2
        # if self.x+(self.SIZE//2) > self.X:
        #     self.x = self.SIZE//2

        snake_surface.fill('green')
        self.DISPLAY.blit(snake_surface, snake_cords)

        for seg in self.tail:
            seg.render()


    def seg_up(self):
        segment = pygame.Surface((self.SIZE, self.SIZE))

        if self.ACTIVE:
            if len(self.list)==0:
                for i in range(len(self.list_value)):
                    if self.list_value[i]:
                        if i == 0: vector = (self.x-(self.SIZE+10),self.y)
                        elif i == 1: vector = (self.x,self.y-(self.SIZE+10))
                        elif i == 2: vector = (self.x,self.y+(self.SIZE+10))
                        elif i == 3: vector = (self.x+(self.SIZE+10),self.y)
                        self.point = vector
            else:
                for i in range(len(self.list_value_old)):
                    if self.list_value_old[i]:
                        if i == 0: vector = (self.point[0]-(self.SPEED+(self.SIZE+10)),self.point[1])
                        elif i == 1: vector = (self.point[0],self.point[1]-(self.SPEED+(self.SIZE+10)))
                        elif i == 2: vector = (self.point[0],self.point[1]+(self.SPEED-(self.SIZE+10)))
                        elif i == 3: vector = (self.point[0]+(self.SPEED-(self.SIZE+10)),self.point[1])

                if self.list[0] == vector:
                    del self.list[0]
            # print(self.list)
            segment_coords = segment.get_rect(center=vector)
            segment.fill('green')
            self.DISPLAY.blit(segment,segment_coords)

        # x,y = (self.s_x,self.s_y)
        # for i in range(1):
        #     segment = pygame.Surface((self.SIZE, self.SIZE))
        #
        #     if self.s_x == self.x or self.s_y == self.y:
        #         for i in (0, len(self.list_value) - 1):
        #             if self.list_value[i]:
        #                 if i == 0: self.s_x -= self.SPEED
        #                 elif i == 1: self.s_y -= self.SPEED
        #                 elif i == 2: self.s_y += self.SPEED
        #                 elif i == 3: self.s_x += self.SPEED
        #     else:
        #         for i in (0,len(self.list_value_old)-1):
        #             if self.list_value_old[i]:
        #                 if i == 0: self.s_x -= self.SPEED
        #                 elif i == 1: self.s_y -= self.SPEED
        #                 elif i == 2: self.s_y += self.SPEED
        #                 elif i == 3: self.s_x += self.SPEED
        #
        #     segment_coords = segment.get_rect(center=(x-(self.SIZE+10),y))
        #     segment.fill('green')
        #     self.DISPLAY.blit(segment,segment_coords)
        #
        #     x = x-(self.SIZE+10)


snake = Snake_Head(SNAKE_COLOR,SNAKE_SIZE,SNAKE_SPEED,DISPLAY,X,Y,0)
time = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            snake.grow()
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            # snake.add_checkpoint()
            if event.key == pygame.K_UP:
                snake.set_value(1)
            elif event.key == pygame.K_DOWN:
                snake.set_value(2)
            elif event.key == pygame.K_LEFT:
                snake.set_value(0)
            elif event.key == pygame.K_RIGHT:
                snake.set_value(3)

    DISPLAY.fill('black')

    # snake.seg_up()
    snake.head_up()



    time.tick(60)
    pygame.display.update()

pygame.quit()
import pygame

X,Y = (700,700)
DISPLAY = pygame.display.set_mode((X,Y))

SNAKE_COLOR =  (0, 0, 200)
SNAKE_SIZE = 25
SNAKE_SPEED = 1

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
        self.list_value_old = [i for i in self.list_value]

        for num in range(len(self.list_value)):
            if self.list_value[num]:self.list.append((self.x,self.y))
            self.list_value[num] = False
        self.list_value[number] = True
        self.ACTIVE = True

    def grow(self):
        print("bigger snake!")
        self.add_segment()

    def add_segment(self):
        seg = pygame.Surface((self.SIZE, self.SIZE))
        seg.fill('blue')
        self.tail.append(seg)


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
            coord = seg.get_rect(center=(self.x + 20 * self.count, self.y + 20 * self.count))
            self.DISPLAY.blit(seg, coord)

        # print(self.list)


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
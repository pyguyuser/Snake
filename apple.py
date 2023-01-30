import pygame, random

class Apple:
    def __init__(self, x, y, color, display, disp_x, disp_y):
        self.X = x
        self.Y = y
        self.DISP_X = disp_x
        self.DISP_Y = disp_y
        self.DISPLAY = display
        self.COLOR = color

    def set_coords(self):
        self.coords = (random.randint(0, self.DISP_X - (self.X // 2)), random.randint(0, self.DISP_Y) - (self.Y // 2))

    def update(self):
        apple = pygame.Surface((self.X, self.Y))
        apple_coords = apple.get_rect(center=self.coords)

        apple.fill(self.COLOR)
        self.DISPLAY(apple, apple_coords)
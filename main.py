import pygame,random,time,json
from  glow import colormix
pygame.init()

def main():

    # static values
    SCR_SIZE = (500,500)
    SCORE = 0
    SIZE = 20

    src = pygame.display.set_mode(SCR_SIZE)
    x,y = (random.randrange(0,SCR_SIZE[0]-SIZE,SIZE),random.randrange(0,SCR_SIZE[0]-SIZE,SIZE))
    coords = [(x, y)]
    nx, ny = (0, 0)
    lenth = 1

    real_coords = (random.randrange(0, SCR_SIZE[0] - SIZE * 2, SIZE), random.randrange(0, SCR_SIZE[0] - SIZE * 2, SIZE))
    apple = (random.randrange(0, SCR_SIZE[0] - SIZE, SIZE), random.randrange(0, SCR_SIZE[0] - SIZE, SIZE))

    fps = 10
    run = True

    # values for real apple
    value = 1
    WON = 1000
    time = []

    # values for stones
    coords_stones = []

    # logic of game
    while run:

        pygame.display.set_caption(f"Score: {SCORE}")
        src.fill("black")

        # spawn all objects
        [(pygame.draw.line(src,(50,50,50),(xy,0),(xy,SCR_SIZE[0])),pygame.draw.line(src,(50,50,50),(0,xy),(SCR_SIZE[0],xy))) for xy in range(0,SCR_SIZE[0],SIZE)]
        pygame.draw.rect(src, (200, 0, 0), (*apple, SIZE, SIZE))
        [(pygame.draw.rect(src,(0,200,0),(x,y,SIZE,SIZE))) for x,y in coords]
        [(pygame.draw.rect(src, (110,110,110), (x, y, SIZE, SIZE))) for x, y in coords_stones]


        # movement
        x += nx * SIZE
        y += ny * SIZE

        # control over a coords
        coords.append((x,y))
        coords = coords[-lenth:]

        # interaction with real apple
        if random.randint(0,2000) == 0 and value == 1:value = 2
        if value == 2:
            if not real_apple(src,SIZE,real_coords,colormix(),coords):
                value = 3
                SCORE += WON
            elif len(set(time)) == 5:
                value = 3

            time.append(real_apple(src,SIZE,real_coords,colormix(),coords))

        # interaction with default apple
        for coord in coords:
            if coord == apple:
                apple = (random.randrange(0,SCR_SIZE[0]-SIZE,SIZE),random.randrange(0,SCR_SIZE[0]-SIZE,SIZE))
                while True:
                    for i in coords_stones:
                        if apple == i:
                            apple = (random.randrange(0, SCR_SIZE[0] - SIZE, SIZE),random.randrange(0, SCR_SIZE[0] - SIZE, SIZE))
                            break
                    else:
                        break

                coords_stones.append(stone(SCR_SIZE,SIZE,apple,coords,(nx,ny)))

                lenth += 1
                # fps += 1
                SCORE += 10

            elif ((real_coords or (real_coords[0]+SIZE,real_coords[1]) or (real_coords[0]+SIZE,real_coords[1]+SIZE) or (real_coords[0],real_coords[1]+SIZE)) == apple) and value == 2:
                apple = (random.randrange(0, SCR_SIZE[0] - SIZE, SIZE), random.randrange(0, SCR_SIZE[0] - SIZE, SIZE))
                WON += 10

        for st in coords_stones:
            if ((real_coords or (real_coords[0] + SIZE, real_coords[1]) or (real_coords[0] + SIZE, real_coords[1] + SIZE) or (real_coords[0], real_coords[1] + SIZE)) == stone) and value == 2:
                WON -= 10
                coords_stones.remove(st)

        # interaction with walls
        if coords[-1][0]>=SCR_SIZE[0]:
            x = 0
        elif coords[-1][0]<0:
            x = SCR_SIZE[0]
        elif coords[-1][1]>=SCR_SIZE[0]:
            y = 0
        elif coords[-1][1]<0:
            y = SCR_SIZE[0]

        # game over
        if len(coords) != len(set(coords)):
            if not game_over(SCORE):
                return False
            return True


        for i in coords_stones:
            for ic in coords:
                if ic == i:
                    if not game_over(SCORE):
                        return False
                    return True

        pygame.display.update()
        pygame.time.Clock().tick(fps)

        # all events
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                return  False
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    if not game_over(SCORE):
                        return False
                    return True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and nx != 1:
            nx, ny = (-1, 0)
        elif keys[pygame.K_RIGHT] and nx != -1:
            nx, ny = (1, 0)
        elif keys[pygame.K_UP] and ny != 1:
            nx, ny = (0, -1)
        elif keys[pygame.K_DOWN] and ny != -1:
            nx, ny = (0, 1)

def real_apple(screen,size,coords,color,snake_coords):

    apple_top = pygame.Surface((size*2,size*2))
    apple_body = apple_top.get_rect(topleft=coords)

    for i in snake_coords:
        if apple_body.collidepoint(i):
            return False

    apple_top.fill(color)
    screen.blit(apple_top,apple_body)

    return time.asctime().split(" ")[3].split(":")[2]

def stone(src_size,size,apple,coords,vector):

    head = coords[-1]
    for i in range(1,6):
        cx,cy = (head[0]+i*(size*vector[0]),head[1]+i*(size*vector[1]))
        if cx>src_size[0]:cx -= src_size[0]
        elif cx<0: cx += src_size[0]
        if cy>src_size[1]:cy -= src_size[1]
        elif cy<0:cy += src_size[1]

        coords.append((cx,cy))

    sc = (random.randrange(0, src_size[0] - size, size), random.randrange(0, src_size[0] - size, size))
    while True:
        for i in coords:
            if sc == i or sc == apple:
                sc = (random.randrange(0, src_size[0] - size, size), random.randrange(0, src_size[0] - size, size))
                break
        else:
            break

    for i in range(1,6):del coords[-1]
    return sc

def col_change(button,coords):
    if coords.collidepoint(pygame.mouse.get_pos()):
        button.fill("white")
    else:
        button.fill("grey")

def press_test(coords,event):
    if coords.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        return  True
    else:
        return  False

def records(size):
    W,H = size

    display = pygame.display.set_mode((W, H))

    rec = pygame.font.SysFont('arial', 40, True).render("Records", 1, "red")
    with open("scores.json","r") as file:
        all = json.load(file)

    done_all = []
    for i,v in enumerate(all):
        done_all.append((i+1,v[f"{i+1}"]))

    run = True
    while run:
        for i in pygame.event.get():
            if i.type ==pygame.QUIT:
                return False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    return True

        display.fill("black")
        display.blit(rec, rec.get_rect(center=(W // 2, H - 400)))

        y = 355
        for i,v in done_all:
            text = pygame.font.SysFont('arial', 20).render(f"{v}", 1, "yellow")
            display.blit(text, text.get_rect(center=(W // 2, H - y)))
            y-=30

        pygame.display.update()
        pygame.time.Clock().tick(60)


def scores(num):
    with open("scores.json","r",encoding="utf-8") as file:
        js = json.load(file)
    for i in range(0,len(js)):
        if js[i][f"{i+1}"] == num:
            break
        elif int(js[i][f"{i+1}"]) < num:
            for itm in range(1,len(js)-i):
                js[-itm][f"{len(js)+1-itm}"]=js[-itm-1][f"{len(js)+1+(-itm-1)}"]
            js[i][f"{i + 1}"] = num
            with open("scores.json","w",encoding="utf-8") as file:
                file.write(json.dumps(js,ensure_ascii=3))
            return

def menu():
    W,H = 500,500

    display = pygame.display.set_mode((W,H))
    pygame.display.set_caption("Snake")

    item = pygame.image.load("bg.png")

    w,h = (150,50)
    buttons =[
        pygame.Surface((w,h)),pygame.Surface((w,h)),pygame.Surface((w,h)),
    ]

    b_coords = [
        buttons[0].get_rect(center=(W//2,H//2-25)),buttons[1].get_rect(center=(W//2,H//2+40)),
        buttons[2].get_rect(center=(W//2,H//2+105)),
    ]

    text = [
        pygame.font.SysFont('arial', 25,True).render("Play", 1, "black"),pygame.font.SysFont('arial', 25,True).render("Records", 1, "black"),
        pygame.font.SysFont('arial', 25,True).render("Exit", 1, "black"),pygame.font.SysFont('Times New Roman', 75,True,True).render("Snake", 1, "red")

    ]

    run = True
    while run:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False

            elif press_test(b_coords[0],i):
                run = main()
                if run:
                    display = pygame.display.set_mode((W, H))
                    pygame.display.set_caption("Snake")

            elif press_test(b_coords[1], i):
                run = records((W,H))

            elif press_test(b_coords[2],i):
                run = False

        if not run:break

        display.fill("black")
        display.blit(item,(0,0))


        col_change(buttons[0],b_coords[0])
        col_change(buttons[1],b_coords[1])
        col_change(buttons[2],b_coords[2])

        [buttons[0].blit(text[0],text[0].get_rect(center=(w//2,h//2))),display.blit(buttons[0],b_coords[0]),
         buttons[1].blit(text[1], text[1].get_rect(center=(w // 2, h // 2))), display.blit(buttons[1], b_coords[1]),
         buttons[2].blit(text[2], text[2].get_rect(center=(w // 2, h // 2))), display.blit(buttons[2], b_coords[2]),


         display.blit(text[3], text[3].get_rect(center=(W // 2, H // 2-155)))]


        pygame.display.update()
        pygame.time.Clock().tick(60)

def game_over(score):
    scores(score)

    W, H = 500, 500

    display = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Snake")

    go = pygame.font.SysFont('arial', 40, True).render("Game Over", 1, "red")
    sc = pygame.font.SysFont('arial', 25, True).render(f"Score: {score}", 1, "yellow")

    run = True
    while run:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                return False

            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    return True

        display.fill("black")

        display.blit(go,go.get_rect(center=(W//2,H-375)))
        display.blit(sc, sc.get_rect(center=(W // 2, H - 325)))

        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    menu()
    pygame.quit()
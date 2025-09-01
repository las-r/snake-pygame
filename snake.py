import argparse
import pygame
import random
import time

# made by las-r on github
# v1.0

# init pygame
pygame.init()
font = pygame.font.SysFont("Roboto Mono", 16)

# arg parser
prsr = argparse.ArgumentParser(prog="Snake", description="Simple snake game written in Python")
prsr.add_argument("-DS", "--displaysize", type=int, nargs=2, default=[800, 600], help="Display dimensions in pixels (default: 800 600)")
prsr.add_argument("-GS", "--gridsize", type=int, nargs=2, default=[40, 30], help="Game grid dimensions (default: 40 30)")
prsr.add_argument("-SHC", "--snakeheadcolor", type=int, nargs=3, default=[0, 191, 0], help="Snake head color as R,G,B (default: 0 191 0)")
prsr.add_argument("-SC", "--snakecolor", type=int, nargs=3, default=[0, 127, 0], help="Snake body color as R,G,B (default: 0 127 0)")
prsr.add_argument("-AC", "--applecolor", type=int, nargs=3, default=[255, 0, 0], help="Apple color as R,G,B (default: 255 0 0)")
prsr.add_argument("-T", "--tick", type=float, default=0.1, help="Time between each game tick in seconds (default: 0.1)")
prsr.add_argument("-GT", "--gametype", choices=["normal", "warp"], default="normal", help="Game type (default: normal)")
prsr.add_argument("-HS", "--hidescore", action="store_true", help="Hide score counter")
args = prsr.parse_args()

# settings
DISPW, DISPH = args.displaysize
GRIDW, GRIDH = args.gridsize
TILEW, TILEH = DISPW // GRIDW, DISPH // GRIDH
SNKHDCOL = tuple(args.snakeheadcolor)
SNKCOL = tuple(args.snakecolor)
APLCOL = tuple(args.applecolor)
TICK = args.tick
GMTYP = args.gametype
HDSCR = args.hidescore

# variables
snk = [[GRIDW // 3, GRIDH // 2]]
snkdir = (1, 0)
apl = [GRIDW // 2, GRIDH // 2]
score = 0

# display
screen = pygame.display.set_mode((DISPW, DISPH))
pygame.display.set_caption("Snake")

# main loop
run = True
while run:
    # events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        
        # movement
        if e.type == pygame.KEYDOWN:
            if e.key in (pygame.K_w, pygame.K_UP) and snkdir[1] != 1:
                snkdir = (0, -1)
            elif e.key in (pygame.K_s, pygame.K_DOWN) and snkdir[1] != -1:
                snkdir = (0, 1)
            elif e.key in (pygame.K_d, pygame.K_RIGHT) and snkdir[0] != -1:
                snkdir = (1, 0)
            elif e.key in (pygame.K_a, pygame.K_LEFT) and snkdir[0] != 1:
                snkdir = (-1, 0)
            elif e.key == pygame.K_r:
                snk = [[GRIDW // 3, GRIDH // 2]]
                snkdir = (1, 0)
                apl = [GRIDW // 2, GRIDH // 2]
                score = 0
                
    # update screen
    screen.fill((0, 0, 0))
    for i, pos in enumerate(snk):
        col = SNKHDCOL if i == 0 else SNKCOL
        pygame.draw.rect(screen, col, pygame.Rect(pos[0] * TILEW, pos[1] * TILEH, TILEW, TILEH))
    pygame.draw.rect(screen, APLCOL, pygame.Rect(apl[0] * TILEW, apl[1] * TILEH, TILEW, TILEH))
    if not HDSCR:
        screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (4, 4))
    pygame.display.flip()
    
    # snake movement
    if GMTYP == "normal":
        nh = [snk[0][0] + snkdir[0], snk[0][1] + snkdir[1]]
    elif GMTYP == "warp":
        nh = [(snk[0][0] + snkdir[0]) % GRIDW, (snk[0][1] + snkdir[1]) % GRIDH]
    snk.insert(0, nh)
    
    # apple check
    if nh != apl:
        snk.pop()
    else:
        apl = [random.randint(0, GRIDW - 1), random.randint(0, GRIDH - 1)]
        score += 1
    
    # snake death
    if nh in snk[1:] or not GRIDW > nh[0] > -1 or not GRIDH > nh[1] > -1:
        time.sleep(1)
        
        # restart
        snk = [[GRIDW // 3, GRIDH // 2]]
        snkdir = (1, 0)
        apl = [GRIDW // 2, GRIDH // 2]
        score = 0
        
    # tick
    time.sleep(TICK)
            
# quit
pygame.quit()

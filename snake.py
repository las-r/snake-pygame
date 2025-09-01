import argparse
import pygame
import random
import time

# made by las-r on github
# v1.1

# init pygame
pygame.init()
font = pygame.font.SysFont("Roboto Mono", 16)

# arg parser
prsr = argparse.ArgumentParser(prog="Snake", description="Simple snake game written in Python")
prsr.add_argument("-DS", "--displaysize", type=int, nargs=2, default=[800, 600], help="Display dimensions in pixels (default: 800 600)")
prsr.add_argument("-GS", "--gridsize", type=int, nargs=2, default=[40, 30], help="Game grid dimensions (default: 40 30)")
prsr.add_argument("-SHC", "--snakeheadcolor", type=int, nargs=3, default=[0, 191, 0], help="Snake head color as R G B (default: 0 191 0)")
prsr.add_argument("-SC", "--snakecolor", type=int, nargs=3, default=[0, 127, 0], help="Snake body color as R G B (default: 0 127 0)")
prsr.add_argument("-AC", "--applecolor", type=int, nargs=3, default=[255, 0, 0], help="Apple color as R G B (default: 255 0 0)")
prsr.add_argument("-BC", "--bgcolor", type=int, nargs=3, default=[0, 0, 0], help="Background color as R G B (default: 0 0 0)")
prsr.add_argument("-TC", "--scorecolor", type=int, nargs=3, default=[127, 127, 127], help="Score text color as R G B (default: 127 127 127)")
prsr.add_argument("-WC", "--wallcolor", type=int, nargs=3, default=[255, 255, 255], help="Wall color as R G B, only applies in wall mode (default: 255 255 255)")
prsr.add_argument("-T", "--tick", type=float, default=0.1, help="Time between each game tick in seconds (default: 0.1)")
prsr.add_argument("-GM", "--gamemode", choices=["normal", "warp", "wall"], default="normal", help="Game mode (default: normal)")
prsr.add_argument("-HS", "--hidescore", action="store_true", help="Hide score counter")
args = prsr.parse_args()

# settings
DISPW, DISPH = args.displaysize
GRIDW, GRIDH = args.gridsize
TILEW, TILEH = DISPW // GRIDW, DISPH // GRIDH
SNKHDCOL = tuple(args.snakeheadcolor)
SNKCOL = tuple(args.snakecolor)
APLCOL = tuple(args.applecolor)
BGCOL = tuple(args.bgcolor)
SCRCOL = tuple(args.scorecolor)
WLLCOL = tuple(args.wallcolor)
TICK = args.tick
GMMD = args.gamemode
HDSCR = args.hidescore

# functions
def restart():
    global snk, snkdir, apl, wlls, score
    
    snk = [[GRIDW // 3, GRIDH // 2]]
    snkdir = (1, 0)
    apl = [GRIDW // 2, GRIDH // 2]
    wlls = []
    score = 0

# variables
snk = [[GRIDW // 3, GRIDH // 2]]
snkdir = (1, 0)
apl = [GRIDW // 2, GRIDH // 2]
wlls = []
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
            if e.key in (pygame.K_w, pygame.K_UP) and (snkdir[1] != 1 or len(snk) <= 1):
                snkdir = (0, -1)
            elif e.key in (pygame.K_s, pygame.K_DOWN) and (snkdir[1] != -1 or len(snk) <= 1):
                snkdir = (0, 1)
            elif e.key in (pygame.K_d, pygame.K_RIGHT) and (snkdir[0] != -1 or len(snk) <= 1):
                snkdir = (1, 0)
            elif e.key in (pygame.K_a, pygame.K_LEFT) and (snkdir[0] != 1 or len(snk) <= 1):
                snkdir = (-1, 0)
            elif e.key == pygame.K_r:
                restart()
                
    # update screen
    screen.fill(BGCOL)
    for i, pos in enumerate(snk):
        col = SNKHDCOL if i == 0 else SNKCOL
        pygame.draw.rect(screen, col, pygame.Rect(pos[0] * TILEW, pos[1] * TILEH, TILEW, TILEH))
    for x, y in wlls:
        pygame.draw.rect(screen, WLLCOL, pygame.Rect(x * TILEW, y * TILEH, TILEW, TILEH))
    pygame.draw.rect(screen, APLCOL, pygame.Rect(apl[0] * TILEW, apl[1] * TILEH, TILEW, TILEH))
    if not HDSCR:
        screen.blit(font.render(f"Score: {score}", True, SCRCOL), (4, 4))
    pygame.display.flip()
    
    # snake movement
    if GMMD == "warp":
        nh = [(snk[0][0] + snkdir[0]) % GRIDW, (snk[0][1] + snkdir[1]) % GRIDH]
    else:
        nh = [snk[0][0] + snkdir[0], snk[0][1] + snkdir[1]]
    snk.insert(0, nh)
    
    # apple check
    if nh != apl:
        snk.pop()
    else:
        score += 1
        apl = [random.randint(0, GRIDW - 1), random.randint(0, GRIDH - 1)]
        while apl in snk or apl in wlls:
            apl = [random.randint(0, GRIDW - 1), random.randint(0, GRIDH - 1)]
        if GMMD == "wall":
            wll = [random.randint(0, GRIDW - 1), random.randint(0, GRIDH - 1)]
            while wll in snk or wll in apl:
                wll = [random.randint(0, GRIDW - 1), random.randint(0, GRIDH - 1)]
            wlls.append(wll)
    
    # snake death
    if nh in snk[1:] or nh in wlls or not GRIDW > nh[0] > -1 or not GRIDH > nh[1] > -1:
        time.sleep(1)
        
        # restart
        restart()
        
    # tick
    time.sleep(TICK)
            
# quit
pygame.quit()

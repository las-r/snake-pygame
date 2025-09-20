import argparse
import pygame
import random
import sys
import time

# made by las-r on github
# v1.3

# init pygame
pygame.init()
font = pygame.font.SysFont("Roboto Mono", 16)
clock = pygame.time.Clock()

# arg parser
prsr = argparse.ArgumentParser(prog="Snake", description="Simple snake game written in Python")
#prsr.add_argument("-D", "--debug", type=int, default=0, help="Debug level (default: 0)")
prsr.add_argument("-DS", "--displaysize", type=int, nargs=2, default=[800, 600], help="Display dimensions in pixels (default: 800 600)")
prsr.add_argument("-GS", "--gridsize", type=int, nargs=2, default=[40, 30], help="Game grid dimensions (default: 40 30)")
prsr.add_argument("-SHC", "--snakeheadcolor", type=int, nargs=3, default=[0, 191, 0], help="Snake head color as R G B (default: 0 191 0)")
prsr.add_argument("-SC", "--snakecolor", type=int, nargs=3, default=[0, 127, 0], help="Snake body color as R G B (default: 0 127 0)")
prsr.add_argument("-AC", "--applecolor", type=int, nargs=3, default=[255, 0, 0], help="Apple color as R G B (default: 255 0 0)")
prsr.add_argument("-BC", "--bgcolor", type=int, nargs=3, default=[0, 0, 0], help="Background color as R G B (default: 0 0 0)")
prsr.add_argument("-TC", "--textcolor", type=int, nargs=3, default=[127, 127, 127], help="Text color as R G B (default: 127 127 127)")
prsr.add_argument("-WC", "--wallcolor", type=int, nargs=3, default=[255, 255, 255], help="Wall color as R G B, only applies in wall mode (default: 255 255 255)")
prsr.add_argument("-ST", "--scoretext", default="Score: +s+", help="Score text with '+s+' as value (default: 'Score: ~s~')")
prsr.add_argument("-AA", "--appleamount", type=int, default=1, help="Amount of apples at once (default: 1)")
prsr.add_argument("-T", "--tick", type=float, default=0.1, help="Time between each game tick in seconds (default: 0.1)")
prsr.add_argument("-P", "--preset", default="", help="Argument preset (default: None)")
prsr.add_argument("-GM", "--gamemods", nargs="*", default=[], help="Game modifers (default: None)")
prsr.add_argument("-HS", "--hidescore", action="store_true", help="Hide score counter")
prsr.add_argument("-DP", "--disablepause", action="store_true", help="Disable pausing the game")
args = prsr.parse_args()

# load preset
PR = args.preset
if PR:
    filename = PR if "." in PR else f"{PR}.skp"
    with open(filename, "r") as f:
        preset_args = f.read().split()
    merged_args = preset_args + sys.argv[1:]
    args = prsr.parse_args(merged_args)
    

# settings
#DB = args.debug
DISPW, DISPH = args.displaysize
GRIDW, GRIDH = args.gridsize
TILEW, TILEH = DISPW // GRIDW, DISPH // GRIDH
SNKHDCOL = args.snakeheadcolor
SNKCOL = args.snakecolor
APLCOL = args.applecolor
APLAMT = args.appleamount
BGCOL = args.bgcolor
TXTCOL = args.textcolor
WLLCOL = args.wallcolor
SCTXT = args.scoretext
GMMDS = args.gamemods
HDSCR = args.hidescore
DISPSE = args.disablepause

# functions
def restart():
    global snk, snkdir, nextdir, apls, wlls, paused, scr, tick
    
    # reset game
    snk = [[GRIDW // 3, GRIDH // 2]]
    snkdir = (1, 0)
    nextdir = snkdir
    apls = [randPos() for _ in range(APLAMT)]
    wlls = []
    paused = False
    scr = 0
    tick = args.tick
def die():
    time.sleep(1)
    restart()
def randPos(initial=False):
    pos = [random.randint(0, GRIDW - 1), random.randint(0, GRIDH - 1)]
    if initial:
        while pos == [GRIDW // 3, GRIDH // 2]:
            pos = [random.randint(0, GRIDW - 1), random.randint(0, GRIDH - 1)]
        return pos
    else:
        while pos in snk or pos in apls or pos in wlls:
            pos = [random.randint(0, GRIDW - 1), random.randint(0, GRIDH - 1)]
        return pos

# variables
snk = [[GRIDW // 3, GRIDH // 2]]
snkdir = (1, 0)
nextdir = snkdir
apls = [randPos(True) for _ in range(APLAMT)]
paused = False
scr = 0
tick = args.tick
wlls = []

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
        
        # key events
        if e.type == pygame.KEYDOWN:
            # restart
            if e.key == pygame.K_r:
                restart()
                
            if not DISPSE:
                # pause
                if e.key == pygame.K_SPACE:
                    paused = not paused

            # movement
            if not paused:
                if e.key in (pygame.K_w, pygame.K_UP) and (snkdir[1] != 1 or len(snk) <= 1):
                    nextdir = (0, -1)
                elif e.key in (pygame.K_s, pygame.K_DOWN) and (snkdir[1] != -1 or len(snk) <= 1):
                    nextdir = (0, 1)
                elif e.key in (pygame.K_d, pygame.K_RIGHT) and (snkdir[0] != -1 or len(snk) <= 1):
                    nextdir = (1, 0)
                elif e.key in (pygame.K_a, pygame.K_LEFT) and (snkdir[0] != 1 or len(snk) <= 1):
                    nextdir = (-1, 0)
                
    # update screen
    screen.fill(BGCOL)
    for i, pos in enumerate(snk):
        col = SNKHDCOL if i == 0 else SNKCOL
        pygame.draw.rect(screen, col, pygame.Rect(pos[0] * TILEW, pos[1] * TILEH, TILEW, TILEH))
    for ax, ay in apls:
        pygame.draw.rect(screen, APLCOL, pygame.Rect(ax * TILEW, ay * TILEH, TILEW, TILEH))
    for wx, wy in wlls:
        pygame.draw.rect(screen, WLLCOL, pygame.Rect(wx * TILEW, wy * TILEH, TILEW, TILEH))
    if not HDSCR:
        screen.blit(font.render(SCTXT.replace("+s+", str(scr)), True, TXTCOL), (4, 4))
    pygame.display.flip()
    
    # game loop
    if not paused:
        # update snake direction
        snkdir = nextdir
        
        # movement
        if "warp" in GMMDS:
            nh = [(snk[0][0] + snkdir[0]) % GRIDW, (snk[0][1] + snkdir[1]) % GRIDH]
        else:
            nh = [snk[0][0] + snkdir[0], snk[0][1] + snkdir[1]]
    
        # apple check 
        if nh in apls:
            scr += 1
            apls.remove(nh)
            apls.append(randPos())
            if "wall" in GMMDS:
                wlls.append(randPos())
            if "incspeed" in GMMDS:
                tick *= 0.95
            if "teleport" in GMMDS:
                nh = randPos()
        else:
            snk.pop()
        
        # snake death
        if (nh in snk[1:] and "passthrough" not in GMMDS) or nh in wlls or not GRIDW > nh[0] > -1 or not GRIDH > nh[1] > -1:
            die()
        else:
            snk.insert(0, nh)
        
    # tick
    clock.tick(1 / tick)
            
# quit
pygame.quit()

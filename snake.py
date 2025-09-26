import argparse
import json
import pygame
import random
import sys

# made by las-r on github
# v1.6

# init pygame
pygame.init()
font = pygame.font.SysFont("Roboto Mono", 16)
clock = pygame.time.Clock()

# arg parser
prsr = argparse.ArgumentParser(prog="Snake", description="Simple snake game written in Python")
prsr.add_argument("-D", "--debug", type=int, default=0, help="Debug output level (default: 0)")
prsr.add_argument("-DS", "--displaysize", type=int, nargs=2, default=[800, 600], help="Display dimensions in pixels (default: 800 600)")
prsr.add_argument("-GS", "--gridsize", type=int, nargs=2, default=[40, 30], help="Game grid dimensions (default: 40 30)")
prsr.add_argument("-SHC", "--snakeheadcolor", type=int, nargs=3, default=[0, 191, 0], help="Snake head color as R G B (default: 0 191 0)")
prsr.add_argument("-SC", "--snakecolor", type=int, nargs=3, default=[0, 127, 0], help="Snake body color as R G B (default: 0 127 0)")
prsr.add_argument("-S2HC", "--snake2headcolor", type=int, nargs=3, default=[0, 0, 191], help="Snake 2 head color as R G B (default: 0 0 191)")
prsr.add_argument("-S2C", "--snake2color", type=int, nargs=3, default=[0, 0, 127], help="Snake 2 body color as R G B (default: 0 0 127)")
prsr.add_argument("-AC", "--applecolor", type=int, nargs=3, default=[255, 0, 0], help="Apple color as R G B (default: 255 0 0)")
prsr.add_argument("-BC", "--bgcolor", type=int, nargs=3, default=[0, 0, 0], help="Background color as R G B (default: 0 0 0)")
prsr.add_argument("-TC", "--textcolor", type=int, nargs=3, default=[127, 127, 127], help="Text color as R G B (default: 127 127 127)")
prsr.add_argument("-WC", "--wallcolor", type=int, nargs=3, default=[255, 255, 255], help="Wall color as R G B, only applies in wall mod (default: 255 255 255)")
prsr.add_argument("-PAC", "--portalacolor", type=int, nargs=3, default=[0, 127, 255], help="Portal A color as R G B, only applies in portal mod (default: 0 127 255)")
prsr.add_argument("-PBC", "--portalbcolor", type=int, nargs=3, default=[255, 127, 0], help="Portal B color as R G B, only applies in portal mod (default: 255 127 0)")
prsr.add_argument("-SSC", "--shedskincolor", type=int, nargs=3, default=[120, 120, 120], help="Shed skin color as R G B, only applies in shedding mod (default: 128 191 128)")
prsr.add_argument("-STX", "--scoretext", default="Score: +s+", help="Score text with '+s+' as value (default: 'Score: +s+')")
prsr.add_argument("-HSTX", "--highscoretext", default="Highscore: +h+", help="Highscore text with '+h+' as value (default: 'Highscore: +h+')")
prsr.add_argument("-TTX", "--ticktext", default="Tick: +t+", help="Tick text with '+t+' as value (default: 'Tick: +t+')")
prsr.add_argument("-TD", "--tickdecimals", type=int, default=3, help="How many decimals to show in the tick text (default: 3)")
prsr.add_argument("-AA", "--appleamount", type=int, default=1, help="Amount of apples at once (default: 1)")
prsr.add_argument("-DD", "--deathdelay", type=int, default=1000, help="Time of pause after snake death in milliseconds (default: 1000)")
prsr.add_argument("-T", "--tick", type=float, default=0.1, help="Time between each game tick in seconds (default: 0.1)")
prsr.add_argument("-P", "--preset", default="", help="Load a preset of arguments (default: None)")
prsr.add_argument("-GM", "--gamemods", nargs="*", default=[], help="Game modifers (default: None)")
prsr.add_argument("-HS", "--hidescore", action="store_true", help="Hide score counter")
prsr.add_argument("-HHS", "--hidehighscore", action="store_true", help="Hide highscore")
prsr.add_argument("-ST", "--showtick", action="store_true", help="Show current tick speed")
prsr.add_argument("-RS", "--randomseed", type=float, default=None, help="RNG seed (default: None)")
args = prsr.parse_args()

# load random seed
if args.randomseed != None:
    random.seed(args.randomseed)

# load preset
PR = args.preset
if PR:
    filen = PR if "." in PR else f"{PR}.skp"
    with open(filen, "r") as f:
        pargs = f.read().split()
    margs = pargs + sys.argv[1:]
    args = prsr.parse_args(margs)

# display settings
DISPW, DISPH = args.displaysize
GRIDW, GRIDH = args.gridsize
TILEW, TILEH = DISPW // GRIDW, DISPH // GRIDH

# game settings
GMMDS = args.gamemods
APLAMT = args.appleamount
DIEDEL = args.deathdelay
TWOP = "2player" in GMMDS

# customization settings
SNKHDCOL = args.snakeheadcolor
SNKCOL = args.snakecolor
SNK2HDCOL = args.snake2headcolor
SNK2COL = args.snake2color
APLCOL = args.applecolor
WLLCOL = args.wallcolor
BGCOL = args.bgcolor
TXTCOL = args.textcolor
PRTLCOLA = args.portalacolor
PRTLCOLB = args.portalbcolor
SSCOL = args.shedskincolor
TXT = args.scoretext
if not args.hidehighscore: TXT += f", {args.highscoretext}"
if args.showtick: TXT += f", {args.ticktext}"
HDSCR = args.hidescore

# misc settings
DB = args.debug

# functions
def restart():
    global snk, snkdir, nextdir, snk2, snk2dir, nextdir2, apls, paused, scr, tick, wlls, prtl, prtls, shedskin
    
    # reset game
    if DB > 1: print(f"Game has been restarted")
    snk = [[GRIDW // 3, GRIDH // 2]]
    snkdir = (1, 0) if not TWOP else (0, -1)
    nextdir = snkdir
    if TWOP:
        snk2 = [[GRIDW // 3 * 2, GRIDH // 2]]
        snk2dir = (0, 1)
        nextdir2 = snk2dir
    apls = [randPos() for _ in range(APLAMT)]
    paused = False
    scr = 0
    tick = args.tick
    wlls = []
    prtl = []
    prtls = []
    shedskin = []
def die():
    global run

    if DB > 1: print(f"Snake death has occurred")
    if not "1try" in GMMDS:
        pygame.time.wait(DIEDEL)
        restart()
    else:
        run = False
def randPos(initial=False):
    # initial generation
    pos = [random.randint(0, GRIDW - 1), random.randint(0, GRIDH - 1)]
            
    # 2 player check
    if not TWOP:
        if initial:
            while pos == [GRIDW // 3, GRIDH // 2]:
                pos = [random.randint(0, GRIDW - 1), random.randint(0, GRIDH - 1)]
        else:
            while pos in snk or pos in apls or pos in wlls or pos in prtl or pos in flattenTriSet(prtls) or pos in shedskin:
                pos = [random.randint(0, GRIDW - 1), random.randint(0, GRIDH - 1)]
    else:
        if initial:
            while pos not in [[GRIDW // 3, GRIDH // 2], [GRIDW // 3 * 2, GRIDH // 2]]:
                pos = [random.randint(0, GRIDW - 1), random.randint(0, GRIDH - 1)]
        else:
            while pos in snk or pos in snk2 or pos in apls or pos in wlls or pos in prtl or pos in flattenTriSet(prtls) or pos in shedskin:
                pos = [random.randint(0, GRIDW - 1), random.randint(0, GRIDH - 1)]
    return pos
def randCol():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
def flattenTriSet(triset):
    flat = []
    for _, pa, pb in triset:
        flat.extend([pa, pb])
    return flat
def saveHs():
    if "dontsavehs" not in GMMDS:
        if DB > 1: print(f"Saving highscore: {hscr}")
        with open("data.skd", "r", encoding="utf-8") as d:
            data = json.load(d)
        data["hscrs"][argstr] = hscr
        with open("data.skd", "w", encoding="utf-8") as dw:
            json.dump(data, dw, indent=4)

# variables
snk = [[GRIDW // 3, GRIDH // 2]]
snkdir = (1, 0) if not TWOP else (0, -1)
nextdir = snkdir
if TWOP:
    snk2 = [[GRIDW // 3 * 2, GRIDH // 2]]
    snk2dir = (0, 1)
    nextdir2 = snk2dir
apls = [randPos(True) for _ in range(APLAMT)]
paused = False
scr = 0
hscr = 0
tick = args.tick
wlls = []
prtl = []
prtls = []
shedskin = []
argstr = " ".join(sys.argv[1:])

# load highscore
if "dontsavehs" not in GMMDS:
    try:
        with open("data.skd", "r", encoding="utf-8") as d:
            data = json.load(d)
    except FileNotFoundError:
        data = {"hscrs": {}}
    except json.JSONDecodeError:
        print("Error: invalid format in data.skd — resetting")
        data = {"hscrs": {}}
    if "hscrs" not in data:
        data["hscrs"] = {}
    if argstr not in data["hscrs"]:
        data["hscrs"][argstr] = 0
        with open("data.skd", "w", encoding="utf-8") as dw:
            json.dump(data, dw, indent=4)
    hscr = data["hscrs"][argstr]
    
if DB > 0:
    print(f"Arguments: {sys.argv[1:]}")
    print(f"Arguments String: {argstr}")
    print(f"Game modifers: {GMMDS}")
    print(f"Random seed (if any): {args.randomseed}")
    print(f"Highscore: {hscr}")

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
            if "noreset" not in GMMDS:
                # restart
                if e.key == pygame.K_r:
                    restart()
                    
            if "nopause" not in GMMDS:
                # pause
                if e.key == pygame.K_SPACE:
                    paused = not paused
                    if DB > 1: print(f"Game pause state: {paused}")
            
            if "dontsavehs" not in GMMDS:
                # pause
                if e.key == pygame.K_h:
                    saveHs()
            
            # movement
            if not paused:
                if not TWOP:
                    if e.key in (pygame.K_w, pygame.K_UP) and (snkdir[1] != 1 or len(snk) <= 1):
                        nextdir = (0, -1)
                    elif e.key in (pygame.K_s, pygame.K_DOWN) and (snkdir[1] != -1 or len(snk) <= 1):
                        nextdir = (0, 1)
                    elif e.key in (pygame.K_d, pygame.K_RIGHT) and (snkdir[0] != -1 or len(snk) <= 1):
                        nextdir = (1, 0)
                    elif e.key in (pygame.K_a, pygame.K_LEFT) and (snkdir[0] != 1 or len(snk) <= 1):
                        nextdir = (-1, 0)
                else:
                    # snake 1
                    if e.key == pygame.K_w and (snkdir[1] != 1 or len(snk) <= 1):
                        nextdir = (0, -1)
                    elif e.key == pygame.K_s and (snkdir[1] != -1 or len(snk) <= 1):
                        nextdir = (0, 1)
                    elif e.key == pygame.K_d and (snkdir[0] != -1 or len(snk) <= 1):
                        nextdir = (1, 0)
                    elif e.key == pygame.K_a and (snkdir[0] != 1 or len(snk) <= 1):
                        nextdir = (-1, 0)
                        
                    # snake 2
                    if e.key == pygame.K_UP and (snk2dir[1] != 1 or len(snk2) <= 1):
                        nextdir2 = (0, -1)
                    elif e.key == pygame.K_DOWN and (snk2dir[1] != -1 or len(snk2) <= 1):
                        nextdir2 = (0, 1)
                    elif e.key == pygame.K_RIGHT and (snk2dir[0] != -1 or len(snk2) <= 1):
                        nextdir2 = (1, 0)
                    elif e.key == pygame.K_LEFT and (snk2dir[0] != 1 or len(snk2) <= 1):
                        nextdir2 = (-1, 0)
                
    # update screen
    screen.fill(BGCOL)
    
    # snake(s)
    for i, pos in enumerate(snk):
        col = SNKHDCOL if i == 0 else SNKCOL
        pygame.draw.rect(screen, col, pygame.Rect(pos[0] * TILEW, pos[1] * TILEH, TILEW, TILEH))
    if TWOP:
        for j, pos2 in enumerate(snk2):
            col = SNK2HDCOL if j == 0 else SNK2COL
            pygame.draw.rect(screen, col, pygame.Rect(pos2[0] * TILEW, pos2[1] * TILEH, TILEW, TILEH))
            
    # apple
    for ax, ay in apls:
        pygame.draw.rect(screen, APLCOL, pygame.Rect(ax * TILEW, ay * TILEH, TILEW, TILEH))
    
    # walls
    for wx, wy in wlls:
        pygame.draw.rect(screen, WLLCOL, pygame.Rect(wx * TILEW, wy * TILEH, TILEW, TILEH))
        
    # portal
    if prtl != []:
        pygame.draw.rect(screen, PRTLCOLA, pygame.Rect(prtl[0][0] * TILEW, prtl[0][1] * TILEH, TILEW, TILEH))
        pygame.draw.rect(screen, PRTLCOLB, pygame.Rect(prtl[1][0] * TILEW, prtl[1][1] * TILEH, TILEW, TILEH))
        
    # portals
    for pcol, pa, pb in prtls:
        pygame.draw.rect(screen, pcol, pygame.Rect(pa[0] * TILEW, pa[1] * TILEH, TILEW, TILEH))
        pygame.draw.rect(screen, pcol, pygame.Rect(pb[0] * TILEW, pb[1] * TILEH, TILEW, TILEH))
            
    # shedskin
    for sx, sy in shedskin:
        pygame.draw.rect(screen, SSCOL, pygame.Rect(sx * TILEW, sy * TILEH, TILEW, TILEH))
        
    # score
    if not HDSCR:
        screen.blit(font.render(TXT.replace("+s+", str(scr)).replace("+t+", str(round(tick, args.tickdecimals))).replace("+h+", str(hscr)), True, TXTCOL), (4, 4))
    pygame.display.flip()
    
    # game loop
    if not paused:
        # update snake direction
        snkdir = nextdir
        if TWOP: snk2dir = nextdir2
        
        # movement
        if "warp" in GMMDS:
            nh = [(snk[0][0] + snkdir[0]) % GRIDW, (snk[0][1] + snkdir[1]) % GRIDH]
            if DB > 2: print(f"Snake 1 has moved to {nh}")
            if TWOP: 
                nh2 = [(snk2[0][0] + snk2dir[0]) % GRIDW, (snk2[0][1] + snk2dir[1]) % GRIDH]
                if DB > 2: print(f"Snake 2 has moved to {nh2}")
        else:
            nh = [snk[0][0] + snkdir[0], snk[0][1] + snkdir[1]]
            if DB > 2: print(f"Snake 1 has moved to {nh}")
            if TWOP: 
                nh2 = [snk2[0][0] + snk2dir[0], snk2[0][1] + snk2dir[1]]
                if DB > 2: print(f"Snake 2 has moved to {nh2}")
    
        # apple check 
        if nh in apls:
            if DB > 1: print(f"Apple has been eaten at {nh} by Snake 1")
            scr += 1
            if scr > hscr: hscr = scr
            apls.remove(nh)
            apls.append(randPos())
            if "wall" in GMMDS:
                wlls.append(randPos())
            if "incspeed" in GMMDS:
                tick *= 0.95
            if "teleport" in GMMDS:
                nh = randPos()
            if "portal" in GMMDS:
                prtl = [randPos(), randPos()]
            if "portals" in GMMDS:
                prtls.append([randCol(), randPos(), randPos()])
            if "shedding" in GMMDS:
                if shedskin != []:
                    for _ in range(len(shedskin) // 3):
                        shedskin.remove(random.choice(shedskin))
                for s in snk[1:]:
                    shedskin.append(s)
        else:
            snk.pop()
        if TWOP:
            if nh2 in apls:
                if DB > 1: print(f"Apple has been eaten at {nh2} by Snake 2")
                scr += 1
                if scr > hscr: hscr = scr
                apls.remove(nh2)
                apls.append(randPos())
                if "wall" in GMMDS:
                    wlls.append(randPos())
                if "incspeed" in GMMDS:
                    tick *= 0.95
                if "teleport" in GMMDS:
                    nh2 = randPos()
                if "portal" in  GMMDS:
                    prtl = [randPos(), randPos()]
                if "portals" in GMMDS:
                    prtls.append([randCol(), randPos(), randPos()])
            else:
                snk2.pop()
            
        # portal check
        if prtl != []:
            if nh == prtl[0]: nh = prtl[1]
            elif nh == prtl[1]: nh = prtl[0]
            if TWOP:
                if nh2 == prtl[0]: nh2 = prtl[1]
                elif nh2 == prtl[1]: nh2 = prtl[0]
                
        # portals check
        for p in prtls:
            if nh == p[1]: nh = p[2]
            elif nh == p[2]: nh = p[1]
            if TWOP:
                if nh2 == p[1]: nh2 = p[2]
                elif nh2 == p[2]: nh2 = [1]
        
        # snake death
        if not TWOP:
            if ((nh in snk[1:] and "passthrough" not in GMMDS) or 
            nh in wlls or 
            nh in shedskin or
            not GRIDW > nh[0] > -1 or 
            not GRIDH > nh[1] > -1):
                die()
            else:
                snk.insert(0, nh)
        else:
            if ((nh in snk[1:] and "passthrough" not in GMMDS) or 
                (nh in snk2 and "2ppassthrough" not in GMMDS) or 
                nh == nh2 or
                nh in wlls or 
                nh in shedskin or
                not GRIDW > nh[0] > -1 or 
                not GRIDH > nh[1] > -1):
                die()
            else:
                snk.insert(0, nh)
            if ((nh2 in snk2[1:] and "passthrough" not in GMMDS) or 
                (nh2 in snk and "2ppassthrough" not in GMMDS) or 
                nh2 == nh or
                nh2 in wlls or 
                nh2 in shedskin or
                not GRIDW > nh2[0] > -1 or 
                not GRIDH > nh2[1] > -1):
                die()
            else:
                snk2.insert(0, nh2)
        
    # tick
    clock.tick(1 / tick)
            
# save and quit
if DB > 1: print("Game has been quit")
saveHs()
pygame.quit()

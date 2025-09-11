<img width="512" alt="Screenshot showing the game." src="https://github.com/user-attachments/assets/d35c09bf-fa54-47f5-9e36-3511b58303df" />

# Snake Pygame
A simple snake game written in Python.

## Usage
```
python snake.py [args]
```

### Gameplay
WASD / Arrow keys for snake movement, R for restart.

### Command Line Arguments
|Argument|Subargument Amount|Description|Type|Default Value|
|-|-|-|-|-|
|`--displaysize`, `-DS`|2|Display dimensions in pixels|Integer|`800 600`|
|`--gridsize`, `-GS`|2|Game grid dimensions|Integer|`40 30`|
|`--snakeheadcolor`, `-SHC`|3|Snake head color as R G B|Integer|`0 191 0`|
|`--snakecolor`, `-SC`|3|Snake body color as R G B|Integer|`0 127 0`|
|`--applecolor`, `-AC`|3|Apple color as R G B|Integer|`255 0 0`|
|`--bgcolor`, `-BC`|3|Background color as R G B|Integer|`0 0 0`|
|`--scorecolor`, `-TC`|3|Score text color as R G B|Integer|`127 127 127`|
|`--wallcolor`, `-WC`|3|Wall color as R G B, only applies in wall mode|Integer|`255 255 255`|
|`--tick`, `-T`|1|Time between each game tick in seconds|Float|`0.1`|
|`--gamemode`, `-GM`|1|Game mode (Modes: `normal`, `warp`, `wall`)|String|`normal`|
|`--hidescore`, `-HS`|0|Hide score counter|Boolean|`False`|

## Planned Features
- More gamemodes
    - Local multiplayer
        - 2 and maybe 3? or 4? players
    - Self phasing
    - Teleport
    - Flashlight?
    - Spotlight
- Multiple gamemodes stacked
- More customization
    - Apple count
    - Player count?
    - Score text
        - Size, font, score
- Customization GUI?
- Customization presets?
- Compiled binaries?
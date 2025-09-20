<img width="512" alt="Screenshot showing the game." src="https://github.com/user-attachments/assets/d35c09bf-fa54-47f5-9e36-3511b58303df" />

# Snake Pygame
A simple snake game written in Python.

## Usage
```
python snake.py [args]
```

### Gameplay
- **WASD / Arrow keys**: move the snake
- **R**: restart the game
- **Space**: pause/unpause (unless disabled) 

#### Game Modifiers
|Modifier|Effect|
|-|-|
|incspeed|Decrements the tick delay by 5% upon eating an apple.|
|passthrough|Allows the snake to pass through itself.|
|wall|Makes a wall spawn at a random location upon eating an apple.|
|warp|Makes the borders teleport you to the other side.|
|teleport|Makes apples teleport you to a random location.|

### Command Line Arguments
|Argument|Subargument Amount|Description|Type|Default Value|
|-|-|-|-|-|
|`--displaysize`, `-DS`|2|Display dimensions in pixels|Integer|`800 600`|
|`--gridsize`, `-GS`|2|Game grid dimensions|Integer|`40 30`|
|`--snakeheadcolor`, `-SHC`|3|Snake head color as R G B|Integer|`0 191 0`|
|`--snakecolor`, `-SC`|3|Snake body color as R G B|Integer|`0 127 0`|
|`--applecolor`, `-AC`|3|Apple color as R G B|Integer|`255 0 0`|
|`--bgcolor`, `-BC`|3|Background color as R G B|Integer|`0 0 0`|
|`--textcolor`, `-TC`|3|Text color as R G B|Integer|`127 127 127`|
|`--wallcolor`, `-WC`|3|Wall color as R G B|Integer|`255 255 255`|
|`--scoretext`, `-ST`|1|Score text with `+s+` as value|String|`Score: ~s~`|
|`--appleamount`, `-AA`|1|Amount of apples at once|Integer|`1`|
|`--tick`, `-T`|1|Time between each game tick in seconds|Float|`0.1`|
|`--preset`, `-P`|1|Load a preset of arguments|String|`None`|
|`--gamemods`, `-GM`|*|Space-separated list of game modifers|String|`None`|
|`--hidescore`, `-HS`|0|Hide score counter|Boolean|`False`|
|`--disablepause`, `-DP`|0|Disable pausing the game|Boolean|`False`|

## Planned Features
- More game modifiers
  - Local multiplayer (2–4 players)
  - Teleport
  - Flashlight / Spotlight modes
  - Portals
- More customization
  - Player count
  - Score text options (size, font)
  - Keybinds
- Customization GUI and presets
  - Premade sets
  - Custom sets
- Sounds
- Highscore system
  - Save highscores per customization set
- Debug mode
- Config file?

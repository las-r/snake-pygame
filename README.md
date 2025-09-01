<img width="512" alt="Screenshot showing the game." src="https://github.com/user-attachments/assets/d35c09bf-fa54-47f5-9e36-3511b58303df" />

# Snake Pygame
A simple snake game written in Python.

## Usage
```
python snake.py [args]
```

### Command Line Arguments
|Argument|Subargument Amount|Description|Type|Default Value|
|-|-|-|-|-|
|`--displaysize`, `-DS`|2|Display dimensions in pixels|Integer|`800 600`|
|`--gridsize`, `-GS`|2|Game grid dimensions|Integer|`40 30`|
|`--snakeheadcolor`, `-SHC`|3|Snake head color as R G B|Integer|`0 191 0`|
|`--snakecolor`, `-SC`|3|Snake body color as R G B|Integer|`0 127 0`|
|`--applecolor`, `-AC`|3|Apple color as R G B|Integer|`255 0 0`|
|`--tick`, `-T`|1|Time between each game tick in seconds|Float|`0.1`|
|`--gametype`, `-GT`|1|Game type (Possible values: `normal`, `warp`)|String|`normal`|
|`--hidescore`, `-HS`|0|Hide score counter|Boolean|`False`|

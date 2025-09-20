<img width="512" alt="Screenshot showing the game." src="https://github.com/user-attachments/assets/d35c09bf-fa54-47f5-9e36-3511b58303df" />

# Snake Pygame
A simple snake game written in Python.

## Usage
```
python snake.py [args]
```

### Gameplay
- **WASD / Arrow keys**: move the snake
- **R**: restart (unless disabled) 
- **Space**: pause/unpause (unless disabled) 

### Game Modifiers
|Modifier|Effect|
|-|-|
|1try|Closes the game upon death.|
|2player|Two player cooperative mode.|
|incspeed|Decrements the tick delay by 5% upon eating an apple.|
|nopause|Disable the pause functionality.|
|noreset|Disable the reset functionality.|
|passthrough|Allows the snake to pass through itself.|
|portal|Changes location of a portal upon eating an apple.|
|portals|Spawns a new portal upon eating an apple.|
|wall|Makes a wall spawn at a random location upon eating an apple.|
|warp|Makes the borders teleport you to the other side.|
|teleport|Makes apples teleport you to a random location.|

### Command Line Arguments
| Argument | Subargument Amount | Description | Type | Default Value |
|----------|--------------------|-------------|------|---------------|
| `--displaysize`, `-DS` | 2 | Display dimensions in pixels | Integer | `800 600` |
| `--gridsize`, `-GS` | 2 | Game grid dimensions | Integer | `40 30` |
| `--snakeheadcolor`, `-SHC` | 3 | Snake head color as R G B | Integer | `0 191 0` |
| `--snakecolor`, `-SC` | 3 | Snake body color as R G B | Integer | `0 127 0` |
| `--snake2headcolor`, `-S2HC` | 3 | Snake 2 head color as R G B | Integer | `0 0 191` |
| `--snake2color`, `-S2C` | 3 | Snake 2 body color as R G B | Integer | `0 0 127` |
| `--applecolor`, `-AC` | 3 | Apple color as R G B | Integer | `255 0 0` |
| `--bgcolor`, `-BC` | 3 | Background color as R G B | Integer | `0 0 0` |
| `--textcolor`, `-TC` | 3 | Text color as R G B | Integer | `127 127 127` |
| `--wallcolor`, `-WC` | 3 | Wall color as R G B (only in wall mode) | Integer | `255 255 255` |
| `--scoretext`, `-STX` | 1 | Score text with `+s+` as value | String | `Score: +s+` |
| `--ticktext`, `-TTX` | 1 | Tick text with `+t+` as value | String | `Tick: +t+` |
| `--tickdecimals`, `-TD` | 1 | How many decimals to show in tick text | Integer | `3` |
| `--appleamount`, `-AA` | 1 | Amount of apples at once | Integer | `1` |
| `--deathdelay`, `-DD` | 1 | Pause after snake death (ms) | Integer | `1000` |
| `--tick`, `-T` | 1 | Time between each game tick (seconds) | Float | `0.1` |
| `--preset`, `-P` | 1 | Load a preset of arguments | String | `""` (empty / None) |
| `--gamemods`, `-GM` | * | Space-separated list of game modifiers | String | `[]` (None) |
| `--hidescore`, `-HS` | 0 | Hide score counter | Boolean | `False` |
| `--showtick`, `-ST` | 0 | Show current tick speed | Boolean | `False` |

### Presets
Presets are a way to store a set of command line arguments so you don't have to type it all in each time you want to play the game.

It's very easy to make a preset. Just put the command line arguments in a plaintext file.

The file extension for presets is `.skp`. Using this extension will allow you to only type in the preset name, not the file extension. You don't *need* to use the extension to get a functioning preset, but it's recommended you do.

**Example**
```
lightspeed.skp:
-GM incspeed warp passthrough teleport -AA 25 -T 0.05 -ST -TD 5

cmd:
python snake.py -P lightspeed
```

## Planned Features
- More game modifiers
  - Flashlight / Spotlight modes
  - Mirror
- More customization
  - Player count
  - Score text options (size, font)
  - Keybinds
- Sounds
- Highscore system
  - Save highscores per customization set
- Debug mode
- Config file?

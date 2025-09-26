<img width="512" alt="Screenshot showing the game." src="https://github.com/user-attachments/assets/d35c09bf-fa54-47f5-9e36-3511b58303df" />

# Snake Pygame
A simple and customizable snake game written in Python.

## Usage
```bash
python snake.py [args]
```

## Gameplay
- **WASD / Arrow keys**: move the snake
  - In 2-player mode: WASD controls Snake 1, Arrow Keys control Snake 2
- **R**: restart (unless disabled)
- **Space**: pause/unpause (unless disabled)
- **H**: save highscore (unless disabled)

## Game Modifiers
| Modifier        | Effect                                                           |
| --------------- | ---------------------------------------------------------------- |
| `1try`          | Closes the game upon death.                                      |
| `2player`       | Enables two-player cooperative mode.                             |
| `2ppassthrough` | Allows both players to pass through each other.                  |
| `dontsavehs`    | Disables highscore saving.                                       |
| `incspeed`      | Snake speed increases (tick reduced by 5%) after each apple.     |
| `nopause`       | Disables pause functionality.                                    |
| `noreset`       | Disables restart functionality.                                  |
| `passthrough`   | Snake can pass through its own body.                             |
| `portal`        | Spawns a paired portal when an apple is eaten.                   |
| `portals`       | Spawns additional random-colored portals upon eating apples.     |
| `wall`          | Spawns a wall block at a random location when an apple is eaten. |
| `warp`          | Borders wrap around instead of killing the snake.                |
| `teleport`      | Eating an apple teleports the snake’s head to a random location. |
| `shedding`      | Snake leaves behind "shed skin" blocks as obstacles.             |

## Command Line Arguments
| Argument            | Short   | Values | Description                        | Default            |
| ------------------- | ------- | ------ | ---------------------------------- | ------------------ |
| `--debug`           | `-D`    | int    | Debug output level                 | `0`                |
| `--displaysize`     | `-DS`   | 2 ints | Display dimensions in pixels       | `800 600`          |
| `--gridsize`        | `-GS`   | 2 ints | Grid dimensions                    | `40 30`            |
| `--snakeheadcolor`  | `-SHC`  | 3 ints | Snake 1 head color (R G B)         | `0 191 0`          |
| `--snakecolor`      | `-SC`   | 3 ints | Snake 1 body color (R G B)         | `0 127 0`          |
| `--snake2headcolor` | `-S2HC` | 3 ints | Snake 2 head color (R G B)         | `0 0 191`          |
| `--snake2color`     | `-S2C`  | 3 ints | Snake 2 body color (R G B)         | `0 0 127`          |
| `--applecolor`      | `-AC`   | 3 ints | Apple color (R G B)                | `255 0 0`          |
| `--bgcolor`         | `-BC`   | 3 ints | Background color (R G B)           | `0 0 0`            |
| `--textcolor`       | `-TC`   | 3 ints | Text color (R G B)                 | `127 127 127`      |
| `--wallcolor`       | `-WC`   | 3 ints | Wall color (R G B)                 | `255 255 255`      |
| `--portalacolor`    | `-PAC`  | 3 ints | Portal A color (R G B)             | `0 127 255`        |
| `--portalbcolor`    | `-PBC`  | 3 ints | Portal B color (R G B)             | `255 127 0`        |
| `--shedskincolor`   | `-SSC`  | 3 ints | Shed skin color (R G B)            | `120 120 120`      |
| `--scoretext`       | `-STX`  | str    | Score text (`+s+` = score)         | `"Score: +s+"`     |
| `--highscoretext`   | `-HSTX` | str    | Highscore text (`+h+` = highscore) | `"Highscore: +h+"` |
| `--ticktext`        | `-TTX`  | str    | Tick text (`+t+` = tick speed)     | `"Tick: +t+"`      |
| `--tickdecimals`    | `-TD`   | int    | Decimals to show in tick text      | `3`                |
| `--appleamount`     | `-AA`   | int    | Number of apples at once           | `1`                |
| `--deathdelay`      | `-DD`   | int    | Pause after snake death (ms)       | `1000`             |
| `--tick`            | `-T`    | float  | Time between ticks (seconds)       | `0.1`              |
| `--preset`          | `-P`    | str    | Load preset file                   | `""`               |
| `--gamemods`        | `-GM`   | list   | Space-separated list of modifiers  | `[]`               |
| `--hidescore`       | `-HS`   | flag   | Hide score counter                 | `False`            |
| `--hidehighscore`   | `-HHS`  | flag   | Hide highscore display             | `False`            |
| `--showtick`        | `-ST`   | flag   | Show tick speed                    | `False`            |
| `--randomseed`      | `-RS`   | float  | RNG seed                           | `None`             |

## Presets
Presets are saved argument sets in plaintext files (`.skp` recommended).
If no extension is given, `.skp` is assumed.

**Example preset file:**
```txt
# lightspeed.skp
-GM incspeed warp passthrough teleport shedding -AA 25 -T 0.05 -ST -TD 5
```

**Run with preset:**
```bash
python snake.py -P lightspeed
```

## Data Storage
- Highscores and settings are stored in `data.skd` (JSON format).
- Each unique set of arguments has its own highscore entry.

## Planned Features
- More modifiers
  - Spotlight
  - Mirror
- GUI-based customization
- Sound effects
- Better graphics
- Smarter highscore system
- Better multiplayer
  - Online?
  - Competitive and cooperative modes
- Config file support
- Better presets

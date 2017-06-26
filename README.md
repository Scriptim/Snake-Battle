# Snake Battle 

Play **Snake** with two players

**THIS GAME IS ALSO PLAYABLE ON A RASPBERRY PI USING GPIO INPUTS!**

## Python Installation

### Windows

- Download the latest Python 2 release from [here](https://www.python.org/downloads/windows/)
- Run the installer (make sure to include *pip*)
- Open `cmd.exe` as administrator and install the required packages by running `pip install <package>` or `python -m pip install <package>`

### Linux

- Install Python 2 (`python2.7`) using your package manager
- Open a terminal and install the required packages by running `pip install <package>` as root

## Required Python Packages

- `pygame`
- `RPi` (only when using on Raspberry Pi)

## Setup Font

Before starting the game, go to line *68* and *69* and change *None* to the path of a font file

If you don't do this, Pygame will choose a font

I recommend using [VT323 by Peter Hull](https://fonts.google.com/specimen/VT323 "Google Fonts")

**Example:**
   
    FONT_DB = pygame.font.Font("VT232.ttf", 20) # debug font
    FONT_SC = pygame.font.Font("VT232.ttf", TILE_SIZE * 5) # score

**Note: You should use an absolute path if you do not run the game from inside the directory**

## Start Game

Open a Terminal and navigate to this folder, then run
	
	python2.7 snakebattle.py 
	
The game is tested with **Python v2.7**, feel free to use another compatible version

## Play Game

- Player 1:
    - Turn left with `A`
    - Turn right with `D`
- Player 2:
    - Turn left with `LEFT ARROW`
    - Turn right with `RIGHT ARROW`
- Collect Food to grow
- You lose, when you touch your opponent or the window borders
- When both players "lose" at once, the longer snake will win

## Arguments

`$ python2.7 snakebattle.py --help`

    usage: snakebattle.py [-h] [-r] [-s PX] [-t X Y] [-d] [-f TPS] [-b MS]
    
    optional arguments:
      -h, --help            show this help message and exit
      -r, --raspi           run snake battle on a raspberry pi
      -s PX, --tilesize PX  the size of a tile
      -t X Y, --tiles X Y   the number of tiles
      -d, --debug           show debug information on the screen
      -f TPS, --fps TPS     framerate in ticks per second
      -b MS, --delay MS     button delay (raspi mode)
      
## Raspberry Pi Mode (`--raspi`)

Connect buttons to the following GPIO pins (BCM numbering)

- Player 1 Left: **25**
- Player 1 Right: **24**
- Player 2 Left: **23**
- Player 2 Right: **18**

Alternatively, you can use other pins and change the pin numbers on lines *23 - 26*
# Simp City

**[Ngee Ann Polytechnic](https://www.np.edu.sg/) - CSF Year 1 - PRG Assignment**

You are the mayor of Simp City, and you want to build the happiest and most prosperous city possible, i.e., score the most points.

This city-building strategy game is played over 16 turns. In each turn, you will build one of two randomly-selected buildings in your 4x4 city. In the first turn, you can build anywhere in the city. In subsequent turns, you can only build on squares that are connected to existing buildings. The other building that you did not build is discarded.

Each building scores in a different way. The objective of the game is to build a city that scores as many points as possible.

There are 5 types of buildings, with 8 copies of each:
- Beach (BCH): Scores 3 points if it is built on the left or right side of the city, or 1 point otherwise
- Factory (FAC): Scores 1 point per factory (FAC) in the city, up to a maximum of 4 points for the first 4 factories. All subsequent factories only score 1 point each.
- House (HSE): If it is next to a factory (FAC), then it scores 1 point only. Otherwise, it scores 1 point for each adjacent house (HSE) or shop (SHP), and 2 points for each adjacent beach (BCH).
- Shop (SHP): Scores 1 point per different type of building adjacent to it.
- Highway (HWY): Scores 1 point per connected highway (HWY) in the same row.

## Basic Requirements
1. Display Main Menu
Example:
```
Welcome, mayor of Simp City!
----------------------------
1. Start new game
2. Load saved game

0. Exit
Your choice? 
```

1.1. Start New Game
This option starts a new game. The player is given an empty 4x4 board; the building “pool” is initialized with 8 copies of each building (40 buildings in total); and two buildings are randomly selected from the pool:
```
Turn 1
     A     B     C     D  
  +-----+-----+-----+-----+
 1|     |     |     |     |
  +-----+-----+-----+-----+
 2|     |     |     |     |
  +-----+-----+-----+-----+
 3|     |     |     |     |
  +-----+-----+-----+-----+
 4|     |     |     |     |
  +-----+-----+-----+-----+
1. Build a HSE
2. Build a BCH
3. See remaining buildings
4. See current score

5. Save game
0. Exit to main menu
Your choice? 
```

2. Playing the Game
When you are playing the game, it should display the game menu as shown in Figure 1.1.  When a user enters an option from 1 to 5 (or 0), the program will process the option accordingly. 

2.1. Build a Building
When the player chooses option 1 or 2, the game will ask for a location expressed as a letter-number pair.
```
Your choice? 1
Build where? b2

Turn 2
     A     B     C     D  
  +-----+-----+-----+-----+
 1|     |     |     |     |
  +-----+-----+-----+-----+
 2|     | HSE |     |     |
  +-----+-----+-----+-----+
 3|     |     |     |     |
  +-----+-----+-----+-----+
 4|     |     |     |     |
  +-----+-----+-----+-----+
1. Build a SHP
2. Build a SHP
3. See remaining buildings
4. See current score

5. Save game
0. Exit to main menu
Your choice?
```
**Must check for existing building on current tile and that the building is built orthogonally adjacent to existing ones.

2.2. See Remaining Buildings
When the player chooses option 3, a list of buildings still remaining in the “pool” is displayed.
```
Building           Remaining
--------           ---------
HSE                7
FAC                8
SHP                6
HWY                8
BCH                7
```
2.3. See Current Score
```
Turn 8
     A     B     C     D
  +-----+-----+-----+-----+
 1|     | HWY |     |     |
  +-----+-----+-----+-----+
 2|     | SHP | HSE | BCH |
  +-----+-----+-----+-----+
 3|     | HSE | HSE | BCH |
  +-----+-----+-----+-----+
 4|     |     |     |     |
  +-----+-----+-----+-----+
1. Build a SHP
2. Build a HSE
3. See remaining buildings
4. See current score

5. Save game
0. Exit to main menu
Your choice? 4

HSE: 4 + 2 + 4 = 10
FAC: 0
SHP: 2 = 2
HWY: 1 = 1
BCH: 3 + 3 = 6
Total score: 19
```
3. Save Game and Load Game
Can be exported and encrypted to an external file.

4. End of Game
Shows the final score and layout, and exit to main menu when a game ends.
```
Turn 16
     A     B     C     D  
  +-----+-----+-----+-----+
 1| SHP | SHP | HSE |     |
  +-----+-----+-----+-----+
 2| BCH | HSE | HSE | BCH |
  +-----+-----+-----+-----+
 3| BCH | SHP | HSE | HSE |
  +-----+-----+-----+-----+
 4| HWY | HWY | HWY | HWY |
  +-----+-----+-----+-----+
1. Build a HWY
2. Build a FAC
3. See remaining buildings

4. Save game
0. Exit to main menu
Your choice? 2
Build where? d1

Final layout of Simp City:
     A     B     C     D  
  +-----+-----+-----+-----+
 1| SHP | SHP | HSE | FAC |
  +-----+-----+-----+-----+
 2| BCH | HSE | HSE | BCH |
  +-----+-----+-----+-----+
 3| BCH | SHP | HSE | HSE |
  +-----+-----+-----+-----+
 4| HWY | HWY | HWY | HWY |
  +-----+-----+-----+-----+
HSE: 1 + 5 + 5 + 3 + 3 = 17
FAC: 1 = 1
SHP: 2 + 2 + 3 = 7
HWY: 4 + 4 + 4 + 4 = 16
BCH: 3 + 3 + 3 = 9
Total score: 50
```
Disclaimer: The requirements as well as the documentation for the program Simp City are not authored by me, but by Ngee Ann Polytechnic's School of ICT. Only the spaghetti code that I've included in this repo for future reference is coded by my ownself.

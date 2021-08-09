# SimpCity

## [Ngee Ann Polytechnic](https://www.np.edu.sg/) - CSF Year 1 - PRG Assignment

You are the mayor of Simp City, and you want to build the happiest and most prosperous city possible, i.e., score the most points.

This city-building strategy game is played over 16 turns. In each turn, you will build one of two randomly-selected buildings in your 4x4 city. In the first turn, you can build anywhere in the city. In subsequent turns, you can only build on squares that are connected to existing buildings. The other building that you did not build is discarded.

Each building scores in a different way. The objective of the game is to build a city that scores as many points as possible.

There are 5 types of buildings, with 8 copies of each:
- Beach (BCH): Scores 3 points if it is built on the left or right side of the city, or 1 point otherwise
- Factory (FAC): Scores 1 point per factory (FAC) in the city, up to a maximum of 4 points for the first 4 factories. All subsequent factories only score 1 point each.
- House (HSE): If it is next to a factory (FAC), then it scores 1 point only. Otherwise, it scores 1 point for each adjacent house (HSE) or shop (SHP), and 2 points for each adjacent beach (BCH).
- Shop (SHP): Scores 1 point per different type of building adjacent to it.
- Highway (HWY): Scores 1 point per connected highway (HWY) in the same row.

Example:
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

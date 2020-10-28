# game-of-life

# Conway's Game of Life

A populated cell will:

-Depopulate if it has one or fewer neighbors
-Depopulate if it has four or more neighbors
-Survive if it has two or three neighbors

An unpopulated cell will become populated if it has exactly three neighbors.

From these simple rules, complex behaviors emerge. 

Click a few cells to populate them. Try different patterns. Once a pattern resolves to stasis, try introducing noise back into it and see what happens.

When you're done, clear the board with the clear button.

Use the random button to generate a random pattern. Note any interesting shapes as they play out before you.

Use the speed button to make the simulation run faster.

# Sources

https://www.pygame.org/wiki/tutorials

Pygame Docs Wiki

Pygame is quite well documented and was fun to use once I got the hang of it. The Pygame docs were my principal reference once I had an initial flow figured out.

http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids

"Chapter 16: Array-Backed Grid" from Program Arcade Games by Paul Craven

This chapter laid the foundation for the entire program. Pygame's docs were useful for nitty-gritty details, but this page on writing array-backed grids gave me the high-level understanding of the system.

https://www.youtube.com/watch?v=4_9twnEduFA

"How to Create a Button in Pygame [CODE IN DESCRIPTION]" by Tech With Tim

Having a very well-structured button class made my life much easier when it came time to start grafting extra features onto this Game of Life, and those buttons came from this video.

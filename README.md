# Python Uno Game
This small project introduces some non-AI Uno game in Python as a practice project for OOP in Python and some simple game logic. No frontend is implemented. The card game is called MauMau in Germany you can find the full description (https://en.wikipedia.org/wiki/Mau-Mau_(card_game))[here]. It mainly aims as a practice project for OOP in Python and some pretty simple AI.

## Basic usage
You can just start the App via the main.py file (python main.py in the terminal when you're in the root project folder). It is modified to either let the user play against a computer or simulate a number of matches between two computer players. The computer players can have different skill levels. So far 'easy' for random choice of valid card to play or 'medium' for highest point choice for card to play are implemented. 'Hard' was planned to build on data and machine learning to become better over time. If you feel like it, I'm happy to collaborate on a project to get it running.

If you would want more (partly unfair ;-) ) data output during the game, just uncomment part of the print_board method within the Board.py. The general data flow should become clear through ample comments and docstrings, if not, shoot me a message anytime.

## Techniques used
The project was meant to implementa dummy card game leveraging the code models of OOP in Python. It avoids data manipulation libraries and works with native python arrays. It utlizies class inheritance (Human and Computer player inherit basic properties from a generic 'Player' interface) and code modularization.

I hope ypu enjoy the project and maybe use it as a starting point for your own future work. Open to-dos can be found in the main.py file as inspiration. Let me know what you think!

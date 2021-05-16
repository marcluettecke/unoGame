from Gameflow import play_games

player1, player2 = play_games(number_of_games=50)

print(player1.total_points)
print(player1.total_wins)
print(player2.total_points)
print(player2.total_wins)

"""
next to do's:
- fix jack in first round
- fix 10 from '1S' f.ex.
- include strategies (include high-skill strategy, aka awareness of the cards already played to base decisions on)
- user interface
- read up in ML techniques to learn strategies 
- comment and document everything, set up GitHub
"""

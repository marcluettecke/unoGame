from ComputerPlayer import ComputerPlayer
from HumanPlayer import HumanPlayer
from Board import Board
from Rules import check_specialty_card


def set_up():
    """
    Function to define the set up of the game, such as how many rounds we want to simulate, setting up the board,
    and initializing the player objects.

    Returns:
        2 player objects and a board object necessary for the other stages of the game.
    """
    # global player1, player2, board
    # player1 = HumanPlayer(name="Marc")
    # player2 = ComputerPlayer(name="Sue", skill_level='medium')
    # board = Board()
    # start_hand1, start_hand2 = board.game_start()
    #
    # player1.set_hand(cards=start_hand1), player2.set_hand(cards=start_hand2)
    # print(f"Current middle card: {board.middle_cards[0]}")
    # print(f"{player1.name}'s hand: {player1.hand}")
    # board.print_board(player1_hand=player1.hand, player2_hand=player2.hand, player1_name=player1.name,
    #                   player2_name=player2.name)



    global player1, player2, board

    playmode = input('Do you want to simulate two Computer players (enter "Computer") or play yourself (enter "Human")?')
    computer_skill2 = 'medium'
    if playmode == 'Human':
        player_Name = input("What's your username?")
        player1 = HumanPlayer(name=player_Name)
    elif playmode == 'Computer':
        computer_skill1 = input("How good do you want Player1 to be? So far 'easy' and 'medium' are available ")
        if computer_skill1 in ['easy', 'medium']:
            player1 = ComputerPlayer(name="John", skill_level=computer_skill1)
        else:
            print('Nota valid skill option, computer skill level set to easy by default')
            player1 = ComputerPlayer(name="John", skill_level='easy')
    else:
        print("This is a not a valid option, please enter either 'Human' or 'Computer' as player type for player1")

    computer_skill2 = input("How good do you want Player2 to be? So far 'easy' and 'medium' are available " )
    if computer_skill2 in ['easy', 'medium']:
        player2 = ComputerPlayer(name="Sue", skill_level=computer_skill2)
    else:
        print('Nota valid skill option, computer skill level set to easy by default')
    player2 = ComputerPlayer(name="Sue", skill_level='easy')
    board = Board()
    start_hand1, start_hand2 = board.game_start()

    player1.set_hand(cards=start_hand1), player2.set_hand(cards=start_hand2)

    board.print_board(player1_hand=player1.hand, player2_hand=player2.hand, player1_name=player1.name,
                      player2_name=player2.name)



def main_stage(game_ongoing: bool = True):
    """
    Main function to let the two computer players actively play. This includes drawing cards, playing cards,
    and interacting for the specialty cards (7, 8, and J)
    Args:
        game_ongoing: boolean which changes once the winning condition has been reached to end the game.

    Returns:
        Updates the respective player attributes and prints the result of the game to the console.
    """
    while game_ongoing:
        for player in [player1, player2]:
            if len(board.remaining_cards) <= 2:
                # check if cards to draw is empty, if so, shuffle in the middle cards (other than the currend active
                # middle card)
                board.refill_remaining_cards()

            if check_specialty_card(current_board=board, current_player=player):
                continue

            played_card = player.play_card(remaining_cards=board.remaining_cards,
                                           middle_card=board.middle_cards[0])
            # condition of players just played his last card
            if played_card == 'Empty':
                game_ongoing = False
                break
            if played_card is not None:
                board.middle_cards.insert(0, played_card)
        print(f"Current middle card: {board.middle_cards[0]}")
        # if isinstance(player, HumanPlayer):
        print(f"{player1.name}'s hand: {player1.hand}")
        print(f"Remaining cards of the opponent: {len(player2.hand)}")

        board.print_board(player1_hand=player1.hand, player2_hand=player2.hand, player1_name=player1.name,
                          player2_name=player2.name)


def end_game():
    """
    Function necessary to end the game, such as counting the points of the remaining cards on the hand and printing
    the result to the console.

    Assigns:
        card values to the players.points property
    """
    player1.points = sum([board.card_values[card[0]] for card in player1.hand])
    player2.points = sum([board.card_values[card[0]] for card in player2.hand])

    if player1.points < player2.points:
        player1.total_wins += 1
        print(f"{player1.name} wins!")
    else:
        player2.total_wins += 1
        print(f"{player2.name} wins!")
    print(f"{player1.name} points: {player1.points}, {player2.name} points: {player2.points}")


def play_games(number_of_games):
    """
    The main function to simulate n games between two computer players
    Args:
        number_of_games: integer for how many games are simulated

    Returns:
        player1 and player2 ComputerPlayer Objects, which carry the property .total_points as a benchmark of who won
        overall
    """
    # global_player1 = ComputerPlayer(name="Marc")
    global_player1 = HumanPlayer(name="Marc")
    global_player2 = ComputerPlayer(name="Sue", skill_level='medium')
    for _ in range(number_of_games):
        set_up()
        main_stage()
        end_game()
        global_player1.total_points += player1.points
        global_player1.total_wins += player1.total_wins
        global_player2.total_points += player2.points
        global_player2.total_wins += player2.total_wins
    return global_player1, global_player2

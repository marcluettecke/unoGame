from Player import Player
from Board import Board


def is_valid(card: str, middle_card: str):
    """
    Function to determine if a card to play is valid given a current middle card. it checks if either the suit,
    the number are acceptable or if the card is a Jack, which can be played on any middle card
    Args:
        card: String of the current card
        middle_card: String of the current middle card

    Returns:
        Boolean if the card is valid
    """
    return card[1] == middle_card[1] or card[0] == middle_card[0] or card[0] == 'J'


def special_card_7(current_player: Player, current_board: Board):
    """
    Function to describe the action for special card 7: draw two cards.
    Args:
        current_player: current_board Player object' turn
        current_board: current_board board object

    Assigns:
        two extra cards to the player object'special hand.
    """
    current_player.draw_card(remaining_cards=current_board.remaining_cards, seven=True)
    current_player.draw_card(remaining_cards=current_board.remaining_cards, seven=True)
    print(f"{current_player.name} draws 2 cards ({current_player.hand[-2]}, {current_player.hand[-1]}) for a 7 in the "
          f"middle.")


def special_card_8(current_player: Player, current_board: Board):
    """
    Function to describe the action for special card 8: sit out.
    Args:
        current_player: current_board Player object' turn
        current_board: current_board board object

    Assigns:
        the played card to the list of eights played.
    """
    print(f"{current_player.name} has to sit out for {current_board.middle_cards[0]} in the middle.")
    current_board.list_of_eights.append(current_board.middle_cards[0][1])
    return True


def check_specialty_card(current_player: Player, current_board: Board):
    """
    Function to check if special card is (7 for 8) is_valid played and conducting the required action.
    Args:
        current_player: current_board Player object' turn
        current_board: current_board board object

    Assigns:
       updated board and player objects and describe the Function special card 7 and 8
    """
    if current_board.middle_cards[0][0] in current_board.special_cards:
        # special card 7 - draw 2 cards
        if current_board.middle_cards[0][0] == '7':

            special_card_7(current_player=current_player, current_board=current_board)

        # special card 8 - sit out
        if current_board.middle_cards[0][0] == '8' and current_board.middle_cards[0][
            1] not in current_board.list_of_eights:
            return special_card_8(current_player=current_player, current_board=current_board)

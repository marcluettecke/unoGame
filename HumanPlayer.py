from Board import Board
from Player import Player
from typing import List
from Rules import is_valid
import sys


class HumanPlayer(Player):
    """
    Class to define the human player of an Uno game. Inherits basic properties from parent class 'Player'
    """

    def __init__(self, name: str):
        super(HumanPlayer, self).__init__(name)
        self.action = None

    def draw_card(self, remaining_cards: List[str], seven: bool = False):
        """
        Draws one or multiple cards from the remaining cards
        Args:
            remaining_cards: List of strings of the remaining cards pile
            seven: boolean that indicates if player has to draw twice and not once as usual
            strategy: a string indicating the strategy that the player follows (for computer players)

        Assigns:
            Adds the extra card(s) to a player's hand
        """
        if not seven:
            print(f"Can't play draw a card: {remaining_cards[0]}")
        self.hand.append(remaining_cards[0])
        remaining_cards.pop(0)

    def play_card(self, remaining_cards: List[str], middle_card: str, on_redraw=False):
        """
        Function to play a card.
        Args:
            on_redraw: boolean if the player plays the card on a redrawn card (after not being able to play with his
            original current hand), or not.
            remaining_cards: List of remaining cards as strings in a list
            middle_card: current middle cards to establish which cards are valid to play.

        Returns:
            Updates the middle cards and removes played card from a player's hand
        """
        card = input("Which card would you like to play? (Answer None, if you cannot play a card.)")
        if card == "None" and not on_redraw:
            self.draw_card(remaining_cards=remaining_cards)
            return self.play_card(remaining_cards=remaining_cards, middle_card=middle_card, on_redraw=True)
        elif card == "None" and on_redraw:
            return None
        try:
            index = self.hand.index(card)
        except ValueError:
            print("You do not have this card in your hand.")
            if not on_redraw:
                return self.play_card(remaining_cards=remaining_cards, middle_card=middle_card)
            else:
                return self.play_card(remaining_cards=remaining_cards, middle_card=middle_card, on_redraw=True)

        if is_valid(card=card, middle_card=middle_card):
            if len(self.hand) == 1:
                self.hand.pop(index)
                self.won_game = 'Empty'
                return self.won_game
            if card[0] == 'J':
                self.hand.pop(self.hand.index(card))
                original_jack = card
                new_suit = input("Which suit do you wish for?")
                new_card = "J" + new_suit
                print(f"{self.name} played {original_jack} and wishes for {new_card[1]}")
                return new_card

            print(f"{self.name} played {card}")
            return self.hand.pop(index)
        else:
            print(f"You cannot play a {card} with {middle_card} in the middle.")
            if not on_redraw:
                return self.play_card(remaining_cards=remaining_cards, middle_card=middle_card)
            else:
                return self.play_card(remaining_cards=remaining_cards, middle_card=middle_card, on_redraw=True)


# if __name__ == '__main__':
#     remaining_cards_out = ['AC', '2H', 'JC', '7H', '9H', '1D', '2D', '5S', '6S', '6D', '3S', '6C', '2S', 'QH', 'QC',
#                            '9S']
#     board_instance = Board()
#     player1 = HumanPlayer(name="Marc")
#     middle_card = "JH"
#     start_hand1, start_hand2 = board_instance.game_start()
#
#     player1.set_hand(cards=start_hand1)
#     print(player1.hand)
#     print(middle_card)
#     print(remaining_cards_out)
#     player1.play_card(remaining_cards=remaining_cards_out, middle_card=middle_card)

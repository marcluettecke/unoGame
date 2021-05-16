from typing import List


class Player():
    """
    Parent class for a player in a Maumau game.
    """

    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.won_game = None
        self.points = 0
        self.total_points = 0
        self.total_wins = 0

    def get_hand(self):
        """
        Getter for hand property
        Returns:
            list of cards on hand
        """
        return self.hand

    def set_hand(self, cards: List[str]):
        """
        Setter for the hand property
        Args:
            cards: List of cards to be set to hand, especially at beginning of game.

        Assigns:
            sets the hand of a player with string of cards as list
        """
        self.hand = cards

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
        pass

    def play_card(self, remaining_cards: List[str], middle_card: str):
        """
        Function to play a card.
        Args:
            remaining_cards: List of remaining cards as strings in a list
            middle_card: current middle cards to establish which cards are valid to play.

        Returns:
            Updates the middle cards and removes played card from a player's hand
        """
        pass

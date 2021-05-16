import itertools
import random
from typing import List
suits = ["H", "D", "C", "S"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "1", "J", "Q", "K", "A"]


class Board:
    """
    Class defining the playing board for Uno
    """

    def __init__(self):
        self.possible_cards = ["".join(i) for i in (itertools.product(values, suits))]
        self.card_values = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "1": 10,
            "J": 20,
            "Q": 10,
            "K": 10,
            "A": 11
        }
        self.remaining_cards = []
        self.middle_cards = []
        self.special_cards = ["7", "8", "J", "A"]
        self.list_of_eights = []

    def game_start(self):
        self.remaining_cards = self.possible_cards
        random.shuffle(self.remaining_cards)

        player1_cards = []
        player2_cards = []
        for _ in range(7):
            player1_cards.append(self.remaining_cards.pop(0))
            player2_cards.append(self.remaining_cards.pop(0))
        self.middle_cards.append(self.remaining_cards.pop(0))
        return player1_cards, player2_cards

    def next_card(self):
        self.middle_cards.insert(0, self.remaining_cards.pop(0))

    def print_board(self, player1_hand: List[str], player2_hand: List[str], player1_name: str, player2_name: str):
        print(f""
              # f"{len(self.remaining_cards)} remaining cards in deck: {self.remaining_cards} \n"
              f"Current middle card: {self.middle_cards[0]} \n"
              # f"Already played cards: {self.middle_cards[1:]} \n"
              # f"{player1_name}'s hand: {player1_hand} \n"
              # f"{player2_name}'s hand: {player2_hand} \n"
              # f"Total cards in game "
              f"{len(self.remaining_cards) + len(self.middle_cards) + len(player1_hand) + len(player2_hand)}")

    def refill_remaining_cards(self):
        self.remaining_cards.extend(self.middle_cards[1:])
        # print(self.remaining_cards)
        random.shuffle(self.remaining_cards)
        self.middle_cards = [self.middle_cards[0]]

# if __name__ == '__main__':



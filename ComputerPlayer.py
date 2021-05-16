import random
from Board import Board
from Player import Player
from typing import List
from Rules import is_valid


class ComputerPlayer(Player):
    """
    Class to define the computer player of an Uno game. Inherits basic properties from parent class 'Player'
    """

    def __init__(self, name: str, skill_level: str = 'low'):
        super(ComputerPlayer, self).__init__(name)
        self.skill_level = skill_level

    def draw_card(self, remaining_cards: List[str], seven: bool = False):
        """
        Methods to draw a card, which means to remove the top card from the remaining cards and add the card(s) to
        the player's hand
        Args:
            remaining_cards: List of strings of remaining cards
            seven: boolean to indicate if two cards have to be drawn for the special card 7

        Assigns:
            new card to self.player.hand and removed the first list item from list of remaining cards
        """
        if not seven:
            pass
            print(f"{self.name} can't play and draws {remaining_cards[0]}")
        self.hand.append(remaining_cards[0])
        remaining_cards.pop(0)

    def play_jack(self, index_of_jack: int, original_jack: str):
        """
        Helper function to play the special card Jack. The logic by which a player chooses her suit changes depending
        on the skill-level assigned:
            low: chooses the suit randomly of the suits available in her hand
            medium: chooses the most frequent suit (first one in hand for a tie) of the suits available in her hand
        Args:
            index_of_jack: indicates the index of the Jack in the current player's hand
            original_jack: indicates the original jack. Important, here I use a trick to change the suit of the Jack
            to the suit that a player wishes for, this is of course not equivalent to what happens in a real game,
            but helps to continue the game flow, without changes to the dynamic

        Returns:
            The new card, aka the Jack with the wished for suit.
        """
        self.hand.pop(index_of_jack)
        if self.skill_level == 'low':
            suits_in_hand = set([i[1] for i in self.hand])
            # choose suit randomly
            new_card = "J" + str(random.sample(suits_in_hand, 1)[0])

        elif self.skill_level == 'medium':
            suits_in_hand = [i[1] for i in self.hand]
            # find the most most frequent suit in hand
            new_card = "J" + str(max(set(suits_in_hand), key=suits_in_hand.count))

        print(f"{self.name} played {original_jack} and wishes for {new_card[1]}")
        return new_card

    def play_card(self, remaining_cards: List[str], middle_card: str):
        """
        Methods to play a card. This method plays one of the cards the current player's hand. The logic depends on
        the skills-level assigned to the player.
            low: play the first card of the randomly shuffled hand that qualifies as a valid play (matching suit or
            matching number)
            medium: order the cards and play the first card that qualifies as a valid play from the ordered hand.
            This results in higher point cards to be played more often.
        Args:
            remaining_cards: List of strings of remaining cards
            middle_card: Str of the current middle card

        Returns:
            None if no card can be played (even after one try of drawing a new card)
            Str of card played if card can be played
        """
        if self.skill_level == 'medium':
            self.hand = sorted([i for i in self.hand], key=lambda k: Board().card_values[k[0]], reverse=True)

        for index, card in enumerate(self.hand):
            if is_valid(card=card, middle_card=middle_card):
                # condition to win on an empty hand
                if len(self.hand) == 1:
                    self.hand.pop(index)
                    self.won_game = 'Empty'
                    return self.won_game
                if card[0] == 'J':
                    return self.play_jack(index_of_jack=index, original_jack=card)

                print(f"{self.name} played {card}")
                return self.hand.pop(index)

        self.draw_card(remaining_cards=remaining_cards)
        if is_valid(card=self.hand[-1], middle_card=middle_card):
            if self.hand[-1][0] == 'J':
                original_jack = self.hand.pop(-1)
                suits_in_hand = set([i[1] for i in self.hand])
                new_card = "J" + str(random.sample(suits_in_hand, 1)[0])
                print(f"{self.name} played {original_jack} and wishes for {new_card[1]}")
                return new_card
            print(f"{self.name} played {self.hand[-1]}")
            return self.hand.pop(len(self.hand) - 1)


# if __name__ == '__main__':
#     player1 = ComputerPlayer(name="Steve", skill_level='medium')
#     player2 = ComputerPlayer(name="Sue")
#     board = Board()
#     start_hand1, start_hand2 = board.game_start()
#
#     player1.hand = ['JH', '8D', '4S', '2S', '9H', '8H', '10H']
#     player2.set_hand(cards=start_hand2)
#
#     board.print_board(player1_hand=player1.hand, player2_hand=player2.hand, player1_name=player1.name,
#                       player2_name=player2.name)
#
#     player1.play_card(remaining_cards=['3D', '9C', '8H', '4C', 'JH', 'QC', '5D', '8D', 'AC', 'AH', '7S', '1H',
#                                        'AD', 'KH', '6H', '3C', 'KS', '2C', '3H', '2D', 'KC', '6D', '7D', 'JS',
#                                        '6C',
#                                        '5S', '5H', '9D', '1C', 'QS',
#                                        'KD', '3S', '6S', 'JD', 'QH', '7H', '2H'],
#                       middle_card='9S')
#
#     board.print_board(player1_hand=player1.hand, player2_hand=player2.hand, player1_name=player1.name,
#                       player2_name=player2.name)

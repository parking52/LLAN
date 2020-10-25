
import random
import itertools

class Deck():

    def __init__(self):
        self.deck = [
            1,1,1,1,1,
            2,2,
            3,3,
            4,4,
            5,5,
            6,
            7,
            8,
        ]

    def shuffle(self):
        random.shuffle(self.deck)

    def display_deck(self):
        for card in self.deck:
            print(card.value, card.color)

    def set_trump(self, card_color):
        for card in self.deck:
            if card.color == card_color:
                card.trump = True
            else:
                card.trump = False
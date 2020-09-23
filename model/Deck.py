from model.Card import Card, CardSuit
import random


class Deck:

    def __init__(self):
        self.cards = []
        for suit in CardSuit:
            for val in range(2, 15):
                self.cards.append(Card(val, suit))
                random.shuffle(self.cards)

    def display(self):
        for card in self.cards:
            print(card.display())

    def draw_card(self):
        return self.cards.pop()



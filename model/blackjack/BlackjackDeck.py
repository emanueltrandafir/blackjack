import random

from model.Card import CardSuit
from model.Deck import Deck
from model.blackjack.BlackjackCard import BlackjackCard


class BlackjackDeck(Deck):
    def __init__(self):
        self.cards = []
        for suit in CardSuit:
            for val in range(2, 15):
                self.cards.append(BlackjackCard(val, suit))
                random.shuffle(self.cards)


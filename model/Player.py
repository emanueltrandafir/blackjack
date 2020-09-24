from model import Card


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def add_card_to_hand(self, card):
        self.hand.add(card)

    # def does_continue(self):
    #     print("press (D) to Draw another card")
    #     print("press (E) to End your turn")
    #     return input().upper() == "D"

    def get_hand_display(self):
       return self.hand.display()


class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        # if type(card) != type(Card):
        #     raise Exception("the argument {0} is not a valid Card object!".format(card))
        self.cards.append(card)

    def display(self):
        str=""
        for card in self.cards:
            str = str + " |" + card.display() + "|  "
        return str
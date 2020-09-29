import enum


class CardSuit(enum.Enum):
    Hearts = ("Hearts", "♥")
    Diamonds = ("Diamonds", "♦")
    Spades = ("Spades", "♠")
    Clubs = ("Clubs", "♣")


class Card:

    def __init__(self, value, suit):
        if suit not in CardSuit or value < 2 or value > 14:
            raise Exception("illegal args!")

        self.suit = suit
        self.value = value

        if value == 11:
            self.cardName = "A"
        elif value == 12:
            self.cardName = "J"
        elif value == 13:
            self.cardName = "Q"
        elif value == 14:
            self.cardName = "K"
        else:
            self.cardName = str(value)

    def display(self):
        s = self.cardName
        if self.value != 10:
            s += " "
        s += self.suit.value[1]
        return s

    def get_values(self):
        return [self.value]

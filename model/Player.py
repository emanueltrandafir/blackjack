from abc import abstractmethod

from model.Hand import Hand


class Player:
    def __init__(self, name, age, country_code, amount):
        self.name = name
        self.age = age
        self.amount = amount
        self.country_code = country_code
        self.hand = Hand()
        self.is_his_turn = False

    def get_hand_values(self):
        return self.hand.calculate_values()

    def add_card_to_hand(self, card):
        self.hand.add(card)

    def get_hand_display(self):
        return self.hand.display()

    def get_hand_values_str(self):
        return str(self.hand.calculate_values())

    @abstractmethod
    def still_playing(self):
        pass






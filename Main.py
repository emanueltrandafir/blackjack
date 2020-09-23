import os

from model.Deck import Deck
from model.Player import Player

nr_of_players = input("Number of players: ")

deck = Deck()

dealer = Player("Dealer")
player1 = Player("player1")

dealer.add_card_to_hand(deck.draw_card())

player1.add_card_to_hand(deck.draw_card())
player1.add_card_to_hand(deck.draw_card())


print(player1.name + "'s  turn! \n")
player1.print_hand()

while player1.does_continue():
    os.system('cls')
    player1.add_card_to_hand(deck.draw_card())
    player1.print_hand()
